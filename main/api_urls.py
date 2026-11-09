from django.urls import path
from main import api_views

app_name = "api"

urlpatterns = [
    # Projects
    path("projects/", api_views.project_list, name="project-list"),
    path("projects/<uuid:project_id>/", api_views.project_detail, name="project-detail"),
    path("projects/<uuid:project_id>/star/", api_views.project_star, name="project-star"),
    
    # Experience
    path("experience/", api_views.experience_list, name="experience-list"),
    path("experience/<uuid:pk>/", api_views.experience_detail, name="experience-detail"),
    path("experience/<uuid:pk>/star/", api_views.experience_star, name="experience-star"),

    # Education
    path("education/", api_views.education_list, name="education-list"),
    path("education/<uuid:pk>/", api_views.education_detail, name="education-detail"),
    path("education/<uuid:pk>/star/", api_views.education_star, name="education-star"),

    # Competition
    path("competitions/", api_views.competition_list, name="competition-list"),
    path("competitions/<uuid:pk>/", api_views.competition_detail, name="competition-detail"),
    path("competitions/<uuid:pk>/star/", api_views.competition_star, name="competition-star"),
]