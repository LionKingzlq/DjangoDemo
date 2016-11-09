"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from DjangoDemo import views

from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [

                  url(r'^$', views.index),

                  url(r'^IT/', include('IT.urls')),

                  url('^food$', TemplateView.as_view(template_name='food.html')),
                  url('^photo$', TemplateView.as_view(template_name='Photo/index.html')),
                  url('^food$', TemplateView.as_view(template_name='sport.html')),
                  url('^photo$', TemplateView.as_view(template_name='photo.html')),
                  url('^sport$', TemplateView.as_view(template_name='sport.html')),
                  url('^reading$', TemplateView.as_view(template_name='reading.html')),
                  url('^contact$', TemplateView.as_view(template_name='contact.html')),

                  url(r'^admin/', admin.site.urls),
                  url('^logout/$', TemplateView.as_view(template_name='logout.html')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
