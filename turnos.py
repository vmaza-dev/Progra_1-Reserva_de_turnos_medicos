# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Nicolás Seijo, Victor Maza
# Descripción: Módulo Turnos
# Fecha de creación: 10/08/2025
# ==============================================================================

import fun_aux, random
from datetime import datetime, time, date, timedelta

# Funciones del CRUD

def mostrar_encabezado_consulta(encabe):
    """
    Mustra encabezado personalizado de consulta.

    Imprime por pantalla el encabezado en MAYÚSCULAS.
    
    Args:
        encabe(str): Encabezado personalizado.
    
    Returns:
    """
    print(f"{encabe.upper()}")

def generar_informe():
    """
    
    
    Parámetros:
    
    Returns:
    """
    # La idea de esta función es generar una salida por pantalla tipo
    # informe tuneada con ansi
    print("x")

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
    c = int(len(hora_turnos)/2)
    print("")
    fun_aux.imprimir_lista(hora_turnos[:c], True)
    print("")
    fun_aux.imprimir_lista(hora_turnos[c:], True, 8)
    print("")
    seleccion = fun_aux.ingresar_entero_positivo("Horario seleccionado: ")
    if seleccion == 1:
        seleccion = 0
    else:
        seleccion -= 1
    hora = hora_turnos[seleccion] 
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

def elegir_especialidad_med():
    """
    Permite la elección de la especialidad médica.
    
    Parámetros:
          
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
    mat_meds = []
    for medico in lista_meds:
        if espec in medico:
            meds_espec.append(medico[1])
            mat_meds.append(medico[0])
    fun_aux.imprimir_lista(meds_espec, True)
    return mat_meds

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

def crear_horario_atencion(inicio, fin):
    """
    Crea el horario de atención del consultorio.
    
    Parámetros:
        inicio(time): Hora del primer turno.
        fin(time): Hora del último turno.
    Returns:
        list: Lista con los horarios de los turnos.
    """
    h_turnos = [inicio.strftime("%H:%M")]
    h_turno =  inicio
    while h_turno <= fin:
        h_turno += timedelta(minutes = 30)
        h_turnos.append(str(h_turno.strftime("%H:%M")))
    return h_turnos

def crear_mes(inicio, fin):
    """
    Genera todas las fechas entre inicio y fin
    
    Parámetros:
    
    Returns:
    """
    rango_fechas = [inicio + timedelta(days=i) for i in range((fin - inicio).days + 1)]
    return rango_fechas
    
def devolver_paciente(paci, dni):
    """
    Devuelve el nombre del paciente según el DNI.
    
    Parámetros:
        paci(list[list]): Matriz de pacientes.
        dni(int): DNI del paciente a buscar.
    
    Returns:
    """
    buscar = True
    i = 0
    while buscar:
        if paci[i][0] == dni:
            nombre = paci[i][1]
            buscar = False
        i += 1
    return nombre
                
def devolver_medico(meds, mat):
    """
    Devuelve el nombre del médicos según el matrícula.
    
    Parámetros:
        meds(list[list]): Matriz de médicos.
        mat(int): Matrícula del médico a buscar.
    
    Returns:
    """
    buscar = True
    i = 0
    while buscar:
        if meds[i][0] == mat:
            nombre = meds[i][1]
            buscar = False
        i += 1
    return nombre

def consultar_por_fecha(encabezados, m_turnos, paci, meds):
    """
    Filtra y muestra turnos según la fecha a ingresar.
    
    Parámetros:
        encabezados(list): Lista de encabezados de la matriz de turnos.
        m_turnos(list[list]): Matriz de turnos
        paci(list[list]): Matriz de pacientes.
        meds(list[list]): Matriz de médicos.
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
    fecha_cons = date(anio, mes, dia)
    turnos_por_fecha = []
    for turno in m_turnos:
        if fecha_cons in turno:
            turnos_por_fecha.append(turno)
            # por acá agregaría la función para hacer el informe
    leer_turnos(turnos_por_fecha, encabezados, paci, meds)

def consultar_por_paciente(encabezados, m_turnos, paci, meds):
    """
    Filtra y muestra turnos según el DNI del paciente.
    
    Parámetros:
        encabezados(list): Lista de encabezados de la matriz de turnos.
        m_turnos(list[list]): Matriz de turnos
        paci(list[list]): Matriz de pacientes.
        meds(list[list]): Matriz de médicos.    
    Returns:
    """
    mostrar_encabezado_consulta("consulta por paciente")
    pac = fun_aux.ingresar_entero_positivo("Ingrese el DNI del paciente: ")
    while len(str(pac)) < 8:
        print("DNI incorrecto, ingrese nuevamente")
        pac = fun_aux.ingresar_entero_positivo("Ingrese el DNI del paciente: ")
    
    turnos_pac_cons = []
    for turno in m_turnos:
        if pac in turno:
            turnos_pac_cons.append(turno)
        # por acá agregaría la función para hacer el informe
    leer_turnos(turnos_pac_cons, encabezados, paci, meds)

def consultar_por_horario():
    """
    
    
    Parámetros:
    
    Returns:
    """

### Funciones CRUD

