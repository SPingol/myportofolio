from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse

from main.models import Experience, Education, Competition
from main.forms import EducationForm, ExperienceForm, CompetitionForm


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



def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pendidikan baru berhasil ditambahkan!")
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
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
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
        messages.success(request, "Kompetisi baru berhasil ditambahkan!")
        return redirect("main:show_competition")

    context = {
        "name": "Serafin Reysetyo Amantresno Grajo Pingol",
        "form": form,
    }
    return render(request, "competition_form.html", context)