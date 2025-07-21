import sys
sair = "n"
while sair == "n":
    entrada = input("Digite algo: ")
    try:
        variavel = eval(entrada)
    
    except:
        variavel = entrada
        print(type(entrada))
    print("Valor digitado:", variavel)
    print("Tipo da variável:", type(variavel))

    sair = input("Digite 'n' para continuar ou outra tecla para sair: ")









#fazer um programa que diga o tipo da variavel digitada
#x = input(var)
#fazer uma conversão desse input
#if x int(x) elif float(x) elif bool(x)
#print(type(x))





# import math


# def mathpotencia(a, b):
#     return float(a ** b)


# print(mathpotencia(2,2))


def print_lyrics():
    print('Era um garoto que como eu')
    print('Amava os beatles e os rolling stones')

print_lyrics()
