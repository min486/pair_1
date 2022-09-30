from django.urls import path
from . import views

app_name = "movie"

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('review/', views.review, name='review'),
    path('detail/<int:movie_pk>', views.detail, name='detail'),
    path('update/<int:update_pk>', views.update, name='update'),
    path('edit/<int:edit_pk>', views.edit, name='edit'),
    path('delete/<int:delete_pk>', views.delete, name='delete'),
]