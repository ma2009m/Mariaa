class livro():
    def __init__(self, titulo, autor, paginas):
        print("um livro foi criado")
        self.titulo = titulo 
        self.autor = autor 
        self.paginas = paginas
        
    def __str__(self):
        return "titulo: "+self.titulo+" autor: "+self.autor+" paginas: "+str(self.paginas)

    def __len__(self):
        return self.paginas

    def __del__(self):
        print("livro destruido")

book = livro("Clrl+Play" , "Mateus" , 2009)

print(book)

print(len(book))

del book
