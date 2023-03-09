def funcao():
    print("Hello World")

funcao()

def imprime(valor):
    print(valor)

lista = [1, 2, 3, 4, 5, 6]
imprime(lista)

def retornaMaior(lista):
    maior = 0
    i = 0
    while i < len(lista):
        if lista[i] > maior:
            maior = lista[i]
        i += 1
    return maior

maior = retornaMaior(lista)
print(maior)

def potencia(num): return num ** 2
pot = lambda num: num ** 2

print(potencia(10))
print(pot(10))

reversoUpper = lambda valor: valor.upper()[::-1]

print(reversoUpper("Davi Miguel de Sousa Machado"))