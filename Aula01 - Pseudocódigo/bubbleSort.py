lista = [9595,7670,558,4187,7031,8020,2221,9589,6522,1918]

def bubble_sort(arr):
    n= len(arr)
    for i in range(n):
        for j in range (0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
    return arr
print(bubble_sort(lista))