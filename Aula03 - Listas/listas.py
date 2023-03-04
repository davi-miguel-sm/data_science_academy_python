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