from django.contrib import admin

from Blog.Model.models import Question,Choice

admin.site.register(Question)
admin.site.register(Choice)