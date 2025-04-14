class Tienda():
    def __init__(self, nombre, productos):
        self.nombres = nombre
        self.productos = productos

    def obtener_nombre(self):
        return self.nombres
    
    def obtener_productos(self):
        return self.productos
    
    def añadir_productos(self, producto):
        self.productos.append(producto)

    def eliminar_productos(self,producto):
        for p in self.productos:
            if (p == producto):
                self.productos.remove(producto)

if __name__ == "__main__":
    tienda = Tienda("Argenchino",["banana", "manzana", "arrroz", "reloj desechable"])

    print(f"""
Tienda : {tienda.obtener_nombre()}
Productos disponibles: {tienda.obtener_productos()}""")
    
    r = int(input("\nPresione 2 para añadir productos, 1 para eliminarlos o 0 para no hacer nada: "))
    while (r != 0):
        if (r == 2):
            producto = input("Ingrese el nombre del producto que desea añadir: ")
            tienda.añadir_productos(producto)
            print(f"Productos actualizados: {tienda.obtener_productos()}")
        elif(r == 1):
            producto = input("Ingrese el nombre del producto que desea eliminar: ")
            tienda.eliminar_productos(producto)
            print(f"Productos actualizados: {tienda.obtener_productos()}")
        else:
            print("Ingreso invalido")
        r = int(input("\nPresione 2 para añadir productos, 1 para eliminarlos o 0 para terminar: "))
    print("chau")
