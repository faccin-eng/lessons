import turtle

bob = turtle.Turtle() #atribui a função turtle a bob

for _ in range (16):
    bob.pencolor("blue")  # azul
    bob.forward(50)  # Move para frente 100 unidades
    bob.right(90)     # Gira 90 graus à direita
    bob.pencolor("green") #verde
    bob.forward(50) 
    bob.left(30) #gira 30 graus para ESQUERDA
    bob.pencolor("red") #vermelho
    bob.forward(100)

turtle.mainloop() #mantem a janela aberta