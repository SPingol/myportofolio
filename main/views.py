from django.shortcuts import render
from main.models import Experience, Education, Competition


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