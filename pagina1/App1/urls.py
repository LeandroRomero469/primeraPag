from django.urls import path
from App1 import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('profesores/', views.profesores, name="Profesores"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('cursos/', views.cursos, name="Cursos"),
    path('entregables/', views.entregables, name="Entregables")
]