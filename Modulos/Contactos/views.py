from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmpresaSerializer
from .models import *

# Create your views here.

class EmpresaView(viewsets.ModelViewSet):
    serializer_class = EmpresaSerializer
    queryset = Empresa.objects.all()