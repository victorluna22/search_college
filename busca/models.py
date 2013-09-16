from django.db import models
from busca.signals import inseriu_relatorio, inseriu_relatorio_receiver

class Relatorio(models.Model):
	nome = models.CharField(u'Nome', max_length=255)
	email = models.EmailField(u'E-Mail')
	universidade = models.CharField(u'Universidade', max_length=255)
	de = models.IntegerField()
	ate = models.IntegerField()
	data = models.DateTimeField(auto_now=True)
	status_crowler = models.BooleanField(default=False)
	status_busca = models.BooleanField(default=False)

	def __unicode__(self):
		return self.nome

	def post_save(self):
		self.url = 'http://google.com'
		self.save()


inseriu_relatorio.connect(inseriu_relatorio_receiver, dispatch_uid='busca.signals.inseriu_relatorio')