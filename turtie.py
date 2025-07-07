import turtle

<<<<<<< Updated upstream
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
=======
bob = turtle.Turtle()
for _ in range(20) :
    bob.right(320)
    for _ in range (2):
        bob.pencolor("purple")  # Move para frente 100 unidades
        bob.forward(10)  # Move para frente 100 unidades
        bob.right(10)   
        bob.forward(10)  # Gira 90 graus à direita
        bob.left(12)
>>>>>>> Stashed changes

turtle.mainloop() #mantem a janela aberta