from .models import Paciente, historia
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
