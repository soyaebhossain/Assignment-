from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contact, name='contact'), 
    path('services/', views.services, name='services'),
    path('products/', views.products, name='products'),
    path('about/', views.about, name='about'),
    path('index/', views.index, name='index'),
    path('admin/', views.admin, name='admin'),
]