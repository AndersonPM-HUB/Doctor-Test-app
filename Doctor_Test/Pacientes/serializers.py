from .models import Paciente, historia, diagnostico
from rest_framework import serializers

#manipular objeros json

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields= '__all__'


class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = historia
        fields= '__all__'

class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = diagnostico
        fields= '__all__'