import django.dispatch

inseriu_relatorio = django.dispatch.Signal(providing_args=["relatorio"])


def inseriu_relatorio_receiver(sender, relatorio, **kwargs):
	print 'a'