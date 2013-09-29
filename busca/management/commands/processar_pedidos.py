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
			path_result_crowler = start_crowler(id_relatorio, universidade)
			path_result_conf = create_file_conf(id_relatorio, path_result_crowler, de, ate)
			relatorio = Relatorio.objects.get(id=id_relatorio)
			if relatorio:
				relatorio.status_crowler = True
				relatorio.save()
			




