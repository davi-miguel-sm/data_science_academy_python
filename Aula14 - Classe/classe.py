class Livro:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
    def imprime(self):
        print(f"O livro {self.titulo} foi criado por {self.autor}.")

livro_principe = Livro("O Princípe", "Nicolau Maquiavel")
livro_principe.imprime()

livro_rangers = Livro("Rangers - A Ordem dos Arqueiros", "John Flanagan")
livro_rangers.imprime()

# Trabalhando com Mais Metódos
class Circulo:
    _pi = 3.14
    def __init__(self, raio = 5):
        self.raio = raio
    
    def retornaArea(self):
        return self.raio ** 2 * Circulo._pi
    
    def retornaCircuferencia(self):
        return 2 * self.raio * Circulo._pi

    def setRaio(self, novo_raio):
        self.raio = novo_raio
    
    def getRaio(self):
        return self.raio
    
circulo_raio12 = Circulo(12)
print(circulo_raio12.retornaArea())
print(circulo_raio12.retornaCircuferencia())

circulo = Circulo()
print(circulo.getRaio())
circulo.setRaio(6)
print(circulo.getRaio())

# Herança

class Animal:
    def __init__(self):
        print("Animal Criado.")
    
    def imprimir(self):
        print("Este é um animal.")
    
    def comer(self):
        print("Hora de comer.")
    
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Cachorro Criado.")
    
    def emitir_som(self):
        print("Au Au.")
    
rex = Cachorro()
rex.comer()

# Polimorfismo

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