# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Nicolás Seijo, Victor Maza
# Descripción: Módulo Turnos
# Fecha de creación: 10/08/2025
# ==============================================================================

import auxiliares
import crear_leer_turnos

def imprimir_menu_horarios_disponibles(horarios_lista, hora_actual):
    """
    Imprime un menú vertical de horarios, marcando disponibles,
    ocupados y el turno actual con colores para mayor claridad.
    """
    print("Seleccione un nuevo horario:")
    auxiliares.linea_guiones(auxiliares.ANCHO)
    for i, hora in enumerate(horarios_lista):
        op_num = i + 1
        if hora == hora_actual:
            auxiliares.imprimir_opcion(op_num, f"{hora} (TURNO ACTUAL)", '1;34', False) 
        elif hora == "No disponible":
            auxiliares.imprimir_opcion(op_num, hora, '1;31', False) 
        else:
            auxiliares.imprimir_opcion(op_num, hora, '1;32', False)
    auxiliares.linea_guiones(auxiliares.ANCHO)

def elim_turno(m_turnos):
    try:
        id_turno = str(auxiliares.ingresar_entero_positivo("Ingresar ID del turno: ")).zfill(6)
        
        turno_encontrado = False
        
        for turno in m_turnos:
            
            if turno['id'] == id_turno:
                turno_encontrado = True 
                
                if turno['estado_turno'] == auxiliares.estado_turno['activo']:
                    
                    archivo = "datos/turnos_cancelados.txt"
                    try:
                        with open(archivo, "a", encoding="UTF-8") as arch:
                            linea = (f"ID: {turno['id']} - FECHA: {str(turno['fecha'])} - HORA: {turno['hora']} - "
                                     f"PACIENTE_DNI: {turno['paciente']} - MEDICO_ID: {turno['medico']} - "
                                     f"ESPECIALIDAD: {turno['especialidad_medica']}\n")
                            arch.write(linea)
                    except OSError:
                        print(f"Error: No se pudo escribir en el archivo'{archivo}'.")
                    
                    turno['estado_turno'] = auxiliares.estado_turno['cancelado']
                    print(f"Turno de ID: [{id_turno}] cancelado exitosamente. ")
                    crear_leer_turnos.escribir_turnos(m_turnos)

                elif turno['estado_turno'] == auxiliares.estado_turno['cancelado']:
                    auxiliares.imprimir_error("Este turno ya se encuentra cancelado.")
                elif turno['estado_turno'] == auxiliares.estado_turno['finalizado']:
                    auxiliares.imprimir_error("Este turno ya está finalizado y no se puede cancelar.")

                input("Presione Enter para volver al menú anterior...")
                break 

        if not turno_encontrado:
            print("Turno no encontrado.")
            input("Presione Enter para volver al menú anterior...")
            
        return turno_encontrado
        
    except ValueError:
        print("Error: El ID ingreFsado no es válido.")
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
        
        id_encontrado = False

        for turno in m_turnos:
            
            if turno['id'] == id_turno:
                id_encontrado = True
                
                if turno['estado_turno'] != auxiliares.estado_turno['activo']:
                    auxiliares.imprimir_error(f"No se puede editar este turno. Su estado es: '{turno['estado_turno']}'.")
                    input("Presione Enter para volver al menú anterior...")
                    break 

                editando = True
                
                while editando: 
                    print("1 - Cambiar fecha")
                    print("2 - Cambiar hora")
                    print("0 - Volver")
                    
                    opcion = auxiliares.pedir_valor("Opción: ", tipo=int, opciones=[0, 1, 2])

                    if opcion == 1:
                        fecha_nueva, dia = crear_leer_turnos.elegir_fecha(mes, anio)
                        hora_actual = turno['hora']
                        medico_actual = turno['medico']

                        if fecha_nueva == turno['fecha']:
                            auxiliares.imprimir_error("Ya tienes esta fecha. No se realizaron cambios.")
                            continue 

                        horarios_tomados_dic = crear_leer_turnos.devolver_turnos_med(m_turnos, medico_actual, fecha_nueva, hora_turnos, libres=False)
                        horarios_tomados_lista = horarios_tomados_dic[medico_actual]

                        if hora_actual in horarios_tomados_lista:
                            auxiliares.imprimir_error(f"El médico no está disponible a las {hora_actual} en la fecha {fecha_nueva}.")
                            continue 
                        
                        turno['fecha'] = fecha_nueva
                        print("Fecha modificada exitosamente a:", turno['fecha'])
                        crear_leer_turnos.escribir_turnos(m_turnos)

                    elif opcion == 2:
                        fecha_actual = turno['fecha']
                        medico_actual = turno['medico']
                        hora_actual = turno['hora']

                        horarios_dic = crear_leer_turnos.devolver_turnos_med(m_turnos, medico_actual, fecha_actual, hora_turnos)
                        horarios_lista = horarios_dic[medico_actual]
                        
                        imprimir_menu_horarios_disponibles(horarios_lista, hora_actual)
                        
                        while True: 
                            try:
                                seleccion_str = auxiliares.ingresar_respuesta_str("Nuevo horario (0 para cancelar): ")
                                seleccion = int(seleccion_str)
                            except ValueError:
                                auxiliares.imprimir_error("Debe ingresar un número.")
                                continue

                            if seleccion == 0:
                                break 

                            if seleccion < 0 or seleccion > len(horarios_lista):
                                auxiliares.imprimir_error("Opción inválida, intente nuevamente.")
                                continue
                            
                            hora_seleccionada = horarios_lista[seleccion - 1]

                            if hora_seleccionada == hora_actual:
                                auxiliares.imprimir_error("Ya tienes este horario. No se realizaron cambios.")
                                continue

                            if hora_seleccionada == "No disp.":
                                auxiliares.imprimir_error("Ese horario no está disponible.")
                                continue

                            turno['hora'] = hora_seleccionada
                            print("Horario modificado exitosamente a:", turno['hora'])
                            crear_leer_turnos.escribir_turnos(m_turnos)
                            break 

                    elif opcion == 0:
                        editando = False 
                        
                    else:
                        auxiliares.imprimir_error("Opción inválida.")
                
                input("Presione Enter para volver al menú anterior...")
                break 

        if not id_encontrado:
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
        
        return edit_turnos(matriz_turnos, hora_turnos, info_mes['mes_en_numero'], info_mes['anio'])
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