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