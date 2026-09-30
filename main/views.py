import datetime
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required  
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import serializers
from django.core.exceptions import PermissionDenied        
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

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


def show_experience(request):
    title_query = request.GET.get("title", "").strip()
    experience_list = Experience.objects.all()

    if title_query:
        experience_list = experience_list.filter(
            Q(title__icontains=title_query) | Q(role__icontains=title_query)
        )

    for item in experience_list:
        item.form = ExperienceForm(instance=item)

    context = {
        "name": "Serafin",
        "experience_list": experience_list,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)


def show_competition(request):
    title_query = request.GET.get("title", "").strip()
    competition_list = Competition.objects.all()

    if title_query:
        competition_list = competition_list.filter(
            Q(title__icontains=title_query) | Q(organizer__icontains=title_query)
        )

    for item in competition_list:
        item.form = CompetitionForm(instance=item)

    context = {
        "name": "Serafin",
        "competition_list": competition_list,
        "title_query": title_query,
    }
    return render(request, "competition.html", context)


def show_education(request):
    title_query = request.GET.get("title", "").strip()
    education_list = Education.objects.all()

    if title_query:
        education_list = education_list.filter(
            Q(degree__icontains=title_query) | Q(institution__icontains=title_query)
        )

    for item in education_list:
        item.form = EducationForm(instance=item)

    context = {
        "name": "Serafin",
        "education_list": education_list,
        "title_query": title_query,
    }
    return render(request, "education.html", context)


def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    for item in projects:
        item.form = ProjectForm(instance=item)

    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Serafin",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)



@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")

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


# --- UPDATE VIEWS ---

@login_required(login_url="/login/")
def update_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=experience_id)
    if request.method == "POST":
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            messages.success(request, "Experience updated successfully!")
    return redirect("main:show_experience")


@login_required(login_url="/login/")
def update_education(request, education_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    education = get_object_or_404(Education, pk=education_id)
    if request.method == "POST":
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            messages.success(request, "Education updated successfully!")
    return redirect("main:show_education")


@login_required(login_url="/login/")
def update_competition(request, competition_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    competition = get_object_or_404(Competition, pk=competition_id)
    if request.method == "POST":
        form = CompetitionForm(request.POST, instance=competition)
        if form.is_valid():
            form.save()
            messages.success(request, "Competition updated successfully!")
    return redirect("main:show_competition")


@login_required(login_url="/login/")
def update_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project updated successfully!")
    return redirect("main:show_projects")


# --- CREATE VIEWS ---

@login_required(login_url="/login/")
def create_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New education entry added successfully!")
        return redirect("main:show_education")

    context = {
        "name": "Serafin",
        "form": form,
    }
    return render(request, "education_form.html", context)


@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New experience entry added successfully!")
        return redirect("main:show_experience")

    context = {
        "name": "Serafin",
        "form": form,
    }
    return render(request, "experience_form.html", context)


@login_required(login_url="/login/")
def create_competition(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = CompetitionForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New competition entry added successfully!")
        return redirect("main:show_competition")

    context = {
        "name": "Serafin",
        "form": form,
    }
    return render(request, "competition_form.html", context)


@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New project added successfully!")
        return redirect("main:show_projects")

    context = {
        "name": "Serafin",
        "form": form,
    }
    return render(request, "projects_form.html", context)



def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects, use_natural_foreign_keys=True)
    return HttpResponse(projects_json, content_type="application/json")

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

    context = {
        "name": "Serafin",
        "form": form,
    }
    return render(request, "register.html", context)


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Serafin",
        "form": form,
    }
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response