from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render

def custom_404_view(request, exception):
    return render(request, '404.html', {})

def custom_500_view(request):
    return render(request, '500.html', {})
