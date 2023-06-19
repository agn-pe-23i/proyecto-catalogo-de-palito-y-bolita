"""
Programa: mostrar.py
Autores: Erik Muñoz Rodriguez, Abdiel Yared Pimentel Cruz

Este código permite agregar productos de diferentes tipos
(películas, series, documentales y eventos deportivos) a un catálogo.

1. Constantes:

2. Los datos de entrada son:
-la opción del menú

3.Operaciones

4. Los datos de salida son:
- los mensajes impresos en la consola
-categorías de productos
"""
import catalogo

def mostrar_catalogo():
    # Mostrar opciones del menú
    print("Menú mostrar catálogo")
    print("1. Películas")
    print("2. Series")
    print("3. Documentales")
    print("4. Eventos deportivos")
    print("5. Todo")
    print("6. Regresar")

    opcion = input("Seleccione una opción: ")  # Pedir al usuario que seleccione una opción

    if opcion == "1":
        mostrar_peliculas()  # Mostrar películas
    elif opcion == "2":
        mostrar_series()  # Mostrar series
    elif opcion == "3":
        mostrar_documentales()  # Mostrar documentales
    elif opcion == "4":
        mostrar_eventos_deportivos()  # Mostrar eventos deportivos
    elif opcion == "5":
        mostrar_todo()  # Mostrar todo el catálogo
    elif opcion == "6":
        return  # Regresar al menú anterior
    else:
        print("Selección incorrecta. Por favor, seleccione una opción válida.")

def mostrar_peliculas():
    # Filtrar películas del catálogo
    peliculas = [producto for producto in catalogo.catalogo_productos if producto["Tipo"] == "Película"]
    if len(peliculas) > 0:
        # Mostrar películas
        print("Películas:")
        for pelicula in peliculas:
            print_producto(pelicula)
    else:
        print("No hay películas en el catálogo.")

def mostrar_series():
    # Filtrar series del catálogo
    series = [producto for producto in catalogo.catalogo_productos if producto["Tipo"] == "Serie"]
    if len(series) > 0:
        # Mostrar series
        print("Series:")
        for serie in series:
            print_producto(serie)
    else:
        print("No hay series en el catálogo.")

def mostrar_documentales():
    # Filtrar documentales del catálogo
    documentales = [producto for producto in catalogo.catalogo_productos if producto["Tipo"] == "Documental"]
    if len(documentales) > 0:
        # Mostrar documentales
        print("Documentales:")
        for documental in documentales:
            print_producto(documental)
    else:
        print("No hay documentales en el catálogo.")

def mostrar_eventos_deportivos():
    # Filtrar eventos deportivos del catálogo
    eventos = [producto for producto in catalogo.catalogo_productos if producto["Tipo"] == "Evento deportivo en vivo"]
    if len(eventos) > 0:
        # Mostrar eventos deportivos
        print("Eventos deportivos en vivo:")
        for evento in eventos:
            print_producto(evento)
    else:
        print("No hay eventos deportivos en vivo en el catálogo.")

def mostrar_todo():
    if len(catalogo.catalogo_productos) > 0:
        # Mostrar todo el catálogo
        print("Catálogo completo:")
        for producto in catalogo.catalogo_productos:
            print_producto(producto)
    else:
        print("El catálogo está vacío.")

def print_producto(producto):
    # Imprimir información del producto
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
