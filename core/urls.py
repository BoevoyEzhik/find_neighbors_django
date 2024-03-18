from django.urls import path
from core import views


urlpatterns = [
    path('find-neighbors', views.find_neighbors, name='find-neighbors'),
    path('create-user', views.create_user, name='create-user'),
]