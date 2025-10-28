from django import forms
from .models import Avion, Vuelo
from django.utils import timezone

class AvionForm(forms.ModelForm):
    class Meta:
        model = Avion
        fields = ['modelo_avion', 'capacidad_pasajeros', 'anio_fabricacion', 'estado_mantenimiento', 'horas_vuelo', 'foto']
        widgets = {
            'modelo_avion': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad_pasajeros': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'max': '1000'
            }),
            'anio_fabricacion': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1900',
                'max': '2024'
            }),
            'estado_mantenimiento': forms.Select(attrs={'class': 'form-control'}),
            'horas_vuelo': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'modelo_avion': 'Modelo del Avión',
            'capacidad_pasajeros': 'Capacidad de Pasajeros',
            'anio_fabricacion': 'Año de Fabricación',
            'estado_mantenimiento': 'Estado de Mantenimiento',
            'horas_vuelo': 'Horas de Vuelo Acumuladas',
            'foto': 'Foto del Avión',
        }

    def clean_capacidad_pasajeros(self):
        capacidad = self.cleaned_data.get('capacidad_pasajeros')
        if capacidad <= 0:
            raise forms.ValidationError("La capacidad debe ser mayor a 0")
        return capacidad

    def clean_anio_fabricacion(self):
        anio = self.cleaned_data.get('anio_fabricacion')
        if anio < 1900 or anio > 2024:
            raise forms.ValidationError("Ingrese un año válido entre 1900 y 2024")
        return anio

class VueloForm(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = ['numero_vuelo', 'origen', 'destino', 'fecha_hora_salida', 'id_avion']
        widgets = {
            'numero_vuelo': forms.TextInput(attrs={'class': 'form-control'}),
            'origen': forms.TextInput(attrs={'class': 'form-control'}),
            'destino': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_hora_salida': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'id_avion': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'numero_vuelo': 'Número de Vuelo',
            'origen': 'Ciudad de Origen',
            'destino': 'Ciudad de Destino',
            'fecha_hora_salida': 'Fecha y Hora de Salida',
            'id_avion': 'Avión Asignado',
        }

    def clean_fecha_hora_salida(self):
        fecha_hora = self.cleaned_data.get('fecha_hora_salida')
        if fecha_hora and fecha_hora < timezone.now():
            raise forms.ValidationError("La fecha y hora de salida no puede ser en el pasado")
        return fecha_hora

    def clean(self):
        cleaned_data = super().clean()
        origen = cleaned_data.get('origen')
        destino = cleaned_data.get('destino')
        
        if origen and destino and origen.lower() == destino.lower():
            raise forms.ValidationError("El origen y destino no pueden ser la misma ciudad")
        
        return cleaned_data