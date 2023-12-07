# graphapp/urls.py
from django.urls import path
from .views import generate_graphs

urlpatterns = [
    path('generate-graphs/', generate_graphs, name='generate_graphs'),
]
