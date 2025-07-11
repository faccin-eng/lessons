# Pedir a nota com o input
# Se a nota for maior que 8 então aprovado com honra (print)
# Se for maior que 6 aprovado
# Se for menor que 6 reprovado
n = float(input("Qual a nota do aluno: "))
x = input("Qual o comportamento do aluno:(y/n) ")
if( n > 8 and x == "y"):
    print("Aprovado com honra")
elif ( n > 6 ):
    print("Aprovado")
elif ( n > 4 ):
    print("Recuperação")
else :
    print("Reprovado")


    
