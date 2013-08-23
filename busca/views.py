from django.shortcuts import render


def home(request):
	return render(request, 'index.html', {})


def busca(request):
	return render(request, 'busca.html', {})
