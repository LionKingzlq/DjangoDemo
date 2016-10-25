from django.conf.urls import url
from Demo import views as DemoViews

urlpatterns = [
    url(r'^$', DemoViews.index),
    url(r'^json$', DemoViews.jsonTest)
]