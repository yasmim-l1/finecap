from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages import views

from .models import Reserva, Stand
from .forms import ReservaForm, StandForm

class HomeView(generic.TemplateView):
    template_name = "FINECAP/index.html"

##############################################################

class reserva_criarView(generic.CreateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("FINECAP:reserva_criar")
    template_name = "FINECAP/reserva.html"
    success_message = "Reserva cadastrada com sucesso!"

class reserva_editarView(generic.UpdateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("FINECAP:reserva_editar")
    template_name = "FINECAP/reserva.html"

class reserva_removerView(generic.DeleteView):
    model = Reserva
    success_url = reverse_lazy("FINECAP:reserva_remover")
    template_name = "FINECAP/reserva_exclusao.html"

class reserva_listarView(generic.ListView):
    model = Reserva
    template_name = "FINECAP/listagem.html"

class reserva_detalheView(generic.DetailView):
    model = Reserva
    template_name = "FINECAP/detalhe.html"

############################################################

class stand_criarView(generic.CreateView):
    model = Stand
    form_class = StandForm
    success_url = reverse_lazy("FINECAP:stand_criar")
    template_name = "FINECAP/stand.html"
    success_message = "Reserva cadastrada com sucesso!"

class stand_editarView(generic.UpdateView):
    model = Stand
    form_class = StandForm
    success_url = reverse_lazy("FINECAP:stand_editar")
    template_name = "FINECAP/stand.html"

class stand_removerView(generic.DeleteView):
    model = Stand
    success_url = reverse_lazy("FINECAP:stand_remover")
    template_name = "FINECAP/stand_exclusao.html"

class stand_listarView(generic.ListView):
    model = Stand
    template_name = "FINECAP/listagem.html"

class stand_detalheView(generic.DetailView):
    model = Stand
    template_name = "FINECAP/detalhe_stand.html"