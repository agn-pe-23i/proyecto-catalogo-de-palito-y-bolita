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
import os
import catalogo

def cargar_catalogo():
    # Solicita al usuario el nombre del archivo donde está almacenado el catálogo
    nombre_archivo = input("Ingrese el nombre del archivo donde está almacenado el catálogo, al final agrega (.txt): ")

    if os.path.exists(nombre_archivo):
        # Abre el archivo en modo lectura
        archivo = open(nombre_archivo, "r")
        # Lee el contenido del archivo y evalúa su contenido como un diccionario
        catalogo.catalogo_productos = eval(archivo.read())
        archivo.close()
        print("El catálogo se ha cargado correctamente.")
    else:
        print("El archivo no existe.")

def guardar_catalogo():
    # Solicita al usuario el nombre del archivo donde se guardará el catálogo
    nombre_archivo = input("Ingrese el nombre del archivo donde se guardará el catálogo, al final agrega (.txt): ")

    # Abre el archivo en modo escritura
    archivo = open(nombre_archivo, "w")
    # Escribe el catálogo en el archivo como una representación en cadena
    archivo.write(str(catalogo.catalogo_productos))
    archivo.close()
    print("El catálogo se ha guardado correctamente.")

