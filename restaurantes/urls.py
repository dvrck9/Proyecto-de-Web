from django.urls import path, include
from rest_framework import routers
from .views import UsuarioViewSet, RestauranteViewSet, ReservaViewSet

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'restaurantes', RestauranteViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
