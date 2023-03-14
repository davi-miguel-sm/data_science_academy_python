conteudo = []
with open('Aula13 - Projeto Hangman\palavras.txt', 'r',encoding='utf-8') as arquivo:
    conteudo = arquivo.read().split()
print(conteudo)

import random
from os import system,name

def limpa_tela():
    if name =='nt':
        _ = system('cls')
    else:
        _ = system('clear')

def texto_inicial(traços, chances, letras_erradas):
    print("".join(traços))
    print(f"\nChances Restantes: {chances}")
    print(f"Letras Erradas: ", "".join(letras_erradas))

def calcula_chances(palavra):
    chances = len(set(palavra))
    return chances

def game():
    limpa_tela()

    print("\nBem Vindo ao Jogo da Forca\n")
    print("\nQue os jogos comecem!\n")
    palavras_forca = conteudo
    palavra = random.choice(palavras_forca)

    traços_letras = ['_' for letra in palavra]
    chances = calcula_chances(palavra)
    letras_erradas = []

    while chances > 0:
        texto_inicial(traços_letras, chances, letras_erradas)    

        tentativa = input("\nTente a sua sorte:\n").lower()

        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    traços_letras[index] = letra
                index +=1
        else:
            chances -=1
            letras_erradas.append(tentativa)

        if "".join(traços_letras) == palavra:
            texto_inicial(traços_letras, chances, letras_erradas)
            print("VOCÊ SAIU VIVO DESSA VEZ!")
            break
    else:
        texto_inicial(traços_letras, chances, letras_erradas)
        print("VOCÊ FOI ELIMINADO!!!")
        print(f"A JUSTIÇA SERIA FEITA COM: {palavra}!")
game()