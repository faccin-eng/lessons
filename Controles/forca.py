#Lista de palavras:

import random
import unicodedata

def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

palavras = [
    "abacaxi",  
    "banana",   
    "cachorro", 
    "dicionário",       
    "elefante", 
    "futebol",  
    "guitarra", 
    "hipopótamo", 
    "jacaré",   
    "kiwi",     
    "leão",     
]

palavra_escolhida = random.choice(palavras)
palavra_sem_acentos = remover_acentos(palavra_escolhida)  # Versão sem acentos
letras = []
tentativas = 7

while True:
    # Mostrar a palavra
    for i, letra_original in enumerate(palavra_escolhida):
        letra_sem_acento = palavra_sem_acentos[i]
        if letra_sem_acento in letras or letra_original in letras:
            print(letra_original, end=" ")  # Mantém a letra original (com acento)
        else:
            print("_", end=" ")
    print()

    palpite = input("Digite um palpite: ").lower()
    palpite_sem_acento = remover_acentos(palpite)

    if palpite_sem_acento in letras:
        print("Você já tentou essa letra.")
    elif palpite_sem_acento in palavra_sem_acentos:
        print("Acertou!")
        letras.append(palpite_sem_acento)
    else:
        print("Errou.")
        letras.append(palpite_sem_acento)
        tentativas -= 1

    if all(c in letras or c == ' ' for c in palavra_sem_acentos):
        print(f"Você ganhou! A palavra era: {palavra_escolhida}")
        break

    if tentativas == 0:
        print(f"Você perdeu! A palavra era: {palavra_escolhida}")
        break






    



