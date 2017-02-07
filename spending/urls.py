"""spending URL Configuration

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
import random

from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse


# view functions
def hello(request):
    return HttpResponse("hello!<b>hello!")


def boom(request):
    assert False, "BOOM!!!!"


def magic(request):
    html = "The magic number is: {}!!!".format(random.randint(1, 10))
    return HttpResponse(html)


urlpatterns = [
    url(r"^$", hello),
    url(r"^boom/$", boom),
    url(r"^magic/$", magic),
    url(r'^admin/', admin.site.urls),
]
