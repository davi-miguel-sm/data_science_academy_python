#Criando uma Tupla
tupla = ("Geografia", 9, "História", 8.8, "Matemática", 9.5)

#Tuplas são estruturas imutáveis, ou seja, não modificáveis

# tupla.append("Filosofia") # Não suporta append
# del tupla("Geografia") #Não suporta delete de elementos

print(tupla[0]) # indexação normal
print(tupla[0::2]) #slicing como em listas

tupla_em_lista = list(tupla)

tupla_em_lista.append("Filosofia")
tupla_em_lista.append(7.58)
tupla_em_lista.append("Trembo")
tupla_em_lista.pop()
print(tupla_em_lista)
lista_em_tupla = tuple(tupla_em_lista)
print(lista_em_tupla, type(lista_em_tupla))