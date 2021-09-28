#from _typeshed import Self
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContactoSerializer, EmpresaSerializer
from .models import *

# Create your views here.

class EmpresaView(viewsets.ModelViewSet):
    serializer_class = EmpresaSerializer
    queryset = Empresa.objects.all()
    
class ContactoView(viewsets.ModelViewSet):
    serializer_class = ContactoSerializer
    queryset = Contacto.objects.all()