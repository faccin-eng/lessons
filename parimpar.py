import random

#if soma % 2 = 0 and escolha = par { print("Jogador ganhou")}
#elif soma % 2 = 1 and escolha = impar { print("Jogador ganhou")}
#else print("Perdeu playboy")
escolha = input('Escolha par ou impar: ')
e2 = int(input('Escolha um numero: '))
e3 = random.randint(1,20)
e4 = e2 + e3
print(e4 % 2)
if(e4 % 2==0 and escolha == "par"):
    print("Voce ganhou")
elif(e4 % 2==1 and escolha =="impar"):
    print("Voce ganhou")
else : print("Voce perdeu")





