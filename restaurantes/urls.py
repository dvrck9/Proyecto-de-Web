from django.urls import path, include
from rest_framework import routers
from .views import UsuarioViewSet, RestauranteViewSet, ReservaViewSet, HomeView

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'restaurantes', RestauranteViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # <-- Agrega esta línea
    path('api/', include(router.urls)),         # <-- Cambia '' por 'api/' aquí
]
