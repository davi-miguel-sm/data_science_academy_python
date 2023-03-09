tupla = (1, 2, 3, 4, 5)
for num in tupla:
    print(num**2)

lista_strings = ["Alfa", "Beta", "Omega", "Sigma"]
for letra_grega in lista_strings:
    print(letra_grega[0:3])

for count in range(0, 100):
    if count % 2 == 0:
        print(count)

# For aninhado
for palavra in lista_strings:
    for char in palavra:
        print(f"{char} : {palavra}")

# Busca
matriz = [[654, 465, 231], [98, 796, 656], [334, 465, 798], [
    465, 132, 987], [25, 49, 82], [46, 79, 35], [99, 106, 46], [98, 797, 646]]
maior_num = 0
for listas in matriz:
    for num in listas:
        if num > maior_num:
            maior_num = num
print(maior_num)
