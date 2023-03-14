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

    def imprimir(self):
        return Animal.imprimir()
    
    def emitir_som(self):
        print("Au Au.")
    
rex = Cachorro()
rex.imprimir