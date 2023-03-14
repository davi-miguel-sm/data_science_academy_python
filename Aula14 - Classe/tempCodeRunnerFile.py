class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        pass

    def frear(self):
        pass

class Carro(Veiculo):
    def acelerar(self):
        print("O carro está acelerando.")
    
    def frear(self):
        print("O carro está freando.")

class Moto(Veiculo):
    def acelerar(self):
        print("A moto está acelerando.")
    
    def frear(self):
        print("A moto está freando.")

class Aviao(Veiculo):
    def acelerar(self):
        print("A avião está acelerando.")
    
    def frear(self):
        print("A avião está freando.")
    
    def decolar(self):
        print("O avião está decolando.")

lista_veiculos = [ Moto('Honda', 'Biz 125'), Carro('Ford', 'Focus 2020'), Aviao('USArmy', 'F22-Raptor')]

for item in lista_veiculos:
    item.acelerar()
    item.frear()

    if isinstance(item,Aviao):
        item.decolar()
    print("----")