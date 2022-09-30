from django.urls import path
from . import views

app_name = "movie"

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('review/', views.review, name='review'),
    path('detail/<int:movie_pk>', views.detail, name='detail'),
]