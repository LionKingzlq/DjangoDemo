from django.contrib import admin

from Blog.models import Question, Choice, Blog, Tag, BlogTag

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(BlogTag)