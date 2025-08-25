# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Nicolás Seijo, Victor Maza
# Descripción: 
# Fecha de creación: 10/08/2025
# ==============================================================================

import fun_aux, random


def mostrar_encabezado_consulta(encabe):
    """
    Mustra encabezado personalizado de consulta.

    Imprime por pantalla el encabezado en MAYÚSCULAS.
    
    Args:
        encabe(str): Encabezado personalizado.
    
    Returns:
    """
    print(f"{encabe.upper()}")


#def generar_informe()

def logo_turnos():
    """
    Imprime logo turnos.
    """

    fun_aux.limpiar_terminal()
    print("G6: SISTEMA DE GESTIÓN DE TURNOS")

    print(r"""
 _____                           
|_   _|   _ _ __ _ __   ___  ___ 
  | || | | | '__| '_ \ / _ \/ __|
  | || |_| | |  | | | | (_) \__ \
  |_| \__,_|_|  |_| |_|\___/|___/
""")

def ingresar_fecha():
    """
    Permite el ingreso de tres números para crear un fecha.

    Returns
        Tres número enteros(tuple)
    """
    d = fun_aux.ingresar_entero_positivo("Ingrese el día: ")
    m = fun_aux.ingresar_entero_positivo("Ingrese el mes: ")
    a = fun_aux.ingresar_entero_positivo("Ingrese el año: ")
    return d, m, a

def elegir_horario(hora_turnos):
    """
    Permite la elección del horario del turno.

    Muestra las posibles horarios de turnos.
    
    Parámetros:
        hora_turnos(list[list]): Matriz de los horarios de turnos del consultorio.
    
    Returns:
        Horario elegido(str)
    """
    print("Seleccione el horario del turno")
    print("-"*10, "HORARIO DE ATENCIÓN 9 A 17 HS", "-"*10)
    print("FRECUENCIA DE TURNOS: 20 MINUTOS")
    m_t = fun_aux.ingresar_respuesta_str("Mañana o tarde? m/t: ").lower()
    if m_t != "t":
        print("MAÑANA")
        print("h: 9/10/11/12")
        fun_aux.imprimir_lista(hora_turnos)
    else:
        print("TARDE")
        print("h: 13/14/15/16")
        fun_aux.imprimir_lista(hora_turnos)
    print("Ingrese el horario seleccionado sin los ':'. Ejemplo: 920")
    ingreso = fun_aux.ingresar_respuesta_str("Horario seleccionado: ")
    if len(ingreso) % 2 == 0:   
        hora = f"{ingreso[:2]}:{ingreso[2:]}"
    else:
        hora = f"{ingreso[:1]}:{ingreso[1:]}"
    return hora

def generar_consulta_med(tipos_consultas):
    """
    Permite la elección del tipo de consulta médica.
    
    Parámetros:
        tipos_consultas(list): Lista con los tipos de consultas ofrecidas.
    
    Returns:
        consulta(str)
    """
    print("Seleccione el tipo de consulta del turno")
    print("-"*10, "CONSULTAS OFRECIDAS", "-"*10)
    fun_aux.imprimir_lista(tipos_consultas,True)
    seleccion = fun_aux.ingresar_entero_positivo("Seleccione la consulta: ")
    if seleccion == 1:
        seleccion = 0
    else:
        seleccion -= 1
    consulta = tipos_consultas[seleccion]    
    return consulta

def elegir_especialidad_med(lista_meds):
    """
    Permite la elección de la especialidad médica.
    
    Parámetros:
        lista_meds(list): Lista con los datos del médico.    
    Returns:
        espec(str): Especilidad elegida.
    """
    print("Seleccione el tipo de especialidad médica")
    print("-"*10, "ESPECIALIDADES", "-"*10)
    fun_aux.imprimir_lista(fun_aux.especialidades, True)
    seleccion = fun_aux.ingresar_entero_positivo("Seleccione la especialidad: ")
    if seleccion == 1:
        seleccion = 0
    else:
        seleccion -= 1
    espc = fun_aux.especialidades[seleccion]    
    return espc   

