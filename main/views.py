from django.shortcuts import render
from main.models import Experience, Education, Competition


def show_main(request):
    context = {
        "name": "Serafin Reysetyo Amantresno Grajo Pingol",
        "npm": "2506637136",
        "study_program": "S1 Ilmu Komputer KKI",
        "bio": (
            "A Computer Science student at Universitas Indonesia interested "
            "in software development and education. Truth Nuke"
        ),
        "education_list": Education.objects.all(),
        "experience_list": Experience.objects.all(),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Serafin",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)


def show_competition(request):
    context = {
        "name": "Serafin",
        "competition_list": Competition.objects.all(),
    }
    return render(request, "competition.html", context)


def show_education(request):
    context = {
        "name": "Serafin",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)