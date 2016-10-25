#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from Demo.models import Question, Choice
from django.core import serializers
import json
def index(request):
    context = {}
    context['str'] = "Hi Abraham Zhang!"
    context['question'] = Question.objects.all()
    return render(request, "Demo/index.html", context)

def test(request):
    return render(request,"test.html")

def jsonTest(request):
    response_data = {}
    response_data['result'] = 'failed'
    response_data['message'] = 'You messed up'
    # json_adta = serializers.serialize('json',response_data)
    return HttpResponse(json.dumps(response_data), content_type="application/json")