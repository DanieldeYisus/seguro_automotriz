from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from .models import Usuario, Taller, Asegurado, Vehiculo, Poliza
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import PolizaForm, AseguradoForm,DeshabilitarAseguradoForm,VehiculoForm


# Create your views here.


class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'


class SiniestrosView(TemplateView):
    template_name = 'dashboard/siniestros.html'


def TallerView(request):
    taller = Taller.objects.all().order_by('id_taller')
    context = {'taller': taller}
    return render(request, 'dashboard/taller.html', context)


def UsuariosView(request):
    usuarios = Usuario.objects.all().order_by('rol_id_rol')
    context = {'usuarios': usuarios}
    return render(request, 'dashboard/usuarios.html', context)

# CRUD ASEGURADO


def SaveAllAsegurado(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            asegurados = Asegurado.objects.all().order_by('fecha_nacimiento')
            context = {'asegurados': asegurados}
            data['asegurados'] = render_to_string(
                'dashboard/asegurados/asegurado_2.html', context)
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)

# READ
def AseguradosView(request):
    asegurados = Asegurado.objects.all().order_by('fecha_nacimiento')
    context = {'asegurados': asegurados}
    return render(request, 'dashboard/asegurados/asegurado.html', context)

# CREATE
def AseguradoCreate(request):
    if request.method == 'POST':
        form = AseguradoForm(request.POST)
    else:
        form = AseguradoForm()
    return SaveAllAsegurado(request, form, 'dashboard/asegurados/asegurado_create.html')

# UPDATE
def AseguradoUpdate(request, id):
    asegurado = get_object_or_404(Asegurado, rut_asegurado=id)
    if request.method == 'POST':
        form = AseguradoForm(request.POST, instance=asegurado)
    else:
        form = AseguradoForm(instance=asegurado)
    return SaveAllAsegurado(request, form, 'dashboard/asegurados/asegurado_update.html')

#DELETE
def AseguradoDelete(request, id):
    data = dict()
    asegurado = get_object_or_404(Asegurado, rut_asegurado=id)
    if request.method == 'POST':
        form = DeshabilitarAseguradoForm(request.POST,instance=asegurado)
        asegurado = form.save(commit=False)
        asegurado.estado = 0
        asegurado.save()
        form.save()
        data['form_is_valid'] = True
        asegurados = Asegurado.objects.all().order_by('fecha_nacimiento')
        context = {'asegurados': asegurados}
        data['asegurados'] = render_to_string(
            'dashboard/asegurados/asegurado_2.html', context)
    else:
        form = DeshabilitarAseguradoForm(instance=asegurado)
        data['form_is_valid'] = False
        context = {'asegurado': asegurado}
        data['html_form'] = render_to_string(
            'dashboard/asegurados/asegurado_delete.html', context, request=request)
    return JsonResponse(data)

#CRUD VEHICULOS
def SaveAllVehiculo(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            vehiculos = Vehiculo.objects.all().order_by('anio')
            context = {'vehiculos': vehiculos}
            data['vehiculos'] = render_to_string(
                'dashboard/vehiculos/vehiculo_2.html', context)
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)

#READ
def VehiculosView(request):
    vehiculos = Vehiculo.objects.all().order_by('anio')
    context = {'vehiculos': vehiculos}
    return render(request, 'dashboard/vehiculos/vehiculo.html', context)

#CREATE
def VehiculoCreate(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
    else:
        form = VehiculoForm()
    return SaveAllVehiculo(request, form, 'dashboard/vehiculos/vehiculo_create.html')

def SaveAll(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            polizas = Poliza.objects.all().order_by('-id_poliza')
            context = {'polizas': polizas}
            data['polizas'] = render_to_string(
                'dashboard/polizas/poliza_2.html', context)
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)


# Read
def PolizasView(request):
    polizas = Poliza.objects.all().order_by('-id_poliza')
    context = {'polizas': polizas}
    return render(request, 'dashboard/polizas/poliza.html', context)

# Create


def CreatePoliza(request):
    if request.method == 'POST':
        form = PolizaForm(request.POST)
    else:
        form = PolizaForm()
    return SaveAll(request, form, 'dashboard/polizas/poliza_create.html')

# Update


def UpdatePoliza(request, id):
    poliza = get_object_or_404(Poliza, id_poliza=id)
    if request.method == 'POST':
        form = PolizaForm(request.POST, instance=poliza)
    else:
        form = PolizaForm(instance=poliza)
    return SaveAll(request, form, 'dashboard/polizas/poliza_update.html')

# Delete


def DeletePoliza(request, id):
    data = dict()
    poliza = get_object_or_404(Poliza, id_poliza=id)
    if request.method == 'POST':
        poliza.delete()
        data['form_is_valid'] = True
        polizas = Poliza.objects.all().order_by('-id_poliza')
        context = {'polizas': polizas}
        data['polizas'] = render_to_string(
            'dashboard/polizas/poliza_2.html', context)
    else:
        context = {'poliza': poliza}
        data['html_form'] = render_to_string(
            'dashboard/polizas/poliza_delete.html', context, request=request)
    return JsonResponse(data)
