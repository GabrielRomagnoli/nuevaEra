# Create your views here.
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from core.forms import UserForm
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, "core/home.html")

def registrar(request):
    if request.user.is_authenticated():
        return redirect("core_home")
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("core_home")
    return render(request, "core/registrar.html", {'form': form })


def loguearse(request):
    username = request.POST['username']
    password = request.POST['password']
    print request.POST
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return redirect("core_home")
        else:
            # Return a 'disabled account' error message
            return error(request, "La cuenta esta deshabilitada")
    else:
        # Return an 'invalid login' error message.
        return error(request, "La cuenta es invalida")

    
def error(request, mensaje):
    return render(request, "core/error.html", { 'msj' : mensaje })

def desloguearse(request):
    logout(request)
    return redirect("core_home")