texto = "Cientista de Dados pode sr uma excelente alternativa de carreira\n"
texto = texto + "Esses profissionais precisam saber como programar em Python\n"
texto += "E, claro, devem ser proeficientes em Data Science."

import os

arquivo = open(os.path.join('Aula11 - Modulo OS/cientista.txt'),'w')

for palavra in texto.split():
    arquivo.write(palavra + ' ')
arquivo.close()

arquivo = open('Aula11 - Modulo OS/cientista.txt','r')
conteudo = arquivo.read()
arquivo.close()
print(conteudo)