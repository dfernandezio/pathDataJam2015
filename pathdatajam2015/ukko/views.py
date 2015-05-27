from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ukko/home.html')

def chart(request):
    return render(request, 'ukko/chart.html')

def table(request):
    return render(request, 'ukko/table.html')

def about(request):
    return render(request, 'ukko/about.html')