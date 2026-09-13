from django.urls import path
from main.views import (
    show_main,
    show_experience,
    show_competition,
    show_education,
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('experience/', show_experience, name='show_experience'),
    path('competition/', show_competition, name='show_competition'),
    path('education/', show_education, name='show_education'),
]