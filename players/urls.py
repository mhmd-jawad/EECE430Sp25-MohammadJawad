from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='player_list'),
    path('add/', views.add_player, name='add_player'),
    path('player/<int:pk>/', views.view_player, name='view_player'),
    path('player/<int:pk>/edit/', views.edit_player, name='edit_player'),
    path('player/<int:pk>/delete/', views.delete_player, name='delete_player'),
]