def crear_turnos_random(turnos, mes, hora_turnos, tipo_consultas, estado,
                         paci ,meds , n_turnos):
    """
    Crea una matriz de turnos al azar.

    Usa las matrices creadas en los módulos pacientes y médicos.
    
    Parámetros:
        turnos(list[list]): Matriz de turnos.
        mes(date): Lista de los días del mes. 
        hora_turnos(list): Lista con los horarios de los turnos.
        tipo_consultas(list): Lista con el tipo de consultas.
        estado(list): Lista de estados.
        paci(list[list]): Matriz de pacientes.
        meds(list[list]): Matriz de médicos.
        n_turnos(int): Número de turnos a generar.

    Returns:
    """
    # Falta ver como hacer que un médico tome mas de un turno.
    for i in range(n_turnos):
        id = crear_id_turno(turnos)
        fecha = mes[i]
        hora_turno = random.choice(hora_turnos)
        especialidad = random.choice(fun_aux.especialidades)
        consulta = random.choice(tipo_consultas)
        estado_turno = random.choice(estado)
        paciente = random.choice(paci)
        dni_pac =  paciente[0]
        medico = random.choice(meds)
        mat_med =  medico[0]
        turnos.append([id, fecha, hora_turno, dni_pac, especialidad, mat_med, 
                       consulta, estado_turno])

def crear_turno(turnos, hora_turnos, tipo_consultas, 
                lista_pacs, lista_meds):
    """
    Permite la creación de un turno y guardarlo en la matriz de turnos.
    
    Parámetros:
        turnos(list[list]): Matriz de turnos.
        hora_turnos(list): Lista con los horarios de los turnos.
        tipo_consultas(list): Lista con el tipo de consultas.
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
    especialidad = elegir_especialidad_med()
    print(f"{especialidad.upper()}: Elija un médico disponible.")
    meds_a_selec= mostrar_meds_por_especialidad(lista_meds, especialidad)
    seleccion = fun_aux.ingresar_entero_positivo("Seleccione médico: ")
    if seleccion == 1:
        seleccion = 0
    else:
        seleccion -= 1
    medico_selec = meds_a_selec[seleccion]
    id = crear_id_turno(turnos)
    turno = [id, fecha_turno, horario_turno, paciente[0], 
             especialidad, medico_selec, tipo_consulta, "Activo"]
    # Generar una confirmación del turno y mensaje de "generado exitosamente"
    turnos.append(turno)
    print(f"Turno: {turno} generado exitosamente")

def leer_turnos(turnos, encabezado, paci, meds):
    """
    Leer y imprime matriz de turnos mas encabezado.
    
    Parámetros:
        turnos(list[lis]): Matriz de turnos.
        encabezado(list): Lista de encabezados de la matriz.
        paci(list[list]): Matriz de pacientes.
        meds(list[list]): Matriz de médicos.
    Returns:
    """
    # Tendría que ir un encabezado.
    filas = len(turnos)
    columnas = len(turnos[0])
    for t in range(columnas):
        match t:
            case 0|2:
                print(f"{encabezado[t]:<7}", end="\t")
            case _:
                print(f"{encabezado[t]:<15}", end="\t")        
    print()
    for i in range(filas):
        # print("-"*107)
        for j in range(columnas):
            match j:
                case 0|2:
                    print(f"{turnos[i][j]:<7}", end = "\t")
                case 1:
                    print(f"{str(turnos[i][j].strftime("%d/%m/%Y")):<15}", end = "\t")
                case 3:
                    nombre = devolver_paciente(paci,turnos[i][j])
                    apellido = nombre.split()[1]
                    print(f"{nombre[:1]}. {apellido}", end = "\t")
                case 5:
                    nombre = devolver_medico(meds,turnos[i][j])
                    apellido = nombre.split()[1]
                    print(f"{nombre[:1]}. {apellido:<10}", end = "\t")
                case _:
                    print(f"{turnos[i][j]:<15}", end = "\t")
        print()
    
def consultar_turno(encabezados, turnos, paci, meds):


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
            consultar_por_fecha(encabezados, turnos, paci, meds)
        case 3:
            consultar_por_paciente(encabezados, turnos, paci, meds)
        case 4:
            print("x")
        case 5:
            print("x")
        case 6:
            print("x")
        case 7:
            print("x")


# ==============================================================================
# ==============================PROGRAMA PRINCIPAL==============================
# ==============================================================================

# Matriz hard para prueba de código
turnos_hard = [
    [1, "22/8/2025", "10:00", 35023963, "Traumatología", 154892, "Urgencia", "Activo"],
    [2, "22/8/2025", "10:45", 32490932, "Psiquiatría", 153167, "Revisión", "Cancelado"],
    [3, "23/8/2025", "11:30", 20488909, "Urología", 123858, "Control", "Finalizado"],
    [4, "22/8/2025", "12:15", 20101983, "Clínica Médica", 456176, "Urgencia", "Activo"]
]

ENCABEZADO = ["ID","FECHA", "HORA","PACIENTE","ESPECIALIDAD", "MEDICO","TIPO CONSULTA","ESTADO"]
                                    #ID_PAC     #ID_ESP        #ID_MED
ESTADO_TURNO = ["Activo", "Cancelado", "Finalizado"]
CONSULTA = ["Control", "Revisión", "Urgencia"]
INICIO_TURNOS = datetime(2025,1,1,9,0)# Pongo una fecha cualquiera lo que importa es la hora
FIN_TURNOS = datetime(2025,1,1,16,0)# Pongo una fecha cualquiera lo que importa es la hora
INICIO_MES = date(2025, 8, 1)
FIN_MES = date(2025, 8, 31)

turnos = []
horario_turnos = crear_horario_atencion(INICIO_TURNOS, FIN_TURNOS)
mes = crear_mes(INICIO_MES, FIN_MES)

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

# crear_turno(turnos, horario_turnos, CONSULTA, pacientes, medicos)
crear_turnos_random(turnos, mes, horario_turnos, CONSULTA, ESTADO_TURNO, 
                    pacientes, medicos, 31)
leer_turnos(turnos, ENCABEZADO, pacientes, medicos)
# consultar_turno(ENCABEZADO, turnos, pacientes, medicos)

#### Esto es lo que va quedando pendiente de arrancar

# baja de turnos
# edición de turnos

