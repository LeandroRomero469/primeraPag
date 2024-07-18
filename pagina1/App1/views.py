from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "App1/index.html")

def cursos(request):
    return render(request, "Vista cursos")

def profesores(request):
    return render(request, "Vista Profesores")

def estudiantes(request):
    return render(request, "Vista estudiantes")

def entregables(request):
    return render(request, "Vista entregables")