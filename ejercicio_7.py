class Banco():
    def __init__(self, nombre, interes, dinero):
        self.nombre = nombre
        self.interes = interes
        self.dinero = dinero

    def obtener_nombre(self):
        return self.nombre
    
    def obtener_dinero(self):
        return self.dinero
    
    def obtener_interes(self):
        return self.interes
    
    def agregar_dinero(self, dinero):
        self.dinero = dinero

    def calcular_interes(self):
        total = (self.interes/100) * self.dinero
        total += self.dinero
        return total
    
    def calcular_doble(self):
        doble = self.dinero * 2
        parcial = self.dinero
        años = 1
        while (parcial <= doble and años < 100):
            interes = (self.interes / 100) * parcial
            parcial += interes
            años += 1
        return años

if (__name__ == "__main__"):
    banco = Banco("Supervielle", 20, 0)

    print(f"""
Banco: {banco.obtener_nombre()}
Interés: {banco.obtener_interes()}%
""")

    dinero = int(input("Ingrese la cantidad de dinero que desee: "))
    banco.agregar_dinero(dinero)

    print(f"""
Dinero: {banco.obtener_dinero()}
Dinero con intereses(1 año): {banco.calcular_interes()}
Tiempo para duplicar dinero: {banco.calcular_doble()} años""")
