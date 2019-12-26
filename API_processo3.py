
"""
Created on Mon Dec 26 09:10:20 2019

@author: Ybenson Augustave
"""
### IMPORTACAO DAS BIBLIOTECA "BeautifulSoup" PARA PROCURAR AS TAGS NA PAGINA HTML E JSON
from bs4 import BeautifulSoup
import json


#### CODIGO PARA LER O ARQUIVO HTMTL ######
path = '/home/aluno/Desktop/archive/' # O DIRETORIO DO ARQUIVO
file_read = 'processo3.html' # O NOME DO ARQUIVO
arquivo = open(path + file_read, 'r')
documento = arquivo.read()

def processo3(documento):
    #def processo1(documento):
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
    soup = BeautifulSoup(str(valor_da_causa[7]))
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
    soup = BeautifulSoup(str(nome_do_juiz[5]))
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
    found = str(found[0])
    partes_do_processo = soup.find('span').contents
    partes_do_processo = partes_do_processo[0].strip()
    
    advogado_processo = BeautifulSoup(documento, 'html.parser')

    for s in advogado_processo.findAll('span', attrs = {'class':'mensagemExibindo'}):    
        
        #TRATAMENTO DE ERROR
        try:
            
            advogado_processo = (s.next_sibling.strip())
            if advogado_processo == '':
                pass
            else:
                advogado_processo = 'Advogado(a)', advogado_processo
                partes_do_processo = (partes_do_processo, advogado_processo)
              
                
        except NoneType:
            pass 
    
    result=({'Número do processo': numero_de_processo, 'Valor da causa': valor_da_causa, 'Classe': classe, 'Nome do Juiz':nome_do_juiz, 'Partes do Processo': partes_do_processo})
    return str(result)
       
    
print(processo3(documento))







