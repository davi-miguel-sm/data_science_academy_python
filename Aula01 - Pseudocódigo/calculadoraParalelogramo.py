print('Bem vindo ao calculador de area do paralelogramo!')

valor_da_base = input('Digite o valor da base:')
base_float = float(valor_da_base) 
valor_da_altura = input('Digite o valor da altura:')
altura_float = float(valor_da_altura) 

area_do_paralelogramo = base_float * altura_float
print(f'A area do paralelogramo é {area_do_paralelogramo:.2f}')