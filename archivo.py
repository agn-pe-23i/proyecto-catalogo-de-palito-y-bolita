"""
Programa:archivo.py
Autores: Erik Muñoz Rodriguez, Abdiel Yared Pimentel Cruz

Este código permiten cargar un catálogo de productos desde
un archivo y guardar el catálogo actualizado en otro archivo

1. Constantes:

2. Los datos de entrada son:
-el nombre del archivo

3. Operaciones:

4. Los datos de salida son:
- los mensajes impresos en la consola
"""
import catalogo

def cargar_catalogo():
    # Solicita al usuario el nombre del archivo donde está almacenado el catálogo
    nombre_archivo = input("Ingrese el nombre del archivo donde está almacenado el catálogo, al final agrega (.txt): ")
    try:
        # Intenta abrir el archivo en modo lectura
        with open(nombre_archivo, "r") as archivo:
            # Lee el contenido del archivo y evalúa su contenido como un diccionario
            catalogo.catalogo_productos = eval(archivo.read())
        print("El catálogo se ha cargado correctamente.")
    except FileNotFoundError:
        # Maneja la excepción si el archivo no existe
        print("El archivo no existe.")
    except:
        # Maneja cualquier otra excepción que ocurra al cargar el catálogo
        print("Ocurrió un error al cargar el catálogo.")

def guardar_catalogo():
    # Solicita al usuario el nombre del archivo donde se guardará el catálogo
    nombre_archivo = input("Ingrese el nombre del archivo donde se guardará el catálogo, al final agrega (.txt): ")
    try:
        # Intenta abrir el archivo en modo escritura
        with open(nombre_archivo, "w") as archivo:
            # Escribe el catálogo en el archivo como una representación en cadena
            archivo.write(str(catalogo.catalogo_productos))
        print("El catálogo se ha guardado correctamente.")
    except:
        # Maneja cualquier excepción que ocurra al guardar el catálogo
        print("Ocurrió un error al guardar el catálogo.")
