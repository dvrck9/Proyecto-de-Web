from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario, Restaurante, Reserva
from .serializers import UsuarioSerializer, RestauranteSerializer, ReservaSerializer
from django.views.generic import TemplateView

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class RestauranteViewSet(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class HomeView(TemplateView):
    template_name = "home.html"
