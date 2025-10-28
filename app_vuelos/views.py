from django.shortcuts import render, get_object_or_404, redirect
from .models import Avion, Vuelo
from .forms import AvionForm, VueloForm

def listar_aviones(request):
    aviones = Avion.objects.all()
    return render(request, 'listar_aviones.html', {'aviones': aviones})

def detalle_avion(request, avion_id):
    avion = get_object_or_404(Avion, id_avion=avion_id)
    vuelos_del_avion = avion.vuelos.all()
    return render(request, 'detalle_avion.html', {'avion': avion, 'vuelos_del_avion': vuelos_del_avion})

def crear_avion(request):
    if request.method == 'POST':
        form = AvionForm(request.POST, request.FILES)  # ← AGREGADO request.FILES
        if form.is_valid():
            form.save()
            return redirect('app_vuelos:listar_aviones')
    else:
        form = AvionForm()
    return render(request, 'formulario_avion.html', {'form': form, 'titulo': 'Crear Avión'})

def editar_avion(request, avion_id):
    avion = get_object_or_404(Avion, id_avion=avion_id)
    if request.method == 'POST':
        form = AvionForm(request.POST, request.FILES, instance=avion)  # ← AGREGADO request.FILES
        if form.is_valid():
            form.save()
            return redirect('app_vuelos:detalle_avion', avion_id=avion.id_avion)
    else:
        form = AvionForm(instance=avion)
    return render(request, 'formulario_avion.html', {'form': form, 'titulo': 'Editar Avión'})

def borrar_avion(request, avion_id):
    avion = get_object_or_404(Avion, id_avion=avion_id)
    if request.method == 'POST':
        avion.delete()
        return redirect('app_vuelos:listar_aviones')
    return render(request, 'confirmar_borrar_avion.html', {'avion': avion})

def crear_vuelo(request, avion_id):
    avion = get_object_or_404(Avion, id_avion=avion_id)
    if request.method == 'POST':
        form = VueloForm(request.POST)
        if form.is_valid():
            vuelo = form.save(commit=False)
            vuelo.id_avion = avion
            vuelo.save()
            return redirect('app_vuelos:detalle_avion', avion_id=avion.id_avion)
    else:
        form = VueloForm()
    return render(request, 'formulario_vuelo.html', {'form': form, 'titulo': f'Crear Vuelo para {avion.modelo_avion}', 'avion': avion})

def editar_vuelo(request, vuelo_id):
    vuelo = get_object_or_404(Vuelo, id_vuelo=vuelo_id)
    if request.method == 'POST':
        form = VueloForm(request.POST, instance=vuelo)
        if form.is_valid():
            form.save()
            return redirect('app_vuelos:detalle_avion', avion_id=vuelo.id_avion.id_avion)
    else:
        form = VueloForm(instance=vuelo)
    return render(request, 'formulario_vuelo.html', {'form': form, 'titulo': f'Editar Vuelo: {vuelo.numero_vuelo}', 'avion': vuelo.id_avion})

def borrar_vuelo(request, vuelo_id):
    vuelo = get_object_or_404(Vuelo, id_vuelo=vuelo_id)
    avion_id = vuelo.id_avion.id_avion
    if request.method == 'POST':
        vuelo.delete()
        return redirect('app_vuelos:detalle_avion', avion_id=avion_id)
    return render(request, 'confirmar_borrar_vuelo.html', {'vuelo': vuelo, 'avion': vuelo.id_avion})

# Vista adicional para listar todos los vuelos
def listar_vuelos(request):
    vuelos = Vuelo.objects.all().select_related('id_avion')
    return render(request, 'listar_vuelos.html', {'vuelos': vuelos})

# Vista para detalle de vuelo individual
def detalle_vuelo(request, vuelo_id):
    vuelo = get_object_or_404(Vuelo, id_vuelo=vuelo_id)
    return render(request, 'detalle_vuelo.html', {'vuelo': vuelo})