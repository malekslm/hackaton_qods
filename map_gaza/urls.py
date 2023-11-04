from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('edit/<int:map_id>/', views.edit_map, name='edit_map'),
    path('delete/<int:map_id>/', views.delete_map, name='delete_map'),

    
    path('map/<int:pk>/', views.map_detail, name='map_detail'),


    path('user-maps/', views.user_maps, name='user_maps'),


    path('edit-map/<int:map_id>/', views.edit_map, name='edit_map'),
    path('delete-map/<int:map_id>/', views.delete_map, name='delete_map'),
    # Autres chemins d'URL de votre application...
    
    path('maps/', views.map_list, name='map_list'),
    path('map_form/', views.map_form, name='map_form'),
    path('NewsList/', views.NewsList, name='NewsList'),    
    path('', views.index, name='index'),   
    path('home', views.home, name='home'),  

    
]