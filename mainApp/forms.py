from django import forms
from .models import Contacto, Figura
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        
class FiguraForm(forms.ModelForm):
    
    
    class Meta:
        model = Figura
        fields = '__all__'
    
class RegisterForm(UserCreationForm):
    
    def clean_nombre(self):
        username =self.cleaned_data["nombre"]
        existe = User.objects.filter(username=username).exists()
        if existe:
            raise ValidationError("Ya existe un producto con ese nombre")
        return username
    
    class Meta:
        model = User
        fields = ["username", "first_name","last_name","email", "password1", "password2"]
        