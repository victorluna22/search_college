#! -*- encoding:utf-8 -*- 
from django.contrib import admin
from models import Relatorio


class RelatorioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'universidade', 'status_crowler', 'status_busca')
    search_fields = ('universidade',)
    list_filter = ('status_crowler', 'status_busca')

admin.site.register(Relatorio, RelatorioAdmin)