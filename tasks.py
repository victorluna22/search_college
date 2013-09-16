from celery import Celery
import time
from busca.crowler import *
from django.conf import settings
from busca.models import Relatorio
celery = Celery('tasks', broker='amqp://guest@localhost//')

@celery.task
def add(id_relatorio, universidade, de, ate):
	path_result_crowler = start_crowler(id_relatorio, universidade)
	path_result_conf = create_file_conf(id_relatorio, path_result_crowler, de, ate)
	relatorio = Relatorio.objects.get(id=id_relatorio)
	if relatorio:
		relatorio.status_crowler = True
		relatorio.save()

