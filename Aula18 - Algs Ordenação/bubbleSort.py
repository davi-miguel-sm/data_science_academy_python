array = [30, 50, 10, 35, 70, 45, 80, 100, 22]

def bubble_sort(array):
    tamanho = len(array)

    for i in range(tamanho - 1):
        for j in range(tamanho - 1):
            if array[j] > array[j + 1]: # Compara se o atual é maior que o proximo
                array[j + 1], array[j] = array[j], array[j + 1] # Se maior troca as posições
    return array

array = bubble_sort(array)
print(array)