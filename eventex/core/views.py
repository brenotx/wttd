# -*- coding: latin-1 -*-

###################################################################
#########    Maneira de retornar um texto       ################### 
#                                                        		  #	
#	from django.http import HttpResponse                    	  #
#                                                         		  #
#	def homepage(request):                              		  #
#		return HttpResponse('Bem-vindo ao EventeX!')       		  #
###################################################################


###################################################################
##### Maneira 'bruta' de rederizar um template.html ###############
#																  #
#	from django.http import HttpResponse                          #
#   from django.template import loader, Context					  #
#																  #
#	def homepage(request):										  #
#		t = loader.get_template('index.html')					  #
#		c = Context()											  #
#																  #
#		#o .render renderiza a saida a partir do Context()		  #
#		content = t.render(c)									  #
#																  #
#		return HttpResponse(content)							  #
#																  #
###################################################################
# O loader eh o carregador de templates, ele consegue 			  #
# encontrar o template e instanciar uma classe template           #
# com o conteudo.												  #
# 																  #
# O Context eh uma instancia de contexto						  #
###################################################################


####################################################################
#### Maneira 'facil' de rederizar um template.html #################
#																   #
#	from django.shortcuts import render_to_response				   #
#																   #
#	def homepage(request):										   #
#		return render_to_response('index.html', context)		   #
#																   #
####################################################################


####################################################################
#### Forma 'bruta' de passar o diretorio dos arquivos estaticos ####
#																   #
#	from django.shortcuts import render_to_reponse				   #
#	from django.conf import settings							   #
#																   #
#	def homepage(request):										   #
#		context = {'STATIC_URL': settings.STATIC_URL}			   #
#		return render_to_response('index.html', context)		   #
#																   #
####################################################################
# Importar o settings para referenciar o diretorio estaticos.      #
# 																   #	
# A variavel context esta recebendo uma string imutavel que foi    #
# importada do settings e que diz o diretorio de onde estao meus   #
# arquivos estatios.											   #	
#																   #	
# render_to_response eh uma funcao de atalho do Django que faz     #
# todo trabalho de pegar um template e renderizar com o conteudo.  #	
####################################################################

####################################################################
# RequestContext eh uma classe que herda de Context e faz os 
# processamentos do 'Context Processors' Ex.: Coloca o STATIC_URL e 
# o MEDIA_URL dentro do contexto automaticamente.

from django.shortcuts import render_to_response
from django.template import RequestContext

def homepage(request):
	context = RequestContext(request)
	return render_to_response('index.html', context)
#
####################################################################


####################################################################
### Melhor forma porem ela esta sendo descontinuada no Django 1.5 ##
#																   #	
#	from django.views.generic.simple import direct_to_template     #
#																   #	
#	def homepage(request):										   #	
#		return direct_to_template(request, template='index.html')  #
#																   #
####################################################################
