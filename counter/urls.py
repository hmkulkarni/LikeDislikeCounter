from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('likes/', views.incrementLikes, name='incrementLikes'),
    path('dislikes/', views.incrementDislikes, name='incrementDislikes'),
]