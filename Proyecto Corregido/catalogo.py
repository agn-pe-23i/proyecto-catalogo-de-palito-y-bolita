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

catalogo_productos = []

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


def obtener_numero(mensaje):
    while True:
        valor = input(mensaje)
        try:
            numero = float(valor)
            return numero
        except ValueError:
            print("Error: Debe ingresar un número válido.")

def mostrar_catalogo():
    print("Menú mostrar catálogo")
    print("1. Películas")
    print("2. Series")
    print("3. Documentales")
    print("4. Eventos deportivos")
    print("5. Todo")
    print("6. Regresar")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        mostrar_peliculas()
    elif opcion == 2:
        mostrar_series()
    elif opcion == 3:
        mostrar_documentales()
    elif opcion == 4:
        mostrar_eventos_deportivos()
    elif opcion == 5:
        mostrar_todo()

def mostrar_peliculas():
    peliculas = [producto for producto in catalogo_productos if producto["Tipo"] == "Película"]
    if len(peliculas) > 0:
        print("Películas:")
        for pelicula in peliculas:
            print_producto(pelicula)
    else:
        print("No hay películas en el catálogo.")

def mostrar_series():
    series = [producto for producto in catalogo_productos if producto["Tipo"] == "Serie"]
    if len(series) > 0:
        print("Series:")
        for serie in series:
            print_producto(serie)
    else:
        print("No hay series en el catálogo.")

def mostrar_documentales():
    documentales = [producto for producto in catalogo_productos if producto["Tipo"] == "Documental"]
    if len(documentales) > 0:
        print("Documentales:")
        for documental in documentales:
            print_producto(documental)
    else:
        print("No hay documentales en el catálogo.")

def mostrar_eventos_deportivos():
    eventos = [producto for producto in catalogo_productos if producto["Tipo"] == "Evento deportivo en vivo"]
    if len(eventos) > 0:
        print("Eventos deportivos en vivo:")
        for evento in eventos:
            print_producto(evento)
    else:
        print("No hay eventos deportivos en vivo en el catálogo.")

def mostrar_todo():
    if len(catalogo_productos) > 0:
        print("Catálogo completo:")
        for producto in catalogo_productos:
            print_producto(producto)
    else:
        print("El catálogo está vacío.")

def print_producto(producto):
    print("--------------")
    print(f"Tipo: {producto['Tipo']}")
    print(f"Título: {producto['Título']}")
    if producto['Tipo'] == 'Película' or producto['Tipo'] == 'Serie':
        print(f"Actor principal: {producto['Actor principal']}")
    if producto['Tipo'] == 'Película' or producto['Tipo'] == 'Serie' or producto['Tipo'] == 'Documental':
        print(f"Director: {producto['Director']}")
    if producto['Tipo'] == 'Serie':
        print(f"Temporadas: {producto['Temporadas']}")
    if producto['Tipo'] == 'Documental':
        print(f"Tema: {producto['Tema']}")
    if producto['Tipo'] == 'Película' or producto['Tipo'] == 'Documental':
        print(f"Año: {producto['Año']}")
    if producto['Tipo'] == 'Evento deportivo en vivo':
        print(f"Deporte: {producto['Deporte']}")
        print(f"Fecha: {producto['Fecha']}")
        print(f"Hora: {producto['Hora']}")
        print(f"Lugar: {producto['Lugar']}")
    if 'Costo de renta' in producto:
        print(f"Costo de renta: {producto['Costo de renta']}")
    if 'Costo de venta' in producto:
        print(f"Costo de venta: {producto['Costo de venta']}")
    print("--------------")
