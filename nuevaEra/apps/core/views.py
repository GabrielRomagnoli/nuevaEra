# Create your views here.
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from core.forms import UserForm
from django.contrib.auth import authenticate, login
    
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



def loguearse(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return redirect(reverse("core_home"))
        else:
            # Return a 'disabled account' error message
            error(request, "La cuenta esta deshabilitada")            
    else:
        # Return an 'invalid login' error message.
        error(request, "La cuenta es invalida")

    
def error(request, mensaje):
    return redirect(reverse("core_error"), {'mensaje': mensaje})
    #return render(request, "core/error.html", {'mensaje': mensaje})