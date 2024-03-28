from django.db import models

# Create your models here.
#Clase origen
class Origen(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    imagen = models.ImageField(upload_to='imagenes/origen', verbose_name ="Imagen" ,null=True)

    def __str__(self):
        return self.nombre
        
    
    #Borrar imgs del admin
    def delete(self, using=None, keep_parent=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
        
        
        
#Clase fabricante
class Fabricante(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    imagen = models.ImageField(upload_to='imagenes/fabricante', verbose_name ="Imagen" ,null=True)

    def __str__(self):
        return self.nombre
        
    
    #Borrar imgs del admin
    def delete(self, using=None, keep_parent=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

#Clase figura
class Figura(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    origen = models.ForeignKey(Origen, on_delete=models.PROTECT, verbose_name="Origen")
    fabricante = models.ForeignKey(Fabricante, on_delete=models.PROTECT, verbose_name="Fabricante")
    imagen = models.ImageField(upload_to='imagenes/figuras', verbose_name ="Imagen" ,null=True)
    escala = models.CharField(max_length=50, verbose_name="escala")
    precio = models.IntegerField(verbose_name="Precio")
    descripcion = models.CharField(max_length=1000, verbose_name="Descripción")    
    cantidad = models.IntegerField(verbose_name="Cantidad")
    
    def __str__(self):
        return self.nombre
    
    #Borrar imgs del admin
    def delete(self, using=None, keep_parent=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()


#Clase carro
class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session["carro"]
        if not carro:
            self.session["carro"] = {}
            self.carro = self.session["carro"]
        else:
            self.carro = carro
    
    def agregar(self, Figura):
        id = str(Figura.id)
        if id not in self.carro.keys():
            self.carro[id]={
                "id_figura":Figura.id,
                "nombre": Figura.titulo,
                "acumulado": Figura.precio,
                "cantidad": 1,
            }
        else:
            self.carro[id]["cantidad"]+=1
            self.carro[id]["acumulado"]+=Figura.precio
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carro"]=self.carro
        self.session.modified = True
    
    def eliminar(self, Figura):
        id = str(Figura.id)
        if id in self.carro:
            del self.carro[id]
            self.guardar_carrito()
    
    def restar(self, Figura):
        id= str(Figura.id)
        if id in self.carro.keys():
            self.carro[id]["cantidad"]-=1
            self.carro[id]["acumulado"]-= Figura.precio
            if self.carro[id]["cantidad"]<=0: self.eliminar(Figura)
            self.guardar_carrito()
    
    def limpiar(self):
        self.session["carro"]={}
        self.session.modified= True

#Clase contacto 

opciones_consulta = [
    [0,"Consulta"],
    [1,"Reclamo"],
    [2,"Sugerencia"],
    [3,"Felicitacion"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    correo = models.EmailField(verbose_name="Correo")
    tipo_consulta = models.IntegerField(choices=opciones_consulta, verbose_name="Tipo de consulta")
    mensaje = models.TextField(max_length=1000, verbose_name="Mensaje")
    avisos = models.BooleanField(verbose_name="Avisos")
    
    def __str__(self) :
        return self.nombre