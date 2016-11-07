from django.conf.urls import url
from IT import views as DemoViews

urlpatterns = [
    url(r'^$', DemoViews.index),
    url(r'^json$', DemoViews.jsonTest)
]