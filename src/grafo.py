class Vertice:
  def __init__(self, rotulo):
    self.rotulo = rotulo
  def __eq__(self, outro):
    return outro.rotulo == self.rotulo
  def __repr__(self):
    return self.rotulo  
  def __hash__(self):
    return hash(self.rotulo)

class Grafo:
  def __init__(self):
    self.numVerticesMaximo = 51
    self.numVertices = 0
    self.listaVertices = []
    self.matrizIncidencias = []
    for i in range(self.numVerticesMaximo):
      linhaMatriz = []
      for j in range(self.numVerticesMaximo):
        linhaMatriz.append(0)
      self.matrizIncidencias.append(linhaMatriz)

  def adicionaVertice(self, rotulo):
    self.numVertices += 1
    self.listaVertices.append(Vertice(rotulo))

  def adicionaArco(self, inicio, fim, peso):
    i = self.localizaRotulo(inicio)
    j = self.localizaRotulo(fim) 
    if i == -1 or j == -1: return
    self.matrizIncidencias[i][j] = peso
    self.matrizIncidencias[j][i] = peso    

  def localizaRotulo(self, rotulo):
    for i in range(self.numVertices):
      if self.listaVertices[i].rotulo == rotulo : return i
    return -1

  def distancia(self, r1, r2):
    i = self.localizaRotulo(r1)
    j = self.localizaRotulo(r2)
    if i == -1 or j == -1: return -1
    return self.matrizIncidencias[j][i]

  def mostraVertice(self, vertice):
    print(self.matrizIncidencias[vertice].rotulo)

  def imprimeMatriz(self):
    print(" ", end = ',')
    for i in range(self.numVertices):
      print(self.listaVertices[i].rotulo, end=",")
    print()
    for i in range(self.numVertices):
      for j in range(self.numVertices):
        print(self.matrizIncidencias[i][j], end=',')
      print()
