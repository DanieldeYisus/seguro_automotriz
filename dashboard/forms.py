from django import forms
from .models import Poliza


class PolizaForm(forms.ModelForm):
    class Meta:
        model = Poliza
        fields = ['id_poliza', 'vigente',
                  'fecha_inicio', 'fecha_fin', 'firma', 'asegurado_rut_asegurado', 'vehiculo_patente_vehiculo']
        widgets = {
            'id_poliza': forms.NumberInput(attrs={'class': 'required form-control', 'placeholder': 'Ingresa ID póliza'}),
            'vigente': forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Ingresa estado vigencia'}),
            'fecha_inicio': forms.TextInput(attrs={'class': 'required form-control', 'type': 'date'}),
            'fecha_fin': forms.TextInput(attrs={'class': 'required form-control', 'type': 'date'}),
            'firma': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa firma'}),
            'asegurado_rut_asegurado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa rut asegurado'}),
            'vehiculo_patente_vehiculo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa patente vehículo'})
        }
