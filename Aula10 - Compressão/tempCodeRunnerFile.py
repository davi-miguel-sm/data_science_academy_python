dict_alunos = {'Bob':6.8, 'Henry':7.9, 'Dennis':9.5, 'Pedro': 6.9}
dict_alunos_status = {k:('Aprovado' if v>7 else 'Reprovado') for (k,v) in dict_alunos.items()}
print(dict_alunos)
print(dict_alunos_status)