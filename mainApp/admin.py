from django.contrib import admin
from .models import Figura, Origen, Contacto, Fabricante
# Register your models here.

class Homeadmin(admin.ModelAdmin):
    list_display =["id","nombre", "precio","cantidad"]
    list_editable = ["precio"]
    search_fields = ["nombre", "origen"]
    ordering = ('-id',)
    list_filter = ('origen',)
    list_per_page = 10
    
class Homeadmin2(admin.ModelAdmin):
    list_display =["id","nombre",]
    search_fields = ["nombre",]
    ordering = ('-id',)
    list_per_page = 10

class Homeadmin3(admin.ModelAdmin):
    list_display = ["id", "nombre", "tipo_consulta"]
    search_fields= ["tipo_consulta",]
    list_per_page = 10
    
class Homeadmin4(admin.ModelAdmin):
    list_display =["id","nombre",]
    search_fields = ["nombre",]
    ordering = ('-id',)
    list_per_page = 10

admin.site.register(Figura, Homeadmin)
admin.site.register(Origen, Homeadmin2)
admin.site.register(Contacto, Homeadmin3)
admin.site.register(Fabricante, Homeadmin4)