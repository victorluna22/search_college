#! -*- coding:utf-8 -*-
from django.core.management.base import CommandError, BaseCommand
from busca.models import Relatorio
from tasks import add

class Command(BaseCommand):
	help = u'Command line para processar os pedidos de busca realizadas no sistema'

	def handle(self, *args, **options):
		relatorios = Relatorio.objects.filter(status_crowler=False)
		for relatorio in relatorios:
			print relatorio.id
			add.delay(relatorio.id, relatorio.universidade, relatorio.de, relatorio.ate)
			




