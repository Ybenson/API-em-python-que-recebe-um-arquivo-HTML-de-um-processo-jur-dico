#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 21:13:38 2019

@author: Ybenson Augustave
"""
### IMPORTACAO DA BIBLIOTECA "BeautifulSoup" PARA PROCURAR AS TAGS NA PAGINA HTML
from bs4 import BeautifulSoup
import json

#### CODIGO PARA LER O ARQUIVO HTMTL ######
path = '/home/aluno/Desktop/archive/' # O DIRETORIO DO ARQUIVO
file_read = 'processo1.html' # O NOME DO ARQUIVO
arquivo = open(path + file_read, 'r')
documento = arquivo.read()

def processo1(documento):
    ##### Codigo para pegar o numero do processo na pagina  HTML ######
    soup = BeautifulSoup(documento, "lxml")
    selector = 'html > body > div > table > tbody > tr > td > div > table > tbody > tr > td > table > tbody > tr > td > span'
    numero_de_processo = (soup.select(selector))
    soup = BeautifulSoup(str(numero_de_processo[0]))
    selector = 'html > body > span'
    found = soup.select(selector)
    numero_de_processo = soup.find('span').contents
    
    numero_de_processo = numero_de_processo[0].strip()
    
    #### CODIGO PARA PEGAR O VALOR DA CAUSA #####
    soup = BeautifulSoup(documento, "lxml")
    selector = 'html > body > div > table > tbody > tr > td > div > table > tbody > tr > td > span'
    valor_da_causa = (soup.select(selector))
    soup = BeautifulSoup(str(valor_da_causa[5]))
    selector = 'span'
    found = soup.select(selector)
    valor_da_causa = soup.find('span').contents
    
    valor_da_causa = valor_da_causa[0].strip()
    valor_da_causa = valor_da_causa.replace(" ", "")
        
    
    ##### CODIGO PARA PEAGAR A CLASSE DO PROCESSO NA PAGINA HTML #########
    soup = BeautifulSoup(documento, "lxml")
    selector = 'html > body > div > table > tbody > tr > td > div > table > tbody > tr > td > table > tbody > tr > td > span > span'
    classe = (soup.select(selector))
    soup = BeautifulSoup(str(classe[0]))
    selector = 'span'
    found = soup.select(selector)
    classe = soup.find('span').contents
    classe = classe[0].strip()
        
    ####### CODIGO PARA PEGAR O NOME DO JUIZ DO PROCESSO #######
    soup = BeautifulSoup(documento, "lxml")
    selector = 'html > body > div > table > tbody > tr > td > div > table > tbody > tr > td > span'
    nome_do_juiz = (soup.select(selector))
    soup = BeautifulSoup(str(nome_do_juiz[4]))
    selector = 'span'
    found = soup.select(selector)
    nome_do_juiz = soup.find('span').contents
    nome_do_juiz = nome_do_juiz[0].strip()
    
    
    #### CODIGO PARA PEGAR AS PARTES DO PROCESSO  ####
    soup = BeautifulSoup(documento, "lxml")
    selector = 'html > body > div > table > tbody > tr > td > div > span'
    partes_do_processo = (soup.select(selector))
    soup = BeautifulSoup(str(partes_do_processo[0]))
    
    selector = 'span'
    found = soup.select(selector)
    partes_do_processo = soup.find('span').contents
    partes_do_processo = partes_do_processo[0].strip()
    
    
    ##### ULTIMA MOVIMENTACAO DO PROCESSO #######
    soup = BeautifulSoup(documento, "lxml")
    selector = 'html > body > div > table > tbody > tr > td > table > tbody'
    ultima_movimentacao = (soup.select(selector))
    soup = BeautifulSoup(str(ultima_movimentacao[6]))
    selector = 'span'
    found = soup.select(selector)
    found = str(found[1])
    
    ultima_movimentacao = soup.find('span').contents
    ultima_movimentacao = ultima_movimentacao[0].strip()
    ultima_movimentacao = ultima_movimentacao.replace('\n',' ')
    
    
    #print(ultima_movimentacao)
    
    result=({'Número do processo': numero_de_processo, 'Valor da causa': valor_da_causa, 'Classe': classe, 'Nome do Juiz':nome_do_juiz, 'Ultima movimentacao': ultima_movimentacao, 'Partes do Processo': partes_do_processo})
    return str(result)
       
    
    
print(processo1(documento))



