from django.shortcuts import render

from .forms import MapForm
from .models import Map
from django.utils import timezone

from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
def index(request):
    
    return render(request, 'index.html')
def home(request):
    
    return render(request, 'home.html')
def edit_map(request, map_id):
    map_instance = get_object_or_404(Map, id=map_id)
    if request.method == 'POST':
        form = MapForm(request.POST, instance=map_instance)
        if form.is_valid():
            form.save()
            return redirect('app:map_list')  # Redirigez l'utilisateur vers la liste des cartes après la modification
    else:
        form = MapForm(instance=map_instance)
    return render(request, 'edit_map.html', {'form': form, 'map_instance': map_instance})

def delete_map(request, map_id):
    map_instance = get_object_or_404(Map, id=map_id)
    if request.method == 'POST':
        map_instance.delete()
        return redirect('app:map_list')  # Redirigez l'utilisateur vers la liste des cartes après la suppression
    return render(request, 'delete_map.html', {'map_instance': map_instance})




def map_detail(request, pk):
    map_instance = get_object_or_404(Map, pk=pk)
    return render(request, 'map_detail.html', {'map_instance': map_instance})



def map_form(request):
    if request.method == 'POST':
        form = MapForm(request.POST, request.FILES)
        if form.is_valid():
            # Récupérez l'utilisateur connecté
            user = request.user
            
            # Créez une nouvelle instance de Map en associant l'utilisateur
            new_map = form.save(commit=False)
            new_map.user = user
            new_map.save()
            
            # Redirigez l'utilisateur vers une autre page après avoir soumis le formulaire si nécessaire
            # Redirigez par exemple vers la page de détails de la nouvelle carte
            return redirect('app:map_detail', pk=new_map.pk)  # Assurez-vous d'avoir une URL nommée 'map_detail' avec un paramètre 'pk'
    else:
        form = MapForm()

    return render(request, 'map_form.html', {'form': form})
def map_list(request):
    # Obtenez l'heure actuelle
    current_time = timezone.now()
    
    # Calculez l'heure il y a 24 heures
    twenty_four_hours_ago = current_time - timezone.timedelta(hours=24)
    
    # Filtrer les objets Map avec une date supérieure à twenty_four_hours_ago
    maps = Map.objects.filter(date__gte=twenty_four_hours_ago)
    
    return render(request, 'map_list.html', {'maps': maps})


def NewsList(request):
    maps = Map.objects.all().order_by('date')  # Triez les objets Map par date
    return render(request, 'news_list.html', {'maps': maps})


def user_maps(request):
    user = request.user  # L'utilisateur actuellement connecté
    maps = Map.objects.filter(user=user)  # Récupérer toutes les cartes de l'utilisateur
    return render(request, 'user_maps.html', {'maps': maps})

def edit_map(request, map_id):
    map_instance = get_object_or_404(Map, id=map_id)
    # Logique d'édition de la carte ici
    return render(request, 'edit_map.html', {'map_instance': map_instance})

def delete_map(request, map_id):
    map_instance = get_object_or_404(Map, id=map_id)
    # Logique de suppression de la carte ici
    map_instance.delete()
    return redirect('app:user_maps')