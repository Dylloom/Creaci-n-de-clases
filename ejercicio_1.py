class persona:
    def __init__(self, nombre, edad, altura,):
        self.nombre = nombre
        self.edad = eda
        self.altura = altura

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre
    
    def obtener_edad(self):
        return self.edad

    def establecer_edad(self, edad):
        self.edad = eda

    def obtener_altura(self):
        return self.altura

    def establecer_altura(self, altura):
        self.altura = altura

if __name__ == "__main__":
    persona1 = persona("Juan", 30, 1.75)

    print(f"Nombre: {persona1.obtener_nombre()}")
    print(f"Edad: {persona1.obtener_eda()}")
    print(f"Altura: {persona1.obtener_altura()} m")

    persona1.establecer_nombre("Carlos")
    persona1.establecer_edad(31)
    persona1.establecer_altura(1.80)

    print("\nDespués de actualizar:")
    print(f"Nombre: {persona1.obtener_nombre()}")
    print(f"Edad: {persona1.obtener_edad()}")
    print(f"Altura: {persona1.obtener_altura()} m")
