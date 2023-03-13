conteudo = []
with open('Aula13 - Projeto Hangman\palavras.txt', 'r',encoding='utf-8') as arquivo:
    conteudo = arquivo.read().split()
print(conteudo)