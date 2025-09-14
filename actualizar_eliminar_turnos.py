# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Nicolás Seijo, Victor Maza
# Descripción: Módulo Turnos
# Fecha de creación: 10/08/2025
# ==============================================================================

import auxiliares
import crear_leer_turnos


def elim_turno(m_turnos):
    id_turno = auxiliares.ingresar_entero_positivo("Ingresar id del turno: ")
    for turno in m_turnos:
        if turno[0] == id_turno:
            turno[7] = "Cancelado"
            return True  
    return False  

def edit_turnos(m_turnos, hora_turnos):
    id_turno = auxiliares.ingresar_entero_positivo("Ingresar id del turno: ")
    for turno in m_turnos:
        if turno[0] == id_turno:
            print("1 - Cambiar fecha")
            print("2 - Cambiar hora")
            opcion = auxiliares.ingresar_entero_positivo("Opción: ")

            if opcion == 1:
                d, m, a = crear_leer_turnos.ingresar_fecha()
                turno[1] = f"{d}/{m}/{a}"
            elif opcion == 2:
                auxiliares.imprimir_lista(hora_turnos, True)
                seleccion = auxiliares.ingresar_entero_positivo("Nuevo horario: ")
                if 1 <= seleccion <= len(hora_turnos):
                    turno[2] = hora_turnos[seleccion - 1]
            return True  # <-- éxito al editar
    return False  # <-- turno no encontrado

def principal_actualizar_turnos(matriz_turnos, hora_turnos):
    if not matriz_turnos:
        print("No hay turnos cargados")
        return False
    return edit_turnos(matriz_turnos, hora_turnos)  

def principal_eliminar_turnos(matriz_turnos):
    if not matriz_turnos:
        print("No hay turnos cargados")
        return False
    return elim_turno(matriz_turnos)  

