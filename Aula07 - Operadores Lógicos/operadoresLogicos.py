#and - True se ambas forem true {É curto circuito, primero valor false interrompe a verificação}
num = 9
if num > 10 and num <15:
    print("Docin de Leite")
else:
    print("Jiló assado")

#or - True se pelo menos uma for true {É curto circuito, primeiro valor true interrompe a verificação}
if num > 10 or num <15:
    print("Docin de maracujá")
else:
    print("Pimenta malagueta")

#not - Inverte o valor lógico da expressão

if not(num>10 or num <15):
    print("Docin de maracujá")
else:
    print("Pimenta malagueta")