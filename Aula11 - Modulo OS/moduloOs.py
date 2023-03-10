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

Brasil = "O Brasil, um vasto país sul-americano, estende-se da Bacia Amazônica, no norte,\naté os vinhedos e as gigantescas Cataratas do Iguaçu, no sul. O Rio de Janeiro, simbolizado pela sua estátua\nde 38 metros de altura do Cristo Redentor, situada no topo do Corcovado, é famoso pelas movimentadas praias de Copacabana\ne Ipanema, bem como pelo imenso e animado Carnaval, com desfiles de carros alegóricos, fantasias extravagantes e samba. "
with open('Aula11 - Modulo OS/Brasil.txt','w',encoding="utf-8") as arquivo2:
    arquivo2.write(Brasil[::-1])

with open('Aula11 - Modulo OS/Brasil.txt','r',encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo[::-1])