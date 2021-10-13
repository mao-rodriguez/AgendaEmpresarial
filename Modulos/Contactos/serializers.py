from rest_framework import serializers
from .models import *

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('id', 'NIT', 'Nombre', 'Telefono', 'Direccion', 'Ciudad')
class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = (
                    'id',
                    'Nombre',
                    'Apellido',
                    'Compañia',
                    'Cargo',
                    'Email',
                    'Celular',
                    'Direccion',
                    'Ciudad',
                    'Estado'
                )