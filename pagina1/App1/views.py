from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "App1/index.html")

def cursos(request):
    return HttpResponse("Vista cursos")

def profesores(request):
    return HttpResponse("Vista Profesores")

def estudiantes(request):
    return HttpResponse("Vista estudiantes")

def entregables(request):
    return HttpResponse("Vista entregables")