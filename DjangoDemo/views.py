from django.shortcuts import render
from django.http import Http404
import os
import Blog.Model.OsService as osService

def index(request):
    return render(request, "index.html")


def logout(request):
    return render(request, "logout.html")


def login(request):
    raise Http404("Question does not exist")


def test(request):
    context = {}
    context['str'] = os.path.join(os.path.dirname(__file__), "..")
    context['osName'] = os.name
    context['osCWD'] = os.getcwd()
    context['files'] = os.listdir(os.getcwd())
    context['answer'] = osService.add(1, 2)
    return render(request, "test.html", context)
