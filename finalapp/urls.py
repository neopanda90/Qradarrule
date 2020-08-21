from django.urls import path
from . import views

urlpatterns = [
    path('', views.alldata, name='home'),
    path('search/', views.search, name='search'),
]