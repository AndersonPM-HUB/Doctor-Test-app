from .models import Paciente
from rest_framework import serializers

#manipular objeros json

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields= '__all__'
