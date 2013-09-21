#! -*- coding:utf-8 -*-
from django.core.management.base import CommandError, BaseCommand
from busca.models import Relatorio
from tasks import add

class Command(BaseCommand):
	help = u'Command line para enviar os resultado das buscas realizadas'

	def handle(self, *args, **options):
		relatorios = Relatorio.objects.filter(status_crowler=True, status_busca=True, status_email=False)
		for relatorio in relatorios:
			assunto = 'O resultado da sua busca está pronto!'
			mensagem = 'Para acessar o resultado da busca que você cadastrou em nosso sistema, basta acessar o seguinte link: http://localhost/%d/' % relatorio.id
			send_mail(assunto, mensagem, 'victorluna22@gmail.com',[relatorio.email])
			




