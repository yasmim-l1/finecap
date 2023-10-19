from django.forms import ModelForm
from .models import Reserva, Stand

class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'

class StandForm(ModelForm):
    class Meta:
        model = Stand
        fields = '__all__'