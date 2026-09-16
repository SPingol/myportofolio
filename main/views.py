from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse

from main.models import Experience, Education, Competition, Project
from main.forms import EducationForm, ExperienceForm, CompetitionForm, ProjectForm


def show_main(request):
    context = {
        "name": "Serafin Reysetyo Amantresno Grajo Pingol",
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
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Serafin Reysetyo Amantresno Grajo Pingol",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)


def show_competition(request):
    context = {
        "name": "Serafin Reysetyo Amantresno Grajo Pingol",
        "competition_list": Competition.objects.all(),
    }
    return render(request, "competition.html", context)


def show_education(request):
    context = {
        "name": "Serafin Reysetyo Amantresno Grajo Pingol",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)


def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Serafin Reysetyo Amantresno Grajo Pingol",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

# --- Form Handling Views ---

def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New education entry added successfully!")
        return redirect("main:show_education")

    context = {
        "name": "Serafin Reysetyo Amantresno Grajo Pingol",
        "form": form,
    }
    return render(request, "education_form.html", context)


def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New experience entry added successfully!")
        return redirect("main:show_experience")

    context = {
        "name": "Serafin Reysetyo Amantresno Grajo Pingol",
        "form": form,
    }
    return render(request, "experience_form.html", context)



def create_competition(request):
    form = CompetitionForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New competition entry added successfully!")
        return redirect("main:show_competition")

    context = {
        "name": "Serafin Reysetyo Amantresno Grajo Pingol",
        "form": form,
    }
    return render(request, "competition_form.html", context)


def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New project added successfully!")
        return redirect("main:show_projects")

    context = {
        "name": "Serafin Reysetyo Amantresno Grajo Pingol",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")