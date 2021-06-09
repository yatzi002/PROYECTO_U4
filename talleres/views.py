from django.shortcuts import render
from .models import Alumnos, Administradores, Talleres
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login


# Create your views here. 


def index_view(request):
	return render(request, '../templates/index.html', {})

def login_view(request):
	return render(request, '../templates/login.html', {})

def formulario_view(request):
	return render(request, '../templates/formulario.html', {})



@permission_required('login_view')
def adminTalleres_view(request):
	qs_Alumnos = Alumnos.objects.filter(id_taller=1)
	return render(request, '../templates/adminTalleres.html', {'vAlumnos':qs_Alumnos})

def altasA_view(request):
	return render(request, '../templates/altasA.html', {})

def altasT_view(request):
	return render(request, '../templates/altasT.html', {})

def bajasA_view(request):
	return render(request, '../templates/bajasA.html', {})

def bajasT_view(request):
	return render(request, '../templates/bajasT.html', {})

def cambiosA_view(request):
	return render(request, '../templates/cambiosA.html', {})

def cambiosT_view(request):
	return render(request, '../templates/cambiosT.html', {})

def consultasA_view(request):
	return render(request, '../templates/consultasA.html', {})

def consultasT_view(request):
	return render(request, '../templates/consultasT.html', {})
