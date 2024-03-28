from django.urls import path
from .views import IsekaiStore, Figuras, Origenes, SigIn, LogIn, Carrito, Contactanos,\
    Agregar, Listar, Modificar, Eliminar, VerFigura
# Para las imagenes de las figuras
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', IsekaiStore, name="IsekaiStore"),
    path('figuras/', Figuras, name="Figuras"),
    path('origenes/', Origenes, name="Origenes"),
    path('sigIn/', SigIn, name="SigIn"),
    path('login/', LogIn, name="LogIn"),
    path('carrito/', Carrito, name="Carrito"),
    path('contacto/', Contactanos, name="Contactanos"),
    path('agregar/', Agregar, name="Agregar"),   
    path('listar/', Listar, name="Listar"),   
    path('modificar/<id>/', Modificar, name="Modificar"),   
    path('eliminar/<id>/', Eliminar, name="Eliminar"), 
    path('vistaFigura/<str:id>/', VerFigura, name="VerFigura"), 
      
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
