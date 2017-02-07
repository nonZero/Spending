from django.conf.urls import url

from . import views

app_name = "expenses"

urlpatterns = [
    url(r'^$', views.list, name="list"),
    url(r'^create/$', views.create, name="create"),
    url(r'^([0-9]+)/$', views.detail, name="detail"),
    url(r'^feedback/$', views.send_feedback, name="feedback"),
]
