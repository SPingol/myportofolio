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
    get_projects_json,
    delete_project,
    delete_experience,
    delete_education,
    delete_competition,
    update_competition,
    update_education,
    update_experience,
    update_project,
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
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),
    path('experience/<uuid:experience_id>/delete/', delete_experience, name='delete_experience'),
    path('competition/<uuid:competition_id>/delete/', delete_competition, name='delete_competition'),
    path('education/<uuid:education_id>/delete/', delete_education, name='delete_education'),
    path("experience/update/<uuid:experience_id>/", update_experience, name="update_experience"),
    path("education/update/<uuid:education_id>/", update_education, name="update_education"),
    path("competition/update/<uuid:competition_id>/", update_competition, name="update_competition"),
    path("project/update/<uuid:project_id>/", update_project, name="update_project"),
]