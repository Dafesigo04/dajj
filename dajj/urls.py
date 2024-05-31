"""dajj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from. import views
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls,name='admin:index'),
    path('', views.index,name='index'),
    path('contacto/', views.contacto,name='contacto'),
    path('Asignacion/', views.Asignacion, name=''),
    path('BuscarUsuario/', views.BuscarUsuario, name='BuscarUsuario'),
    path('consultarusuario/', views.consultarusuario, name='consultarusuario'),
    path('dashboardAdmin-CrearUsuario/', views.dashboardAdminCrearUsuario, name='dashboardAdmin-CrearUsuario'),
    path('dashboardAdmin-Disponibilidad/', views.dashboardAdminDisponibilidad, name='dashboardAdmin-Disponibilidad'),
    path('dashboardAdmin/', views.dashboardAdmin, name='dashboardAdmin'),
    path('dashboardAdminCrearCita/', views.dashboardAdminCrearCita, name='dashboardAdminCrearCita'),
    path('dashboardAsigHor/', views.dashboardAsigHor, name='dashboardAsigHor'),
    path('dashboardAsistencia/', views.dashboardAsistencia, name='dashboardAsistencia'),
    path('dashboardNuevoHorario/', views.dashboardNuevoHorario, name='dashboardNuevoHorario'),
    path('indexlogin/', views.indexlogin_view, name='indexlogin'),
    path('loginInvent/', views.loginInvent, name='loginInvent'),
    path('logoutporf/', views.logout_view, name='logoutporf'),
    path('quienessomos/', views.quienessomos, name='quienessomos'),
    #path('registro', views.register, name="registro")
    path('', include('libreria.urls')),
    path('registro/', views.Registro, name='registro')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
