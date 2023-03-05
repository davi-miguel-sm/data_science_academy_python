# Isso é uma lista
estudantes_list = ["Pedro",24,"Ana",22,"Ronaldo",25,"Jime",19]
print(type(estudantes_list))
#Isso é um dicionário
estudantes_dict = {"Pedro":24, "Ana":22, "Ronaldo":26, "Jime":19}
print(type(estudantes_dict))

print(estudantes_list[0])
print(estudantes_dict["Pedro"])

estudantes_dict["Marcelo"] = 25
print(estudantes_dict["Marcelo"])

# .clear() Limpa elementos
# del deleta objeto da memória

print(len(estudantes_dict))
print(estudantes_dict.keys()) # Retorna as chaves
print(estudantes_dict.values()) # Retorna os valores
print(estudantes_dict.items()) # Retorna o conjunto chave valor
