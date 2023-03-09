lista_numeros = [x for x in range(0,11)]
print(lista_numeros)

lista_frutas = ["Abacate", "Melão", "Banana", "Morango", "Uva", "maçã"]

frutas_comeca_m = [x for x in lista_frutas if x[0] =='M' or x[0] == 'm']
print(frutas_comeca_m)

dict_alunos = {'Bob':6.8, 'Henry':7.9, 'Dennis':9.5, 'Pedro': 6.9}
dict_alunos_status = {k:('Aprovado' if v>7 else 'Reprovado') for (k,v) in dict_alunos.items()}
print(dict_alunos)
print(dict_alunos_status)