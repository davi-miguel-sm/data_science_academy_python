# Isso é uma lista
estudantes_list = ["Pedro",24,"Ana",22,"Ronaldo",25,"Jime",19]
#print(type(estudantes_list))
#Isso é um dicionário
estudantes_dict = {"Pedro":24, "Ana":22, "Ronaldo":26, "Jime":19}
#print(type(estudantes_dict))

print(estudantes_list[0])
print(estudantes_dict["Pedro"])

estudantes_dict["Marcelo"] = 25
#print(estudantes_dict["Marcelo"])

# .clear() Limpa elementos
# del deleta objeto da memória

print(len(estudantes_dict)) # 5 pares de valor
print(estudantes_dict.keys()) # Retorna as chaves
print(estudantes_dict.values()) # Retorna os valores
print(estudantes_dict.items()) # Retorna o conjunto chave valor

estudantes_dict2 = {"Camila":22, "Maria":32, "Naldo":16, "Jime":19}

estudantes_dict.update(estudantes_dict2)
#print(estudantes_dict)

idade_ana = estudantes_dict["Ana"]
print(idade_ana)

dict_lists = {"key_1":["username","password"], "key_2":["username","password"]}
print(dict_lists["key_1"][1].upper()) #Acesso ao item da lista dentro chave

#Dicionários aninhados
dict_dicts = {"dict_1":{"dict_2_0":{"nome":"idade"}, "dict_2_1":{"endereço":"cep"}}}