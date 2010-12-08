from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:

from django.contrib import admin
admin.autodiscover()



#from core.views import *

urlpatterns = patterns('django.views.generic.simple',
    # Example:
    # (r'^eventex/', include('eventex.foo.urls')),
    #(r'^$', homepage),
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'direct_to_template', {'template': 'index.html'}),
    (r'^inscricao/', include('subscription.urls', namespace='subscription')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root': settings.MEDIA_ROOT }),
    )
