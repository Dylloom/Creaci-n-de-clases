class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.notas = []

    def obtener_nombre(self):
        return self.nombre

    def obtener_edad(self):
        return self.edad

    def obtener_carrera(self):
        return self.carrera
    
    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def establecer_edad(self, edad):
        self.edad = edad

    def establecer_carrera(self, carrera):
        self.carrera = carrera

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def calcular_promedio(self):
        suma = 0
        if (len(self.notas) != 0):
            for nota in self.notas:
                suma += nota
            promedio = int(suma/len(self.notas))
            return promedio
        else:
            return 0
        
if __name__ == "__main__":
    estudiante = Estudiante("Gabriel", 17, "carnicero")
    print(f"""
Estudiante: {estudiante.obtener_nombre()}
Edad: {estudiante.obtener_edad()}
Carrera: {estudiante.obtener_carrera()}
Promedio: {estudiante.calcular_promedio()}""")
    
estudiante.agregar_nota(9.5)
estudiante.agregar_nota(10)
estudiante.agregar_nota(8.5)

print("Luego de 3 examenes: ")
print(f"Promedio: {estudiante.calcular_promedio()}")
