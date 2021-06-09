from django.urls import path
from talleres import views
from django.contrib.auth.models import User
from .models import Administradores, Talleres, Alumnos
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('', views.index_view, name= 'index_view'),
	path('login', views.login_view, name= 'login_view'),
	path('formulario', views.formulario_view, name= 'formulario_view'),
	path('adminTalleres', login_required(views.adminTalleres_view), name = 'adminTalleres_view'),
	path('altasA', views.altasA_view, name = 'altasA_view'),
	path('altasT', views.altasT_view, name = 'altasT_view'),
	path('bajasA', views.bajasA_view, name = 'bajasA_view'),
	path('bajasT', views.bajasT_view, name = 'bajasT_view'),
	path('cambiosA', views.cambiosA_view, name = 'cambiosA_view'),
	path('cambiosT', views.cambiosT_view, name = 'cambiosT_view'),
	path('consultasA', views.consultasA_view, name = 'consultasA_view'),
	path('consultasT', views.consultasT_view, name = 'consultasT_view'),

]  