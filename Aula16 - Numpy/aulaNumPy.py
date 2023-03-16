#Numerical Python
import numpy as np

array1 = np.array([10,21,31,45,64,73,23,59,30,62])

# print(type(array1))
# print(np.shape(array1))

print(array1[-1:-6:-2])

mask = (array1 % 2 != 0)
print(type(mask))

indices = [1,4,6,2,3]
print(array1[indices])

try:
    array1[9]= '*'
except ValueError:
    print("Esse valor não pode ser convertido para int.")
finally:
    print(array1)