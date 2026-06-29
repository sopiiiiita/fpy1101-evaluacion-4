def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-6): "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Error: Ingrese un número entre 1 y 6.")
        except ValueError:
            print("Error: Por favor, ingrese un número entero.")

def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_copias(copias_str):
    try:
        copias = int(copias_str)
        return copias >= 0
    except ValueError:
        return False

def validar_prestamo(prestamo_str):
    try:
        prestamo = int(prestamo_str)
        return prestamo > 0
    except ValueError:
        return False

def agregar_libro(lista):
    print("\n--- AGREGAR LIBRO ---")
    titulo = input("Ingrese el título del libro: ")
    copias_str = input("Ingrese la cantidad de copias: ")
    prestamo_str = input("Ingrese el período de préstamo (días): ")
    
    if not validar_titulo(titulo):
        print("Error: El título no puede estar vacío ni tener solo espacios en blanco.")
        return
    if not validar_copias(copias_str):
        print("Error: Las copias deben ser un número entero mayor o igual a cero.")
        return
    if not validar_prestamo(prestamo_str):
        print("Error: El préstamo debe ser un número entero mayor que cero.")
        return
    
    nuevo_libro = {
        "titulo": titulo,
        "copias": int(copias_str),
        "prestamo": int(prestamo_str),
        "disponible": False 
    }
    lista.append(nuevo_libro)
    print("¡Libro agregado exitosamente!")

def buscar_libro(lista, titulo_buscar):
    for index, libro in enumerate(lista):
        if libro["titulo"] == titulo_buscar:
            return index
    return -1

def actualizar_disponibilidad(lista):
    for libro in lista:
        if libro["copias"] >= 1:
            libro["disponible"] = True
        else:
            libro["disponible"] = False

def mostrar_libros(lista):
    actualizar_disponibilidad(lista)
    print("\n=== LISTA DE LIBROS ===")
    for libro in lista:
        print(f"Título: {libro['titulo']}")
        print(f"Copias: {libro['copias']}")
        print(f"Préstamo: {libro['prestamo']}")
        
        estado = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"
        print(f"Estado: {estado}")
        print("********************************************")