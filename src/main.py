'''
O Objeto Labirinto desenha um labirinto tomando como base uma matriz n x m, a funçao criaGrafo gera um grafo recebendo como parâmetros os nós, os arcos e as distancias que são gerados respectivamente pelas fuções mapearGrafo e medirDistancias tendo como base a matriz anterior.
então são medidos dois caminhos pela função astar que são os menores como pode ser visto pelo percurso das tartarugas
'''

import math
import time
from grafo import Grafo
from labirinto import Labirinto

matriz = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [1, 0, 0, 0, 1],
]

def calculaDistancia(a, b, dados):
  try:
    d = dados[a+":"+b]
  except(Exception):
    d = dados[b+":"+a]
  return d

def criaGrafo(nohs, arcos, dists):
  gr = Grafo()
  for n in nohs:
    gr.adicionaVertice(n)
  for t in arcos:
    gr.adicionaArco(t[0],t[1],calculaDistancia(t[0],t[1],dists))
  return gr

def mapearGrafo(matriz):
  nohs = []
  vizinhos = []
  n = len(matriz)
  m = len(matriz[0])
  for i in range(n):
    for j in range(m):
      if matriz[i][j] == 0:
        nohs.append(str(i)+','+str(j))

  for i in range(n):
    for j in range(m):
      if matriz[i][j] == 0:
          a = str(i) +','+ str(j)
          if (j + 1) < m and matriz[i][j + 1] != 1:
            r = str(i) +','+ str(j + 1)
            vizinhos.append((a,r))
          if (i + 1) < n and matriz[i + 1][j] != 1:
            d = str(i + 1) +','+ str(j)
            vizinhos.append((a,d))
          if (j - 1) >= 0 and matriz[i][j - 1] != 1:
            l = str(i) +','+ str(j - 1)
            vizinhos.append((a,l))
          if (i - 1) >= 0  and matriz[i - 1][j] != 1:
            u = str(i - 1) +','+ str(j)
            vizinhos.append((a,u))


  return nohs, vizinhos

nohs, vizinhos = mapearGrafo(matriz)

def medirDistancias(nohs):
  distancias = {}
  for i in range(len(nohs)):
    for j in range(len(nohs)):
      xi, yi = eval(str(nohs[i]))
      xd, yd = eval(str(nohs[j]))      
      d = math.hypot(yd - yi, xd - xi)

      distancias[str(xi)+','+str(yi)+':'+str(xd)+','+str(yd)] = d

  return distancias

distancias = medirDistancias(nohs)

gr = criaGrafo(nohs,vizinhos,distancias)

def calculaCustoCaminhos(grafo, fronteira, meta):

  custos = []
  for i in fronteira:
    c = 0
    for j in range(1, len(i)):      
      c += grafo.distancia(i[j-1],i[j])
    else:
      c += grafo.distancia(fronteira[-1], meta)
    custos.append(c)
  return custos

def astar(grafo, inicio, meta):
  fronteira = [[inicio]]
  
  while fronteira:
    custos = calculaCustoCaminhos(grafo, fronteira, meta)
    indC = custos.index(min(custos))
    caminho = fronteira.pop(indC)
    
    v = caminho[-1]
    if v == meta:
      return caminho
    else:
      vi = grafo.localizaRotulo(v)
      for i,w in enumerate(grafo.matrizIncidencias[vi]):
        if w>0:
          novoCaminho = list(caminho)
          novoElemento = grafo.listaVertices[i].rotulo
          novoCaminho.append(novoElemento)
          fronteira.append(novoCaminho)

  return "Busca mal sucedida"

labirinto = Labirinto(-100,0,30, matriz,'black','white')

caminho1 = astar(gr, '0,0','2,3')
caminho2 = astar(gr, '1,4','0,0')

labirinto.tartaruga.percorrerCaminho(caminho1)


labirinto.novaTartaruga('red', 1, 4) #cria uma tartaruga na posição (col,lin) da matriz com uma cor dada
time.sleep(2)
labirinto.tartaruga.percorrerCaminho(caminho2)
