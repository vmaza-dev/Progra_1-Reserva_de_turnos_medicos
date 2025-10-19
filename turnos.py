# ==============================================================================
# Autor: Victor Maza
# Descripción: Modulo de integracion de funcionalidades de turnos
# Fecha de creación: 06/10/2025
# ==============================================================================

#-------------------------------------------------------------------------------
#----------------------------- MODULOS DE PYTHON -------------------------------
#-------------------------------------------------------------------------------

from datetime import datetime

#-------------------------------------------------------------------------------
#---------------------------- MODULOS DEL PROYECTO -----------------------------
#-------------------------------------------------------------------------------

import auxiliares
import crear_leer_turnos
import actualizar_eliminar_turnos

# ==============================================================================
# ===============================FUNCION PRINCIPAL==============================
# ==============================================================================

def principal_crear_leer_turnos(matriz_turnos, matriz_meds, matriz_pacs, opcion = 0):
    """
    Función principal del módulo turnos.

    Args:
        matriz_turnos(list[list])
        opcion(int): Opción elegida. Por defecto = 0 para generar turnos random.
        matriz_pacs[list[list]]: Matriz de pacientes.
        matriz_meds[list[list]]: Matriz de médicos.
    """

    #-------------------------------------------------
    # Bloque de menú
    #-------------------------------------------------
    auxiliares.limpiar_terminal()
    crear_leer_turnos.logo_turnos()
    match opcion:
        case 0:
            crear_leer_turnos.crear_turnos(matriz_turnos,
                                matriz_pacs,
                                matriz_meds, True)
        case 1:

            while True:
                crear_leer_turnos.logo_turnos()
                while True:
                    opciones = 4
                    auxiliares.linea_iguales(auxiliares.ANCHO)
                    auxiliares.imprimir_un_encabezado('MENU TURNOS', auxiliares.ANCHO)
                    print("")

                    auxiliares.linea_iguales(auxiliares.ANCHO)
                    auxiliares.imprimir_opcion(1, 'CREAR TURNOS', '1;33', False)
                    auxiliares.imprimir_opcion(2, 'CONSULTAR TURNOS', '1;34')
                    auxiliares.imprimir_opcion(3, 'ACTUALIZAR TURNOS', '1;35')
                    auxiliares.imprimir_opcion(4, 'ELIMINAR TURNOS', '1;31')
                    auxiliares.imprimir_opcion(0, 'VOLVER AL MENU ANTERIOR', '1;36')
                    auxiliares.linea_iguales(auxiliares.ANCHO)
            
                    
                    opcion = input("Seleccione una opción: ")
                    if opcion in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcion == "0": # Opción salir del submenú
                    break # No salimos del programa, volvemos al menú anterior
                elif opcion == "1":   # Opción 1
                    while True:
                        crear_leer_turnos.logo_turnos()
                        while True:
                            opciones = 4

                            auxiliares.linea_iguales(auxiliares.ANCHO)
                            auxiliares.imprimir_un_encabezado('MENÚ TURNOS > CREAR TURNO', auxiliares.ANCHO)
                            print("")

                            auxiliares.linea_iguales(auxiliares.ANCHO)
                            auxiliares.imprimir_opcion(1, 'CREAR TURNO', '1;33', False)
                            auxiliares.imprimir_opcion(0, 'VOLVER AL MENU ANTERIOR', '1;36')
                            auxiliares.linea_iguales(auxiliares.ANCHO)
                            
                            opcion = input("Seleccione una opción: ")
                            # Sólo continua si se elije una opcion de menú válida
                            if opcion in [str(i) for i in range(0, opciones + 1)]: 
                                break
                            else:
                                input("Opción inválida. Presione ENTER para volver a seleccionar.")
                        print()

                        if opcion == "0": # Opción salir del submenú
                            break # No salimos del programa, volvemos al menú anterior
                        elif opcion == "1":   # Opción 1
                            crear_leer_turnos.crear_turno(matriz_turnos,
                                                          matriz_pacs,
                                                          matriz_meds)
                            input("\nPresione ENTER para volver al menú.")
                    
                elif opcion == "2":   # Opción 2
                    while True:
                        crear_leer_turnos.logo_turnos()
                        while True:
                            opciones = 4
                            auxiliares.linea_iguales(auxiliares.ANCHO)
                            auxiliares.imprimir_un_encabezado('MENÚ TURNOS > CONSULTA', auxiliares.ANCHO)
                            print("")

                            auxiliares.linea_iguales(auxiliares.ANCHO)
                            auxiliares.imprimir_opcion(1, 'CONSULTAR TODOS LOS TURNOS', '1;33', False)
                            auxiliares.imprimir_opcion(2, 'OTRAS CONSULTAS', '1;34', False)
                            auxiliares.imprimir_opcion(0, 'VOLVER AL MENU ANTERIOR', '1;36')
                            auxiliares.linea_iguales(auxiliares.ANCHO)
                            
                            opcion = input("Seleccione una opción: ")
                            # Sólo continua si se elije una opcion de menú válida
                            if opcion in [str(i) for i in range(0, opciones + 1)]: 
                                break
                            else:
                                input("Opción inválida. Presione ENTER para volver a seleccionar.")
                        print()

                        if opcion == "0": # Opción salir del submenú
                            break # No salimos del programa, volvemos al menú anterior
                        elif opcion == "1":   # Opción 1
                            crear_leer_turnos.leer_turnos(matriz_turnos,
                                                          matriz_pacs,
                                                          matriz_meds)
                            input("\nPresione ENTER para volver al menú.")
                            
                        elif opcion == "2":   # Opción 2
                            crear_leer_turnos.consultar_turno(matriz_turnos,
                                                              matriz_pacs,
                                                              matriz_meds)
                            input("\nPresione ENTER para volver al menú.")

                elif opcion == "3":   # Opción 3
                    actualizar_eliminar_turnos.principal_actualizar_turnos(matriz_turnos, auxiliares.crear_horario_atencion(), auxiliares.crear_mes())   
                elif opcion == "4":   # Opción 4
                    actualizar_eliminar_turnos.principal_eliminar_turnos(matriz_turnos)