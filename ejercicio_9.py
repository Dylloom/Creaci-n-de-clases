class Empleado():
    def __init__(self, nombre, edad, salario, cargo):
        self. nombre = nombre
        self.edad = edad
        self.salario = salario
        self.cargo = cargo

    def obtener_nombre(self):
        return self.nombre 
    
    def obtener_edad(self):
        return self.edad 
    
    def obtener_salario(self):
        return self.salario 
    
    def obtener_cargo(self):
        return self.cargo 
    
    def agregar_nombre(self, nombre):
        self.nombre = nombre
    
    def agregar_edad(self, edad):
        self.edad = edad
    
    def agregar_salario(self, salario):
        self.salario = salario
    
    def agregar_cargo(self, cargo):
        self.cargo = cargo

    def salario_anual(self):
        anual = (self.salario * 12)
        return anual
    
if __name__ == "__main__":
    empleado = Empleado("Mohammed", 75, 75000000, "Cajero")

    print(f"""
Empleado: {empleado.obtener_nombre()}
Edad: {empleado.obtener_edad()} años
Salario: ${empleado.obtener_salario():,}
Cargo: {empleado.obtener_cargo()}
Salario anual: ${empleado.salario_anual():,}""")
