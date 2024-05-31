from django import forms
from .models import Citas
from .models import Empleado
from .models import Servicio

class CitasForm(forms.ModelForm):
    class Meta:
        model = Citas
        fields = ['id','nombre','apellido','correo','documento','fecha','hora','servicio','estilista']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['fecha'].widget.attrs.update({
            'min': '2022-09-28',
            'max': '2025-09-28',
        })

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['foto','name','apellido','disponibilidad','servicio']

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['id','foto','nombre']


