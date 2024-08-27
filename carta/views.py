from django.shortcuts import render, HttpResponse
from .models import Product
# Create your views here.
# request -> response

def inicio(request):
    """Renderiza la página de inicio."""
    template_name = 'home.html'
    return render(request, template_name)

def menu(request):
    productos = Product.objects.all()    
    return render(request, 'menu.html', {'productos': productos})

def localizaciones(request):
    """Renderiza la página de ubicaciones."""
    template_name = 'localizacion.html'
    return render(request, template_name)

