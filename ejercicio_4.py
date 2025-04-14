class Rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho
    
    def obtener_longitud(self):
        return self.longitud
    
    def obtener_ancho(self):
        return self.ancho
    
    def calcular_area(self):
        area = self.ancho * self.longitud
        return area

    def calcular_perimetro(self):
        perimetro = 2 *(self.ancho * self.longitud)
        return perimetro
    
if __name__ == "__main__":
    rectangulo = Rectangulo(20, 30)

    print(f"""Rectangulo
Longitud: {rectangulo.obtener_longitud()}
Ancho: {rectangulo.obtener_ancho()}

Perímetro: {rectangulo.calcular_perimetro()}
Área: {rectangulo.calcular_area()}""")
