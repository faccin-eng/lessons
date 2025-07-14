#random > selecionar um numero de 1 a 999 > atribuir a X
#input('Digite seu palpite...
#if palpite = x então CABOU!
#if palpite < x então dizer que é menor
#else então dizer que é maior

import random


repeticao = 0
palpite = 0
x = random.randint(1,999)
while palpite != x:
    palpite = int(input("Digite um palpite: "))
    repeticao += 1
    dif = palpite - x
        #y = input("Qualquer coisa ")
    #if palpite == int(y):print("Igual")
    if palpite == x:
        print("Você acertou o número {}".format(x))
        print("Você teve {} repetições".format(repeticao))
    elif palpite < x and dif < -100:
        print("O palpite é menor Tá frio")
    elif palpite < x:
        print("O palpite é menor")
    elif palpite > x and dif > 100:
        print("O palpite é maior Tá frio")
    else:
        print("O palpite é maior")
