
from .models import Paciente, historia
from .serializers import PacienteSerializer, HistoriaSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class Pacientes_api(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    
    
class Historia_api(viewsets.ModelViewSet):
    queryset = historia.objects.all()
    serializer_class = HistoriaSerializer
    


