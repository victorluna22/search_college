#! -*- coding:utf-8 -*-
from django.core.management.base import CommandError, BaseCommand
from busca.models import Relatorio
from django.conf import settings
import subprocess     
import os

class Command(BaseCommand):
	help = u'Command line para processar as buscas cadastradas no sistema'

	def handle(self, *args, **options):
		relatorios = Relatorio.objects.filter(status_crowler=True, status_busca=False)
		if settings.DEBUG:
			os.chdir("/home/nadhine/scriptLattesV8.08/")
		else:
			os.chdir("/home/ubuntu/scriptLattesV8.08/")
		for relatorio in relatorios:
			if settings.DEBUG:
				process = subprocess.Popen(['sudo', 'python', './scriptLattes.py', '/home/nadhine/media/search_college/conf/%s.txt' % relatorio.id])
			else:
				process = subprocess.Popen(['./scriptLattes.py', '/home/ubuntu/media/search_college/conf/%s.txt' % relatorio.id])
			relatorio.status_busca = True
			relatorio.save()

			




