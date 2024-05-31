from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings


from dajj.forms import *




def index(request):
    return render(request, 'index.html', {
        # conext
        'mensaje': 'este es el contexto o diccionario Productos',
        'prod1': 'Maleta',
        'prod2': 'Audífonos',
        'prod3': 'Celular',
    })

    
def contacto(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        template = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'message': message
        })
    
        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['danielfernando0u@gmail.com']#correo empleado
        )
    
        email.fail_silently = False
        email.send()
    
    return render(request, 'contacto.html',{

    })
	 


def indexlogin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('citas')
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'indexlogin.html',{

    })

def Asignacion(request):
    return render(request, 'Asignacion.html', {

    })

def BuscarUsuario(request):
    return render(request, 'BuscarUsuario.html', {

    })

def consultarusuario(request):
    return render(request, 'consultarusuario.html', {

    })

def dashboardAdminCrearUsuario(request):
    return render(request, 'dashboardAdmin-CrearUsuario.html', {

    })

def dashboardAdminDisponibilidad(request):
    return render(request, 'dashboardAdmin-Disponivilidad.html', {

    })

def dashboardAdmin(request):
    return render(request, 'dashboardAdmin.html', {

    })

def dashboardAdminCrearCita(request):
    return render(request, 'dashboardAdminCrearCita.html', {

    })

def dashboardAsigHor(request):
    return render(request, 'dashboardAsigHor.html', {

    })

def dashboardAsistencia(request):
    return render(request, 'dashboardAsistencia.html', {

    })

def dashboardNuevoHorario(request):
    return render(request, 'dashboardNuevoHorario.html', {

    })

def Horario(request):
    return render(request, 'Horario.html', {

    })

def indexlogin(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username)
        print(password)

    return render(request, 'indexlogin.html', {

    })

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('indexlogin')#admin:index
    

def loginInvent(request):
    return render(request, 'loginInvent.html', {

    })


def quienessomos(request):
    return render(request, 'quienessomos.html', {

    })


def Registro(request):
    data = {
        "form": CustomUserCreationForm()
    }
    formulario = CustomUserCreationForm(data=request.POST)
    if request.method == 'POST':
     if formulario.is_valid():
        formulario.save()
        user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
        messages.success(request,"Te has registrado correctamente")
        return redirect(to="index")
    data['form'] = formulario
    return render(request,'Registro.html',data)



    







