from django.urls import path
from . import views

app_name = 'app_vuelos'  # ← ESTE ES EL NAMESPACE CORRECTO

urlpatterns = [
    path('', views.listar_aviones, name='listar_aviones'),
    path('aviones/', views.listar_aviones, name='listar_aviones'),
    path('vuelos/', views.listar_vuelos, name='listar_vuelos'),
    path('avion/<int:avion_id>/', views.detalle_avion, name='detalle_avion'),
    path('avion/crear/', views.crear_avion, name='crear_avion'),
    path('avion/editar/<int:avion_id>/', views.editar_avion, name='editar_avion'),
    path('avion/borrar/<int:avion_id>/', views.borrar_avion, name='borrar_avion'),
    path('avion/<int:avion_id>/vuelo/crear/', views.crear_vuelo, name='crear_vuelo'),
    path('vuelo/editar/<int:vuelo_id>/', views.editar_vuelo, name='editar_vuelo'),
    path('vuelo/borrar/<int:vuelo_id>/', views.borrar_vuelo, name='borrar_vuelo'),
    path('vuelo/<int:vuelo_id>/', views.detalle_vuelo, name='detalle_vuelo'),
]