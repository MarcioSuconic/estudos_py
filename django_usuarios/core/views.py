from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import logout

# Create your views here.



def home(request):
    return render (request, 'core/home.html')

def logout_forcado(request):
    logout(request)
    return redirect("home")

@login_required
def pagina1(request):
    return render (request, 'core/pagina1.html')

@login_required
def pagina2(request):
    return render (request, 'core/pagina2.html')

