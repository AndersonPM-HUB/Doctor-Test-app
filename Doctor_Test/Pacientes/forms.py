from django import forms
from .models import Paciente, historia


class PacienteForm(forms.ModelForm): 
    class Meta:
        model = Paciente
        fields ='__all__'


class HistoriaForm(forms.ModelForm): 
    class Meta:
        model = historia
        fields ='__all__'