def mostrar_meds_por_especialidad(lista_meds, espec):
    """
    Filtra y muestra nombre de médicos según la especialidad indicada.
    
    Parámetros:
        lista_meds(list): Lista de médicos.
        espec(str): Nombre de la especialidad a buscar.
    Returns:
        
    """
    meds_espec = []
    for medico in lista_meds:
        if espec in medico:
            meds_espec.append(medico[1])
    fun_aux.imprimir_lista(meds_espec, True)
    return meds_espec

def crear_id_turno(turnos):
    """
    Crea el id de turnos.
    
    Parámetros:
        turnos(list[list]): Matriz de turnos.

    Returns:
        int: Número de id turno
    """
    if len(turnos) == 0:
        return 1
    else:
        return len(turnos) + 1
    
def crear_turno(turnos, hora_turnos, tipo_consultas, 
                lista_pacs, lista_espe, lista_meds):
    """
    Permite la creación de un turno y guardarlo en la matriz de turnos.
    
    Parámetros:
        turnos(list[list]): Matriz de turnos.
        lists_pac(list): Lista con los datos del paciente.
        lista_meds(list): Lista con los datos del médico.
    Returns:
    """
    print("-"*10, "NUEVO TURNO", "-"*10)
    print("-"*40)
    print("Ingrese paciente")
    paciente = random.choice(lista_pacs)
    print(f"Paciente ingresado: {paciente}")
    print("Ingrese fecha solcitida para turno")
    dia, mes, anio = ingresar_fecha()
    fecha_turno = f"{dia}/{mes}/{anio}"
    horario_turno = elegir_horario(hora_turnos)
    tipo_consulta = generar_consulta_med(tipo_consultas)
    especialidad = elegir_especialidad_med(lista_espe)
    print(f"{especialidad.upper()}: Elija un médico disponible.")
    meds_a_selec= mostrar_meds_por_especialidad(lista_meds, especialidad)
    seleccion = fun_aux.ingresar_entero_positivo("Seleccione médico: ")
    if seleccion == 1:
        seleccion = 0
    else:
        seleccion -= 1
    medico_selec = meds_a_selec[seleccion]
    id = crear_id_turno(turnos)
    turno = [id, fecha_turno, horario_turno, paciente[1], 
             especialidad, medico_selec, tipo_consulta, "Activo"]
    turnos.append(turno)
    print(f"Turno: {turno} generado exitosamente")


def consultar_por_fecha(encabezados, m_turnos):
    """
    Filtra y muestra turnos según la fecha a ingresar.
    
    Parámetros:
        encabezados(list): Lista de encabezados de la matriz de turnos.
        m_turnos(list[list]): Matriz de turnos
    Returns:
    """
    mostrar_encabezado_consulta("consulta por fecha")
    print("Ingrese la fecha a consultar")

    dia, mes, anio = ingresar_fecha()
    valido, bisiesto = fun_aux.validar_fecha(dia, mes, anio)
    while valido == False:
        print("Fecha inválida, ingrese nuevamente: ")
        dia, mes, anio = ingresar_fecha()
        valido, bisiesto = fun_aux.validar_fecha(dia, mes, anio)
    fecha_cons = f"{dia}/{mes}/{anio}"
    turnos_por_fecha = []
    for turno in m_turnos:
        if fecha_cons in turno:
            turnos_por_fecha.append(turno)
            # por acá agregaría la función para hacer el informe
    fun_aux.imprimir_datos(encabezados, turnos_por_fecha)

def consultar_por_paciente(encabezados, m_turnos):
    """
    Filtra y muestra turnos según la fecha a ingresar.
    
    Parámetros:
        encabezados(list): Lista de encabezados de la matriz de turnos.
        m_turnos(list[list]): Matriz de turnos    
    Returns:
    """
    mostrar_encabezado_consulta("consulta por paciente")
    pac = fun_aux.ingresar_entero_positivo("Ingrese el DNI del paciente: ")
    while len(str(pac)) < 8:
        print("DNI incorrecto, ingrese nuevamente")
        pac = fun_aux.ingresar_entero_positivo("Ingrese el DNI del paciente: ")
    
    turnos_pac_cons = []
    #for 



