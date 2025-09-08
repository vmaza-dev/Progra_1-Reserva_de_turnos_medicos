# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Nicolás Seijo, Victor Maza
# Descripción: Módulo Turnos
# Fecha de creación: 10/08/2025
# ==============================================================================

#-------------------------------------------------------------------------------
#----------------------------- MODULOS DE PYTHON -------------------------------
#-------------------------------------------------------------------------------

import random
from datetime import datetime, date, timedelta
import calendar
import re

#-------------------------------------------------------------------------------
#---------------------------- MODULOS DEL PROYECTO -----------------------------
#-------------------------------------------------------------------------------

import fun_aux
from . import calendario # importo mi módulo calendario
# es necesatio importarlo así para que python busque dentro de este paquete
# sino busca al mismo nivel que fun_aux

#-------------------------------------------------------------------------------
#---------------------------- FUNCIONES DEL MODULO -----------------------------
#-------------------------------------------------------------------------------

def transponer_matriz(matriz):
    """
    Transpone una matriz dada.
    
    Parámetros:
    
    Returns:
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta = [[0] * filas for i in range(columnas)]
    for i in range(filas):
        for j in range(columnas):
            transpuesta[j][i] = matriz[i][j]
    return transpuesta

def mostrar_encabezado_consulta(encabe):
    """
    Mustra encabezado personalizado de consulta.

    Imprime por pantalla el encabezado en MAYÚSCULAS.
    
    Args:
        encabe(str): Encabezado personalizado.
    
    Returns:
    """
    print("---------------------------")
    print(f"MENÚ PRINCIPAL > TURNOS > CONSULTA > OTRAS > {encabe.upper()}")
    print("---------------------------")

def generar_informe(matriz, consulta):#❓
    """
    Devuelve un informe con métricas de una matriz
    
    Parámetros:
        matriz(list[list])
    Returns:
    """
    linea = "="*80
    consulta = f"{consulta}"


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

def ingresar_opcion_elegida(lista_opciones):
    """
    Permite el ingreso de una opción empezando en 1..

    Parámetros:
        lista_opciones(list): Lista con la opciones.
    
    Returns:
        int: Devuelve el índice de la opción.
    """
    opcion = fun_aux.ingresar_respuesta_str("Ingrese el número de opción escogida: ")
    opcion_valida = False
    while opcion_valida  == False:
        # valido que no ingrese letras
        if re.findall("[a-zA-Z]", opcion):
            print("Ingrese una opción válida")
            opcion= fun_aux.ingresar_respuesta_str("")
        elif int(opcion) <= 0 or int(opcion) > len(lista_opciones) :
            print("Ingrese una opción válida")
            opcion = fun_aux.ingresar_respuesta_str("")
        else:
            opcion_valida = True
    opcion_elegida = int(opcion)-1
    return opcion_elegida

def elegir_fecha(mes, anio):
    """
    Permite la elección de una fecha para cargar un turno.
    
    Parámetros:
        mes(int)
        anio(int)
    
    Returns:
        date: Fecha seleccionada.
        str: Nombre del día de la fecha seleccionada.
    """
    calendario.calendario_mes(mes, anio)
    nombres_dias_semana = ["Domingo", "Lunes", "Martes","Miércoles", 
                    "Jueves", "Viernes","Sábado"]
    # estructura:
    # 6 filas = semanas
    # 7 columnas = D-S
    # [..., 
    # [Domingo, Lunes, Martes, Miercoles, Jueves, Viernes, Sábado],
    # [Domingo, Lunes, Martes, Miercoles, Jueves, Viernes, Sábado],
    # ...]
    print("Seleccione una fecha ingresando el dia")
    dia_ingresado = fun_aux.ingresar_respuesta_str("")
    dia_valido = False
    while dia_valido == False:
        # valido que no ingrese letras
        if re.findall("[a-zA-Z]", dia_ingresado):
            print("Ingrese una fecha válida")
            dia_ingresado = fun_aux.ingresar_respuesta_str("")
            # acá falta ver como validar que no elija el mas allá del
            # último día del mes actual, puse 31 para hacerlo general
        elif int(dia_ingresado) <= 0 or int(dia_ingresado) > 31 :
            print("Ingrese una fecha válida")
            dia_ingresado = fun_aux.ingresar_respuesta_str("")
        else:
            dia_valido = True
    # saco el dia de la semana y su nombre para que quede mas lindo

    n_dia_semana = calendario.dia_de_la_semana(int(dia_ingresado), mes, anio)

    nombre_dia = nombres_dias_semana[n_dia_semana]

    # paso a tipo date para que despúes puda ordernar con sorted
    # al usar leer_turnos. 
    fecha_seleccionada = date(anio, mes, int(dia_ingresado))

    return fecha_seleccionada, nombre_dia

def elgir_consulta_med(tipos_consultas):
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

def elegir_medico(mat_turnos, fecha_turno, dia_semana, hora_turnos,
                                  meds, especialidad):
    """
    Permite la elección de un medico disponible. 
    
    Parámetros:
        mat_turnos(list[list]): Matriz de turnos del mes.
        fecha_turno(date): Fecha seleccionada para el turno.
        dia_semana(str): Nombre del día de la fecha.
        horario_turno(str): Hora del turno seleccionada para el turno.
        meds(list[list]): Matriz de médicos.
        especialidad(str): Especialidad seleccionada para el turno.
    
    Returns:
    """
    # ya se que el paciente no tiene turno con esta especilidad en este fecha
    # 1 busco las matriculas de todos los medicos de la especialidad requerida
    mat_medicos_especialidad = filtrar_meds_por_especialidad(meds, especialidad)
    # 2 construyo una matriz con todos los medicos y sus horarios libres
    medicos_turnos_libres = []
    for mat in mat_medicos_especialidad:
        turnos_libres = devolver_turnos_med(mat_turnos, fecha_turno, mat, hora_turnos)
        medicos_turnos_libres.append(turnos_libres)
    # 3 crear el menu de selección
    print(f"Medicos y horarios disponibles parar el {dia_semana} {fecha_turno.strftime("%d/%m/%Y")}")
    print()
    # transpongo mi matriz de turnos libres
    tras_medicos_turnos_libres = transponer_matriz(medicos_turnos_libres)
    encabezado =  tras_medicos_turnos_libres.pop(0)# me quedo con la lista de matriculas
    # de los médicos
    # imprimo de manera linda la transpuesta
    filas = len(tras_medicos_turnos_libres)
    columnas = len(tras_medicos_turnos_libres[0])# me quedo con las mat de los medicos

    opcion = 0
    for titulo in encabezado:
        opcion += 1
        print(f"|OP {opcion}| {devolver_medico(meds, titulo):<15}", end="\t")
    print()

    op_horario = 0
    for i in range(filas):
        op_horario += 1
        for j in range(columnas):
            print(f"|{op_horario:<2}|-{tras_medicos_turnos_libres[i][j]:<15}", end = "\t")
        print()

    # selecciono medico
    print("---------------------------")
    print("Seleccione médico")
    print("---------------------------")

    op_medico = ingresar_opcion_elegida(encabezado) 
    medico_selec = encabezado[op_medico]
    # selecciono hoarario
    print("---------------------------")
    print("Seleccione horario")
    print("---------------------------") 
    op_horario = ingresar_opcion_elegida(hora_turnos) 

    horario_selec = hora_turnos[op_horario]

    return medico_selec, horario_selec

def devolver_turnos_med(mat_turno, fecha, mat_med, hora_turnos, libres = True):
    """
    Devuelve una lista con los horarios libres del médico en un fecha dada.
    
    Args:
    
    Returns:
    """
    turnos_tomados = []
    turnos_fecha = filtrar_turnos(mat_turno, fecha)
    for turno in turnos_fecha:
        if mat_med == turno[5]:
            turnos_tomados.append(turno[2])
    turnos_tomados.sort()        
    if libres:
        turnos_libres = []
        for hora_turno in hora_turnos:
            if hora_turno not in turnos_tomados:
                turnos_libres.append(hora_turno)
            elif hora_turno in turnos_tomados:
                turnos_libres.append("No disp.")
        turnos_libres[0:0] = [mat_med]
        return turnos_libres
        
    turnos_tomados[0:0] = [mat_med]
    return turnos_tomados

def filtrar_turnos(mat_turnos, filtro, inverso = False):
    """
    Filtra turnos según lo solicitado.

    Si inverso True, filtra lo que no coincide.

    Parámetros:
        mat_turnos(list[list]): Matriz de turnos.
        filtro(str|int|date): Clave de filtrado.
        inverso(bool): Defecto False. 
    
    Returns:
        Matriz de turno filtrada
    """
    turnos_filtrados = []
    if inverso == False:
        for turno in mat_turnos:
            if filtro in turno:
                turnos_filtrados.append(turno)
    elif inverso == True:
        for turno in mat_turnos:
            if filtro not in turno:
                turnos_filtrados.append(turno)
    return turnos_filtrados

def filtrar_meds_por_especialidad(meds, espec):
    """
    Filtra médicos según la especialidad indicada.
    
    Parámetros:
        meds(list): Lista de médicos.
        espec(str): Nombre de la especialidad a buscar.
    Returns:
        list: Matriculas de médicos filtrados por especialidad.
    """
    mat_meds = []
    for medico in meds:
        if espec in medico:
            mat_meds.append(medico[0])
    return mat_meds

def crear_id_turno(mat_turnos):
    """
    Crea el id de turnos.
    
    Parámetros:
        turnos(list[list]): Matriz de turnos.

    Returns:
        int: Número de id turno
    """
    if len(mat_turnos) == 0:
        return 1
    else:
        return len(mat_turnos) + 1

def crear_horario_atencion(inicio, fin, freq = 30):
    """
    Crea el horario de atención del consultorio.

    Por defecto cada turno de se asigna cada media hora.
    
    Parámetros:
        inicio(time): Hora del primer turno.
        fin(time): Hora del último turno.
        freq(int): Tiempo entre cada turno.
    Returns:
        list[time]: Lista con los horarios de los turnos.
    """
    h_turnos = [inicio.strftime("%H:%M")]
    h_turno =  inicio
    while h_turno <= fin:
        h_turno += timedelta(minutes = freq)# sumo la frequencia
        h_turnos.append(h_turno.strftime("%H:%M"))# convierto en un string en el
        # formato que quiero que se vea, horas:minutos
    return h_turnos

def crear_mes():
    """
    Genera todas las fechas del mes actual.
    
    Parámetros:
    
    Returns:
        rango_fechas(list[date]): Lista con las fechas generadas.
        mes_numero(int)
        mes_palabra(str)
        anio(int)
        int: Número de dias del mes.
    """
    hoy = date.today()
    mes_numero = hoy.month# pido el mes actual
    anio = hoy.year
    mes_palabra = calendario.mes_a_palabras(mes_numero)
    ultimo_dia = calendar.monthrange(anio, mes_numero)[1]
    inicio_mes = date(2025, mes_numero, 1)
    fin_mes = date(2025, mes_numero, ultimo_dia )
    rango_fechas = [inicio_mes + timedelta(days=i) for i in range((fin_mes - inicio_mes).days + 1)]
    return rango_fechas, mes_numero, mes_palabra, anio, len(rango_fechas)
    
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
                
def devolver_medico(meds, mat_med):
    """
    Devuelve el nombre del médicos según la matrícula.
    
    Parámetros:
        meds(list[list]): Matriz de médicos.
        mat_med(int): Matrícula del médico a buscar.
    
    Returns:
    """
    buscar = True
    i = 0
    while buscar:
        if meds[i][0] == mat_med:
            nombre = meds[i][1]
            buscar = False
        i += 1
    return nombre

def validar_turno(mat_turnos, fecha, medico, paciente, hora_turno):
    """
    Valida el turno a asignar.

    Si hay superposición de horarios o superposición de médicos devuelve False.

    Parámetros:
        
    Returns:
    """
    mat_turnos_fecha= filtrar_turnos(mat_turnos, fecha)
    for turno in mat_turnos_fecha:
        # acá entra en bucle cuando pido mas de 200 turnos
        # no se por que todavía.
        # print(turno)
        # valido por médico
        if medico == turno[5]:
            # evito que el médico atienda al paciente dos veces en el mismo día
            if paciente == turno[3]:
                return False
            # evito que el médico atienda al paciente en el horario de otro paciente
            elif hora_turno == turno[2]:# solo sirve para turnos random
                return False
        # valido por paciente, que no tenga turno en ese mismo horario
        elif paciente == turno[3]:
            if hora_turno == turno[2]:
                return False

    return True

def validar_turno_por_especialidad(mat_turnos, fecha_turno, especialidad, paciente):
    """
    
    Parámetros:
    
    Returns:
    """
    valido = True
    # 1 filtro por fecha
    turnos_fecha = filtrar_turnos(mat_turnos, fecha_turno)
    # 2 filtro por especialidad
    turnos_por_especialidad = filtrar_turnos(turnos_fecha, especialidad)
    # 3 veo si el paciente ya tiene turno con esta especialidad
    for turno in turnos_por_especialidad:
        if paciente == turno[3]:
            valido = False
    return valido

def confirmar_turno(turno_a_confi, dia):
    """
        
    Args:
    
    Returns:
    """
    print("---------------------------")
    print("[ENTER] CONFIRMAR TURNO")
    print("[0]     CANCELAR")
    print("---------------------------")
    print(f"{turno_a_confi[3]}")
    print(f"{dia} {turno_a_confi[1]} a las {turno_a_confi[2]}\
     MEDICO: {turno_a_confi[5]}-{turno_a_confi[4]}")
    op = input("")
    if op == "":
        return True
    else:
        return False

def contar_ocurr_elementos_turnos(mat_turnos, lista_elementos):
    """
    Devuelve una lista con el conteo de cada elemento en matriz de turnos.
    
    Parámetros:
        mat_turnos(list[list])
        lista_elementos(list)
    
    Returns:
        list[list[]]
    """
    lista_conteos = []
    for elemento in lista_elementos:
        contador = 0
        for turno in mat_turnos:
            if elemento in turno:
                contador += 1
        lista_conteos.append([elemento, contador])
    return lista_conteos

#-------------------------------------------------------------------------------
# FUNCIONES DE CONSULTAS -------------------------------------------------------
#-------------------------------------------------------------------------------

def consultar_por_fecha(encabezados, m_turnos, mes, mes_palabra,
                         anio, paci, meds, estado_turnos, hora_turnos ):
    """
    Filtra y muestra turnos según la fecha a ingresar.
    
    Parámetros:
        encabezados(list): Lista de encabezados de la matriz de turnos.
        m_turnos(list[list]): Matriz de turnos
        paci(list[list]): Matriz de pacientes.
        meds(list[list]): Matriz de médicos.
        estado_turnos(list)
        hora_turnos(list)
    Returns:
    """
    fecha_cons, dia = elegir_fecha(mes, anio)
    turnos_fecha = filtrar_turnos(m_turnos, fecha_cons )
    if len(turnos_fecha) == 0:
        return print(f"No hay turnos asignados para el dia {dia} {fecha_cons}")
    
    # genero una lista con los médicos con turnos en la fecha consultada
    medicos_fecha = []
    for turno in turnos_fecha:
        if turno[5] not in medicos_fecha:
            medicos_fecha.append(turno[5])
    # print(medicos_fecha)
    # informe
    mostrar_encabezado_consulta("por fecha")
    print("="*80)

    # informo cantidad de turnos de la fecha consultada
    print(f"Cantidad de turnos del {dia} {fecha_cons}: {len(turnos_fecha)} ")

    # informo cantidad de turnos según su estado
    conteos_estados = contar_ocurr_elementos_turnos(turnos_fecha, estado_turnos)
    for i in range(len(conteos_estados)):
        print(f"Cantidad de turnos {conteos_estados[i][0]}: {conteos_estados[i][1]} ")

    # informo franja horaria con mas turnos
    conteos_horarios = contar_ocurr_elementos_turnos(turnos_fecha, hora_turnos)
    # ordeno mi matriz según el horario con más turnos (conteos)
    conteos_horarios.sort(key= lambda fila: fila[1], reverse=True)
    # print(conteos_horarios)
    print(f"Horario mas concurrido {conteos_horarios[0][0]}: {conteos_horarios[0][1]} turnos ")

    # informo médico con mayor cantidad de turnos
    conteos_medicos = contar_ocurr_elementos_turnos(turnos_fecha, medicos_fecha )
    # print(conteos_medicos)
    conteos_medicos.sort(key= lambda fila: fila[1], reverse=True )
    print(f"Médico con mayor cantidad de turnos\
    {devolver_medico(meds, conteos_medicos[0][0])}: {conteos_medicos[0][1]} turnos ")
    print("="*80)
    print(f"Lista completa turnos {dia} {fecha_cons}")
    print("="*80)
    
    leer_turnos(turnos_fecha, encabezados, paci, meds, mes_palabra)

def consultar_por_paciente(encabezados, m_turnos, mes_palabra, paci, meds):
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
    # filtro los turnos del paciente
    turnos_pac_cons = [turno for turno in m_turnos if pac in turno]
    # valido si el paciente no tiene turnos en el mes
    if len(turnos_pac_cons) == 0:
        print(f"El paciente ingresado no posee turnos en el mes de {mes_palabra}")
        input("\nPresione ENTER para volver al menú.")
        return
    # filtro las fecha
    fechas_turnos = []
    
    print("="*80)
    print(f"El paciente {pac} - DNI: {pac} tiene turno en {mes_palabra} las siguientes fechas:")
    

    print("----------------------------------")
    print("[1] Consultar una fecha particular")
    print("[2] Ver todos los turnos")
    print("----------------------------------")
    

    #     # por acá agregaría la función para hacer el informe
    leer_turnos(turnos_pac_cons, encabezados, paci, meds, mes_palabra)

def consultar_por_medico():
    """
    
    
    Parámetros:
    
    Returns:
    """

def consultar_informe_turno_mes():
    """
    
    
    Parámetros:
    
    Returns:

    """
    print("x")

#-------------------------------------------------------------------------------
# FUNCIONES LAMBDA -------------------------------------------------------------
#-------------------------------------------------------------------------------

ordenar_turnos_fecha_horario = lambda mat_turnos: sorted(mat_turnos, 
                              key=lambda 
                              fila:(fila[1], fila[2]))

#-------------------------------------------------------------------------------
# FUNCIONES CREAR LEER CONSULTAR -----------------------------------------------
#-------------------------------------------------------------------------------

def crear_turnos_random(mat_turnos, mes, hora_turnos, tipo_consultas, estado,
                         paci , meds , n_turnos):
    """
    Crea una matriz de turnos al azar.

    Usa las matrices creadas en los módulos pacientes y médicos.
    
    Parámetros:
        mat_turnos(list[list]): Matriz de turnos.
        mes(date): Lista de los días del mes. 
        hora_turnos(list): Lista con los horarios de los turnos.
        tipo_consultas(list): Lista con el tipo de consultas.
        estado(list): Lista de estados.
        paci(list[list]): Matriz de pacientes.
        meds(list[list]): Matriz de médicos.
        n_turnos(int): Número de turnos a generar.

    Returns:
    """
    max_turnos_medicos = len(hora_turnos)
    max_turnos_fecha = max_turnos_medicos * len(meds)
    
    for i in range(n_turnos):
        id = crear_id_turno(mat_turnos)
        consulta = random.choice(tipo_consultas)
        estado_turno = random.choice(estado)

        # valido número de turnos por fecha
        fecha = random.choice(mes)
        mat_turnos_fecha= filtrar_turnos(mat_turnos, fecha)
        while len(mat_turnos_fecha) == max_turnos_fecha:
            fecha = random.choice(mes)

        # valido que no haya superposición de turnos
        medico = random.choice(meds)
        paciente = random.choice(paci)
        hora_turno = random.choice(hora_turnos)
        # validar no tomar los médicos y pacientes con 16 turnos
        turno_valido = validar_turno(mat_turnos, fecha, medico[0], paciente[0], hora_turno)
        while turno_valido == False:
            # como entra en bucle en validar turnos, acá también entra en bucle 
            # cuando pido más de 200 turnos, no sé por qué todavía.
            medico = random.choice(meds)
            paciente = random.choice(paci)
            hora_turno = random.choice(hora_turnos)
            turno_valido = validar_turno(mat_turnos, fecha, medico[0], paciente[0], hora_turno)


        matr_med =  medico[0]                
        especialidad = medico[2]
        dni_pac =  paciente[0]

        mat_turnos.append([id, fecha, hora_turno, dni_pac, especialidad, matr_med, 
                    consulta, estado_turno])

def crear_turno(mat_turnos, hora_turnos, tipo_consultas, 
                paci, meds, mes, mes_palabra, mes_dias, anio):
    """
    Permite la creación de un turno y guardarlo en la matriz de turnos.
    
    Parámetros:
        m_turnos(list[list]): Matriz de turnos.
        hora_turnos(list): Lista con los horarios de los turnos.
        tipo_consultas(list): Lista con el tipo de consultas.
        lists_pac(list): Lista con los datos del paciente.
        meds(list): Lista con los datos del médico.
        mes(int)
        mes_palabra(str)
        mes_dias(int): Cantidad de días del mes.
        anio(int)
    Returns:
    """
    print()
    print("Ingrese paciente")
    # EN ESTA PARTE NECESITARÍA INTEGRAR LA CREACIÓN DE UN PACIENTE ############
    # O LA ELECCIÓN DE UN PACIENTE EXISTENTE
    paciente = random.choice(paci)# simulo ingreso de un paciente
    print(f"Paciente ingresado: {paciente}")
    ############################################################################
    print()
    # seleccionar tipo consulta y especialidad
    tipo_consulta = elgir_consulta_med(tipo_consultas)# ✅
    especialidad = elegir_especialidad_med()# ✅    
    # seleccionar fecha
    fecha_turno, dia_semana = elegir_fecha(mes, anio)# ✅

    # aca una función que valide si el paciente ya tiene un turno 
    # con esa especialidad en esta fecha
    especialidad_valida = validar_turno_por_especialidad(mat_turnos, fecha_turno, # ✅
                                                        especialidad, paciente[0])
    if especialidad_valida == False:
        print("El paciente ya tiene un turno con la especialidad solicitada!")
        return

    # seleccionar médico y hora
    op_medico, horario_turno = elegir_medico(mat_turnos, fecha_turno,# ✅
                                dia_semana, hora_turnos,
                                meds, especialidad)
    # paso final
    # verificación de superpoción de turnos
    turno_valido = validar_turno(mat_turnos, fecha_turno, op_medico,# ✅ 
                                paciente[0], horario_turno)
    if turno_valido == False:
        print("El paciente ya tiene un turno asignado en ese horario")
        return
    
    # no hay superposición procedo a confirmar y a crear
    id = crear_id_turno(mat_turnos)# ✅
    turno = [id, fecha_turno, horario_turno, paciente[0], # ✅
             especialidad, op_medico, tipo_consulta, "Activo"]
    
    confirmacion = confirmar_turno(turno, dia_semana)# ✅

    if confirmacion == False:
        print("CREACION DE TURNO CANCELADO")
        return

    mat_turnos.append(turno)# ✅
    print(f"Turno generado exitosamente!")

def leer_turnos(mat_turnos, encabezados, paci, meds, mes_palabra):
    """
    Leer y imprime matriz de turnos mas encabezado.
    
    Parámetros:
        mat_turnos(list[lis]): Matriz de turnos.
        encabezado(list): Lista de encabezados de la matriz.
        paci(list[list]): Matriz de pacientes.
        meds(list[list]): Matriz de médicos.
        mes_palabra(str)
    Returns:
    """
    # Tendría que ir un encabezado.
    # fun_aux.limpiar_terminal()
    print(f"Lista de turnos del mes de {mes_palabra.upper()}")
    turnos_ordenados = ordenar_turnos_fecha_horario(mat_turnos)

    filas = len(turnos_ordenados)
    columnas = len(turnos_ordenados[0])
    for t in range(columnas):
        match t:
            case 0|2:
                print(f"{encabezados[t]:<7}", end="\t")
            case _:
                print(f"{encabezados[t]:<15}", end="\t")        
    print()
    for i in range(filas):
        # print("-"*107)
        for j in range(columnas):
            match j:
                case 0|2:
                    print(f"{turnos_ordenados[i][j]:<7}", end = "\t")
                case 1:
                    print(f"{str(turnos_ordenados[i][j].strftime("%d/%m/%Y")):<15}", end = "\t")
                case 3:
                    nombre = devolver_paciente(paci,turnos_ordenados[i][j])
                    apellido = nombre.split()[1]
                    print(f"{nombre[:1]}. {apellido}", end = "\t")
                case 5:
                    nombre = devolver_medico(meds,turnos_ordenados[i][j])
                    apellido = nombre.split()[1]
                    print(f"{nombre[:1]}. {apellido:<10}", end = "\t")
                case _:
                    print(f"{turnos_ordenados[i][j]:<15}", end = "\t")
        print()
    
def consultar_turno(encabezados, mat_turnos, mes, mes_palabra, anio, paci, meds, estado, hora):
    """
    
    
    Args:
    
    Returns:
    """
    # mi idea es hacer una salida tipo informe, para cada consulta
    # donde se informe también las métricas. La idea sería seguir el
    # ejemplo del profe con la factura.
    
    while True:
                logo_turnos()
                while True:
                    opciones = 4
                    print()
                    print("------------------------------------------")
                    print("MENÚ PRINCIPAL > TURNOS > CONSULTA > OTRAS")
                    print("------------------------------------------")
                    print("[1] Consulta por fecha")
                    print("[2] Consulta por paciente")
                    print("[3] Consulta por médico")
                    print("[4] Consultar horario más demandado")
                    # print("[5] Consulta x")
                    # print("[6] Consulta x")
                    # print("[7] Consulta x")
                    print("------------------------------------------")
                    print("[0] Volver al menú anterior")
                    print("------------------------------------------")
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
                    consultar_por_fecha(encabezados, mat_turnos, mes, mes_palabra, anio, paci, meds, estado, hora)
                    input("\nPresione ENTER para volver al menú.")
                elif opcion == "2":   # Opción 2
                    consultar_por_paciente(encabezados, mat_turnos, mes_palabra, paci, meds)
                    input("\nPresione ENTER para volver al menú.")
                elif opcion == "3":   # Opción 3
                    print("Consulta por medico")
                    input("\nPresione ENTER para volver al menú.")
                elif opcion == "4":   # Opción 4
                    print("Consulta horario mas demandado")
                    input("\nPresione ENTER para volver al menú.")
                # elif opcion == "5":   # Opción 5
                #     print("Consulta x")
                #     input("\nPresione ENTER para volver al menú.")
                # elif opcion == "6":   # Opción 6
                #     print("Consulta x")
                #     input("\nPresione ENTER para volver al menú.")
                # elif opcion == "7":   # Opción 7
                #     print("Consulta x")
                #     input("\nPresione ENTER para volver al menú.")

# ==============================================================================
# ===============================FUNCION PRINCIPAL==============================
# ==============================================================================

def main_crear_leer(turnos, opcion = 0):
    """
    Función principal del módulo turnos.

    Parámetros:
        turnos(list[list]): Matriz de turnos.
        opcion(int): Opción elegida. Por defecto = 0 para generar turnos random.
        paci[list[list]]: Matriz de pacientes.
        meds[list[list]]: Matriz de médicos.
    """
    #-------------------------------------------------
    # Inicialización de variables necesarias
    #-------------------------------------------------
    ENCABEZADO_TURNOS = ["ID","FECHA", "HORA","PACIENTE","ESPECIALIDAD", "MEDICO","TIPO CONSULTA","ESTADO"]
                                    #ID_PAC     #ID_ESP        #ID_MED
    ESTADO_TURNO = ["Activo", "Cancelado", "Finalizado"]
    CONSULTA = ["Control", "Revisión", "Urgencia"]
    INICIO_TURNOS = datetime(2025, 1, 1, 9,0)# Pongo una fecha cualquiera lo que importa es la hora
    FIN_TURNOS = datetime(2025, 1, 1, 16,0)# Pongo una fecha cualquiera lo que importa es la hora
    N_TURNOS_RANDOM = 100

    # turnos = []
    horario_turnos = crear_horario_atencion(INICIO_TURNOS, FIN_TURNOS)
    mes_completo, mes, mes_en_palabra, anio, cant_dias = crear_mes()# creo las fechas del mes actual y
    # guardo mes y anio

    ### DATOS QUE DEBERIAN LLEGAR, DEBERÍAN SER ARGUMENTOS ###
    medicos_h = [[154892, "Rodolfo Galleguillo", "Traumatología", 15, 1],
            [153167, "Obi Wan Kenobi", "Psiquiatría", 15, 1],
            [123858, "Sanji Vismonke", "Urología", 15, 1],
            [456176, "Tony Chopper", "Clínica Médica", 15, 1],
            [789546, "Piccolo DaimaKu", "Traumatología", 15, 1],
            [456188, "Ruperto Rierea", "Clínica Médica", 15, 1]]
    pacientes_h = [[35023963, "Cosme Fulanito", "Total"],
                [32490932, "Anakin Skywalker", "Copago"],
                [20488909, "Judge Vinsmoke", "Particular"],
                [20101983, "Homero Simpson", "Particular"]]

# PACIENTES: ID, DNI, NOMBRE COMPLETO, EDAD, OBRA SOCIAL, ESTADO

    #-------------------------------------------------
    # Bloque de menú
    #-------------------------------------------------
    fun_aux.limpiar_terminal()
    logo_turnos()
    match opcion:
        case 0:
            crear_turnos_random(turnos, mes_completo, horario_turnos, CONSULTA, ESTADO_TURNO, 
                                pacientes_h, medicos_h, N_TURNOS_RANDOM)
        case 1:
            while True:
                logo_turnos()
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > TURNOS > CREAR TURNO")
                    print("---------------------------")
                    print("[1] Crear turno")
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
                    crear_turno(turnos, horario_turnos, CONSULTA, pacientes_h, medicos_h, mes, mes_en_palabra, cant_dias, anio)
                    input("\nPresione ENTER para volver al menú.")
        case 2:
            while True:
                logo_turnos()
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > TURNOS > CONSULTA")
                    print("---------------------------")
                    print("[1] Consultar todos los turnos")
                    print("[2] Otras consultas")
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
                    leer_turnos(turnos, ENCABEZADO_TURNOS, pacientes_h, medicos_h, mes_en_palabra)
                    input("\nPresione ENTER para volver al menú.")
                    
                    
                elif opcion == "2":   # Opción 2
                    consultar_turno(ENCABEZADO_TURNOS, turnos,mes, mes_en_palabra, anio, pacientes_h, medicos_h, ESTADO_TURNO, horario_turnos)
                    input("\nPresione ENTER para volver al menú.")
                    

