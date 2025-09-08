# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Seijo Nicolás, Maza Victor
# Descripción: Sistema CRUD de Reserva de turnos médicos
# Fecha de creación: 10/08/2025
# ==============================================================================


#-------------------------------------------------------------------------------
# MÓDULOS
#-------------------------------------------------------------------------------

# import pacientes
from turnos import main_crear_leer, logo_turnos
# import medicos
import fun_aux


# # ==============================================================================
# # ==============================PROGRAMA PRINCIPAL==============================
# # ==============================================================================

def main():
    #-------------------------------------------------
    # Inicialización de variables que necesitemos
    #-------------------------------------------------
    # matriz_medicos = medicos.crear_medicos_random()
    # matriz_pacientes = crear_pacientes_random()
    matriz_turnos = []
    # creo turnos random
    main_crear_leer(matriz_turnos)


    #-------------------------------------------------
    # Bloque de menú
    #-------------------------------------------------
    while True:
        while True:
            fun_aux.grupo6_dev_logo()
            opciones = 5
            print()
            print("---------------------------")
            print("MENÚ PRINCIPAL")
            print("---------------------------")
            print("[1] Gestión de turnos")
            print("[2] Gestión de pacientes")
            print("[3] Gestión de médicos")
            print("[4] Opción 100 a que lo elije a Lampone")
            print("[5] Opción no son tan incómodos esto tacos")
            print("---------------------------")
            print("[0] Salir del programa")
            print("---------------------------")
            print() 
            
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
                    print("[4] Elimiar turnos")
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
                    main_crear_leer(matriz_turnos, 1)
                    # clientes = altaCliente(clientes)
                    # print("Dando de alta al cliente...")
                    
                elif opcion == "2":   # Opción 2
                    main_crear_leer(matriz_turnos, 2)
                elif opcion == "3":   # Opción 3
                    ...
                elif opcion == "4":   # Opción 4
                    ...

        elif opcion == "2":   # Opción 2
            ...
        elif opcion == "3":   # Opción 3
            ...
        elif opcion == "4":   # Opción 4
            ...
        elif opcion == "5":   # Opción 5
            ...

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")


# Punto de entrada al programa
main()










