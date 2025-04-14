class Circulo:
    def __init__(self, radio, diametro):
        self.diametro = diametro
        self.radio = radio
    
    def obtener_diametro(self):
        return self.diametro
    
    def obtener_radio(self):
        return self.radio
    
    def calcular_area(self):
        area = 3.1416 * self.radio
        return area

    def calcular_circunferencia(self):
        circunferencia = 2 *(3.1416 * self.radio)
        return circunferencia
    
if __name__ == "__main__":
    circulo = Circulo(20, 40)

    print(f"""Circulo
Radio: {circulo.obtener_radio()}
Diametro: {circulo.obtener_diametro()}

Circunferencia: {circulo.calcular_circunferencia()}
Área: {circulo.calcular_area()}""")
