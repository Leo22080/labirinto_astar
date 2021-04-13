import turtle

class Tartaruga:
    def __init__(self, posx, posy, passo, cor):
        
        self.tartaruga = turtle.Turtle()
        self.tartaruga.penup()
        self.tartaruga.setpos(posx, posy)
        self.tartaruga.pendown()
        self.tartaruga.shape("turtle")
        self.tartaruga.color(cor)
        self.pos = 'DIREITA'
        self.passo = passo
        self.cor = cor
        self.inicio = '0,0'

    def move(self, destino):

      if destino == self.inicio: return
      
      xi, yi = eval(self.inicio)
      xd, yd = eval(destino)
      #print(xi, yi, '==>', xd, yd)
      
      if xi == xd:
        if yi > yd: self.toLEFT()
        if yi < yd: self.toRIGHT()
      if xi > xd: self.toUP()
      if xi < xd: self.toDOWN()

      self.inicio = destino

    def moveTo(self, inicio, destino):

      if destino == self.inicio: return
      
      xi, yi = eval(inicio)
      xd, yd = eval(destino)
      #print(xi, yi, '==>', xd, yd)
      
      if xi == xd:
        if yi > yd: self.toLEFT()
        if yi < yd: self.toRIGHT()
      if xi > xd: self.toUP()
      if xi < xd: self.toDOWN()

      self.inicio = destino

    def percorrerCaminho(self, caminho):
      
      for i in range(len(caminho)-1):
        self.moveTo(caminho[i], caminho[i+1])


    def toUP(self):
        if self.pos == 'BAIXO': self.tartaruga.left(180)
        elif self.pos == 'ESQUERDA': self.tartaruga.right(90)
        elif self.pos == 'DIREITA': self.tartaruga.left(90)
        self.tartaruga.forward(self.passo)
        self.pos = 'CIMA'

    def toDOWN(self):
        if self.pos == 'CIMA': self.tartaruga.left(180)           
        elif self.pos == 'ESQUERDA': self.tartaruga.left(90)
        elif self.pos == 'DIREITA': self.tartaruga.right(90)        
        self.tartaruga.forward(self.passo)
        self.pos = 'BAIXO'
        
    def toLEFT(self):
        if self.pos == 'CIMA': self.tartaruga.left(90)
        elif self.pos == 'BAIXO': self.tartaruga.right(90)
        elif self.pos == 'DIREITA': self.tartaruga.right(180)
        self.tartaruga.forward(self.passo)
        self.pos = 'ESQUERDA'
        
    def toRIGHT(self):
        if self.pos == 'CIMA': self.tartaruga.right(90)
        elif self.pos == 'BAIXO': self.tartaruga.left(90)
        elif self.pos == 'ESQUERDA': self.tartaruga.right(180)  
        self.tartaruga.forward(self.passo)
        self.pos = 'DIREITA'

    def setColor(self, cor):
      self.tartaruga.color(cor)
