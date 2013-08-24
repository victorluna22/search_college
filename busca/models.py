from django.db import models

class Relatorio(models.Model):
	nome = models.CharField(u'Nome', max_length=255)
	email = models.EmailField(u'E-Mail')
	universidade = models.CharField(u'Universidade', max_length=255)
	de = models.IntegerField()
	ate = models.IntegerField()
	data = models.DateTimeField(auto_now=True)