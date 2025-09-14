# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Nicolás Seijo, Victor Maza
# Descripción: Módulo Turnos
# Fecha de creación: 10/08/2025
# ==============================================================================

#-------------------------------------------------------------------------------
#----------------------------- MODULOS DE PYTHON -------------------------------
#-------------------------------------------------------------------------------

import random, calendar, re
from datetime import datetime, date, timedelta

#-------------------------------------------------------------------------------
#---------------------------- MODULOS DEL PROYECTO -----------------------------
#-------------------------------------------------------------------------------

import auxiliares, calendario
from pacientes import crear_paciente

#-------------------------------------------------------------------------------
#---------------------------- FUNCIONES DEL MODULO -----------------------------
#-------------------------------------------------------------------------------


def mostrar_encabezado_consulta(encabezado):


    """
    Mustra encabezado personalizado de consulta.

    Imprime por pantalla el encabezado en MAYÚSCULAS.
    
    Args:
        encabezado(str): Encabezado personalizado.
    
    Returns:
    """
    print("-"*66)
    print(f"MENÚ PRINCIPAL > TURNOS > CONSULTA > OTRAS > {encabezado.upper()}")
    print("-"*66)

def logo_turnos():
    """
    Imprime logo turnos.
    """

    auxiliares.limpiar_terminal()
    print("G6: SISTEMA DE GESTIÓN DE TURNOS")

    print(negrita(r"""
 _____                           
|_   _|   _ _ __ _ __   ___  ___ 
  | || | | | '__| '_ \ / _ \/ __|
  | || |_| | |  | | | | (_) \__ \
  |_| \__,_|_|  |_| |_|\___/|___/
"""))

def ingresar_opcion_elegida(lista_opciones):
    """
    Permite el ingreso de una opción empezando en 1..

    Args:
        lista_opciones(list): Lista con la opciones.
    
    Returns:
        int: Devuelve el índice de la opción.
    """
    opcion = auxiliares.ingresar_respuesta_str("Ingrese el número de opción escogida: ")
    opcion_valida = False
    while opcion_valida  == False:
        # valido que no ingrese letras
        if re.findall("[a-zA-Z]", opcion):
            print("Ingrese una opción válida")
            opcion= auxiliares.ingresar_respuesta_str("")
        elif re.findall("[\s]", opcion) or opcion == "":
            print("Ingrese una opción válida")
            opcion= auxiliares.ingresar_respuesta_str("")
        elif int(opcion) <= 0 or int(opcion) > len(lista_opciones) :
            print("Ingrese una opción válida")
            opcion = auxiliares.ingresar_respuesta_str("")
        else:
            opcion_valida = True
    opcion_elegida = int(opcion)-1
    return opcion_elegida

def elegir_fecha(mes_numero, anio):
    """
    Permite la elección de una fecha para cargar un turno.
    
    Args:
        mes(int)
        anio(int)
    
    Returns:
        date: Fecha seleccionada.
        str: Nombre del día de la fecha seleccionada.
    """
    calendario.calendario_mes(mes_numero, anio)# muestro el calendario del mes
    nombres_dias_semana = ["Domingo", "Lunes", "Martes","Miércoles", 
                    "Jueves", "Viernes","Sábado"]
    # estructura:
    # 6 filas = semanas
    # 7 columnas = dias de la semana
    # [..., 
    # [Domingo, Lunes, Martes, Miercoles, Jueves, Viernes, Sábado],
    # [Domingo, Lunes, Martes, Miercoles, Jueves, Viernes, Sábado],
    # ...]
    print("Seleccione una fecha ingresando el dia")
    dia_ingresado = auxiliares.ingresar_respuesta_str("")
    # atencion, si doy enter no lo toma como \n sino como lista vacia
    dia_valido = False
    while dia_valido == False:
        # valido que no ingrese letras
        if re.findall("[a-zA-Z]", dia_ingresado):
            print("Ingrese una fecha válida")
            dia_ingresado = auxiliares.ingresar_respuesta_str("")
        # valido que no ingrese espacios o lista vacia
        elif re.findall("[\s]", dia_ingresado) or dia_ingresado == "":
            print("Ingrese una fecha válida")
            dia_ingresado = auxiliares.ingresar_respuesta_str("") 
            # acá falta ver como validar que no elija el mas allá del
            # último día del mes actual, puse 31 para hacerlo general
        elif int(dia_ingresado) <= 0 or int(dia_ingresado) > 31 :
            print("Ingrese una fecha válida")
            dia_ingresado = auxiliares.ingresar_respuesta_str("")
        else:
            dia_valido = True
    # saco el dia de la semana y su nombre para que quede mas lindo

    n_dia_semana = calendario.dia_de_la_semana(int(dia_ingresado), mes_numero, anio)

    nombre_dia = nombres_dias_semana[n_dia_semana]

    # paso a tipo date para que despúes puda ordernar con sorted
    # al usar leer_turnos. 
    fecha_seleccionada = date(anio, mes_numero, int(dia_ingresado))

    return fecha_seleccionada, nombre_dia

