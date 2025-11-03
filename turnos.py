# ==============================================================================
# Autor: Victor Maza
# Descripción: Modulo de integracion de funcionalidades de turnos
# Fecha de creación: 06/10/2025
# ==============================================================================

#-------------------------------------------------------------------------------
#----------------------------- MODULOS DE PYTHON -------------------------------
#-------------------------------------------------------------------------------

from datetime import date
import json, sys

#-------------------------------------------------------------------------------
#---------------------------- MODULOS DEL PROYECTO -----------------------------
#-------------------------------------------------------------------------------

import auxiliares
import crear_leer_turnos
import actualizar_eliminar_turnos

#-------------------------------------------------------------------------------
# FUNCIONES LECTURA/ESCRITURA DE ARCHIVOS --------------------------------------
#-------------------------------------------------------------------------------

def crear_leer_matriz_turno():
    """
    Crea la base de datos de turnos, una lista.

    En primer lugar verifica si el archivo existe, sino existe crea el 
    archivo vacio.

    """
    try: 
        with open('datos/archivo_turnos.json', 'r', encoding='UTF-8') as turnos:
            lista_turnos = json.load(turnos)
        # paso las fechas que son string a tipo date para poder trabajar en
        # el modulo
        for turno in lista_turnos:
            turno['fecha'] = date.fromisoformat(turno['fecha'])

        return lista_turnos
    except FileNotFoundError:
        try:
            lista_turnos_vacia = []
            with open('datos/archivo_turnos.json', 'w', encoding='UTF-8') as turnos:
                json.dump(lista_turnos_vacia, turnos, ensure_ascii=False, indent=4)
            
            return lista_turnos_vacia
        except FileNotFoundError:
            print('No se pudo crear el archivo principal de turnos')
            input('Presione un tecla para continuar: ')
            sys.exit(1)   # termina la ejecución del programa
        except OSError:
            print('No se pudo crear el archivo principal de turnos')
            input('Presione un tecla para continuar: ')
            sys.exit(1)   # termina la ejecución del programa
    except OSError:
        print('No se pudo inicializar el programa')
        input('Presione un tecla para continuar: ')
        sys.exit(1)   # termina la ejecución del programa


def escribir_turnos(matriz_turnos):
    """
    Actualiza la base de datos de turnos generados.
    
    Args:
        matriz_turnos(list[dic]): Lista de diccionarios actualizada.
    """
    try:
        with open('datos/archivo_turnos.json', 'w', encoding='UTF-8') as turnos:
                json.dump(matriz_turnos, turnos, ensure_ascii=False, indent=4, default=str)
                # el default=str es para que pueda serializar el objeto tipo date
                # que es la fecha, se va a guardar como string
                # al deserilizar es necesario pasar a tipo date.
    except FileNotFoundError:
            print('No se pudo actualizar archivo principal de turnos')
            input('Presione un tecla para continuar: ')
    except OSError:
            print('No se pudo actualizar el archivo principal de turnos')
            input('Presione un tecla para continuar: ')

# ==============================================================================
# ===============================FUNCION PRINCIPAL==============================
# ==============================================================================

def principal_crear_leer_turnos(matriz_meds, matriz_pacs, opcion = 0):
    """
    Función principal del módulo turnos.

    Args:
        matriz_turnos(list[dic])
        opcion(int): Opción elegida. Por defecto = 0 para generar turnos random.
        matriz_pacs[list[dic]]: Matriz de pacientes.
        matriz_meds[list[dic]]: Matriz de médicos.
    """

    #-------------------------------------------------
    # Bloque de menú
    #-------------------------------------------------
    auxiliares.limpiar_terminal()
    crear_leer_turnos.logo_turnos()
    match opcion:
        case 0:
            # creo o cargo el archivo de turnos
            matriz_turnos = crear_leer_matriz_turno()
            if len(matriz_turnos) == 0:# este bloque es para que no sume mas turnos, solo me quedo con 10
                crear_leer_turnos.crear_turnos(matriz_turnos,
                                    matriz_pacs,
                                    matriz_meds, True)
        case 1:

            while True:
                # actualizo el archivo de turnos luego de hacer las operaciones con 
                # las funciones del modulo
                matriz_turnos = crear_leer_matriz_turno()
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
                            crear_leer_turnos.crear_turnos(matriz_turnos,
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
                            crear_leer_turnos.leer_turnos(matriz_turnos,matriz_pacs,
                                                          matriz_meds)
                            input("\nPresione ENTER para volver al menú.")
                            
                        elif opcion == "2":   # Opción 2
                            crear_leer_turnos.consultar_turno(matriz_turnos,matriz_pacs,
                                                              matriz_meds)
                            input("\nPresione ENTER para volver al menú.")

                elif opcion == "3":   # Opción 3
                    actualizar_eliminar_turnos.principal_actualizar_turnos(matriz_turnos, auxiliares.crear_horario_atencion(), auxiliares.crear_mes())  
                elif opcion == "4":   # Opción 4
                    actualizar_eliminar_turnos.principal_eliminar_turnos(matriz_turnos)