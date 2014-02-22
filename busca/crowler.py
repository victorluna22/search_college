# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
from django.conf import settings
import mechanize
import urllib
import re, os

# from django.conf import settings

def start_crowler(id_relatorio, universidade):
	limite_busca = 999999999999999
	url = 'http://buscatextual.cnpq.br/buscatextual/busca.do?metodo=forwardPaginaResultados&registros=0;'+ str(limite_busca) +'&query=%28+%2Bidx_nme_inst_ativ_prof%3A'+ urllib.quote_plus(universidade) +'++++++%2Bidx_particao%3A1+%2Bidx_nacionalidade%3Ae%29+or+%28+%2Bidx_nme_inst_ativ_prof%3A'+ urllib.quote_plus(universidade) +'++++++%2Bidx_particao%3A1+%2Bidx_nacionalidade%3Ab%29&analise=cv&tipoOrdenacao=null&paginaOrigem=index.do&mostrarScore=false&mostrarBandeira=true&modoIndAdhoc=null'
	# browser.open(url)
	req = urllib.urlopen(url).read()
	# res = opener.open(req)
	html = req
	erros = []
	contador = 1
	soup = BeautifulSoup(html)
	lista = soup.find('div', attrs={"class" : 'resultado'}).findAll('li')
	print lista
	path_file = settings.MEDIA_ROOT + 'crowler/%d.txt' % id_relatorio
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


