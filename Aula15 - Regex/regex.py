import re

texto = 'Meu email é testedeemail@teste.com e o rerva é emailreserva@teste.com.'

resultado = len(re.findall('@',texto))
print(resultado)

emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',texto)
print(emails)