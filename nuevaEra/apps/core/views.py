# Create your views here.
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from core.forms import UserForm
    
def home(request):
    return render(request, "core/home.html", {'user': 'Gabriel'})

def registrar(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        #hacer algo aca
        post.save()
        return redirect(reverse("core_home"))
    return render(request, "core/registrar.html", {'form': form})