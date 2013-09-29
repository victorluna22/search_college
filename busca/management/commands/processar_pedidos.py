#! -*- coding:utf-8 -*-
from django.core.management.base import CommandError, BaseCommand
from busca.models import Relatorio
from busca.crowler import *
# from tasks import add

class Command(BaseCommand):
	help = u'Command line para processar os pedidos de busca realizadas no sistema'

	def handle(self, *args, **options):
		relatorios = Relatorio.objects.filter(status_crowler=False)
		for relatorio in relatorios:
			# add.delay(relatorio.id, relatorio.universidade, relatorio.de, relatorio.ate)
			path_result_crowler = start_crowler(relatorio.id, relatorio.universidade)
			path_result_conf = create_file_conf(relatorio.id, path_result_crowler, relatorio.de, relatorio.ate)
			relatorio = Relatorio.objects.get(id=relatorio.id)
			if relatorio:
				relatorio.status_crowler = True
				relatorio.save()
			




