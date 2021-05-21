import urllib.request, json, os
import pandas as pd
import urllib.request, json, pandas as pd, time


user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021911 Firefox/3.0.7'
headers={'User-Agent':user_agent,} 


def Consulta_FGTS(CNPJ):
  # Importação dos dados
  start = time.time()
  url = "https://tools.learningcontainer.com/sample-json.json"
  #url = "https://api.infosimples.com/api/v1/caixa/regularidade.json?token=ggNiWp8f1GLfsFeaQnto_rKRnqriMtJTfjl4rimm&timeout=600&cnpj="+CNPJ+"&cei="
  request=urllib.request.Request(url,None,headers) #The assembled request
  response = urllib.request.urlopen(request)
  data = json.loads(response.read())
  with open("FGTS_"+str(CNPJ)+'.json', 'w') as fp:
    json.dump(data, fp)
  tempo = (round(time.time()-start,2))
  print(f"Tabela com CNPJ:{CNPJ} criada em {tempo} segundos!")

def Consulta_Divida(CNPJ):
  # Importação dos dados
  start = time.time()
  url = "https://tools.learningcontainer.com/sample-json.json"
  #url = "https://api.infosimples.com/api/v1/pge/divida-ativa/sp.json?token=ggNiWp8f1GLfsFeaQnto_rKRnqriMtJTfjl4rimm&timeout=600&cda=&cnpj="+CNPJ+"&cpf=&ie=&renavam="
  request=urllib.request.Request(url,None,headers) #The assembled request
  response = urllib.request.urlopen(request)
  data = json.loads(response.read())
  with open("DividaAtiva_"+str(CNPJ)+'.json', 'w') as fp:
    json.dump(data, fp)
  tempo = (round(time.time()-start,2))
  print(f"Tabela com CNPJ:{CNPJ} criada em {tempo} segundos!")


def Consulta_CertidaoNegativa(CNPJ):
 # Importação dos dados
  start = time.time()
  url = "https://tools.learningcontainer.com/sample-json.json"
  #url = " https://api.infosimples.com/api/v1/mte/certidao-debitos.json?token=ggNiWp8f1GLfsFeaQnto_rKRnqriMtJTfjl4rimm&timeout=600&cnpj="+CNPJ+"&cpf="
  request=urllib.request.Request(url,None,headers) #The assembled request
  response = urllib.request.urlopen(request)
  data = json.loads(response.read())
  with open("CertNegativa_"+str(CNPJ)+'.json', 'w') as fp:
    json.dump(data, fp)
  tempo = (round(time.time()-start,2))
  print(f"Tabela com CNPJ:{CNPJ} criada em {tempo} segundos!")

def Consulta_PGFN(CNPJ):
 # Importação dos dados
  start = time.time()
  url = "https://tools.learningcontainer.com/sample-json.json"
  #url = "https://api.infosimples.com/api/v1/receita-federal/pgfn.json?token=ggNiWp8f1GLfsFeaQnto_rKRnqriMtJTfjl4rimm&timeout=600&cnpj="+CNPJ+"&cpf=&preferencia_emissao="
  request=urllib.request.Request(url,None,headers) #The assembled request
  response = urllib.request.urlopen(request)
  data = json.loads(response.read())
  with open("/PGFN_"+str(CNPJ)+'.json', 'w') as fp:
    json.dump(data, fp)
  tempo = (round(time.time()-start,2))
  print(f"Tabela com CNPJ:{CNPJ} criada em {tempo} segundos!")




def API_REQUEST(CNPJS):
  for pos, id in enumerate(CNPJS):
    if len(id) == 14:  #Validação CNPJ  
      Consulta_FGTS(id)
      Consulta_Divida(id)
      Consulta_PGFN(id)
      Consulta_CertidaoNegativa(id)
    else:
      print(CNPJS[pos], "-- > CNPJ Invalido!") #CNPJ < 14 Digitos
      continue
  print("Tabelas Criadas")

  
  
  
  

def main():


  lista = ["45990181000189", "23643315000152"]
  API_REQUEST(lista)

if __name__ == "__main__":
    main()





