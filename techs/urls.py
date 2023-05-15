from django.urls import path
from . import views

urlpatterns = [
    path("techs/", views.TechView.as_view()),
    path("techs/<int:pk>/", views.TechDetailView.as_view()),
]
