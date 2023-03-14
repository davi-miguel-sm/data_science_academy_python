class Livro():
    def __init__(self,nome,autor):
        self.nome = nome
        self.autor = autor
    def imprime(self):
        print(f"O livro {self.nome} foi criado por {self.autor}.")

livro_principe = Livro("O Princípe", "Nicolau Maquiavel")
livro_principe.imprime()

livro_rangers = Livro("Rangers - A Ordem dos Arqueiros", "John Flanagan")
livro_rangers.imprime()