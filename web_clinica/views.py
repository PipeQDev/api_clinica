from django.shortcuts import render, redirect
from api.models import *
# Create your views here.


def index(request):
    return render(request, "index.html", {"index": index})


def pacientes(request):
    paciente = Paciente.objects.all()
    return render(request, "pacientes.html", {"pacientes": paciente})


def doctores(request):
    doctores = Doctor.objects.all()
    return render(request,  "doctores.html", {"doctores": doctores})

def fichas(request):
    fichas = Ficha_Atencion.objects.all()
    return render(request, "fichas.html", {"fichas":fichas})