from django.conf.urls import patterns, include, url
from busca.views import HomeView, BuscaView, resultado
from django.views.generic import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^busca/$', BuscaView.as_view(), name='busca'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^resultado/(?P<id_relatorio>\d+)/$', resultado, name='resultado'),
    url(r'^resultado/(?P<id_relatorio>\d+)/scriptLattes.css$', TemplateView.as_view(template_name="scriptLattes.css"), name='css')
)
