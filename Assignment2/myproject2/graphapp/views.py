

# Create your views here.
# graphapp/views.py
import matplotlib.pyplot as plt
from django.http import HttpResponse
from django.shortcuts import render

def generate_graphs(request):
    # Data for the graphs
    x_data = [1, 2, 3, 4, 5]
    y_data_bar = [10, 20, 15, 25, 30]
    y_data_line = [5, 15, 10, 20, 25]

    # Bar Chart
    plt.figure(figsize=(6, 4))
    plt.bar(x_data, y_data_bar, color='blue')
    plt.title('Bar Chart')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.savefig('static/bar_chart.png')

    # Line Chart
    plt.figure(figsize=(6, 4))
    plt.plot(x_data, y_data_line, marker='o', color='green', linestyle='--')
    plt.title('Line Chart')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.savefig('static/line_chart.png')

    return render(request, 'graphapp/graphs.html')
