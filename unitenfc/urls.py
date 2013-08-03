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
   	url(r'^objects/users/name/(?P<user_req>.+)/$', views.nameupdate_view, name='nameupdate_view'),
   	url(r'^objects/users/picuri/(?P<user_req>.+)/$', views.picuriupdate_view, name='picuriupdate_view'),
   	url(r'^objects/users/fblink/$', views.getfb_view, name='getfb_view'),   	
   	url(r'^objects/users/friend/$', views.addfriend_view, name='addfriend_view'),
   	url(r'^objects/users/new/$', views.reguser_view, name='reguser_view'),
   	url(r'^objects/users/(?P<user_req>.+)/$', views.restore_view, name='restore_view'),
   	url(r'^objects/nfcp/(?P<user_req>.+)/(?P<isReg>.+)/$', views.regpoint_view, name='regpoint_view'),
   	url(r'^objects/wall/$', views.regwall_view, name='regwall_view'), 
    url(r'^admin/', include(admin.site.urls)),
)