def elgir_consulta_med(tipos_consultas):
    """
    Permite la elección del tipo de consulta médica.
    
    Args:
        tipos_consultas(list): Lista con los tipos de consultas ofrecidas.
    
    Returns:
        consulta(str)
    """
    print("Seleccione el tipo de consulta del turno")
    print("_"*40)
    print(amarillo(f"{' CONSULTAS OFRECIDAS ':=^40}"))
    auxiliares.imprimir_lista_opciones(tipos_consultas,True)
    seleccion = ingresar_opcion_elegida(tipos_consultas)
    consulta = tipos_consultas[seleccion]
    print()    
    return consulta

def elegir_especialidad_med():
    """
    Permite la elección de la especialidad médica.
    
    Args:
          
    Returns:
        espec(str): Especilidad elegida.
    """
    print("Seleccione el tipo de especialidad médica")

    print("_"*40)
    print(amarillo(f"{' ESPECIALIDADES ':=^40}"))
    auxiliares.imprimir_lista_opciones(auxiliares.especialidades, True)
    seleccion = ingresar_opcion_elegida(auxiliares.especialidades)
    espc = auxiliares.especialidades[seleccion]
    print()    
    return espc  

def elegir_medico(matriz_turnos, fecha_turno, dia_semana, hora_turnos,
                                  matriz_meds, especialidad):
    """
    Permite la elección de un medico disponible. 
    
    Args:
        matriz_turnos(list[list]): Matriz de turnos del mes.
        fecha_turno(date): Fecha seleccionada para el turno.
        dia_semana(str): Nombre del día de la fecha.
        horario_turno(str): Hora del turno seleccionada para el turno.
        matriz_meds(list[list]): Matriz de médicos.
        especialidad(str): Especialidad seleccionada para el turno.
    
    Returns:
    """
    # ya se que el paciente no tiene turno con esta especilidad en este fecha
    # 1 busco las matriculas de todos los medicos de la especialidad requerida
    mat_medicos_especialidad = filtrar_meds_por_especialidad(matriz_meds, especialidad)
    # 2 construyo una matriz con todos los medicos y sus horarios libres
    medicos_turnos_libres = []
    for mat in mat_medicos_especialidad:
        turnos_libres = devolver_turnos_med(matriz_turnos, fecha_turno, mat, hora_turnos)
        medicos_turnos_libres.append(turnos_libres)
    # validación si no hay turnos libres
    # validación si es el primer turno del dia
    # 3 crear el menu de selección
    print(verde(f"Medicos y horarios disponibles parar el {dia_semana} {fecha_turno.strftime("%d/%m/%Y")}"))

    print()
    # transpongo mi matriz de turnos libres
    tras_medicos_turnos_libres = auxiliares.transponer_matriz(medicos_turnos_libres)
    encabezado =  tras_medicos_turnos_libres.pop(0)# me quedo con la lista de matriculas
    # de los médicos
    # imprimo de manera linda la transpuesta
    filas = len(tras_medicos_turnos_libres)
    columnas = len(tras_medicos_turnos_libres[0])# me quedo con las mat de los medicos

    opcion = 0
    for matricula in encabezado:
        opcion += 1
        opciones_de_medicos = f"|| ME - {opcion} || {devolver_medico(matriz_meds, matricula):<15}"
        print(f"{opciones_de_medicos:<15}", end=" || ")
    print()

    op_horario = 0
    for i in range(filas):
        op_horario += 1
        for j in range(columnas):
            opciones_de_horarios = f"|| {op_horario:<7}|| {tras_medicos_turnos_libres[i][j]:<15}"
            print(f"{opciones_de_horarios:<15}", end=" || ")
        print()

    # selecciono medico
    print()
    print(contraste("Seleccione médico"))
    print()
    op_medico = ingresar_opcion_elegida(encabezado) 
    medico_selec = encabezado[op_medico]
    # selecciono hoarario
    print()
    print(contraste("Seleccione horario"))
    print()
    op_horario = ingresar_opcion_elegida(hora_turnos) 
    # si selecciona el horario no disponible necesito un mensaje
    print(hora_turnos[op_horario])
    while re.search("[a-zA-Z]", hora_turnos[op_horario]):
        print("Turno no disponible")
        op_horario = ingresar_opcion_elegida(hora_turnos) 

    horario_selec = hora_turnos[op_horario]

    return medico_selec, horario_selec

def devolver_turnos_med(matriz_turnos, fecha, mat_med, hora_turnos, libres = True):
    """
    Devuelve una lista con los horarios libres del médico en un fecha dada.
    
    Args:
    
    Returns:
    """
    turnos_tomados = []
    turnos_fecha = filtrar_turnos(matriz_turnos, fecha)
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

