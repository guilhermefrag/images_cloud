from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('photolist/', views.photo_list, name='photo_list'),
    path('deletephoto/<int:photo_id>/', views.delete_photo, name='delete_photo'),
    path('photolist/downloadfile/<int:photo_id>/', views.download_file, name='download_file'),
]