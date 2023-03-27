array = [30, 50, 10, 35, 70, 45, 80, 100, 22]

def insertion_sort(array):
    tamanho = len(array)

    for i in range(1,tamanho):
        chave = array[i]
        j = i - 1
        while j >= 0 and array[j] > chave:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = chave

    return array


array = insertion_sort(array)
print(array)