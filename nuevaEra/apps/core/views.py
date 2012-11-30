# Create your views here.
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.template.context import RequestContext

    
def home(request):
    return render(request, "core/home.html", {'user': 'Gabriel'}, content_type="text/css")