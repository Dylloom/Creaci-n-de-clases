class Libro():
    def __init__(self, titulo, autor, genero, paginas):
        self.titulo = titulo
        self.autr = autr
        self.genero = genero
        self.paginas = paginas

    def obtener_titulo(self):
        return self.titulo

    def obtener_autor(self):
        return self.autr
    
    def obtener_genero(self):
        return self.genero
    
    def obtener_paginas(self):
        return self.paginas
    
    def establecer_titulo(self, titulo):
        self.titulo = titulo

    def establecer_autor(self, autor):
        self.autr= autr

    def establecer_genero(self, genero):
        self.genero = genero

    def establecer_paginas(self, paginas):
        self.paginas = paginas

    def comprobar_genero(self, genero):
        if (self.genero == genero):
            return True
        else:
            return False
        
if __name__ == "__main__":
    libro = Libro("Yo, robot", "Isaac Asimov", "ficción", 100)

    print(f"""
Libro: {libro.obtener_titulo()}
Autor: {libro.obtener_autr()}
Genero: {libro.obtener_genero()}
Paginas: {libro.obtener_paginas()}
""")
    
    r = int(input("Presione 1 si desea comprobar el genero o 0 para terminar: "))

    if (r == 1):
        g = input("Escriba el género que desea comprobar: ")
        if (libro.comprobar_genero(g)):
            print(f"El libro es del género que mencionó ({g})")
        else:
            print(f"El libro no es de ese género, es de {libro.obtener_genero()}")
    else:
        print("chau")