def create_file_conf(path_result_crowler, relatorio):
	arquivo_base = open(settings.MEDIA_ROOT + 'conf/config_base.txt', 'r')
	arquivo_configuracao = open(settings.MEDIA_ROOT + 'conf/%d.txt' % relatorio.id, 'w')
	path = settings.MEDIA_ROOT + "result/%d/" % relatorio.id
	os.mkdir( path, 0777 );
	for linha in arquivo_base.readlines():
		linha = linha.replace('{{PATH_LIST}}', path_result_crowler).replace('{{PATH_RESULT}}', path).replace('{{DE}}',str(relatorio.de)).replace('{{ATE}}', str(relatorio.ate))
		if relatorio.artigo:
			linha = linha.replace('{{ARTIGO}}', 'sim')
		else:
			linha = linha.replace('{{ARTIGO}}', 'nao')
		if relatorio.livro:
			linha = linha.replace('{{LIVRO}}', 'sim')
		else:
			linha = linha.replace('{{LIVRO}}', 'nao')
		if relatorio.capitulo_livro:
			linha = linha.replace('{{CAPITULO}}', 'sim')
		else:
			linha = linha.replace('{{CAPITULO}}', 'nao')
		if relatorio.jornal:
			linha = linha.replace('{{JORNAL}}', 'sim')
		else:
			linha = linha.replace('{{JORNAL}}', 'nao')
		if relatorio.trabalho_completo:
			linha = linha.replace('{{TRABCOMPLETO}}', 'sim')
		else:
			linha = linha.replace('{{TRABCOMPLETO}}', 'nao')
		if relatorio.resumo_expandido:
			linha = linha.replace('{{RESUMOEXP}}', 'sim')
		else:
			linha = linha.replace('{{RESUMOEXP}}', 'nao')
		if relatorio.resumo:
			linha = linha.replace('{{RESUMO}}', 'sim')
		else:
			linha = linha.replace('{{RESUMO}}', 'nao')
		if relatorio.artigo:
			linha = linha.replace('{{ARTIGOPUBLICADO}}', 'sim')
		else:
			linha = linha.replace('{{ARTIGOPUBLICADO}}', 'nao')
		if relatorio.apresentacao_trabalho:
			linha = linha.replace('{{APRESTRAB}}', 'sim')
		else:
			linha = linha.replace('{{APRESTRAB}}', 'nao')
		if relatorio.software_patenteado:
			linha = linha.replace('{{SOFTWAREPAT}}', 'sim')
		else:
			linha = linha.replace('{{SOFTWAREPAT}}', 'nao')
		if relatorio.software:
			linha = linha.replace('{{SOFTWARE}}', 'sim')
		else:
			linha = linha.replace('{{SOFTWARE}}', 'nao')
		if relatorio.produto:
			linha = linha.replace('{{PRODUTO}}', 'sim')
		else:
			linha = linha.replace('{{PRODUTO}}', 'nao')
		if relatorio.processo_ou_tecnica:
			linha = linha.replace('{{PROCESSTEC}}', 'sim')
		else:
			linha = linha.replace('{{PROCESSTEC}}', 'nao')
		if relatorio.trabalho_tecnico:
			linha = linha.replace('{{TRABALHOTEC}}', 'sim')
		else:
			linha = linha.replace('{{TRABALHOTEC}}', 'nao')
		if relatorio.outras_producoes:
			linha = linha.replace('{{OUTRAS}}', 'sim')
		else:
			linha = linha.replace('{{OUTRAS}}', 'nao')
		if relatorio.orientacoes:
			linha = linha.replace('{{ORIENTACOES}}', 'sim')
		else:
			linha = linha.replace('{{ORIENTACOES}}', 'nao')
		if relatorio.pos_andamento:
			linha = linha.replace('{{APOS}}', 'sim')
		else:
			linha = linha.replace('{{APOS}}', 'nao')
		if relatorio.doutorado_andamento:
			linha = linha.replace('{{ADOUTORADO}}', 'sim')
		else:
			linha = linha.replace('{{ADOUTORADO}}', 'nao')
		if relatorio.mestrado_andamento:
			linha = linha.replace('{{AMESTRADO}}', 'sim')
		else:
			linha = linha.replace('{{AMESTRADO}}', 'nao')
		if relatorio.monografia_andamento:
			linha = linha.replace('{{AMONOGRAFIA}}', 'sim')
		else:
			linha = linha.replace('{{AMONOGRAFIA}}', 'nao')
		if relatorio.tcc_andamento:
			linha = linha.replace('{{ATCC}}', 'sim')
		else:
			linha = linha.replace('{{ATCC}}', 'nao')
		if relatorio.ic_andamento:
			linha = linha.replace('{{AIC}}', 'sim')
		else:
			linha = linha.replace('{{AIC}}', 'nao')
		if relatorio.outras_andamento:
			linha = linha.replace('{{AOUTRAS}}', 'sim')
		else:
			linha = linha.replace('{{AOUTRAS}}', 'nao')
		if relatorio.pos_concluida:
			linha = linha.replace('{{CPOS}}', 'sim')
		else:
			linha = linha.replace('{{CPOS}}', 'nao')
		if relatorio.doutorado_concluida:
			linha = linha.replace('{{CDOUTORADO}}', 'sim')
		else:
			linha = linha.replace('{{CDOUTORADO}}', 'nao')
		if relatorio.mestrado_concluido:
			linha = linha.replace('{{CMESTRADO}}', 'sim')
		else:
			linha = linha.replace('{{CMESTRADO}}', 'nao')
		if relatorio.monografia_concluida:
			linha = linha.replace('{{CMONOGRAFIA}}', 'sim')
		else:
			linha = linha.replace('{{CMONOGRAFIA}}', 'nao')
		if relatorio.tcc_concluida:
			linha = linha.replace('{{CTCC}}', 'sim')
		else:
			linha = linha.replace('{{CTCC}}', 'nao')
		if relatorio.ic_concluida:
			linha = linha.replace('{{CIC}}', 'sim')
		else:
			linha = linha.replace('{{CIC}}', 'nao')
		if relatorio.outras_concluida:
			linha = linha.replace('{{COUTRAS}}', 'sim')
		else:
			linha = linha.replace('{{COUTRAS}}', 'nao')
		arquivo_configuracao.write(linha)

	arquivo_configuracao.close()
	arquivo_base.close()