def filtrar_turnos(matriz_turnos, filtro, inverso = False):
    """
    Filtra turnos según lo solicitado.

    Si inverso True, filtra lo que no coincide.

    Args:
        matriz_turnos(list[list]): Matriz de turnos.
        filtro(str|int|date): Clave de filtrado.
        inverso(bool): Defecto False. 
    
    Returns:
        Matriz de turno filtrada
    """
    turnos_filtrados = []
    if inverso == False:
        for turno in matriz_turnos:
            if filtro in turno:
                turnos_filtrados.append(turno)
    elif inverso == True:
        for turno in matriz_turnos:
            if filtro not in turno:
                turnos_filtrados.append(turno)
    return turnos_filtrados

def filtrar_meds_por_especialidad(matriz_meds, espec):
    """
    Filtra médicos según la especialidad indicada.
    
    Args:
        matriz_meds(list): Lista de médicos.
        espec(str): Nombre de la especialidad a buscar.
    Returns:
        list: Matriculas de médicos filtrados por especialidad.
    """
    mat_meds = []
    for medico in matriz_meds:
        if espec in medico:
            mat_meds.append(medico[0])
    return mat_meds

def filtrar_datos_paciente_por_dni(matriz_pacs, dni_paciente):
    """
    Filtra datos de paciente por dni.
    
    Args:
        matriz_pac(list[list])
        dni_paciente(int)
    
    Returns:
        list: Datos del paciente.
    """
    fila = -1
    for paciente in matriz_pacs:
        if dni_paciente in paciente:
            i = matriz_pacs.index(paciente)
            fila = matriz_pacs[i]
    return fila

def crear_id_turno(matriz_turnos):
    """
    Crea el id de turnos.
    
    Args:
        turnos(list[list]): Matriz de turnos.

    Returns:
        int: Número de id turno
    """
    # TODO: mejorar creando un id informativo pero no muy largo
    # posible idea pasarlo a hexadecimal
    if len(matriz_turnos) == 0:
        id_t = str(1).zfill(6)
        return id_t
    else:
        id_t = str(len(matriz_turnos) + 1).zfill(6)
        return id_t

