# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Seijo Nicolás, Maza Victor
# Descripción: Sistema CRUD de Reserva de turnos médicos
# Fecha de creación: 10/08/2025
# ==============================================================================


#-------------------------------------------------------------------------------
# MÓDULOS
#-------------------------------------------------------------------------------

from pacientes import principal_pacientes
from crear_leer_turnos import principal_crear_leer_turnos, logo_turnos
from medicos import principal_medicos
import auxiliares
import pacientes

# # ==============================================================================
# # ==============================PROGRAMA PRINCIPAL==============================
# # ==============================================================================

def main():
    #-------------------------------------------------
    # Inicialización de variables que necesitemos
    #-------------------------------------------------
    matriz_medicos = principal_medicos()
    print(matriz_medicos)
    matriz_pacientes = principal_pacientes()
    matriz_turnos = []
    # creo turnos random
    principal_crear_leer_turnos(matriz_turnos,matriz_medicos, matriz_pacientes)


    #-------------------------------------------------
    # Bloque de menú
    #-------------------------------------------------
    while True:
        while True:
            auxiliares.grupo6_dev_logo()
            opciones = 5
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
                    principal_crear_leer_turnos(matriz_turnos, matriz_medicos, matriz_pacientes, 1)
                    # clientes = altaCliente(clientes)
                    # print("Dando de alta al cliente...")
                    
                elif opcion == "2":   # Opción 2
                    principal_crear_leer_turnos(matriz_turnos, matriz_medicos, matriz_pacientes, 2)
                elif opcion == "3":   # Opción 3
                    ...
                elif opcion == "4":   # Opción 4
                    ...

        elif opcion == "2":   # Opción 2
            opcion_p ="-1"
            while opcion_p != "0":
                valida = False
                while not valida:
                    opciones = 6
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > PACIENTES")
                    print("---------------------------")
                    print("[1] Crear paciente")
                    print("[2] Consultar pacientes")
                    print("[3] Actualizar paciente")
                    print("[4] Eliminar paciente")
                    print("[5] Estadísticas")
                    print("[6] Mostrar usuarios")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()

                    opcion_p = input("Selecciones una opcion: ")
                    valida = opcion_p in [str(i) for i in range(0, opciones + 1)]

                    if not valida:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcion_p == "1":
                    pac_id = pacientes.id_unico(matriz_pacientes)
                    nuevo = pacientes.crear_paciente(pac_id)
                    matriz_pacientes.append(nuevo)
                    print("\nPaciente creado correctamente: ")
                    pacientes.imprimir_paciente([nuevo])

                elif opcion_p == "2":
                    pacientes.leer_pacientes(matriz_pacientes)

                elif opcion_p == "3":
                    pacientes.actualizar_paciente(matriz_pacientes)
                
                elif opcion_p == "4":
                    pacientes.eliminar_paciente(matriz_pacientes)
                
                elif opcion_p == "5":
                    pacientes.mostrar_estadisticas_pacientes(matriz_pacientes)

                elif opcion_p == "6":
                    pacientes.mostrar_usuarios(matriz_pacientes)
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