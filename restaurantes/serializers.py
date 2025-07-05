from rest_framework import serializers
from .models import Usuario, Restaurante, Reserva

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    restaurante = RestauranteSerializer(read_only=True)

    class Meta:
        model = Reserva
        fields = '__all__'
