#from _typeshed import Self
from rest_framework import status, viewsets
from .serializers import ContactoSerializer, EmpresaSerializer
from .models import *
from rest_framework.filters import SearchFilter
from django.http import Http404
from rest_framework.response import Response

# Create your views here.

class EmpresaView(viewsets.ModelViewSet):
    search_fields = ['=NIT']
    filter_backends = (SearchFilter,)
    serializer_class = EmpresaSerializer
    queryset = Empresa.objects.all()
    
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ContactoView(viewsets.ModelViewSet):
    search_fields = ['Nombre', 'Apellido']
    filter_backends = (SearchFilter,)
    serializer_class = ContactoSerializer
    queryset = Contacto.objects.all()
    
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)
