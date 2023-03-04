#Criando uma lista
lista_1 = ['arroz, frango, tomate, leite']
print(type(lista_1))

lista_2 = ['arroz', 'frango', 'tomate', 'leite']
print(type(lista_2))

lista_3 = [23,100,'Data Science']
print(type(lista_3))

item1 = lista_3[0]
item2 = lista_3[1]
item3 = lista_3[2]

lista_2[2] = 'Chocolate'
del lista_2[3]
print(lista_2)

#Lista de Listas
lista_aninhada = [[1,2,3],['A','B','C'],[True, False, False]]
print(type (lista_aninhada))

lista_nums = lista_aninhada[0]
lista_strs = lista_aninhada[1]
lista_bool = lista_aninhada[2]

print(sum(lista_nums))
print(len(lista_strs))
print(max(lista_bool))

lista_velha = [1,4,66,78,93,12,11]
lista_nova = []

for item in lista_velha:
    if(item % 2 == 0):
        lista_nova.append(item)
print(lista_nova)

nome = 'Davi'
nome = list(nome)
nome.reverse()
print(nome)