from django.conf.urls import patterns, url
from objects import views

urlpatterns = patterns('',
#    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^users/(?P<user_req>.+)/$', views.restore_view, name='restore_view'),
)