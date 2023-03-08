# Loop While

valor = 100
while valor < 10:
    valor += 1
else:
    print("Saindo do Loop...")
print(valor)

while valor >= 10:
    valor -= 1
    if valor == 11:
        break
    if valor == 44:
        continue
    print(valor)
