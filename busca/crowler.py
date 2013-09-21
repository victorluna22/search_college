# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import mechanize
import urllib
import re, os
# from django.conf import settings

def start_crowler(id_relatorio, universidade):
	url = 'http://buscatextual.cnpq.br/buscatextual/busca.do?metodo=forwardPaginaResultados&registros=0;20&query=%28+%2Bidx_nme_inst_ativ_prof%3A'+ urllib.quote_plus(universidade) +'++++++%2Bidx_particao%3A1+%2Bidx_nacionalidade%3Ae%29+or+%28+%2Bidx_nme_inst_ativ_prof%3A'+ urllib.quote_plus(universidade) +'++++++%2Bidx_particao%3A1+%2Bidx_nacionalidade%3Ab%29&analise=cv&tipoOrdenacao=null&paginaOrigem=index.do&mostrarScore=false&mostrarBandeira=true&modoIndAdhoc=null'
	# browser.open(url)
	req = urllib.urlopen(url).read()
	# res = opener.open(req)
	html = req
	erros = []
	contador = 1
	soup = BeautifulSoup(html)
	lista = soup.find('div', attrs={"class" : 'resultado'}).findAll('li')
	path_file = '/home/victor/media/search_college/crowler/%d.txt' % id_relatorio
	arquivo = open(path_file, 'w')
	for pessoa in lista:
		print contador
		li = BeautifulSoup(str(pessoa))
		href = li.find('a')['href']
		nome = li.find('a').contents[0]
		result = re.search("javascript:abreDetalhe.'(\w*)','.*", href)
		id = result.groups()[0]
		
		url = 'http://buscatextual.cnpq.br/buscatextual/visualizacv.do?id=' + id
		
		req = urllib.urlopen(url).read()
		html = req
		soup = BeautifulSoup(unicode(html, errors='ignore').encode('ascii', 'ignore'))
		vinculo = False
		ufrpe = False

		blocos = soup.findAll('div', attrs={"class" : 'title-wrapper'})
		for bloco in blocos:
			if bloco.find('a', attrs={'name': 'AtuacaoProfissional'}):
				conteudo = bloco.find('div')
				for div in conteudo.findAll('div'):
					if 'inst_back' in dict(div.attrs)['class']:
						if universidade.upper() in div.find('b').text:
							vinculo = True
						else:
							vinculo = False

					if div.find('b') and 'Atual' in div.find('b').text:
						if vinculo == True:
							ufrpe = True
		if ufrpe and contador:
			try:
				arquivo.write(id + ' , ' + nome.encode('ascii', 'ignore') + '\n')
			except:
				erros.append(id)
		contador += 1
	arquivo.close()
	return path_file


def create_file_conf(id_relatorio, path_result_crowler, de, ate):
	arquivo_base = open('/home/victor/media/search_college/conf/config_base.txt', 'r')
	arquivo_configuracao = open('/home/victor/media/search_college/conf/%d.txt' % id_relatorio, 'w')
	path = "/home/victor/media/search_college/result/%d/" % id_relatorio
	os.mkdir( path, 0777 );
	for linha in arquivo_base.readlines():
		linha = linha.replace('{{PATH_LIST}}', path_result_crowler).replace('{{PATH_RESULT}}', path).replace('{{DE}}',str(de)).replace('{{ATE}}', str(ate))
		arquivo_configuracao.write(linha)

	arquivo_configuracao.close()
	arquivo_base.close()