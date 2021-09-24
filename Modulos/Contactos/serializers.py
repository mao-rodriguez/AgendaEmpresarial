from rest_framework import serializers
from .models import *

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('NIT', 'Nombre', 'Telefono', 'Direccion', 'Ciudad')