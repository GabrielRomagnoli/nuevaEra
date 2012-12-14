from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login, logout
from musica.models import Artista, Tema
from musica.forms import ComentarioForm

def index(request):
    temas = Tema.objects.all()
    return render(request, "musica/index.html", {'temas' : temas})
    
def detalle(request, tema_id):
    #pedir el tema filtrando con el id y despues pasar los datos al template
    tema = Tema.objects.filter(pk=tema_id)[0]
    
    #manejo del formulario del comentario
    if request.user.is_authenticated():        
        if request.method == "POST":
            form = ComentarioForm(request.POST)
            if form.is_valid():
                comentario = form.save(tema, request.user)
                return redirect("musica_detalle", tema_id)
        else:
            form = ComentarioForm()
        return render(request, "musica/detalle.html", {'tema' : tema, 'form': form })
    return render(request, "musica/detalle.html", {'tema' : tema})
    
    return render(request, "musica/detalle.html", {'tema': tema, 'form' : form })

def comentar(request):
    return render(request, "musica/comentar.html", {'user': 'Gabriel'})
    