from django.urls import path
from main.views import (
    show_main,
    show_experience,
    create_experience,
    show_competition,
    create_competition,
    show_education,
    create_education,
    show_projects,
    create_project,
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('experience/', show_experience, name='show_experience'),
    path('experience/add/', create_experience, name='create_experience'),
    path('competition/', show_competition, name='show_competition'),
    path('competition/add/', create_competition, name='create_competition'),
    path('education/', show_education, name='show_education'),
    path('education/add/', create_education, name='create_education'),
    path('projects/', show_projects, name='show_projects'),
    path('projects/add/', create_project, name='create_project'),
]