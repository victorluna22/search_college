from django.shortcuts import render, redirect
from busca.forms import RelatorioForm
from django.views.generic import TemplateView
from busca.signals import inseriu_relatorio

class HomeView(TemplateView):
	template_name = 'index.html'


class BuscaView(TemplateView):
	template_name = 'busca.html'

	def get_context_data(self, **kwargs):
		context = super(BuscaView, self).get_context_data(**kwargs)
		context['form'] = RelatorioForm(self.request.POST or None)
		return context

	def post(self, request):
		context = self.get_context_data()
		form = context['form']
		if form.is_valid():
			relatorio = form.save()
			if relatorio.pk:
				inseriu_relatorio.send(sender=request,relatorio=relatorio)
			context = {'success': True}
			context['form'] = RelatorioForm()
		return self.render_to_response(context)


def resultado(request, id_relatorio):
	return render(request, '%s/index.html' % id_relatorio, {})
