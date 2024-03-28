from django.shortcuts import render, redirect, get_object_or_404
from .models import Figura, Carro, Origen
from django.contrib.auth.decorators import login_required, permission_required
from .forms import ContactoForm, FiguraForm, RegisterForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login


# Create your views here.

#Inicio
def IsekaiStore(request):
    return render(request, 'app/isekaiStore.html')

#Figuras
def Figuras(request):
    figuras = Figura.objects.all()
    return render(request, 'app/figuras.html', {'figuras': figuras})

#Origenes
def Origenes(request):
    origenes = Origen.objects.all()
    return render(request, 'app/origenes.html', {'origenes': origenes})

#Registrarse
def SigIn(request):
    data = {
        'form':RegisterForm
    }
    if request.method == 'POST':
        formulario = RegisterForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registro exitoso!")
            return redirect(to='IsekaiStore')
        else:
            data['form'] = formulario
    return render(request, 'registration/sigIn.html', data)

#Iniciar sesión
def LogIn(request):
    return render(request, 'accounts/login')

#Carrito
def Carrito(request):
    figuras = Figura.objects.all()
    return render(request, 'app/carrito.html', {'figuras': figuras})


#Contacto
def Contactanos(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Formulario enviado")
        else:
            data['form'] = formulario
    
    
    return render(request, 'app/contacto.html', data)

#Agregar
@permission_required('mainApp.add_figura')
def Agregar(request):
    data = {
        'form': FiguraForm()
    }
    if request.method == 'POST':
        formulario = FiguraForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado Correctamente")
        else:
            data['form'] = formulario
    return render(request, 'app/crudAdmin/agregar.html', data)

#Listar
@permission_required('mainApp.view_figura')
def Listar(request):
    figuras = Figura.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(figuras, 5)
        figuras = paginator.page(page)
    except:
        raise Http404
    
    data={
        'entity':figuras,
        'paginator':paginator
    }
    return render(request, 'app/crudAdmin/listar.html', data)

#Modificar
@permission_required('mainApp.change_figura')
def Modificar (request, id):
    figura = get_object_or_404(Figura, id=id)
    data = {
        'form': FiguraForm(instance=figura)
    }    
    if request.method == 'POST':
        formulario = FiguraForm(data=request.POST,instance=figura ,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modficado correctamente")
            return redirect(to="Listar")
        else:
            data['form'] = formulario
    return render(request, 'app/crudAdmin/modificar.html', data)

#Eliminar
@permission_required('mainApp.delete_figura')
def Eliminar(request, id):
    figura = get_object_or_404(Figura, id=id)
    figura.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="Listar")

#Vista figura
def VerFigura(request, id):
    figuras = get_object_or_404(Figura, id=id)
    data={'figuras':figuras, 'title':figuras.nombre}
    return render(request,'app/vistaFigura.html', data)
    