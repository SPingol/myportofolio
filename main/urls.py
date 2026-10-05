from django.urls import path
from main.views import (
    show_main,
    show_experience,
    show_competition,
    show_education,
    show_projects,
    get_projects_json,
    get_experience_json,
    get_education_json,
    get_competition_json,
    create_project_ajax,
    create_experience_ajax,
    create_education_ajax,
    create_competition_ajax,
    update_project,
    update_experience,
    update_education,
    update_competition,
    delete_project,
    delete_experience,
    delete_education,
    delete_competition,
    toggle_star,
    register,
    login_user,
    logout_user,
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('experience/', show_experience, name='show_experience'),
    path('competition/', show_competition, name='show_competition'),
    path('education/', show_education, name='show_education'),
    path('projects/', show_projects, name='show_projects'),

    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("api/education/", get_education_json, name="get_education_json"),
    path("api/competition/", get_competition_json, name="get_competition_json"),

    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),
    path("experience/add-ajax/", create_experience_ajax, name="create_experience_ajax"),
    path("education/add-ajax/", create_education_ajax, name="create_education_ajax"),
    path("competition/add-ajax/", create_competition_ajax, name="create_competition_ajax"),

    path("project/update/<uuid:project_id>/", update_project, name="update_project"),
    path("experience/update/<uuid:experience_id>/", update_experience, name="update_experience"),
    path("education/update/<uuid:education_id>/", update_education, name="update_education"),
    path("competition/update/<uuid:competition_id>/", update_competition, name="update_competition"),

    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),
    path('experience/<uuid:experience_id>/delete/', delete_experience, name='delete_experience'),
    path('education/<uuid:education_id>/delete/', delete_education, name='delete_education'),
    path('competition/<uuid:competition_id>/delete/', delete_competition, name='delete_competition'),

    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("projects/<uuid:project_id>/star/", toggle_star, name="toggle_star"),
]