import csv

with open('Aula12 - Manipulando CSV/teste.csv','w',encoding='utf-8') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(('nota1','nota2','nota3'))
    writer.writerow((9.0, 7.4, 6.9))
    writer.writerow((9.3, 7.8, 9.5))
    writer.writerow((8.9, 7.5, 8.2))

with open('Aula12 - Manipulando CSV/teste.csv','r',encoding='utf-8', newline='\r\n') as arquivo:
    leitor = csv.reader(arquivo)
    for x in leitor:
        print(x)
