"""
Programa:agregar.py
Autores: Erik Muñoz Rodriguez, Abdiel Yared Pimentel Cruz

Este código implementa una función menu_agregar() que muestra
un menú de opciones para agregar productos al catálogo

1. Constantes:

2. Los datos de entrada son:
- las opciones del menú

3.Operaciones

4. Los datos de salida son:
- los mensajes impresos en la consola
"""
import catalogo


def menu_agregar():
    # Mostrar opciones del menú
    print("Menú agregar producto")
    print("1. Película")
    print("2. Serie")
    print("3. Documental")
    print("4. Evento deportivo en vivo")
    print("5. Regresar")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_pelicula()  # Agregar película
    elif opcion == "2":
        agregar_serie()  # Agregar serie
    elif opcion == "3":
        agregar_documental()  # Agregar documental
    elif opcion == "4":
        agregar_evento_deportivo()  # Agregar evento deportivo
    elif opcion == "5":
        return  # Regresar al menú anterior
    else:
        print("Selección incorrecta. Por favor, seleccione una opción válida.")


def agregar_pelicula():
    # Pedir información de la película al usuario
    titulo = input("Ingrese el título de la película: ")
    actor_principal = input("Ingrese el actor principal de la película: ")
    director = input("Ingrese el director de la película: ")
    anio = input("Ingrese el año de la película: ")
    costo_renta = obtener_numero("Ingrese el costo de renta: ")
    costo_venta = obtener_numero("Ingrese el costo de venta: ")

    # Agregar la película al catálogo
    catalogo.catalogo_productos.append(
        {"Tipo": "Película", "Título": titulo, "Actor principal": actor_principal, "Director": director, "Año": anio,
         "Costo de renta": costo_renta, "Costo de venta": costo_venta})
    print("La película se ha agregado al catálogo.")


def agregar_serie():
    # Pedir información de la serie al usuario
    titulo = input("Ingrese el título de la serie: ")
    actor_principal = input("Ingrese el actor principal de la serie: ")
    director = input("Ingrese el director de la serie: ")
    temporadas = input("Ingrese el número de temporadas de la serie: ")
    costo_renta = obtener_numero("Ingrese el costo de renta: ")
    costo_venta = obtener_numero("Ingrese el costo de venta: ")

    # Agregar la serie al catálogo
    catalogo.catalogo_productos.append(
        {"Tipo": "Serie", "Título": titulo, "Actor principal": actor_principal, "Director": director,
         "Temporadas": temporadas, "Costo de renta": costo_renta, "Costo de venta": costo_venta})
    print("La serie se ha agregado al catálogo.")


def agregar_documental():
    # Pedir información del documental al usuario
    titulo = input("Ingrese el título del documental: ")
    director = input("Ingrese el director del documental: ")
    tema = input("Ingrese el tema del documental: ")
    anio = input("Ingrese el año del documental: ")
    costo_renta = obtener_numero("Ingrese el costo de renta: ")
    costo_venta = obtener_numero("Ingrese el costo de venta: ")

    # Agregar el documental al catálogo
    catalogo.catalogo_productos.append(
        {"Tipo": "Documental", "Título": titulo, "Director": director, "Tema": tema, "Año": anio,
         "Costo de renta": costo_renta, "Costo de venta": costo_venta})
    print("El documental se ha agregado al catálogo.")


def agregar_evento_deportivo():
    # Pedir información del evento deportivo al usuario
    titulo = input("Ingrese el título del evento deportivo en vivo: ")
    deporte = input("Ingrese el deporte del evento: ")
    fecha = input("Ingrese la fecha del evento: ")
    hora = input("Ingrese la hora del evento: ")
    lugar = input("Ingrese el lugar del evento: ")
    costo_venta = obtener_numero("Ingrese el costo de venta: ")

    # Agregar el evento deportivo al catálogo
    catalogo.catalogo_productos.append(
        {"Tipo": "Evento deportivo en vivo", "Título": titulo, "Deporte": deporte, "Fecha": fecha, "Hora": hora,
         "Lugar": lugar, "Costo de venta": costo_venta})
    print("El evento deportivo en vivo se ha agregado al catálogo.")


def obtener_numero(mensaje):
    while True:
        valor = input(mensaje)
        try:
            numero = float(valor)
            return numero
        except ValueError:
            print("Error: Debe ingresar un número válido.")

