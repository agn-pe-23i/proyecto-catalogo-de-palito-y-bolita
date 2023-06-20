"""
Programa: eliminacion.py
Autores: Erik Muñoz Rodriguez, Abdiel Yared Pimentel Cruz

Este código tiene la función eliminar_producto(),
que permite al usuario eliminar un producto del catálogo

1. Constantes:

2. Los datos de entrada son:
-Catálogo de productos
-El número correspondiente

3.Operaciones

4. Los datos de salida son:
- los mensajes impresos en la consola
"""
import catalogo

def eliminar_producto():
    # Mostrar los títulos de los productos disponibles
    print("Títulos disponibles:")
    for i, producto in enumerate(catalogo.catalogo_productos, start=1):
        print(f"{i}. {producto['Título']}")

    # Pedir al usuario que seleccione el título del producto a eliminar
    opcion = input("Seleccione el número del título del producto que desea eliminar: ")
    opcion = int(opcion)

    # Validar la opción seleccionada
    if opcion < 1 or opcion > len(catalogo.catalogo_productos):
        print("Selección incorrecta. Por favor, seleccione un número válido.")
        return

    # Obtener el producto correspondiente a la opción seleccionada
    producto = catalogo.catalogo_productos[opcion - 1]

    # Eliminar el producto del catálogo
    catalogo.catalogo_productos.remove(producto)
    print("El producto ha sido eliminado del catálogo.")

