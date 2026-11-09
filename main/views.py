import datetime
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import PermissionDenied
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
    return render(request, "project.html", {"name": "Serafin", "form": ProjectForm()})

def show_experience(request):
    return render(request, "experience.html", {"name": "Serafin", "form": ExperienceForm()})

def show_competition(request):
    return render(request, "competition.html", {"name": "Serafin", "form": CompetitionForm()})

def show_education(request):
    return render(request, "education.html", {"name": "Serafin", "form": EducationForm()})


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

# Standard fallbacks for update views kept intact as requested in logic
@login_required(login_url="/login/")
def update_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project updated successfully!")
        return redirect("main:show_projects")
    return render(request, "project_form.html", {"form": form})

@login_required(login_url="/login/")
def update_experience(request, experience_id):
    if not request.user.is_superuser and not request.user.groups.filter(name="Editor").exists():
        raise PermissionDenied
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience updated successfully!")
        return redirect("main:show_experience")
    return render(request, "experience_form.html", {"form": form})

@login_required(login_url="/login/")
def update_education(request, education_id):
    if not request.user.is_superuser and not request.user.groups.filter(name="Editor").exists():
        raise PermissionDenied
    education = get_object_or_404(Education, pk=education_id)
    form = EducationForm(request.POST or None, instance=education)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Education updated successfully!")
        return redirect("main:show_education")
    return render(request, "education_form.html", {"form": form})

@login_required(login_url="/login/")
def update_competition(request, competition_id):
    if not request.user.is_superuser and not request.user.groups.filter(name="Editor").exists():
        raise PermissionDenied
    competition = get_object_or_404(Competition, pk=competition_id)
    form = CompetitionForm(request.POST or None, instance=competition)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Competition updated successfully!")
        return redirect("main:show_competition")
    return render(request, "competition_form.html", {"form": form})