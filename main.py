from funciones import (
    mostrar_menu, 
    leer_opcion, 
    agregar_libro, 
    buscar_libro, 
    actualizar_disponibilidad, 
    mostrar_libros
)

def main():
    biblioteca = []

    while True:
        mostrar_menu()
        opcion = leer_opcion()
        
        if opcion == 1:
            agregar_libro(biblioteca)
            
        elif opcion == 2:
            print("\n--- BUSCAR LIBRO ---")
            tit = input("Ingrese el título exacto a buscar: ")
            posicion = buscar_libro(biblioteca, tit)
            if posicion != -1:
                print(f"Libro encontrado en el índice {posicion}: {biblioteca[posicion]}")
            else:
                print("El libro no ha sido encontrado.")
                
        elif opcion == 3:
            print("\n--- ELIMINAR LIBRO ---")
            tit = input("Ingrese el título del libro a eliminar: ")
            posicion = buscar_libro(biblioteca, tit)
            if posicion != -1:
                biblioteca.pop(posicion)
                print("Libro eliminado con éxito.")
            else:
                print(f"El libro '{tit}' no se encuentra registrado.")
                
        elif opcion == 4:
            print("\n--- ACTUALIZAR DISPONIBILIDAD ---")
            actualizar_disponibilidad(biblioteca)
            print("Disponibilidad actualizada para toda la colección.")
            
        elif opcion == 5:
            mostrar_libros(biblioteca)
            
        elif opcion == 6:
            print("Gracias por usar el sistema. Vuelva Pronto")
            break
        
        print("\n")

if __name__ == "__main__":
    main()