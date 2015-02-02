from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PyQa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^punchlists/', include('punchlists.urls', namespace="punchlists")),
    url(r'^admin/', include(admin.site.urls)),
)
