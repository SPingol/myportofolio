import datetime
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import PermissionDenied
from django.core.serializers import serialize
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from main.forms import CompetitionForm, EducationForm, ExperienceForm, ProjectForm
from main.models import Competition, Education, Experience, Project



def show_main(request):
    last_login = request.COOKIES.get('last_login', 'No active login session / Cookie not found')
    context = {
        "name": "Serafin Reysetyo Amantresno Grajo Pingol",
        "short_name": "Serafin",
        "npm": "2506637136",
        "study_program": "S1 Ilmu Komputer KKI",
        "bio": (
            "Hello, I'm Serafin, a computer science student at Universitas Indonesia. "
            "I've been living abroad for 13 years and now the wind has blown me here i.e "
            "I have no idea how I got here. Regardless, "
            "I'm happy to be here and just seeing how things go. "
            "If it wasn't already apparent I am a fan of Project Wingman by Sector D2."
        ),
        "education_list": Education.objects.all(),
        "experience_list": Experience.objects.all(),
        "last_login": last_login,
    }
    return render(request, "index.html", context)


def show_projects(request):
    return render(request, "project.html", {"name": "Serafin"})


def show_experience(request):
    return render(request, "experience.html", {"name": "Serafin"})


def show_competition(request):
    return render(request, "competition.html", {"name": "Serafin"})


def show_education(request):
    return render(request, "education.html", {"name": "Serafin"})



def get_projects_json(request):
    query = request.GET.get("q", request.GET.get("title", "")).strip()
    projects = Project.objects.prefetch_related('starred_by').all()

    if query:
        projects = projects.filter(title__icontains=query)

    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)


def get_experience_json(request):
    query = request.GET.get("q", request.GET.get("title", "")).strip()
    experiences = Experience.objects.all()
    if query:
        experiences = experiences.filter(
            Q(title__icontains=query) | Q(role__icontains=query)
        )
    return HttpResponse(serialize("json", experiences), content_type="application/json")


def get_education_json(request):
    query = request.GET.get("q", request.GET.get("title", "")).strip()
    educations = Education.objects.all()
    if query:
        educations = educations.filter(
            Q(degree__icontains=query) | Q(institution__icontains=query)
        )
    return HttpResponse(serialize("json", educations), content_type="application/json")


def get_competition_json(request):
    query = request.GET.get("q", request.GET.get("title", "")).strip()
    competitions = Competition.objects.all()
    if query:
        competitions = competitions.filter(
            Q(title__icontains=query) | Q(organizer__icontains=query)
        )
    return HttpResponse(serialize("json", competitions), content_type="application/json")



@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add projects."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Project added successfully.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)


@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add experience entries."},
            status=403,
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Experience added successfully.", "pk": str(experience.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)


@require_POST
def create_education_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add education entries."},
            status=403,
        )

    form = EducationForm(request.POST)
    if form.is_valid():
        education = form.save()
        return JsonResponse(
            {"message": "Education added successfully.", "pk": str(education.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)


@require_POST
def create_competition_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add competition entries."},
            status=403,
        )

    form = CompetitionForm(request.POST)
    if form.is_valid():
        competition = form.save()
        return JsonResponse(
            {"message": "Competition added successfully.", "pk": str(competition.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)



@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")


def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect("main:login")

    return render(request, "register.html", {"name": "Serafin", "form": form})


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    return render(request, "login.html", {"name": "Serafin", "form": form})


def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response



@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project deleted successfully!")

    return redirect("main:show_projects")


@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=experience_id)
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience entry deleted successfully!")
    return redirect("main:show_experience")


@login_required(login_url="/login/")
def delete_education(request, education_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    education = get_object_or_404(Education, pk=education_id)
    if request.method == "POST":
        education.delete()
        messages.success(request, "Education entry deleted successfully!")
    return redirect("main:show_education")


@login_required(login_url="/login/")
def delete_competition(request, competition_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    competition = get_object_or_404(Competition, pk=competition_id)
    if request.method == "POST":
        competition.delete()
        messages.success(request, "Competition entry deleted successfully!")
    return redirect("main:show_competition")