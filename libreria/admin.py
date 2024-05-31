from django.contrib import admin
from .models import Citas, Dia, Servicio, Empleado
# Register your models here.
admin.site.register(Citas)
admin.site.register(Dia)
admin.site.register(Servicio)
admin.site.register(Empleado)