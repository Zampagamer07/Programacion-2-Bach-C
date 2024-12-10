class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.inventario = []

    def modificar_producto(self, ):
    nombre = input("Ingrese el nombre del producto a modificar: ").capitalize()
    for producto in productos:
        if producto.nombre == nombre:
            precio = float(input("Ingrese el nuevo precio: "))
            Producto.precio= precio
            print("Producto modificado exitosamente.")
            return
    print("El producto no se encuentra en el inventario.")
    
    def mostrar_inventario(self):
        if not self.inventario: #Esto es por si el inventario esta vacio, es decir comprueba si hay algo.
            print("Tu inventario se encuentra vacio en estos momentos.")
        else:
            print ("Aquí tienes tu inventario") #Esto es para que tengas un texto que te indique donde empieza toda la información del inventario.
            for objeto in self.inventario:
                print (f"{Producto.nombre}, {Producto.cantidad}. Precio: {Producto.precio}") #aquí te da la informacion de cada objeto.

    def añadir_producto(self, producto):
        if  producto not in self.inventario: #Esto comprueba que el objeto no este en tu inventario, para que no haya duplicados.
            self.inventario.append(producto) #esta linea de codigo añade el objeto adquirido al inventario.
            print (f"Se ha añadido un/una {Producto.nombre}.")
        else:
            print(f"El producto {Producto.nombre} ya esta en stock.") #donde pongamos objeto.nombre es para que nos coja la caracteristica nombre de la clase objeto, en vez de que nos devuelva un caracter raro.
    