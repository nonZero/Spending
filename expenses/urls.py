from django.conf.urls import url

from . import views

app_name = "expenses"

urlpatterns = [
    url(r'^$', views.list, name="list"),
    url(r'^([0-9]+)/$', views.detail, name="detail"),
]
