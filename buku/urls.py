from django.urls import path
from . import views 

urlpatterns = [
    path('', views.buku, name='buku'),
    path('daftar/', views.daftar, name='daftar'),
]