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

filename = os.path.join('Aula16 - Numpy\dataset.csv')
array_arqi = np.loadtxt(filename, delimiter=',', usecols=(0,1,2,3),skiprows=1)
# print(array_arqi)
# print(type(array_arqi))

#destructuring
largura,altura = np.loadtxt(filename, delimiter=',',usecols=(0,1),skiprows=1,unpack=True)
# print(f'{largura.min()}\n******\n{altura.max()}')

#plotando gráfico com numpy e matplotlib
# import matplotlib
# matplotlib.use('WebAgg')
# import matplotlib.pyplot as plt
# plt.show(plt.plot(largura,altura,'o',markesize=6,color='red'))

#Calculando Média
array_media = np.array(np.linspace(0,9,41))
# print(array_media.mean()) # Média Aritmética  do Array (Soma todos e Divide pelo Número de Elementos)

#Calculando Variância
array_variancia = np.array(np.linspace(0,9,41))
# print(f"{array_variancia.var():.4f}") # Variância do Array (Média do Quadrado da Diferença do Valor dos Elementos para a Média Aritmética)

#Calculando Desvio Padrão
array_dsvpdr = np.array(np.linspace(0,9,41))
# print(f"{array_variancia.std():.4f}") # Desvio Padrão do Array (Raiz Quadrada da Variância) std = standard deviation

#Operações Matemáticas com Numpy
array_op = np.arange(1,11)
# print(array_op.sum()) # Soma os valores
# print(array_op.cumsum()) # Soma acumulada
# print(array_op.prod()) # Produto dos valores
# print(array_op.cumprod()) # Produto Acumulado

array_somado = np.add(np.linspace(0,9,41),np.linspace(0,3,41)) # Soma dois arrays
# print(array_somado)

matrix_produt1 = np.array([[1000,2000,3000],[4000,5000,6000]])
matrix_produt2 = np.array([[2,3],[2,3],[2,3]])
# print(matrix_produt1)
# print(matrix_produt2)
matrix_prod = np.dot(matrix_produt1,matrix_produt2)
matrix_prod1 = matrix_produt1 @ matrix_produt2
# print(matrix_prod == matrix_prod1)

#slicing arrays e matrizes
array_slicing = np.diag(np.arange(3))
# Metódo diag cria uma matriz preenchida na diagonal
print(array_slicing[::-1,0:2])

array_slicing2 = np.arange(11)
print(array_slicing2[0:11:2])
print(array_slicing2[-2:0:-2])
print(array_slicing2[0:4] **2)

array_slicing3 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# Metódo FLatten converte array multidimensional em unidirecional
print(array_slicing3.flatten())
#Metódo repeat repete os elementos do array n vezes
print(array_slicing3.flatten()[0:5].repeat(2))
#Metódo tile repete o array n vezes
print(np.tile(array_slicing3.flatten()[0:5],2))
#Metódo copy cria uma cópia do array
print(np.copy(array_slicing3.flatten()[0:5]))