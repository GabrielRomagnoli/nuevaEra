from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.template.context import RequestContext

def index(request):
    return render(request, "musica/index.html", {'user': 'Gabriel'})
    
def detalle(request):
    return render(request, "musica/detalle.html", {'user': 'Gabriel'})

def comentar(request):
    return render(request, "musica/comentar.html", {'user': 'Gabriel'})
    
