"""
Programa: Main.py
Autores: Erik Muñoz Rodriguez, Abdiel Yared Pimentel Cruz

Este código implementa un menú interactivo que permite al usuario agregar, buscar, eliminar,
mostrar y gestionar un catálogo de productos. Los detalles de las funciones específicas
se encuentran en los módulos importados: agregar, busqueda, eliminacion, mostrar y archivo.

1. Constantes:

2. Los datos de entrada son:
-Módulos importados
-La opción seleccionada
3. Operaciones:

4. Los datos de salida son:
- Menú principal
- Selección incorrecta
"""
import agregar
import busqueda
import eliminacion
import mostrar
import archivo

def menu_principal():
    print("Menú principal")
    print("1. Agregar un producto")
    print("2. Buscar producto")
    print("3. Eliminar un producto")
    print("4. Mostrar el catálogo")
    print("5. Cargar catálogo")
    print("6. Guardar catálogo")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")
    return opcion

def ejecutar_opcion(opcion):
    if opcion == "1":
        agregar.menu_agregar()  # Llama a la función 'menu_agregar' del módulo 'agregar'
    elif opcion == "2":
        busqueda.buscar_producto()  # Llama a la función 'buscar_producto' del módulo 'busqueda'
    elif opcion == "3":
        eliminacion.eliminar_producto()  # Llama a la función 'eliminar_producto' del módulo 'eliminacion'
    elif opcion == "4":
        mostrar.mostrar_catalogo()  # Llama a la función 'mostrar_catalogo' del módulo 'mostrar'
    elif opcion == "5":
        archivo.cargar_catalogo()  # Llama a la función 'cargar_catalogo' del módulo 'archivo'
    elif opcion == "6":
        archivo.guardar_catalogo()  # Llama a la función 'guardar_catalogo' del módulo 'archivo'
    elif opcion == "7":
        print("Hasta luego")
    else:
        print("Selección incorrecta. Por favor, seleccione una opción válida.")

def main():
    while True:
        opcion = menu_principal()
        if opcion == "7":
            break
        ejecutar_opcion(opcion)

if __name__ == "__main__":
    main()
