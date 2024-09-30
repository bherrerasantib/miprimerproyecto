from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse # type: ignore
from .forms import PersonaForm
from .models import Persona

def crear_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('persona_creada')
    else:
        form = PersonaForm()

    return render(request, 'personas/crear_persona.html', {'form': form})

def persona_creada(request):
    return render(request, 'personas/persona_creada.html')

def home_view(request):
    return render(request, 'home.html')

def personas_view(request):
    return render(request, 'personas/personas.html')

def lista_personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas/lista_personas.html', {'personas': personas})