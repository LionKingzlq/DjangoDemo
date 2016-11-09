# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

from Blog.models import Question, Choice

from django.utils.translation import ugettext

import os
import json


def index(request):
    context = {}
    context['str'] = os.path.join(os.path.dirname(__file__), "..")
    context['question'] = Question.objects.all()
    context['hello'] = ugettext('hello')
    context['world'] = ugettext('world!')
    return render(request, "blog/index2.html", context)
    return render(request, "blog/index.html", context)


def add(request):
    response_data = {}
    response_data['result'] = 'failed'
    response_data['message'] = 'You messed up'
    # json_adta = serializers.serialize('json',response_data)
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def delete(request):
    response_data = {}
    response_data['result'] = 'failed'
    response_data['message'] = 'You messed up'
    # json_adta = serializers.serialize('json',response_data)
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def update(request):
    response_data = {}
    response_data['result'] = 'failed'
    response_data['message'] = 'You messed up'
    # json_adta = serializers.serialize('json',response_data)
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def get(request):
    return render(request, "test.html")


