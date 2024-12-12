class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = float(precio)
        self.cantidad = int(cantidad)
        self.inventario = []

    def __str__(self):
        return f"Nombre: {self.nombre}, Cantidad: {self.cantidad} Precio: {self.precio:.2f}€"

    def modificar_producto(self):
        nombre = input("Ingrese el nombre del producto a modificar: ")
        for producto in self.inventario:
            if producto.nombre == nombre:
                nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                nuevo_cantidad =int(input("Indique la nueva cantidad que haya del producto:"))
                producto.precio = nuevo_precio
                producto.cantidad = nuevo_cantidad
                print("Producto modificado exitosamente.")
                return
        print("Producto no encontrado.")

    def mostrar_inventario(self):
        if not self.inventario: #Esto es por si el inventario esta vacio, es decir comprueba si hay algo.
            print("Tu inventario se encuentra vacio en estos momentos.")
        else:
            print ("Aquí tienes tu inventario") #Esto es para que tengas un texto que te indique donde empieza toda la información del inventario.
            for producto in self.inventario:
                print (producto) #aquí te da la informacion de cada producto.

    def añadir_producto(self):
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese cuanta cantidad del producto se dispone:"))
        for producto in self.inventario:
            if producto.nombre == nombre:
                print("El producto ya existe en el inventario.")
                return
        nuevo_producto = Producto(nombre, precio)
        self.inventario.append(nuevo_producto)
        print("Producto agregado exitosamente.") #donde pongamos Producto.nombre es para que nos coja la caracteristica nombre de la clase objeto, en vez de que nos devuelva un caracter raro.
    
def main():
    gestion_inventario = Producto("Inventario", 0)
    while True:
        print("Menú:")
        print("1. Agregar producto al inventario.")
        print("2. Modificar producto.")
        print("3. Eliminar producto.")
        print("4. Consultar todos los productos.")
        print("5. Salir del programa.")
        opcion = input("Seleccione una opción (1-5): ")
        if opcion == "1":
            gestion_inventario.añadir_producto()
        elif opcion == "2":
            gestion_inventario.modificar_producto()
        elif opcion == "3":
            gestion_inventario.eliminar_producto()
        elif opcion == "4":
            gestion_inventario.mostrar_inventario()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, elija una opción del 1 al 5.")


if __name__ == "__main__":
    main()

