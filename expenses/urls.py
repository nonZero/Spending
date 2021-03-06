from django.conf.urls import url

from . import views

app_name = "expenses"

urlpatterns = [
    url(r'^$', views.ExpenseListView.as_view(), name="list"),
    url(r'^month/$', views.list_months, name="months"),
    url(r'^month/(20[0-9][0-9])/$', views.ExpenseListView.as_view(), name="year"),
    url(r'^month/(20[0-9][0-9])/(1?[0-9])/$', views.ExpenseListView.as_view(), name="month"),

    # url(r'^create/$', views.create, name="create"),
    url(r'^create/$', views.ExpenseCreateView.as_view(), name="create"),
    url(r'^([0-9]+)/$', views.detail, name="detail"),
    # url(r'^(?P<pk>[0-9]+)/$', views.ExpenseDetailView.as_view(), name="detail"),
    # url(r'^([0-9]+)/edit/$', views.update, name="update"),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.ExpenseUpdateView.as_view(), name="update"),
    url(r'^([0-9]+)/delete/$', views.delete, name="delete"),
    # url(r'^feedback/$', views.send_feedback, name="feedback"),
    url(r'^feedback/$', views.FeedbackView.as_view(), name="feedback"),

    url(r'cbv/', views.MyView.as_view()),
    url(r'playground/', views.PlaygroundView.as_view()),
]
