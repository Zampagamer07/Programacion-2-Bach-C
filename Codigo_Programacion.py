class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def modificar_producto():
    nombre = input("Ingrese el nombre del producto a modificar: ").capitalize()
    for producto in productos:
        if producto.nombre == nombre:
            cantidad = int(input("Ingrese la nueva cantidad: "))
            precio = float(input("Ingrese el nuevo precio: "))
            producto.cantidad = cantidad
            producto.precio = precio
            print("Producto modificado exitosamente.")
            return
    print("El producto no se encuentra en el inventario.")