def consultar_turno(encabezados, turnos):


    # mi idea es hacer una salida tipo informe, para cada consulta
    # donde se informe también las métricas. La idea sería seguir el
    # ejemplo del profe con la factura.
    
    print("-"*20, "Consultas turnos", "-"*20)
    print("""
1 - Horario
2 - Fecha
3 - Paciente
4 - Medico
5 - Especialidad
6 - Tipo consulta
7 - Estado
""")
    
    con_selec = fun_aux.ingresar_entero_positivo("Seleccione consulta a realizar: ")

    match con_selec:
        case 1:
            print("x")
        case 2:
            consultar_por_fecha(encabezados, turnos)
            print("x")
        case 3:
            print("x")
        case 4:
            print("x")
        case 5:
            print("x")
        case 6:
            print("x")
        case 7:
            print("x")
    print("x")

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
                    turno[2] = elegir_horario(HORARIO_TURNOS)
                case 3:
                 turno[3] = random.choice(pacientes)[1]
                case 4:
                    turno[4] = elegir_especialidad_med(ESPECIALIDADES)
                case 5:
                  turno[5] = random.choice(medicos)[1]
                case 6:
                    turno[6] = generar_consulta_med(CONSULTA)
                case 7:
                    turno[7] = fun_aux.ingresar_respuesta_str("Ingrese nuevo estado: ")

          print("Turno editado")
          return 
    
  print("Turno no encontrado")


# ==============================================================================
# ==============================PROGRAMA PRINCIPAL==============================
# ==============================================================================

# Matriz hard para prueba de código
turnos_hard = [
    [1, "22/8/2025", "10:00", "Cosme Fulanito", "Traumatología", "Rodolfo Galleguillo", "Urgencia", "Activo"],
    [2, "22/8/2025", "10:45", "Anakin Skywalker", "Psiquiatría", "Obi Wan Kenobi", "Revisión", "Cancelado"],
    [3, "23/8/2025", "11:30", "Judge Vinsmoke", "Urología", "Sanji Vismonke", "Control", "Finalizado"],
    [4, "22/8/2025", "12:15", "Homero Simpson", "Clínica Médica", "Tony Tony Chopper", "Urgencia", "Activo"]
]

ENCABEZADO = ["ID","FECHA", "HORA","PACIENTE","ESPECIALIDAD", "MEDICO","TIPO CONSULTA","ESTADO"]
                                    #ID_PAC     #ID_ESP        #ID_MED
ESTADO_TURNO = ["Activo", "Cancelado", "Finalizado"]
CONSULTA = ["Control", "Revisión", "Urgencia"]
HORARIO_TURNOS = ["h:00", "h:20","h:40"]
ESPECIALIDADES = fun_aux.especialidades
turnos = []

### DATOS QUE DEBERIAN LLEGAR ###
medicos = [[154892, "Rodolfo Galleguillo", "Traumatología", 15, 1],
           [153167, "Obi Wan Kenobi", "Psiquiatría", 15, 1],
           [123858, "Sanji Vismonke", "Urología", 15, 1],
           [456176, "Tony Chopper", "Clínica Médica", 15, 1],
           [789546, "Piccolo DaimaKu", "Traumatología", 15, 1]]
pacientes = [[35023963, "Cosme Fulanito", "Total"],
             [32490932, "Anakin Skywalker", "Copago"],
             [20488909, "Judge Vinsmoke", "Particular"],
             [20101983, "Homero Simpson", "Particular"]]
########################


fun_aux.limpiar_terminal()
logo_turnos()

# crear_turno(turnos, HORARIO_TURNOS, CONSULTA, pacientes, ESPECIALIDADES, medicos)
consultar_turno(ENCABEZADO, turnos_hard)

# if len(turnos) == 0:
#     print("Sin turnos asignados")
#     crear_turno()


# fun_aux.imprimir_datos(ENCABEZADO, turnos)

# matriz de todps los turnos
# consulta de turnos
# creación de turnos

#### Esto es lo que va quedando pendiente de arrancar
