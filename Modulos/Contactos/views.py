#from _typeshed import Self
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContactoSerializer, EmpresaSerializer
from .models import *
from rest_framework.filters import SearchFilter

# Create your views here.

class EmpresaView(viewsets.ModelViewSet):
    search_fields = ['=NIT']
    filter_backends = (SearchFilter,)
    serializer_class = EmpresaSerializer
    queryset = Empresa.objects.all()
    
class ContactoView(viewsets.ModelViewSet):
    search_fields = ['Nombre', 'Apellido']
    filter_backends = (SearchFilter,)
    serializer_class = ContactoSerializer
    queryset = Contacto.objects.all()
