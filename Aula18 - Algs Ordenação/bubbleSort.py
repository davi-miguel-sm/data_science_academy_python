array = [30, 50, 10, 35, 70, 45, 80, 100, 22]
tam_array = len(array)

for i in range(tam_array):
    for j in range(tam_array - 1): 
        if array[j] > array[j+1]: # Compara se o atual é maior que o proximo
            array[j+1], array[j] = array[j], array[j+1] # Se maior troca as posições

print(array)