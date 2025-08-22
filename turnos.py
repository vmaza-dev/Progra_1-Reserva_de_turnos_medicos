# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Nicolás Seijo, Victor Maza
# Descripción: 
# Fecha de creación: 10/08/2025
# ==============================================================================

import fun_aux, random


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

def Mostrar_meds_por_especialidad(lista_meds):
    """
    
    
    Parámetros:
    
    Returns:
    """
    print("x")

def crear_turno(turnos, hora_turnos, tipo_consultas, lista_pacs, lista_espe, lista_meds, estado):
    """
    Permite la creación de un turno y guardarlo en la matriz de turnos.
    
    Parámetros:
        turnos(list[list]): Matriz de turnos.
        lists_pac(list): Lista con los datos del paciente.
        lista_meds(list): Lista con los datos del médico.
        estados(str): Estado del turno
    Returns:
        turno(list): Turno con sus correspondientes datos.
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
    print("Elija un médico disponible")
    


def consultar_turno():
    # Hoy la arranco
    print("x")



# ==============================================================================
# ==============================PROGRAMA PRINCIPAL==============================
# ==============================================================================

# Matriz a obtener
# turnos = [
#     [1, "22/08/2025", "10:00", "Cosme Fulanito", "Traumatología", "Rodolfo Galleguillo", "Urgencia", "Activo"],
#     [2, "22/08/2025", "10:45", "Anakin Skywalker", "Psiquiatría", "Obi Wan Kenobi", "Revisión", "Cancelado"],
#     [3, "22/08/2025", "11:30", "Judge Vinsmoke", "Urología", "Sanji Vismonke", "Control", "Finalizado"],
#     [4, "22/08/2025", "12:15", "Homero Simpson", "Clínica Médica", "Tony Tony Chopper", "Urgencia", "Activo"]
# ]

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
           [456176, "Tony Tony Chopper", "Clínica Médica", 15, 1]]
pacientes = [[35023963, "Cosme Fulanito", "Total"],
             [32490932, "Anakin Skywalker", "Copago"],
             [20488909, "Judge Vinsmoke", "Particular"],
             [20101983, "Homero Simpson", "Particular"]]
########################


fun_aux.limpiar_terminal()
logo_turnos()








# print("Ingrese la fecha a consultar")

# dia, mes, anio = ingresar_fecha()
# valido, bisiesto = fun_aux.validar_fecha(dia, mes, anio)
# while valido == False:
#     print("Fecha inválida, ingrese nuevamente: ")
#     dia, mes, anio = ingresar_fecha()
#     valido, bisiesto = fun_aux.validar_fecha(dia, mes, anio)

# dia_consultado = f"{dia}/{mes}/{anio}"
# print(dia_consultado)
# hora_turno = elegir_horario(HORARIO_TURNOS)
# print(hora_turno)

# tipo_consulta = generar_consulta_med(CONSULTA)
# print(tipo_consulta)

# if len(turnos) == 0:
#     print("Sin turnos asignados")
#     crear_turno()


# fun_aux.imprimir_datos(ENCABEZADO, turnos)

# matriz de todps los turnos
# consulta de turnos
# creación de turnos

#### Esto es lo que va quedando pendiente de arrancar

# baja de turnos
# edición de turnos

