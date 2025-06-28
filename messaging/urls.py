from django.urls import path
from .views import bandeja_view, detalle_mensaje_view, enviar_mensaje_view

urlpatterns = [
    path('', bandeja_view, name='bandeja'),
    path('nuevo/', enviar_mensaje_view, name='enviar_mensaje'),
    path('<int:pk>/', detalle_mensaje_view, name='detalle_mensaje'),
]