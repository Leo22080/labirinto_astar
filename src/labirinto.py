import turtle

from tartaruga import Tartaruga

class Labirinto:
  def __init__(self, posx, posy, lado, matriz,cor_1, cor_2):

    self.mat = matriz
    self.n = len(matriz) #colunas
    self.m = len(matriz[0]) #linhas
    self.lado = lado

    #usa o turtle para desenhar o labirinto modelado pela matriz 
    for i in range(self.n):
      turtle.penup()
      turtle.goto(posx, i*lado)
      turtle.pendown()

      for j in range(self.m):
        if matriz[self.n -1 - i][j] == 1:
          self.quadrado(turtle.xcor(),turtle.ycor(),lado,cor_1)
        else:
          self.quadrado(turtle.xcor(),turtle.ycor(),lado,cor_2)
        turtle.penup()
        turtle.setx(turtle.xcor()+lado)
        turtle.pendown()

    turtle.speed(3)
    self.tartaruga = Tartaruga(-83, (self.n  * self.lado)-15, lado,'green')

  def novaTartaruga(self, cor, ncol, nlin):
    self.tartaruga = Tartaruga(-83+self.lado*nlin, (self.n  * self.lado)-15 - self.lado*ncol , self.lado, cor )

  def quadrado(self, posx,posy,lado,cor):
    turtle.speed(0)
    turtle.showturtle()
    turtle.penup()
    turtle.goto(posx,posy)
    turtle.pendown()
    turtle.fillcolor(cor)
    turtle.begin_fill()
    for i in range(4):
      turtle.forward(lado)
      turtle.left(90)
    turtle.end_fill()
    turtle.hideturtle()
