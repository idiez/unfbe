from django.conf.urls import patterns, include, url
from objects import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'unitenfc.views.home', name='home'),
    # url(r'^unitenfc/', include('unitenfc.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
 #   url(r'^objects/', include('objects.urls', namespace="unitenfc")),
   	url(r'^objects/users/(?P<user_req>.+)/$', views.restore_view, name='restore_view'),
    url(r'^admin/', include(admin.site.urls)),
)
