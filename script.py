import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import re

url = 'https://sigaa.sistemas.ufg.br/sigaa/public/curso/alunos.jsf?lc=pt_BR&id=69675808'


dados = requests.get(url)
pagina = bs(dados.content.decode('utf-8'))


df = pd.DataFrame(columns=['matricula', 'nome'])
i = 0
for linha in pagina.find_all('tr', {'class':re.compile('linhaPar|linhaImpar')}):
    matricula = linha.find('td').text
    nome      = linha.find_all('td')[-1].text
    df.loc[i] = [matricula, nome]
    i += 1

sobrenomes_dict = {}
for i, nome in zip(df.index, df['nome']):
    sobrenomes = nome.split()[1:]
    sobrenomes = [s for s in sobrenomes if len(s)>2]

    # Agora vamos preencher o nosso dicionário de sobrenomes
    for sobrenome in sobrenomes:
        if sobrenome not in sobrenomes_dict:
            sobrenomes_dict[sobrenome] = [i]
        else:
            sobrenomes_dict[sobrenome].append(i)



    gi_clas = {i:[] for i in df.index}


    for sobrenome in sobrenomes_dict.keys():
        if len(sobrenomes_dict[sobrenome]) > 1:
         for i in sobrenomes_dict[sobrenome]:
            for j in sobrenomes_dict[sobrenome]:
                if i != j:
                    gi_clas[i].append(j)



                    from collections import deque
def buscaEmLargura(inicio, objetivo, grafo):
    fila = deque([[inicio]])
    visitados = set()

    while fila:
        caminho = fila.popleft()
        vertice = caminho[-1]

        if vertice not in visitados:
            visitados.add(vertice)

            if vertice == objetivo:
                return caminho

            for vizinho in grafo[vertice]:
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)


def BuscaEmProfundidade (inicio, alvo,grafo,caminho = None):
    if caminho == None:
      caminho = [inicio]
    if inicio == alvo:
       return caminho
    for vizinho in grafo[inicio]:
       if vizinho not in caminho:
          novo_caminho = BuscaEmProfundidade(vizinho,alvo,grafo,caminho+[vizinho])
          if novo_caminho:
              return novo_caminho
          

caminho = BuscaEmProfundidade(2, 47, gi_clas)
[df.loc[discente, 'nome'] for discente in caminho]

caminho = buscaEmLargura(2, 47, gi_clas)
[df.loc[discente, 'nome'] for discente in caminho]