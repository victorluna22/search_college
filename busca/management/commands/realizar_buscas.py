#! -*- coding:utf-8 -*-
from django.core.management.base import CommandError, BaseCommand
from busca.models import Relatorio
import subprocess     
import os

class Command(BaseCommand):
	help = u'Command line para processar as buscas cadastradas no sistema'

	def handle(self, *args, **options):
		relatorios = Relatorio.objects.filter(status_crowler=True, status_busca=False)
		print 'antes'
		# process = subprocess.Popen(['cd','/home/victor/projetos/scriptLattesV8.08/'])
		#r = subprocess.call("cd /home/victor/projetos/scriptLattesV8.08/")
		os.chdir("/home/victor/projetos/scriptLattesV8.08/")
		print 'depois'
		for relatorio in relatorios:
			process = subprocess.Popen(['./scriptLattes.py', '/home/victor/media/search_college/conf/%s.txt' % relatorio.id])

			




