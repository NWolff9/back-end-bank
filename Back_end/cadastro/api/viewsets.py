from rest_framework import viewsets
from cadastro.api.serializers import ClienteSerializer
from cadastro.models import Cliente

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer