# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Nicolás Seijo, Victor Maza
# Descripción: Módulo Turnos
# Fecha de creación: 10/08/2025
# ==============================================================================

import auxiliares
import crear_leer_turnos

def elim_turno(m_turnos):
    try:
        id_turno = str(auxiliares.ingresar_entero_positivo("Ingresar ID del turno: ")).zfill(6)
        for turno in m_turnos:
            if turno[0] == id_turno:
                turno[7] = "Cancelado"
                print(f"Turno de ID: [{id_turno}] cancelado exitosamente")
                input("Presione Enter para volver al menú anterior...")
                return True
        print("Turno no encontrado.")
        input("Presione Enter para volver al menú anterior...")
        return False
    except ValueError:
        print("Error: El ID ingresado no es válido.")
    except IndexError:
        print("Error interno: Estructura del turno inválida.")
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    return False


def edit_turnos(m_turnos, hora_turnos, mes, anio):
    try:
        id_turno = str(auxiliares.ingresar_entero_positivo("Ingresar ID del turno: ")).zfill(6)
        encontrado = False

        for turno in m_turnos:
            if turno[0] == id_turno:
                encontrado = True
                print("1 - Cambiar fecha")
                print("2 - Cambiar hora")
                opcion = auxiliares.ingresar_entero_positivo("Opción: ")

                if opcion == 1:
                    fecha_turno, dia = crear_leer_turnos.elegir_fecha(mes, anio)
                    turno[1] = fecha_turno
                    print("Fecha modificada exitosamente a:", turno[1])

                elif opcion == 2:
                    auxiliares.imprimir_lista(hora_turnos, True)
                    seleccion = auxiliares.ingresar_entero_positivo("Nuevo horario: ")

                    while seleccion < 1 or seleccion > len(hora_turnos):
                        print("Horario ocupado o inválido, intente nuevamente...")
                        seleccion = auxiliares.ingresar_entero_positivo("Nuevo horario: ")

                    turno[2] = hora_turnos[seleccion - 1]
                    print("Horario modificado exitosamente a:", turno[2])

                else:
                    print("Opción inválida.")
                input("Presione Enter para volver al menú anterior...")

        if not encontrado:
            print("Turno no encontrado.")
            input("Presione Enter para volver al menú anterior...")
            return False
        return True

    except ValueError:
        print("Error: Entrada no válida.")
    except IndexError:
        print("Error: Acceso a un índice inexistente en la lista de turnos.")
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    return False


def principal_actualizar_turnos(matriz_turnos, hora_turnos, info_mes):
    try:
        if not matriz_turnos:
            print("No hay turnos cargados")
            return 0
        return edit_turnos(matriz_turnos, hora_turnos, info_mes('mes'), info_mes('anio'))
    except Exception as e:
        print(f"Error al actualizar turnos: {e}")
        return 0


def principal_eliminar_turnos(matriz_turnos):
    try:
        if not matriz_turnos:
            print("No hay turnos cargados")
            return 0
        return elim_turno(matriz_turnos)
    except Exception as e:
        print(f"Error al eliminar turnos: {e}")
        return 0
