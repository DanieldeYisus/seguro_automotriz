from django import forms
from .models import Poliza, Asegurado, Vehiculo, Siniestro


#FORMULARIO CREACION POLIZA
class PolizaForm(forms.ModelForm):
    class Meta:
        model = Poliza
        fields = '__all__'
        widgets = {
            'id_poliza': forms.NumberInput(attrs={'class': 'required form-control', 'placeholder': 'Ingresa id póliza'}),
            'vigente': forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Ingresa estado vigencia'}),
            'fecha_inicio': forms.TextInput(attrs={'class': 'required form-control', 'type': 'date'}),
            'fecha_fin': forms.TextInput(attrs={'class': 'required form-control', 'type': 'date'}),
            'firma': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa firma'}),
            'asegurado_rut_asegurado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingresa rut asegurado'}),
            'vehiculo_patente_vehiculo': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingresa patente vehículo'})
        }

#FORMULARIO CREACION ASEGURADO
class AseguradoForm(forms.ModelForm):

    class Meta:
        model = Asegurado
        fields = [
            'rut_asegurado',
            'primer_nombre',
            'segundo_nombre',
            'primer_apellido',
            'segundo_apeliido',
            'correo',
            'telefono',
            'fecha_nacimiento',
            'usuario_rut_usuario'
        ]
        widgets = {
            'rut_asegurado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su rut'}),
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su primer nombre'}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su segundo nombre'}),
            'primer_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su primer apellido'}),
            'segundo_apeliido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su segundo apellido'}),
            'correo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su correo'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su teléfono'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'usuario_rut_usuario': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingresa rut usuario'}),
        }


class SiniestroForm(forms.ModelForm):
    class Meta:
        model = Siniestro
        fields = '__all__'
        widgets = {
            'nro_siniestro': forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Ingresa n° de siniestro'}),
            'fecha_hr': forms.TextInput(attrs={'class': 'required form-control', 'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'class': 'required form-control', 'placeholder': 'Ingrea una descripción'}),
            'parte_policial': forms.FileInput(attrs={'class': 'form-control'}),
            'foto_licencia': forms.FileInput(attrs={'class': 'form-control'}),
            'tipo_accidente_id_tipo_acc': forms.Select(attrs={'class': 'required form-control', 'placeholder': 'Ingresa tipo accidente'}),
            'est_siniestro_id_est_siniestro': forms.Select(attrs={'class': 'required form-control', 'placeholder': 'Ingresa estado siniestro'}),
            'taller_id_taller': forms.Select(attrs={'class': 'required form-control', 'placeholder': 'Ingresa id taller'}),
            'grua_patente_grua': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingresa patente grúa'}),
            'usuario_rut_usuario': forms.Select(attrs={'class': 'required form-control', 'placeholder': 'Ingresa rut asegurado'}),
            'poliza_id_poliza': forms.Select(attrs={'class': 'required form-control', 'placeholder': 'Ingresa id póliza'}),
        }

#FORMULARIO BORRADO LOGICO ASEGURADO
class DeshabilitarAseguradoForm(forms.ModelForm):

    class Meta:
        model = Asegurado
        fields =['estado']

#FORMULARIO CREACION VEHICULO
class VehiculoForm(forms.ModelForm):

    class Meta:
        model = Vehiculo
        fields = [
        'patente_vehiculo',
        'anio',
        'modelo',
        'nro_motor',
        'tipo_vehiculo_id_tipo_auto',
        'marca_id_marca',
        'asegurado_rut_asegurado'
        ]
        widgets = {
            'patente_vehiculo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa patente'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa año (YYYY)'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa modelo'}),
            'nro_motor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su número del motor'}),
            'tipo_vehiculo_id_tipo_auto': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingresa tipo de vehículo'}),
            'marca_id_marca': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingresa marca'}),
            'asegurado_rut_asegurado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingresa rut usuario'}),
        }

