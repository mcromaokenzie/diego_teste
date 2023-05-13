from django.urls import path
from . import views

urlpatterns = [
    path("projects/", views.ProjectView.as_view()),
    path("projects/<str:pk>/", views.ProjectDetailView.as_view()),
]
