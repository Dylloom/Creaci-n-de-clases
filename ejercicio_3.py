class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def obtener_stock(self):
        return self.stock

    def obtener_precio(self):
        return self.precio

    def obtener_nombre(self):
        return self.nombre
    
    def aumentar_stock(self, aumento):
        self.stock += aumento
        
    def disminuir_stock(self, disminucion):
        self.stock -= disminucion

if __name__ == "__main__":
    producto1 = Producto("banana", 500, 1500)

print(f"""
Producto: {producto1.obtener_nombre()}
Precio: ${producto1.obtener_precio()}
Stock: {producto1.obtener_stock()}""")

n = int(input("¿desea aumentar stock (1) o disminuir stock (2)?: "))
cantidad = int(input("¿Cuanto?: "))

if (n == 1):
    producto1.aumentar_stock(cantidad)
elif (n == 2):
    producto1.disminuir_stock(cantidad)

print(f"Nuevo stock: {producto1.obtener_stock()}")
