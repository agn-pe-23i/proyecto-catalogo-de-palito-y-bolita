"""
Programa: Buscar_y_eliminar.py
Autores: Erik Muñoz Rodriguez, Abdiel Yared Pimentel Cruz

Este código implementa una función buscar_producto() que
 permite buscar productos en el catálogo mediante una palabra clave.

1. Constantes:

2. Los datos de entrada son:
-Palabra clave ingresada

3.Operaciones

4. Los datos de salida son:
- los mensajes impresos en la consola
-el número de resultados encontrados
-la información de cada producto coincidente
"""
import catalogo

def buscar_producto():
    clave = input("Ingrese una palabra clave del título del producto a buscar: ")
    resultados = []

    # Iterar a través de cada producto en el catálogo
    for producto in catalogo.catalogo_productos:
        # Verificar si la clave ingresada está presente en el título del producto (ignorando mayúsculas y minúsculas)
        if clave.lower() in producto["Título"].lower():
            resultados.append(producto)

    # Si se encontraron resultados los muestra
    if len(resultados) > 0:
        print(f"Se encontraron {len(resultados)} resultado(s) que coinciden con la búsqueda:")
        for producto in resultados:
            print(f"Tipo: {producto['Tipo']}")
            print(f"Título: {producto['Título']}")
            print("-----------------------")  # Línea separadora
    else:
        # Si no se encontraron resultados, muestra un mensaje indicando que no se encontraron coincidencias
        print("No se encontraron productos que coincidan con la búsqueda.")

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