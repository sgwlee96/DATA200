from django.shortcuts import render

# Create your views here.


def bubble_chart(request):
    return render(request, 'visualization_app/bubble_chart.html')

def dplot(request):
    return render(request, 'visualization_app/3dplot.html')

def combined_chart(request):
    return render(request, 'visualization_app/combined_chart.html')