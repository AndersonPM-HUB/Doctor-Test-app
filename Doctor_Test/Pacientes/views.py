
from .models import Paciente, historia, diagnostico
from .serializers import PacienteSerializer, HistoriaSerializer, DiagnosticoSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class Pacientes_api(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    
    
class Historia_api(viewsets.ModelViewSet):
    queryset = historia.objects.all()
    serializer_class = HistoriaSerializer
    
class Diagnostico_api(viewsets.ModelViewSet):
    queryset = diagnostico.objects.all()
    serializer_class = DiagnosticoSerializer

