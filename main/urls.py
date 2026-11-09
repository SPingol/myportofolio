from django.urls import path
from main.views import (
    show_main, 
    show_projects, 
    show_experience, 
    show_competition, 
    show_education,
    register, 
    login_user, 
    logout_user,
    update_project, 
    update_experience, 
    update_education, 
    update_competition
)

app_name = "main"

urlpatterns = [
    # Standard HTML pages
    path("", show_main, name="show_main"),
    path("projects/", show_projects, name="show_projects"),
    path("experience/", show_experience, name="show_experience"),
    path("competitions/", show_competition, name="show_competition"),
    path("education/", show_education, name="show_education"),
    
    # Authentication
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    
    # Fallback update pages (if accessed directly rather than via modal)
    path("projects/<uuid:project_id>/update/", update_project, name="update_project"),
    path("experience/<uuid:experience_id>/update/", update_experience, name="update_experience"),
    path("education/<uuid:education_id>/update/", update_education, name="update_education"),
    path("competitions/<uuid:competition_id>/update/", update_competition, name="update_competition"),
]