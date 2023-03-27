array = [30, 50, 10, 35, 70, 45, 80, 100, 22]

def selection_sort(array):
    tamanho = len(array)
    for j in range(tamanho - 1):
        min_index = j
        for i in range(j, tamanho):
            if array[i] < array[min_index]:
                min_index = i
        if array[j] > array[min_index]:
            array[j], array[min_index] = array[min_index], array[j]
        
    return array

array = selection_sort(array)
print(array)