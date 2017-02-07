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
# http://127.0.0.1:8000/boom/
# protocol: http
# host:port(default 80): 127.0.0.1:8000
# path:
def hello(request):
    return HttpResponse("hello!<b>hello!")

# http://127.0.0.1:8000/boom/
# protocol: http
# host:port(default 80): 127.0.0.1:8000
# path: boom/

def boom(request):
    assert False, "BOOM!!!!"


def magic(request):
    html = "The magic number is: {}!!!".format(random.randint(1, 10))
    return HttpResponse(html)

def hello_name(request, name):
    return HttpResponse("hello <b>{}</b>!".format(name))

# /add/10/20/  ==>  10 + 20 = **30**


urlpatterns = [
    url(r"^$", hello),
    url(r"^hello/([a-z]+)/$", hello_name),
    url(r"^boom/$", boom),
    url(r"^magic/$", magic),
    url(r'^admin/', admin.site.urls),
]
