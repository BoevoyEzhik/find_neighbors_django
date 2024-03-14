from django.urls import path
from find_neighbors import views


urlpatterns = [
    path('', views.index, name='hello-neighbors'),
    path('find-neighbors', views.find_neighbors, name='find-neighbors'),
    path('create-user', views.create_user, name='create-user'),
]