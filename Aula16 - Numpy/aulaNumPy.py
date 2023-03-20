#Numerical Python
import numpy as np

array1 = np.array([10,21,31,45,64,73,23,59,30,62])

# print(type(array1))
# print(np.shape(array1))
# print(array1[-1:-6:-2])

mask = (array1 % 2 != 0)
# print(type(mask))

indices = [1,4,6,2,3]
# print(array1[indices])

try:
    array1[9]= '*'
except ValueError:
    pass
    # print("Esse valor não pode ser convertido para int.")
finally:
    pass
    # print(array1)

# Funções Numpy
array1_acumulado = array1.cumsum()
# print(array1_acumulado)

array2 = np.arange(0,101,5)
# print(array2)

array3 = np.eye(4)
# print(array3)

array_bools = np.array([True,False,False,True,False])
# print(array_bools)

array_str = np.array(["Python","JavaScript","TypeScript"])
# print(array_str)

array_linspc = np.linspace(0,3,13) #Espaçados de forma linear
# print(array_linspc)

array_logspc = np.logspace(0,3,4) #Espaçados de forma logarítimica
# print(array_logspc)

#np.array =>Analise de dados | np.matrix => Cálculos

matrix1 = np.matrix([np.linspace(0,3,13),np.linspace(0,6,13)])
#print(matrix1, type(matrix1))

#Objetos 3d e 4d

array_3d = np.array([[np.linspace(0,3,13),np.linspace(0,6,13),np.linspace(0,9,13)],[np.linspace(0,9,13),np.linspace(0,6,13),np.linspace(0,3,13)]])
#print(array_3d)
#print(array_3d.shape)
#print(array_3d.ndim)

array_4d = np.array([[[np.linspace(0,3,13),np.linspace(0,6,13)],[np.linspace(0,9,13),np.linspace(0,6,13)]],[[np.linspace(0,3,13),np.linspace(0,6,13)],[np.linspace(0,9,13),np.linspace(0,6,13)]]])
# print(array_4d)
# print(array_4d.shape)
# print(array_4d.ndim)

#Manipulando arquivos
import os

filename = os.path.join('dataset.csv')
array_arqi = np.loadtxt(filename, delimiter=',', usecols=(0,1,2,3),skiprows=1)
# print(array_arqi)
# print(type(array_arqi))

#destructuring
largura,altura = np.loadtxt(filename, delimiter=',',usecols=(0,1),skiprows=1,unpack=True)
# print(f'{largura.min()}\n******\n{altura.max()}')

#plotando gráfico com numpy e matplotlib
import matplotlib
matplotlib.use('WebAgg')
import matplotlib.pyplot as plt
# plt.show(plt.plot(largura,altura,'o',markesize=6,color='red'))

#Calculando Média
array_media = np.array(np.linspace(0,9,41))
# print(array_media.mean()) # Média Aritmética  do Array (Soma todos e Divide pelo Número de Elementos)

#Calculando Variância
array_variancia = np.array(np.linspace(0,9,41))
print(f"{array_variancia.var():.4f}") # Variância do Array (Média do Quadrado da Diferença do Valor dos Elementos para a Média Aritmética)