def crear_horario_atencion(inicio, fin, freq = 30):
    """
    Crea el horario de atención del consultorio.

    Por defecto cada turno de se asigna cada media hora.
    
    Args:
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
    
    Args:
    
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
    
def devolver_paciente(matriz_pacs, dni_paciente):
    """
    Devuelve el nombre del paciente según el DNI.
    
    Args:
        paci(list[list]): Matriz de pacientes.
        dni(int): DNI del paciente a buscar.
    
    Returns:
    """
    buscar = True
    i = 0
    while buscar:
        if matriz_pacs[i][1] == dni_paciente:
            nombre = matriz_pacs[i][2]
            buscar = False
        i += 1
    return nombre
                
def devolver_medico(matriz_meds, mat_med):
    """
    Devuelve el nombre del médicos según la matrícula.
    
    Args:
        matriz_meds(list[list]): Matriz de médicos.
        mat_med(int): Matrícula del médico a buscar.
    
    Returns:
    """
    buscar = True
    i = 0
    while buscar:
        if matriz_meds[i][0] == mat_med:
            nombre = matriz_meds[i][1]
            buscar = False
        i += 1
    return nombre

def validar_turno(matriz_turnos, fecha, mat_med, dni_paciente, especialidad,
                   hora_turno, random = True):
    """
    Valida el turno a asignar.

    Si hay superposición de horarios, superposición de médico y paciente.

    Args:
        matriz_turnos(list[list])
        fecha(date)
        mat_medico(int)
        dni_paciente(int)
        hora_turno(str)
        
    Returns:
        bool: True turno valido, False turno invalido
        str: Mensaje informativo de la validacion
    """
    matriz_turnos_fecha= filtrar_turnos(matriz_turnos, fecha)
    mensaje = ""
    valido = True
    busqueda = True
    turno = 0
    # uso while para no forzar la finalizacion del bucle con un return o break
    while busqueda and turno <= len(matriz_turnos_fecha) - 1:
        # valido superpocion de horario con otro turno del paciente
        if hora_turno in matriz_turnos_fecha[turno] and dni_paciente in matriz_turnos_fecha[turno]:
            valido = False
            mensaje = "El paciente ya tiene un turno en el horario solicitado"
            busqueda = False
        # valido superpocion de horario del medico con otro turno del medico
        elif mat_med in matriz_turnos_fecha[turno] and hora_turno in matriz_turnos_fecha[turno]:
            valido = False
            mensaje = "El médico solicitado no tiene disponible el horario solicitado"
            busqueda = False
        # valido si el paciente ya tiene turno con el medico
        elif mat_med in matriz_turnos_fecha[turno] and dni_paciente in matriz_turnos_fecha[turno]:
            valido = False
            mensaje = "El paciente ya tiene un turno con el médico solicitado"
            busqueda = False
        # valido si el paciente tiene con la especialidad en la misma fecha
        # la idea es usarlo solo en la creacion manual de turnos y no 
        # en la creacion random de turnos. De esa manera simular la posibilidad
        # de dos cosultas de la misma epecialidad distinto horario y médico
        if random == False:
            if especialidad in matriz_turnos_fecha[turno] and dni_paciente in matriz_turnos_fecha[turno]:
                valido = "opcion"
                mensaje = "El paciente ya tiene un turno con la especialidad requerida"
                busqueda = False
        turno += 1    
    
    return valido, mensaje

def confirmar_ingreso_paciente(datos_del_paciente):
    """
    Confirma el ingreso de un paciente devolviendo su información.
    """

    print("----------------------------------")
    print("[ENTER] CONFIRMAR INGRESO PACIENTE")
    print("----------------------------------")
    print("[0]     CANCELAR")
    print("#"*34)
    print(f"{datos_del_paciente[2]} DNI: {datos_del_paciente[1]}"
          f" EDAD: {datos_del_paciente[3]} OBRA SOCIAL: {datos_del_paciente[4]}")
    print("----------------------------------")
    
    op = input("")
    if op == "":
        return True
    else:
        return False

def confirmar_turno(turno_a_confirmar, dia, matriz_pacs, matriz_meds):
    """
    Menu de confirmacion de turnos
    Args:
        turno_a_confirmar(list): Datos del turno a confirmar.
        dia(str): Dia de la semana. 
        matriz_pacs
        matriz_meds
    
    Returns:
        bool: True si es válido.
    """
    print("---------------------------")
    print("[ENTER] CONFIRMAR TURNO")
    print("[0]     CANCELAR")
    print("---------------------------")
    print(f"{devolver_paciente(matriz_pacs, turno_a_confirmar[3])}")
    print(f"{dia} {turno_a_confirmar[1].strftime("%d/%m/%Y")} a las {turno_a_confirmar[2]} hs\
     MEDICO: {devolver_medico(matriz_meds, turno_a_confirmar[5])} - {turno_a_confirmar[4]}")
    op = input("")
    if op == "":
        return True
    else:
        return False

def contar_ocurr_elementos_turnos(matriz_turnos, lista_elementos):
    """
    Devuelve una lista con el conteo de cada elemento en matriz de turnos.
    
    Args:
        matriz_turnos(list[list])
        lista_elementos(list)
    
    Returns:
        list[list[]]
    """
    lista_conteos = []
    for elemento in lista_elementos:
        contador = 0
        for turno in matriz_turnos:
            if elemento in turno:
                contador += 1
        lista_conteos.append([elemento, contador])
    return lista_conteos

#-------------------------------------------------------------------------------
# FUNCIONES DE CONSULTAS -------------------------------------------------------
#-------------------------------------------------------------------------------

def consultar_por_fecha(encabezados, matriz_turnos, mes_numero, mes_palabra,
                         cant_dias_mes, anio, matriz_pacs, matriz_meds,
                           estado_turnos, horarios_atencion ):
    """
    Filtra y muestra turnos según la fecha a ingresar.
    
    Args:
        encabezados(list): Lista de encabezados de la matriz de turnos.
        m_turnos(list[list]): Matriz de turnos
        mes_numero(int)
        mes_palabra(str)
        anio(str)
        matriz_pacs(list[list]): Matriz de pacientes.
        matriz_meds(list[list]): Matriz de médicos.
        estado_turnos(list)
        horarios_turnos(list)
    Returns:
    """
    fecha_cons, dia = elegir_fecha(mes_numero, anio)
    turnos_fecha = filtrar_turnos(matriz_turnos, fecha_cons )
    if len(turnos_fecha) == 0:
        return print(f"No hay turnos asignados para el dia {dia} {fecha_cons}")
    
    # genero una lista con los médicos con turnos en la fecha consultada
    medicos_fecha = []
    for turno in turnos_fecha:
        if turno[5] not in medicos_fecha:
            medicos_fecha.append(turno[5])
    # informe
    mostrar_encabezado_consulta("por fecha")
    print("#"*110)

    # informo cantidad de turnos de la fecha consultada
    print(f"Cantidad de turnos del {dia} {fecha_cons}: {len(turnos_fecha)} ")

    # informo cantidad de turnos según su estado
    conteos_estados = contar_ocurr_elementos_turnos(turnos_fecha, estado_turnos)
    for i in range(len(conteos_estados)):
        print(f"Cantidad de turnos {conteos_estados[i][0]}: {conteos_estados[i][1]} ")

    # informo franja horaria con mas turnos
    conteos_horarios = contar_ocurr_elementos_turnos(turnos_fecha, horarios_atencion)
    # ordeno mi matriz según el horario con más turnos (conteos)
    conteos_horarios.sort(key= lambda fila: fila[1], reverse=True)
    # print(conteos_horarios)
    print(f"Horario mas concurrido {conteos_horarios[0][0]}: {conteos_horarios[0][1]} turnos ")

    # informo médico con mayor cantidad de turnos
    conteos_medicos = contar_ocurr_elementos_turnos(turnos_fecha, medicos_fecha )
    # print(conteos_medicos)
    conteos_medicos.sort(key= lambda fila: fila[1], reverse=True )
    print(f"Médico con mayor cantidad de turnos\
    {devolver_medico(matriz_meds, conteos_medicos[0][0])}: {conteos_medicos[0][1]} turnos ")
    print("#"*110)
    print()
    print("="*110)
    titulo = f" Lista completa turnos {dia} {fecha_cons} "
    print(f"{titulo:=^110}")
    
    leer_turnos(turnos_fecha, encabezados, matriz_pacs, matriz_meds, mes_palabra, cant_dias_mes, horarios_atencion, False)

def consultar_por_paciente(encabezados, matriz_turnos, mes_palabra, cant_dias_mes,
                            horarios_atencion, matriz_pacs, matriz_meds):
    """
    Filtra y muestra turnos según el DNI del paciente.
    
    Args:
        encabezados(list): Lista de encabezados de la matriz de turnos.
        matriz_turnos(list[list]): Matriz de turnos
        paci(list[list]): Matriz de pacientes.
        matriz_meds(list[list]): Matriz de médicos.    
    Returns:
    """
    mostrar_encabezado_consulta("consulta por paciente")
    dni_paci = auxiliares.ingresar_entero_positivo("Ingrese el DNI del paciente: ")
    while len(str(dni_paci)) < 8:
        print("DNI incorrecto, ingrese nuevamente")
        dni_paci = auxiliares.ingresar_entero_positivo("Ingrese el DNI del paciente: ")


    datos_paci = filtrar_datos_paciente_por_dni(matriz_pacs, dni_paci)
    
    # Necesito usar diccionarios para mejorar mis consultas y aplicar mejor
    # la siguiente idea: 
    if datos_paci == -1:
        print(alerta("PACIENTE NO REGISTRADO"))
        print(alerta("DIRIJASE A GESTIÓN PACIENTES"))
        return

    confirmacion = confirmar_ingreso_paciente(datos_paci)

    if confirmacion == False:
        print(alerta("CONSULTA CANCELADA"))
        input("\nPresione ENTER para volver al menú.")
        return
    
    # filtro los turnos del paciente
    turnos_pac_cons = [turno for turno in matriz_turnos if dni_paci in turno]
    # valido si el paciente no tiene turnos en el mes
    if len(turnos_pac_cons) == 0:
        print(f"El paciente ingresado no posee turnos en el mes de {mes_palabra}")
        input("\nPresione ENTER para volver al menú.")
        return
    # filtro las fecha
    fechas_turnos = []
    for turno in turnos_pac_cons:
        if turno[1] not in fechas_turnos:
            fechas_turnos.append(turno[1])
    
    print("="*110)
    print(f"El paciente {devolver_paciente(matriz_pacs,dni_paci)} -"
          f" DNI: {dni_paci} tiene {len(fechas_turnos)} turnos en {mes_palabra}")

    leer_turnos(turnos_pac_cons, encabezados, matriz_pacs, matriz_meds,
                 mes_palabra, cant_dias_mes, horarios_atencion, False)

def realizar_metricas_matriz_turnos(matriz_turnos, cant_dias_mes,
                                     horarios_turnos, mes_palabra):
    """
    Realiza e imprime métrica sencillas de los turnos del mes dado.
    
    Args:
        matriz_turnos(list(list))
        dias_mes(int)
        horarios_turnos(list)
        mes_palabra(str)
    """
    # metricas
    numero_turnos_mes = len(matriz_turnos)
    promedio_turnos_por_dia = round(numero_turnos_mes/cant_dias_mes, 2)
    demanda_mes_horarios = contar_ocurr_elementos_turnos(matriz_turnos, 
                                                         horarios_turnos)
    demanda_mes_horarios.sort(key=lambda fila: fila[1], reverse=True)
    horario_mas_demandado = demanda_mes_horarios[0][0]
    promedio_turnos_horario_mas_demandado = round(demanda_mes_horarios[0][1] / cant_dias_mes, 2)
    horario_menos_demandado = demanda_mes_horarios[-1][0]
    promedio_turnos_horario_menos_demandado = round(demanda_mes_horarios[-1][1] / cant_dias_mes, 2)

    # salida por pantalla
    ancho = 110
    print("="*ancho)
    titulo = f" INFORME GENERAL TURNOS MES DE {mes_palabra.upper()} "
    linea = f"{titulo:^{ancho}}"
    print(f"{azul_negrita(linea):}")
    print("="*ancho)
    print(negrita(f"Número de turnos del mes: {numero_turnos_mes}'"))
    print(negrita(f"Promedio turnos por día: {promedio_turnos_por_dia}"))
    print(negrita(f"Horario mas demandado del mes: {horario_mas_demandado}\t"
            f"Promedio turnos por día: {promedio_turnos_horario_mas_demandado}"))
    print(negrita(f"Horario menos demandado del mes: {horario_menos_demandado}\t"
            f"Promedio turnos por día: {promedio_turnos_horario_menos_demandado}"))
    print("="*ancho)
#-------------------------------------------------------------------------------
# FUNCIONES LAMBDA -------------------------------------------------------------
#-------------------------------------------------------------------------------

ordenar_turnos_fecha_horario = lambda matriz_turnos: sorted(matriz_turnos, 
                              key=lambda 
                              fila:(fila[1], fila[2]))
# colores
negrita = lambda texto:f"\033[1m{texto}\033[0m"
rojo = lambda texto:f"\033[31m{texto}\033[0m"
verde= lambda texto:f"\033[32m{texto}\033[0m"
amarillo = lambda texto:f"\033[33m{texto}\033[0m"
azul_negrita = lambda texto:f"\033[1;34m{texto}\033[0m"
azul = lambda texto:f"\033[34m{texto}\033[0m"
alerta = lambda texto:f"\033[37;41m{texto}\033[0m"
cyan_fondo_blanco = lambda texto:f"\033[36;40m{texto}\033[0m"
contraste = lambda texto:f"\033[7m{texto}\033[0m"

#-------------------------------------------------------------------------------
# FUNCIONES CREAR LEER CONSULTAR -----------------------------------------------
#-------------------------------------------------------------------------------

def crear_turnos_random(matriz_turnos, mes_completo, horarios_atencion, 
                        tipo_consultas, estado, matriz_pacs,
                          matriz_meds , n_turnos):
    """
    Crea una matriz de turnos al azar.

    Usa las matrices creadas en los módulos pacientes y médicos.
    
    Args:
        matriz_turnos(list[list]): Matriz de turnos.
        mes_completo(list[date]): Lista de los días del mes. 
        horarios_atencion(list): Lista con los horarios de los turnos.
        tipo_consultas(list): Lista con el tipo de consultas.
        estado(list): Lista de estados.
        paci(list[list]): Matriz de pacientes.
        matriz_meds(list[list]): Matriz de médicos.
        n_turnos(int): Número de turnos a generar.

    Returns:
    """
    max_turnos_medicos = len(horarios_atencion)
    max_turnos_fecha = max_turnos_medicos * len(matriz_meds)
    
    for i in range(n_turnos):
        # print("ACAAAA")
        consulta = random.choice(tipo_consultas)
        estado_turno = random.choice(estado)

        # valido número de turnos por fecha
        fecha = random.choice(mes_completo)
        matriz_turnos_fecha= filtrar_turnos(matriz_turnos, fecha)
        while len(matriz_turnos_fecha) == max_turnos_fecha:
            fecha = random.choice(mes_completo)

        # valido que no haya superposición de turnos
        medico = random.choice(matriz_meds)# fila de la matriz
        matricula_med = medico[0]
        paciente = random.choice(matriz_pacs)# fila de la matriz
        dni_pac = paciente[1]
        hora_turno = random.choice(horarios_atencion)# un horario
        especialidad = medico[2]
        turno_valido, mensaje = validar_turno(matriz_turnos, fecha, matricula_med , dni_pac,especialidad, hora_turno)
        while turno_valido == False:
            medico = random.choice(matriz_meds)
            matricula_med = medico[0]
            paciente = random.choice(matriz_pacs)
            dni_pac = paciente[1]
            hora_turno = random.choice(horarios_atencion)
            turno_valido, mensaje = validar_turno(matriz_turnos, fecha, matricula_med, dni_pac,especialidad, hora_turno)

        id = crear_id_turno(matriz_turnos)
        matriz_turnos.append([id, fecha, hora_turno, dni_pac, especialidad, matricula_med, 
                    consulta, estado_turno])

def crear_turno(matriz_turnos, horarios_atencion, tipo_consultas, 
                matriz_pacs, matriz_meds, mes_numero, anio):
    """
    Permite la creación de un turno y guardarlo en la matriz de turnos.
    
    Args:
        matriz_turnos(list[list]): Matriz de turnos.
        horarios_atencion(list): Lista con los horarios de los turnos.
        tipo_consultas(list): Lista con el tipo de consultas.
        matriz_pacs(list): Lista con los datos del paciente.
        matriz_meds(list): Lista con los datos del médico.
        mes(int)
        anio(int)
    Returns:
    """
    print("Ingrese paciente")
    # TODO: EN ESTA PARTE NECESITARÍA INTEGRAR LA CREACIÓN DE UN PACIENTE 
    # O LA ELECCIÓN DE UN PACIENTE EXISTENTE
    paciente = random.choice(matriz_pacs)# simulo ingreso de un paciente
    print(f"Paciente ingresado: {paciente}")
    ############################################################################
    print()
    # seleccionar tipo consulta y especialidad
    tipo_consulta = elgir_consulta_med(tipo_consultas)# ✅
    especialidad = elegir_especialidad_med()# ✅    
    # seleccionar fecha
    fecha_turno, dia_semana = elegir_fecha(mes_numero, anio)# ✅

    # seleccionar médico y hora
    op_medico, horario_turno = elegir_medico(matriz_turnos, fecha_turno,# ✅
                                dia_semana, horarios_atencion,
                                matriz_meds, especialidad)
    # paso final
    # verificación de superpoción de turnos
    turno_valido, mensaje = validar_turno(matriz_turnos, fecha_turno, op_medico,
                                paciente[1],especialidad, horario_turno)
    while turno_valido == False:
        print(mensaje)
        # seleccionar médico y hora
        op_medico, horario_turno = elegir_medico(matriz_turnos, fecha_turno,
                                    dia_semana, horarios_atencion,
                                    matriz_meds, especialidad)
        # paso final
        # verificación de superpoción de turnos
        turno_valido, mensaje = validar_turno(matriz_turnos, fecha_turno, op_medico,
                                    paciente[1],especialidad, horario_turno)
        
    # if turno_valido == "opcion":# TODO: para implementar
    #   # recordar que en validar turno debo poner False para que funcione
    #     print("Acá debe ir la opcion de elegir turno con la misma especialidad")
    #     input("\nPresione ENTER para volver al menú.")
    
    # no hay superposición procedo a confirmar y a crear
    id = crear_id_turno(matriz_turnos)
    turno = [id, fecha_turno, horario_turno, paciente[1], 
             especialidad, op_medico, tipo_consulta, "Activo"]
    
    confirmacion = confirmar_turno(turno, dia_semana, matriz_pacs, matriz_meds)

    if confirmacion == False:
        print("CREACION DE TURNO CANCELADO")
        input("\nPresione ENTER para volver al menú.")
        return

    matriz_turnos.append(turno)
    print(f"Turno generado exitosamente!")

def leer_turnos(matriz_turnos, encabezados, matriz_pacs, matriz_meds,
                 mes_palabra, cant_dias_mes, horarios_atencion, encabe = True):
    """
    Leer y imprime matriz de turnos mas encabezado.
    
    Args:
        matriz_turnos(list[lis]): Matriz de turnos.
        encabezado(list): Lista de encabezados de la matriz.
        matriz_pacs(list[list]): Matriz de pacientes.
        matriz_meds(list[list]): Matriz de médicos.
        mes_palabra(str)
        cant_dia_mes(int)
        horarios_de_atencion(list[list])
        encabe(bool)
    Returns:
    """
    ancho = 110
    print()
    if encabe:
        realizar_metricas_matriz_turnos(matriz_turnos, cant_dias_mes, 
                                        horarios_atencion, mes_palabra)
        print("="*ancho)
        titulo = f" Lista de turnos del mes de {mes_palabra.upper()} "
        print(azul_negrita(f"{titulo:=^{ancho}}"))
    turnos_ordenados = ordenar_turnos_fecha_horario(matriz_turnos)

    filas = len(turnos_ordenados)
    columnas = len(turnos_ordenados[0])
    print("="*ancho)
    for t in range(columnas):
        match t:
            case 0:# id
                print("|"+negrita(f"{encabezados[t]:^7}"), end="||")
            case 1:# fecha
                print(negrita(f"{encabezados[t]:^12}"), end="||")
            case 2:# hora
                print(negrita(f"{encabezados[t]:^7}"), end="||")
            # case 3:# paciente
            #     print(negrita(f"{encabezados[t]:^14}"), end="||")
            # case 4:# especialidad
            #     print(negrita(f"{encabezados[t]:^14}"), end="||")
            case 6:# consulta
                print(negrita(f"{encabezados[t]:^12}"), end="||")
            case 7:# estado
                print(negrita(f"{encabezados[t]:^14}"), end="|")   
            case _:
                print(negrita(f"{encabezados[t]:^14}"), end="||")
    print()        
    print("="*ancho)
    for i in range(filas):
        # print("-"*107)
        for j in range(columnas):
            match j:
                case 0:# ID
                    print(f"|{turnos_ordenados[i][j]:<7}", end = "||")
                case 1:# FECHA que salga formateado y que no ocupe tanto espacio

                    print(f"{turnos_ordenados[i][j].strftime("%d/%m/%Y"):^12}", end = "||")
                case 2:# HORA  que no ocupen tanto espacio
                    print(f"{turnos_ordenados[i][j]:^7}", end = "||")
        
                case 3:# PACIENTE que muestre el nombre del paciente en lugar del DNI
                    # aca esta todo el nombre completo!
                    nombre_completo = devolver_paciente(matriz_pacs,turnos_ordenados[i][j])
                    apellido = nombre_completo.split()[1]# separo apellido
                    nombre_final = " " +nombre_completo[:1] + ". " + apellido
                    print(f"{nombre_final:<14}", end = "||")# me quedo con la inicial
                case 4:# ESPECIALIDAD 
                    print(' '+f"{turnos_ordenados[i][j][:8]:<13}", end = "||")
                case 5:# MEDICO que muestre el nombre del medico en lugar de su id|matricula
                    # aca esta todo el nombre completo!
                    nombre_completo = devolver_medico(matriz_meds,turnos_ordenados[i][j])
                    apellido = nombre_completo.split()[1]# separo apellido
                    nombre_final = " " +  nombre_completo[:1] + ". " + apellido
                    print(f"{nombre_final:<14}", end = "||")# me quedo con la inicial
                case 6:# TIPO CONSULTA 
                    print(' '+f"{turnos_ordenados[i][j]:<11}", end = "||")
                case 7:
                    if turnos_ordenados[i][j].lower() == "activo":
                        print(verde(f"{turnos_ordenados[i][j]:^14}"), end = "|")
                    if turnos_ordenados[i][j].lower() == "finalizado":
                        print(azul(f"{turnos_ordenados[i][j]:^14}"), end = "|")
                    if turnos_ordenados[i][j].lower() == "cancelado":
                        print(rojo(f"{turnos_ordenados[i][j]:^14}"), end = "|")
        print()
    print("="*ancho)

def consultar_turno(encabezados, matriz_turnos, mes_numero,
                     mes_palabra, cant_dias_mes, anio, matriz_pacs,
                       matriz_meds, estado, horarios_atencion):
    """
    Funcion principal de consulta de turnos
    
    Args:
        encabezados(list): Lista de encabezados de datos.
        matriz_turnos(list[list])
        mes_numero(int)
        mes_palabra(str)
        anio(int)
        matriz_pacs(list[list])
        matriz_meds(list[list])
        estado(str)
        hora(str)
    """
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
                    consultar_por_fecha(encabezados, matriz_turnos, mes_numero, mes_palabra, cant_dias_mes, anio, matriz_pacs, matriz_meds, estado, horarios_atencion)
                    input("\nPresione ENTER para volver al menú.")
                elif opcion == "2":   # Opción 2
                    consultar_por_paciente(encabezados, matriz_turnos, mes_palabra,cant_dias_mes, horarios_atencion, matriz_pacs, matriz_meds)
                    input("\nPresione ENTER para volver al menú.")

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
    # Inicialización de variables necesarias
    #-------------------------------------------------
    ENCABEZADO_TURNOS = ["ID","FECHA", "HORA","PACIENTE","ESPECIALIDAD", "MEDICO","CONSULTA","ESTADO"]
    ESTADO_TURNO = ["Activo", "Cancelado", "Finalizado"]
    CONSULTA = ["Control", "Revisión", "Urgencia"]
    # Pongo una fecha cualquiera lo que importa es la hora
    INICIO_TURNOS = datetime(2025, 1, 1, 9,0)
    # Pongo una fecha cualquiera lo que importa es la hora
    FIN_TURNOS = datetime(2025, 1, 1, 16,0)
    N_TURNOS_RANDOM = 10
    horarios_atencion = crear_horario_atencion(INICIO_TURNOS, FIN_TURNOS)
    # creo las fechas del mes actual y guardo su informacion
    mes_completo, mes_numero, mes_palabra, anio, cant_dias_mes = crear_mes()

    #-------------------------------------------------
    # Bloque de menú
    #-------------------------------------------------
    auxiliares.limpiar_terminal()
    logo_turnos()
    match opcion:
        case 0:
            crear_turnos_random(matriz_turnos, mes_completo, horarios_atencion,
                                 CONSULTA, ESTADO_TURNO, matriz_pacs,
                                   matriz_meds, N_TURNOS_RANDOM)
        case 1:
            while True:
                logo_turnos()
                while True:
                    opciones = 4
                    print()
                    print("-------------------------------------")
                    print("MENÚ PRINCIPAL > TURNOS > CREAR TURNO")
                    print("-------------------------------------")
                    print("[1] Crear turno")
                    print("-------------------------------------")
                    print("[0] Volver al menú anterior")
                    print("-------------------------------------")
                    print()
                    
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
                    crear_turno(matriz_turnos, horarios_atencion, CONSULTA,
                                 matriz_pacs, matriz_meds, mes_numero, anio)
                    input("\nPresione ENTER para volver al menú.")
        case 2:
            while True:
                logo_turnos()
                while True:
                    opciones = 4
                    print()
                    print("-------------------------------------")
                    print("MENÚ PRINCIPAL > TURNOS > CONSULTA")
                    print("-------------------------------------")
                    print("[1] Consultar todos los turnos")
                    print("[2] Otras consultas")
                    print("-------------------------------------")
                    print("[0] Volver al menú anterior")
                    print("-------------------------------------")
                    print()
                    
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
                    leer_turnos(matriz_turnos, ENCABEZADO_TURNOS, matriz_pacs,
                                matriz_meds, mes_palabra, cant_dias_mes,
                                horarios_atencion)
                    input("\nPresione ENTER para volver al menú.")
                    
                elif opcion == "2":   # Opción 2
                    consultar_turno(ENCABEZADO_TURNOS, matriz_turnos, mes_numero,
                                    mes_palabra, cant_dias_mes, anio, matriz_pacs,
                                    matriz_meds, ESTADO_TURNO, horarios_atencion)
                    input("\nPresione ENTER para volver al menú.")
                    

