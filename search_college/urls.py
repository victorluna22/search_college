from django.conf.urls import patterns, include, url
from busca.views import HomeView, BuscaView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^busca/$', BuscaView.as_view(), name='busca'),
    url(r'^admin/', include(admin.site.urls)),
)
