# if
if 10>2:
    print("Barões da Pisadinha")
else:
    print("Aviões do Forró")

num = 9

if num >10:
    print("Barões da Pisadinha")
else:
    print("Aviões do Forró")

if num >10:
    print("Barões da Pisadinha")
elif num ==10:
    print("Aviões do Forró")
else:
    print("Péricles")

#Condicionais aninhados
banda = "boa"

if num >10:
    print("Barões da Pisadinha")
elif num ==10:
    if banda == "boa":
        print("Aviões do Forró")
    elif banda == "ruim":
        print("Luisa Sonza")
else:
    print("Péricles")