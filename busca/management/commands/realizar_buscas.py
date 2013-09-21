#! -*- coding:utf-8 -*-
from django.core.management.base import CommandError, BaseCommand
from busca.models import Relatorio
import subprocess     
import os

class Command(BaseCommand):
	help = u'Command line para processar as buscas cadastradas no sistema'

	def handle(self, *args, **options):
		relatorios = Relatorio.objects.filter(status_crowler=True, status_busca=False)
		os.chdir("/home/victor/projetos/scriptLattesV8.08/")
		for relatorio in relatorios:
			process = subprocess.Popen(['./scriptLattes.py', '/home/victor/media/search_college/conf/%s.txt' % relatorio.id])
			relatorio.status_busca = True
			relatorio.save()

			




