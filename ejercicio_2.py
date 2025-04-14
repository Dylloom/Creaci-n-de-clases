class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def obtener_marca(self):
        return self.marca

    def obtener_modelo(self):
        return self.modelo

    def obtener_año(self):
        año = self.año
        año = 2025 - año 
        return año
    
if __name__ == "__main__":
    coche = Coche("fiesta", "Ford", 2000)
    print (f"""
    modelo: {coche.obtener_modelo()}
    marca: {coche.obtener_marca()}
    años: {coche.obtener_año()}""")
