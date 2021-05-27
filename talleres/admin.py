from django.contrib import admin

# Register your models here.
from .models import Talleres
admin.site.register(Talleres)

from .models import Administradores
admin.site.register(Administradores)

from .models import Alumnos
admin.site.register(Alumnos)
