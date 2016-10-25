from django.shortcuts import render
from django.http import Http404

def index(request):
    raise Http404("Question does not exist")

def logout(request):
    return render(request, "Demo/index.html")

