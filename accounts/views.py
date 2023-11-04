from django.shortcuts import render,redirect

from django.contrib.auth import login as auth_login


from django.urls import reverse_lazy

from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
def authentication(request):
    return render(request, 'registration/login.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        hashed_password = make_password(password)  # Hasher le mot de passe
        
        # Créer un nouvel utilisateur
        user = User.objects.create( username=email,   email=email, first_name=first_name, last_name=last_name, password=hashed_password)
        
        # Connecter l'utilisateur
        #login(request, user)
        
        messages.success(request, 'Inscription réussie. Bienvenue !')
        return redirect('../maps')  # Rediriger vers la page d'accueil ou une autre page appropriée
        
    return render(request, 'registration/login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('../maps') # Rediriger vers la page d'accueil après l'authentification
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return redirect('authentication')  # Rediriger vers la page d'authentification en cas d'échec de l'authentification