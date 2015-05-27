from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^chart/$', views.chart, name='chart'),
    url(r'^table/$', views.table, name='table'),
    url(r'^about/$', views.about, name='about'),
]