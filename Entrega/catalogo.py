"""
Programa: catalogo.py
Autores: Erik Muñoz Rodriguez, Abdiel Yared Pimentel Cruz

Este código permite agregar productos de diferentes tipos
(películas, series, documentales y eventos deportivos) a un catálogo.

1. Constantes:

2. Los datos de entrada son:
-tipo de producto,
-el título,
-el actor principal/director
-el año
-el costo de renta/venta
-las temporadas
-el tema
-el deporte
-la fecha, la hora y el lugar
4. Los datos de salida son:
- los mensajes impresos en la consola
"""
catalogo_productos = []  # Lista para almacenar los productos en el catálogo

def agregar_producto():
    print("Menú agregar producto")
    print("1. Película")
    print("2. Serie")
    print("3. Documental")
    print("4. Evento deportivo en vivo")
    print("5. Regresar")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        agregar_pelicula()
    elif opcion == 2:
        agregar_serie()
    elif opcion == 3:
        agregar_documental()
    elif opcion == 4:
        agregar_evento_deportivo()

def agregar_pelicula():
    # Solicita información sobre una película y la agrega al catálogo
    titulo = input("Ingrese el título de la película: ")
    actor_principal = input("Ingrese el actor o actriz principal: ")
    director = input("Ingrese el director o directora: ")
    anio = input("Ingrese el año de la película: ")
    costo_renta = float(input("Ingrese el costo de renta: "))
    costo_venta = float(input("Ingrese el costo de venta: "))
    # Crea un diccionario con la información de la película y lo agrega al catálogo
    catalogo_productos.append({"Tipo": "Película", "Título": titulo, "Actor principal": actor_principal, "Director": director, "Año": anio, "Costo de renta": costo_renta, "Costo de venta": costo_venta})
    print("La película se ha agregado al catálogo.")

def agregar_serie():
    # Solicita información sobre una serie y la agrega al catálogo
    titulo = input("Ingrese el título de la serie: ")
    actor_principal = input("Ingrese el actor o actriz principal: ")
    director = input("Ingrese el director o directora: ")
    temporadas = input("Ingrese la cantidad de temporadas: ")
    costo_renta = float(input("Ingrese el costo de renta: "))
    costo_venta = float(input("Ingrese el costo de venta: "))
    # Crea un diccionario con la información de la serie y lo agrega al catálogo
    catalogo_productos.append({"Tipo": "Serie", "Título": titulo, "Actor principal": actor_principal, "Director": director, "Temporadas": temporadas, "Costo de renta": costo_renta, "Costo de venta": costo_venta})
    print("La serie se ha agregado al catálogo.")

def agregar_documental():
    # Solicita información sobre un documental y la agrega al catálogo
    titulo = input("Ingrese el título del documental: ")
    director = input("Ingrese el director o directora: ")
    tema = input("Ingrese el tema del documental: ")
    anio = input("Ingrese el año del documental: ")
    costo_renta = float(input("Ingrese el costo de renta: "))
    costo_venta = float(input("Ingrese el costo de venta: "))
    # Crea un diccionario con la información sobre el documental y lo agrega al catálogo
    catalogo_productos.append({"Tipo": "Documental", "Título": titulo, "Director": director, "Tema": tema, "Año": anio, "Costo de renta": costo_renta, "Costo de venta": costo_venta})
    print("El documental se ha agregado al catálogo.")

def agregar_evento_deportivo():
    # Solicita información sobre un evento deportivo y la agrega al catálogo
    titulo = input("Ingrese el título del evento deportivo: ")
    deporte = input("Ingrese el deporte del evento: ")
    fecha = input("Ingrese la fecha del evento: ")
    hora = input("Ingrese la hora del evento: ")
    lugar = input("Ingrese el lugar del evento: ")
    costo_venta = float(input("Ingrese el costo de venta: "))
    # Crea un diccionario con la información sobre el evento deportivo y lo agrega al catálogo
    catalogo_productos.append({"Tipo": "Evento deportivo en vivo", "Título": titulo, "Deporte": deporte, "Fecha": fecha, "Hora": hora, "Lugar": lugar, "Costo de venta": costo_venta})
    print("El evento deportivo se ha agregado al catálogo.")