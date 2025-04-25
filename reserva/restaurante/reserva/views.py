
from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva
from .forms import ReservaForm

def lista_reservas(request):
    reservas = Reserva.objects.all().order_by('data', 'horario')
    return render(request, 'lista_reservas.html', {'reservas': reservas})

def nova_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm()
    return render(request, 'reserva_form.html', {'form': form})

def editar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'reserva_form.html', {'form': form})

def deletar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        reserva.delete()
        return redirect('lista_reservas')
    return render(request, 'confirmar_delete.html', {'reserva': reserva})
