from django.conf.urls import url
from Blog import views as blogViews
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', blogViews.index),
    url(r'^get', blogViews.get),
    url(r'^add', blogViews.add),
    url(r'^update', blogViews.add),
    url(r'^detele', blogViews.add),
    url(r'^admin', TemplateView.as_view(template_name='blog/admin/index.html'))
]
