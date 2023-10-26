from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Reserva, Stand
from .forms import ReservaForm, StandForm

class HomeView(generic.TemplateView):
    template_name = "FINECAP/index.html"

##############################################################

class reserva_criarView(generic.CreateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("reserva_listar")
    template_name = "FINECAP/reserva.html"

    def form_valid(self, form):
        messages.success(self.request, 'Reserva Criada Com Sucesso!')
        return super().form_valid(form)

class reserva_editarView(generic.UpdateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("reserva_listar")
    template_name = "FINECAP/reserva.html"

class reserva_removerView(generic.DeleteView):
    model = Reserva
    success_url = reverse_lazy("reserva_listar")
    template_name = "FINECAP/messages/reserva_exclusao.html"

    def form_valid(self, form):
        messages.success(self.request, 'A Reserva Foi Excluída Com Sucesso!')
        return super().form_valid(form)

class reserva_listarView(generic.ListView):
    model = Reserva
    template_name = "FINECAP/listagem.html"
    context_object_name = 'reservas'
    paginate_by = 5
    
class reserva_detalheView(generic.DetailView):
    model = Reserva
    template_name = "FINECAP/detalhe.html"

############################################################

class stand_criarView(generic.CreateView):
    model = Stand
    form_class = StandForm
    success_url = reverse_lazy("stand_listar")
    template_name = "FINECAP/stand.html"
    
    def form_valid(self, form):
        messages.success(self.request, 'Stand Criado Com Sucesso!')
        return super().form_valid(form)

class stand_editarView(generic.UpdateView):
    model = Stand
    form_class = StandForm
    success_url = reverse_lazy("stand_listar")
    template_name = "FINECAP/stand.html"

class stand_removerView(generic.DeleteView):
    model = Stand
    success_url = reverse_lazy("stand_listar")
    template_name = "FINECAP/messages/stand_exclusao.html"

    def form_valid(self, form):
        messages.success(self.request, 'O Stand Foi Excluído Com Sucesso!')
        return super().form_valid(form)

class stand_listarView(generic.ListView):
    model = Stand
    template_name = "FINECAP/listagem_stand.html"
    context_object_name = 'stands'
    paginate_by = 5

class stand_detalheView(generic.DetailView):
    model = Stand
    template_name = "FINECAP/detalhe_stand.html"