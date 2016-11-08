# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

from IT.models import Question, Choice

from django.utils.translation import ugettext

import os
import json


def index(request):
    context = {}
    context['str'] = os.path.join(os.path.dirname(__file__), "..")
    context['question'] = Question.objects.all()
    context['hello'] = ugettext('hello')
    context['world'] = ugettext('world!')
<<<<<<< HEAD
    return render(request, "IT/index2.html", context)
=======
    return render(request, "IT/index.html", context)
>>>>>>> b6ed3cb0427fc3b30fe2f4b569908246cfec5690


def test(request):
    return render(request, "test.html")


def jsonTest(request):
    response_data = {}
    response_data['result'] = 'failed'
    response_data['message'] = 'You messed up'
    # json_adta = serializers.serialize('json',response_data)
    return HttpResponse(json.dumps(response_data), content_type="application/json")
