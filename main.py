# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Seijo Nicolás, Maza Victor
# Descripción: Sistema CRUD de Reserva de turnos médicos
# Fecha de creación: 10/08/2025
# ==============================================================================


#-------------------------------------------------------------------------------
# MÓDULOS
#-------------------------------------------------------------------------------

from pacientes import principal_pacientes,inicializar_pacientes_random
from crear_leer_turnos import principal_crear_leer_turnos, logo_turnos
from medicos import menu_medicos, matrizMedicos
from actualizar_eliminar_turnos import principal_actualizar_turnos, principal_eliminar_turnos
import auxiliares
import pacientes

# # ==============================================================================
# # ==============================PROGRAMA PRINCIPAL==============================
# # ==============================================================================

def main():
    #-------------------------------------------------
    # Inicialización de variables que necesitemos
    #-------------------------------------------------
    matriz_pacientes = inicializar_pacientes_random()

    matriz_turnos = []
    # creo turnos random
    principal_crear_leer_turnos(matriz_turnos,matrizMedicos, matriz_pacientes)


    #-------------------------------------------------
    # Bloque de menú
    #-------------------------------------------------
    while True:
        while True:
            auxiliares.grupo6_dev_logo()
            opciones = 4
            """
            print()
            print("---------------------------")
            print("MENÚ PRINCIPAL")
            print("---------------------------")
            print("[1] Gestión de turnos")
            print("[2] Gestión de pacientes")
            print("[3] Gestión de médicos")
            print("---------------------------")
            print("[0] Salir del programa")
            print("---------------------------")
            print() 
            """

            auxiliares.linea_iguales(auxiliares.ANCHO)
            auxiliares.imprimir_un_encabezado('MENU PRINCIPAL', auxiliares.ANCHO)
            print("")

            auxiliares.linea_iguales(auxiliares.ANCHO)
            auxiliares.imprimir_opcion(1, 'GESTION DE TURNOS', '1;33', False)
            auxiliares.imprimir_opcion(2, 'GESTION DE PACIENTES', '1;34')
            auxiliares.imprimir_opcion(3, 'GESTION DE MEDICOS', '1;35')
            auxiliares.imprimir_opcion(0, 'SALIR DEL PROGRAMA', '1;36')
            auxiliares.linea_iguales(auxiliares.ANCHO)
            
            opcion = input("Seleccione una opción: ")
            if opcion in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0": # Opción salir del programa
            exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

        elif opcion == "1":   # Opción 1
            while True:
                logo_turnos()
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > TURNOS")
                    print("---------------------------")
                    print("[1] Crear turnos")
                    print("[2] Consultar turnos")
                    print("[3] Actualizar turnos")
                    print("[4] Eliminar turnos")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcion = input("Seleccione una opción: ")
                    if opcion in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcion == "0": # Opción salir del submenú
                    break # No salimos del programa, volvemos al menú anterior
                elif opcion == "1":   # Opción 1
                    # Esta función debería tener como parámetros las matrice de los médicos y 
                    # pacientes 
                    principal_crear_leer_turnos(matriz_turnos, matrizMedicos, matriz_pacientes, 1)
                    # clientes = altaCliente(clientes)
                    # print("Dando de alta al cliente...")
                    
                elif opcion == "2":   # Opción 2
                    principal_crear_leer_turnos(matriz_turnos, matrizMedicos, matriz_pacientes, 2)
                elif opcion == "3":   # Opción 3
                 hora_turnos = ["08:00","08:30","09:00","09:30","10:00"] 
                 principal_actualizar_turnos(matriz_turnos, hora_turnos)   
                elif opcion == "4":   # Opción 4
                    principal_eliminar_turnos(matriz_turnos)

        elif opcion == "2":   # Opción 2
            auxiliares.limpiar_terminal()
            matriz_pacientes = principal_pacientes(matriz_pacientes)

        elif opcion == "3":   # Opción 3
            menu_medicos()
        elif opcion == "4":   # Opción 4
            ...
        elif opcion == "5":   # Opción 5
            ...

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")


# Punto de entrada al programa
main()
