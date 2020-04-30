
from django.urls import path
from django.conf.urls import url, include
from .views import DashboardView, SiniestroView, UsuariosView, TallerView
from . import views

urlpatterns = [

    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('siniestros/', views.SiniestroView, name='siniestros'),
    path('siniestros/create', views.CreateSiniestro, name='siniestro_create'),
    path('siniestros/<str:id>/update',views.UpdateSiniestro,name='siniestro_update'),
    path('siniestros/<str:id>/delete',views.DeleteSiniestro,name='siniestro_delete'),
    path('taller/', views.TallerView, name='taller'),
    path('usuarios/', views.UsuariosView, name='usuarios'),
    path('asegurados/', views.AseguradosView, name='asegurados'),
    path('asegurados/create/', views.AseguradoCreate, name='asegurado_create'),
    path('asegurados/<str:id>/update/',views.AseguradoUpdate,name='asegurado_update'),
    path('vehiculos/', views.VehiculosView, name='vehiculos'),
    path('polizas/', views.PolizasView, name='polizas'),
    path('polizas/create', views.CreatePoliza, name='poliza_create'),
    path('polizas/<str:id>/update',views.UpdatePoliza,name='poliza_update'),
    path('polizas/<str:id>/delete',views.DeletePoliza,name='poliza_delete'),
]
