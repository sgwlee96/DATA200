# visualizations_app/urls.py
from django.urls import path

from .views import bubble_chart, dplot, combined_chart

urlpatterns = [
    path('bubble-chart/', bubble_chart, name='bubble_chart'),
    path('3d-chart/', dplot, name='3dplot'),
    path('combined-chart/', combined_chart, name='combined_chart'),
]