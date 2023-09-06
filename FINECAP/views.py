from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva
from .forms import ReservaForm

def index(request):
    return render(request, 'FINECAP/index.html')

def reserva_criar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)

        if form.is_valid():
            form.save()
            form = ReservaForm()

    else:
        form = ReservaForm()

    return render(request, 'FINECAP/reserva.html', {'form':form})

def reserva_editar(request, id):
    reserva = get_object_or_404(Reserva,id=id)

    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('reserva_listar')
        
    else:
        form = ReservaForm(instance=reserva)

    return render(request, 'FINECAP/reserva.html', {'form':form})

def reserva_remover(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('reserva_listar')

def reserva_listar(request):
    reservas = Reserva.objects.all()

    return render(request, 'FINECAP/listagem.html', {'reservas':reservas})

def reserva_detalhe(request, id):
    reserva = get_object_or_404(Reserva, id=id)

    return render(request, 'FINECAP/detalhe.html', {'reserva':reserva})