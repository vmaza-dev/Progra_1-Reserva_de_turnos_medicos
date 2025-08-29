# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Nicolás Seijo, Victor Maza
# Descripción: Módulo Turnos
# Fecha de creación: 10/08/2025
# ==============================================================================

from cre_leer import *
from fun_aux import *



# ==============================================================================
# ==============================PROGRAMA PRINCIPAL==============================
# ==============================================================================

def elim_turno(m_turnos):
    """
    Cancela un turno cambiando el estado
    """
    print("-"*10, "BAJA DE TURNO", "-"*10)
    id_turno = fun_aux.ingresar_entero_positivo("Ingresar id del turno: ")

    for turno in m_turnos:
        if turno [0] == id_turno:
            if turno [7] == "Cancelado":
                print("Su turno ya está cancelado")
                return
            turno[7] = "Cancelado"
            print(f"Turno {id_turno} cancelado")
            return
        print("Turno no encontrado")

def edit_turnos(m_turnos):
  """ 
  Modifica un turno cargado de la matriz
  """
  print("-"*10,"EDITAR TURNO","-"*10)
  id_turno = fun_aux.ingresar_entero_positivo("Ingresar id del turno: ")

  for turno in m_turnos:
      if turno[0] == id_turno:
          print("Seleccione campo a modificar")
          print("1 - Fecha\n2 - Hora\n3 - Paciente\n4 - Especialidad\n5 - Médico\n6 - Tipo de consulta\n7 - Estado")
          opcion = fun_aux.ingresar_entero_positivo("Opcion: ")

          match opcion:
                case 1:
                    d,m,a = ingresar_fecha()
                    turno[1] = f"{d}/{m}/{a}"
                case 2:
                    turno[2] = elegir_horario(INICIO_TURNOS)
                case 3:
                 turno[3] = random.choice(pacientes)[1]
                case 4:
                    turno[4] = elegir_especialidad_med(especialidades)
                case 5:
                  turno[5] = random.choice(medicos)[1]
                case 6:
                    turno[6] = generar_consulta_med(CONSULTA)
                case 7:
                    turno[7] = fun_aux.ingresar_respuesta_str("Ingrese nuevo estado: ")

          print("Turno editado")
          return 
    
  print("Turno no encontrado")
