# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Nicolás Seijo, Victor Maza
# Descripción: Módulo Turnos
# Fecha de creación: 10/08/2025
# ==============================================================================

#-------------------------------------------------------------------------------
#----------------------------- MODULOS DE PYTHON -------------------------------
#-------------------------------------------------------------------------------

import random, re
from datetime import date
import json

#-------------------------------------------------------------------------------
#---------------------------- MODULOS DEL PROYECTO -----------------------------
#-------------------------------------------------------------------------------

import auxiliares, calendario, turnos
from pacientes import crear_paciente

#-------------------------------------------------------------------------------
#---------------------------- FUNCIONES DEL MODULO -----------------------------
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# FUNCIONES GENERALES ----------------------------------------------------------
#-------------------------------------------------------------------------------

def mostrar_encabezado_consulta(encabezado):#✅
    """
    Muestra encabezado personalizado de consulta.

    Imprime por pantalla el encabezado en MAYÚSCULAS.
    
    Args:
        encabezado(str): Encabezado personalizado.
    
    Returns:
    """
    print("-"*66)
    print(f"MENÚ PRINCIPAL > TURNOS > CONSULTA > OTRAS > {encabezado.upper()}")
    print("-"*66)

def logo_turnos():#✅
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

def crear_id_turno(matriz_turnos):#✅
    """
    Crea el id de turnos.
    
    Args:
        turnos(list[dic]): Matriz de turnos.

    Returns:
        int: Número de id turno
    """
    # posible idea pasarlo a hexadecimal
    if len(matriz_turnos) == 0:
        id_t = str(1).zfill(6)
        return id_t
    # el indice de la ultima posición coincide con el id porque empece en 1 y no en 0
    else:
        id_t = str(len(matriz_turnos) + 1).zfill(6)
        return id_t

def ingresar_opcion_elegida(lista_opciones):# TODO: Funciona bien pero refactorizar para que quede mejor.✅
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

def ingresar_dni_paciente():#✅
    """
    Permite el ingreso valido del dni de un paciente

    Returns:
        int
    """
    dni_paci = auxiliares.ingresar_entero_positivo("Ingrese el DNI del paciente: ")
    while len(str(dni_paci)) < 8:
        print("DNI incorrecto, ingrese nuevamente")
        dni_paci = auxiliares.ingresar_entero_positivo("Ingrese el DNI del paciente: ")
    return dni_paci

def ingresar_paciente(matriz_pacs, rnd):
    """
    Permite el ingreso de un paciente.

    Devuelve los datos paciente ingresado.
    
    Args:
        matriz_pacs(list[list]): Matriz de pacientes.
    
    Returns:
        datos_paciente(dic): Datos del paciente
    """
    print("Ingrese paciente")
    # TODO: EN ESTA PARTE NECESITARÍA INTEGRAR LA CREACIÓN DE UN PACIENTE
    # O LA ELECCIÓN DE UN PACIENTE EXISTENTE. HACER UN MENU
    # datos_paciente = crear_paciente()
    datos_paciente = random.choice(matriz_pacs)# simulo ingreso de un paciente
    
    return datos_paciente

def validar_turno(matriz_turnos, datos_turno, rnd = True):#✅
    """
    Valida el turno a asignar.

    Si hay superposición de horarios, superposicion de medico y paciente.

    Args:
        matriz_turnos(list[list])
        neuvo_turno(dic)
        
    Returns:
        bool: True turno valido, False turno invalido
        str: Mensaje informativo de la validacion
    """
    matriz_turnos_fecha= filtrar_turnos(matriz_turnos, datos_turno['fecha'], 'fecha')
    mensaje = ""
    valido = True
    busqueda = True
    turno = 0
    # uso while para no forzar la finalizacion del bucle con un return o break
    while busqueda and turno <= len(matriz_turnos_fecha) - 1:
        # valido superpocion de horario con otro turno del paciente
        if (datos_turno.get('hora') == matriz_turnos_fecha[turno].get('hora')and
            datos_turno.get('paciente') == matriz_turnos_fecha[turno].get('paciente')):
            valido = False
            mensaje = "El paciente ya tiene un turno en el horario solicitado"
            busqueda = False
        # valido superpocion de horario del medico con otro turno del medico
        elif (datos_turno.get('medico') == matriz_turnos_fecha[turno].get('medico')and
              datos_turno.get('hora') == matriz_turnos_fecha[turno].get('hora')):
            valido = False
            mensaje = "El médico solicitado no tiene disponible el horario solicitado"
            busqueda = False
        # valido si el paciente ya tiene turno con el medico
        elif (datos_turno.get('medico') == matriz_turnos_fecha[turno].get('medico')and
              datos_turno.get('paciente') == matriz_turnos_fecha[turno].get('paciente')):
            mensaje = "El paciente ya tiene un turno con el médico solicitado"
            valido = False
            busqueda = False
        # aviso mediante un error tipo warnig mas de un turno con la misma especialidad
        if rnd == False:
            if (datos_turno.get('especialidad_medica') == matriz_turnos_fecha[turno].get('especialidad_medica') and
                datos_turno.get('paciente') == matriz_turnos_fecha[turno].get('paciente')):
                raise Warning("El paciente ya tiene un turno con la especialidad requerida")
        turno += 1    

    return valido, mensaje

def contar_ocurr_valor_turnos(matriz_turnos, clave, lista_valores):#✅
    """
    Devuelve una lista con el conteo de cada valor en matriz de turnos.
    
    Args:
        matriz_turnos(list[dic])
        clave(str)
        lista_valores(list)
    
    Returns:
        list[list[]]
    """
    lista_conteos = []
    for valor in lista_valores:
        coincidencias = list(filter(lambda turno: turno[clave] == valor , matriz_turnos))
        ocurrencias = len(coincidencias)
        lista_conteos.append([valor, ocurrencias]) 

    return lista_conteos

def mostrar_nombre_corto_persona(nombre_completo):
    """
    Formatea la salida por pantalla del nombre de una persona.
    
    Args:
        nombre_completo(str)
    
    Returns:
        str
    """
    apellido = nombre_completo.split()[1]# separo apellido
    nombre_final = " " +nombre_completo[:1] + ". " + apellido

    return nombre_final

def mostrar_estado_turno(estado, alineacion):
    """
    Formatea la salida por pantalla del estado del turno.
    
    Args:
        estado(str)
    
    Returns:
        estado del turno formateado para imprimir por pantalla.
    """
    if estado == auxiliares.estado_turno.get('activo'):
        estado_turno = verde(f"{estado:^{alineacion}}")
    elif estado == auxiliares.estado_turno.get('finalizado'):
        estado_turno = azul(f"{estado:^{alineacion}}")
    elif estado == auxiliares.estado_turno.get('cancelado'):
        estado_turno = rojo(f"{estado:^{alineacion}}")
    return estado_turno 

#-------------------------------------------------------------------------------
# FUNCIONES FILTROS-BUSQUEDAS --------------------------------------------------
#-------------------------------------------------------------------------------

def filtrar_turnos(matriz_turnos, filtro, key_filtro, inverso = False): #✅
    """
    Filtra turnos según lo solicitado.

    Si inverso True, filtra lo que no coincide.

    Args:
        matriz_turnos(list[dic]): Matriz de turnos.
        filtro(str|int|date): Value del filtro.
        key_filtro(str): Key del filtro.
        inverso(bool): Defecto False. 
    
    Returns:
        Matriz de turno filtrada
    """
    if inverso == False:
        turnos_filtrados = list(filter(lambda turno: turno.get(key_filtro) 
                                       == filtro ,matriz_turnos))
    elif inverso == True:
        turnos_filtrados = list(filter(lambda turno: turno.get(key_filtro) 
                                       != filtro ,matriz_turnos))
    return turnos_filtrados

def filtrar_meds_por_especialidad(matriz_meds, espec):#✅
    """
    Filtra medicos segun la especialidad indicada.
    
    Args:
        matriz_meds(list[dic]): Lista de medicos.
        espec(str): Nombre de la especialidad a buscar.
    Returns:
        list: Matriculas de medicos filtrados por especialidad.
    """
    mat_meds = [medico['ID'] for medico in matriz_meds if espec == medico['espec']]
    # aca uso directamente la clave, dado que yo se que existe, sino fuera asi
    # me convendria usar el metodo .get para un mejor manejo de posibles errores
    return mat_meds

def filtrar_personas_por_dato(lista_personas, key, valor):#✅
    """
    Filtra los datos de una persona segun una key y su valor.
    
    Args:
        lista_personas(list(dic))
        key(str): Key del dato de filtro.
        valor(str,int): Valor de filtro
    
    Returns:
        dic: Datos de las persona filtrada.
    """

    lista_valores_personas = obtener_lista_dic_value(lista_personas, key)

    if valor in lista_valores_personas:
        indice_fila = lista_valores_personas.index(valor)
        persona = lista_personas[indice_fila]
        return persona
    else:
        raise Warning('Persona no encontrada')

def devolver_turnos_med(matriz_turnos, mat_med, fecha, hora_turnos, libres = True):#✅
    """
    Devuelve una lista con los horarios del medico en un fecha dada.
    
    Args:
        matriz_turnos(list[dic])
        matricula_medico(str)
        fecha(date)
        horas_turnos(list[str]): Horarios de atencion
        libres(bool): True para devolver turnos libre. False, los tomados.
    
    Returns:
        Diccionario con lista de horarios del medico.
    """
    turnos_fecha = filtrar_turnos(matriz_turnos, fecha, 'fecha')
    horarios_tomados = [turno['hora'] for turno in turnos_fecha if turno['medico'] == mat_med ]
    horarios_tomados.sort()

    # turnos libres        
    if libres:
        hoarios_libres = []
        hoarios_libres = [hora_turno if hora_turno not in horarios_tomados 
                         else "No disp." for hora_turno in hora_turnos]
        turnos_medico = {mat_med: hoarios_libres}
        return turnos_medico
    
    turnos_medico = {mat_med: horarios_tomados}    
    return turnos_medico

def obtener_turnos_libres_medicos(matriz_turnos, matriz_meds, especialidad, fecha_turno):#✅
    """
    Devuelve los horarios libres de medicos según especialidad indicada.
    
    Args:
        matriz_turnos(list[dic])
        matriz_meds(list[dic])
        especialidad(str)
        fecha_turno(str)
    
    Returns:
        Lista de diccionarios con medicos y sus horarios libres
    """
    horarios_atencion = auxiliares.crear_horario_atencion()

    matriculas_medicos_especialidad = filtrar_meds_por_especialidad(matriz_meds, especialidad)#✅

    medicos_horarios_libres = []
    for matricula in matriculas_medicos_especialidad:
        horarios_libres = devolver_turnos_med(matriz_turnos, matricula, fecha_turno, horarios_atencion)
        medicos_horarios_libres.append(horarios_libres)

    return medicos_horarios_libres

def devolver_nombre_persona(lista_personas, id_persona, id_key):# TODO: Para completar, pero debería funcionar bien.✅
    """
    Devuelve el nombre de una persona según el id dado.
    
    Args:
        lista_diccionario(list(dic))
        id_persona(int)
    
    Returns:
        (str): Nombre de la persona
    """
    lista_id_personas = obtener_lista_dic_value(lista_personas, id_key)
    if id_persona in lista_id_personas:
        indice_fila = lista_id_personas.index(id_persona)
        nombre_persona = lista_personas[indice_fila]['nombre']# Este key tiene que ser igual para medicos y pacientes.

        return nombre_persona
    # Acá tiene que ir un try/except

def obtener_lista_dic_value(lista_diccionarios ,key):
    """
    Obtiene una lista de valores de la key indicada
    
    Args:
        lista_diccionarios(list[dic])
        key(str): Key de los valores a buscar.
    
    Returns:
        lista_valores(list): Lista de valores de la key indicada.
    """
    mensaje = "No existe el dato buscado"
    lista_valores = [diccionario.get(key, mensaje) for diccionario in lista_diccionarios]

    return lista_valores

def obtener_datos_turnos(matriz_turnos, matriz_pacs, matriz_meds, info_mes, rnd):
    """
    Obtiene y valida datos para genera un turno.
    
    Args:
        matriz_turnos(list[dic]): Matriz de turnos.
        matriz_pacs(list[dic]): Matriz de pacientes.
        matriz_meds(list[dic]): Matriz de medicos.
        info_mes(dic): Datos del mes.
    
    Returns:
    """
    datos_paciente = ingresar_paciente(matriz_pacs, rnd)# rnd va a servir para diferenciar si creo random o pido ingreso de paciente
    print(f"Paciente ingresado: {datos_paciente}")
    dni_paciente = datos_paciente['dni']
    consulta = elgir_consulta_med()
    especialidad_medico = elegir_especialidad_med()
    fecha, dia_semana = elegir_fecha(info_mes['mes_en_numero'], info_mes['anio'])

    # seleccionar médico y hora
    
    try:
        matricula_medico, hora_turno = elegir_medico(matriz_turnos, matriz_meds,
                                                        especialidad_medico,
                                                        fecha, dia_semana)
    except TypeError as mensaje_error:
        auxiliares.limpiar_terminal()
        print(mensaje_error)
        auxiliares.ingresar_respuesta_str('Presione enter para empezar de nuevo')
        # uso recursividad!
        # el dominio va cambiando porque se elige otras opciones
        # el caso base es cuando no entra en el except, ejecuta la función y devuelve la
        # (datos_turno, dia_semana) a las llamadas recursivas
        # cuando llega a la ultima devuelve la tupla validada 
        # a la funcion crear_turno que es la que llama originalmente
        return obtener_datos_turnos(matriz_turnos, matriz_pacs, matriz_meds, info_mes, rnd)
        
    estado_turno = auxiliares.estado_turno['activo']
    datos_turno = {'fecha':fecha,
                'hora':hora_turno,
                'paciente':dni_paciente,
                'especialidad_medica':especialidad_medico,
                'medico':matricula_medico,
                'tipo_consulta':consulta,
                'estado_turno':estado_turno}

    # verificación de superpoción de turnos
    try:
        datos_valido, mensaje = validar_turno(matriz_turnos, datos_turno)
        while datos_valido == False:
            print(mensaje)
            auxiliares.ingresar_respuesta_str('Presione enter para continuar ')
            matricula_medico, hora_turno = elegir_medico(matriz_turnos, matriz_meds,
                                                    especialidad_medico,
                                                    fecha, dia_semana)
            datos_turno.update({'medico':matricula_medico, 'hora':hora_turno})
            datos_valido, mensaje = validar_turno(matriz_turnos, datos_turno)
    except Warning as alerta:
        print(alerta)
        auxiliares.ingresar_respuesta_str('Presione enter para continuar ')
        return datos_turno, dia_semana
    
    return datos_turno, dia_semana

def obtener_datos_turnos_random(matriz_turnos, matriz_meds, matriz_pacs,
                                info_mes):
    """
    Obtiene y valida datos randoms para genera un turno.
    
    Args:
        matriz_turnos(list[dic]): Matriz de turnos.
        matriz_pacs(list[dic]): Matriz de pacientes.
        matriz_meds(list[dic]): Matriz de medicos.
        info_mes(dic): Datos del mes.
    
    Returns:
    """                  
    horarios_atencion = auxiliares.crear_horario_atencion()
    
    consulta = random.choice(list(auxiliares.tipo_consulta.values()))
    estado_turno = random.choice(list(auxiliares.estado_turno.values()))
    fecha = random.choice(list(info_mes['fechas']))
    hora_turno = random.choice(horarios_atencion)
    matricula_medico = random.choice(obtener_lista_dic_value(matriz_meds, 'ID'))
    especialidad_medico = random.choice(obtener_lista_dic_value(matriz_meds, 'espec'))
    dni_paciente = random.choice(obtener_lista_dic_value(matriz_pacs, 'dni'))
    
    datos_turno = {'fecha':fecha,
                'hora':hora_turno,
                'paciente':dni_paciente,
                'especialidad_medica':especialidad_medico,
                'medico':matricula_medico,
                'tipo_consulta':consulta,
                'estado_turno':estado_turno}

    datos_valido, mensaje = validar_turno(matriz_turnos, datos_turno)
        
    return datos_valido, datos_turno

#-------------------------------------------------------------------------------
# FUNCIONES CON MENU -----------------------------------------------------------
#-------------------------------------------------------------------------------

def elegir_fecha(mes_numero, anio):# TODO: Funciona bien pero refactorizar para que quede mejor.✅
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
            # TODO: acá falta ver como validar que no elija el mas allá del
            # último día del mes actual, puse 31 para hacerlo general
        elif int(dia_ingresado) <= 0 or int(dia_ingresado) > 31 :
            print("Ingrese una fecha válida")
            dia_ingresado = auxiliares.ingresar_respuesta_str("")
        else:
            dia_valido = True
    # saco el dia de la semana y su nombre para que quede mas lindo

    n_dia_semana = calendario.dia_de_la_semana(int(dia_ingresado), mes_numero, anio)

    nombre_dia = nombres_dias_semana[n_dia_semana]

    # paso a tipo date para que despúes pueda ordenar con sorted
    # al usar leer_turnos. 
    fecha_seleccionada = date(anio, mes_numero, int(dia_ingresado))

    return fecha_seleccionada, nombre_dia

def elgir_consulta_med():# TODO: Funciona bien pero revisar la necesidad de tener a tipo consulta como diccionario.#✅
    """
    Permite la elección del tipo de consulta médica.
    
    Returns:
        consulta(str)
    """
    print("Seleccione el tipo de consulta del turno")
    print("_"*40)
    print(amarillo(f"{' CONSULTAS OFRECIDAS ':=^40}"))
    auxiliares.imprimir_lista_opciones(list(auxiliares.tipo_consulta.values()),True)
    seleccion = ingresar_opcion_elegida(list(auxiliares.tipo_consulta.values()))
    consulta = list(auxiliares.tipo_consulta.values())[seleccion]
    print()    
    return consulta

def elegir_especialidad_med():#✅
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

def elegir_medico(matriz_turnos, matriz_meds, especialidad, fecha_turno, dia_semana):#✅
    """
    Permite la elección de un medico disponible. 
    
    Args:
        matriz_turnos(list[list]): Matriz de turnos del mes.
        matriz_meds(list[list]): Matriz de médicos.
        especialidad(str): Especialidad seleccionada para el turno.
        fecha_turno(date): Fecha seleccionada para el turno.
        dia_semana(str): Nombre del día de la fecha.
    
    Returns:
    """

    medicos_horarios_libres = obtener_turnos_libres_medicos(matriz_turnos,
                                                            matriz_meds,
                                                            especialidad,
                                                            fecha_turno)
    if len(medicos_horarios_libres) == 0:
        raise TypeError("Sin turnos disponibles en la fecha solicitada")
    
    # 2 crear el menu de selección
    mostrar_opcion_turnos_medico(matriz_meds, medicos_horarios_libres,
                                 fecha_turno, dia_semana)

    # selecciono medico
    horarios_atencion = auxiliares.crear_horario_atencion()
    print()
    print(contraste("Seleccione médico"))
    print()
    matriculas_medicos = [list(medico)[0] for medico in medicos_horarios_libres]
    fila = ingresar_opcion_elegida(matriculas_medicos) 
    matricula_med_selec = list(medicos_horarios_libres[fila])[0]

    # selecciono horario
    print()
    print(contraste("Seleccione turno"))
    print()
    op_horario = ingresar_opcion_elegida(horarios_atencion) 
    # si selecciona el horario no disponible necesito un mensaje
    print(horarios_atencion[op_horario])
    while re.search("[a-zA-Z]", horarios_atencion[op_horario]):
        print("Turno no disponible")
        op_horario = ingresar_opcion_elegida(horarios_atencion) 

    horario_selec = horarios_atencion[op_horario]

    return matricula_med_selec, horario_selec

def mostrar_opcion_turnos_medico(matriz_meds, medicos_horarios_libres, fecha_turno, dia_semana):#✅
    """
    Muestra medicos y sus turnos disponibles en la fecha indicada.
    
    Args:
        matriz_meds(list[dic])
        medicos_horarios_libres(list[dic])
        fecha_turno(date)
        dia_semana(str)
    
    """
    print(verde(f"Medicos y horarios disponibles parar el {dia_semana} {fecha_turno.strftime('%d/%m/%Y')}"))
    print()

    matriz_horarios = []
    opcion = 0
    auxiliares.linea_iguales(auxiliares.ANCHO)
    for medico_horarios in medicos_horarios_libres:
        opcion += 1
        medico = list(medico_horarios.keys())[0]
        matriz_horarios.append(medico_horarios[medico])
        encabezado = f"MEDICO: {opcion} {devolver_nombre_persona(matriz_meds,medico, 'ID')}"
        print(f"| {encabezado:<34}",end=" |")
    print()
    auxiliares.linea_iguales(auxiliares.ANCHO)

    transpuesta_horarios = auxiliares.transponer_matriz(matriz_horarios)
    opcion = 0
    for fila in range(len(transpuesta_horarios)):
        opcion += 1
        for columna in range(len(transpuesta_horarios[fila])):
            horario = f"TURNO {opcion}: {transpuesta_horarios[fila][columna]}"
            print(f'| {horario:<34}', end="|")       
        print()
    auxiliares.linea_iguales(auxiliares.ANCHO)

def confirmar_ingreso_paciente(datos_del_paciente):
    """
    Confirma el ingreso de un paciente devolviendo su información.
    """

    auxiliares.linea_iguales(auxiliares.ANCHO)
    auxiliares.imprimir_opcion("[ENTER]", 'CONFIRMAR INGRESO PACIENTE', '1;33', False)
    auxiliares.imprimir_opcion(0, 'CANCELAR', '1;36')
    auxiliares.linea_iguales(auxiliares.ANCHO)
    print("#"*auxiliares.ANCHO)
    print(f"{datos_del_paciente['nombre']} DNI: {datos_del_paciente['dni']}"
          f" EDAD: {datos_del_paciente['edad']} OBRA SOCIAL: {datos_del_paciente['obra_social']}")
    auxiliares.linea_iguales(auxiliares.ANCHO)
    
    op = input("")
    if op == "":
        return True
    else:
        return False

def confirmar_turno(datos_turno, dia_semana, matriz_pacs, matriz_meds):#✅
    """
    Menu de confirmacion de turnos
    Args:
        datos_turno(dic): Datos del turno a confirmar.
        dia_semana(str): Dia de la semana. 
        matriz_pacs(list[dic]): Matriz de pacientes.
        matriz_meds(list[dic]): Matriz de medicos.
    
    Returns:
        bool: True si es válido.
    """
    auxiliares.linea_iguales(auxiliares.ANCHO)
    auxiliares.imprimir_opcion("[ENTER]", 'CONFIRMAR TURNO', '1;33', False)
    auxiliares.imprimir_opcion(0, 'CANCELAR', '1;36')
    auxiliares.linea_iguales(auxiliares.ANCHO)
    print(f"{devolver_nombre_persona(matriz_pacs, datos_turno['paciente'], 'dni')}")
    print(f"{dia_semana} {datos_turno['fecha'].strftime('%d/%m/%Y')} a las {datos_turno['hora']} hs\
     MEDICO: {devolver_nombre_persona(matriz_meds, datos_turno['medico'], 'ID')} - {datos_turno['especialidad_medica']}")
    op = input("")
    if op == "":
        return True
    else:
        return False

#-------------------------------------------------------------------------------
# FUNCIONES DE CONSULTAS -------------------------------------------------------
#-------------------------------------------------------------------------------

def consultar_por_fecha(matriz_turnos, matriz_pacs, matriz_meds):#✅
    """
    Filtra y muestra turnos según la fecha a ingresar.
    
    Args:
        m_turnos(list[list]): Matriz de turnos
        matriz_pacs(list[list]): Matriz de pacientes.
        matriz_meds(list[list]): Matriz de médicos.
    """
    info_mes = auxiliares.crear_mes()
    horarios_atencion = auxiliares.crear_horario_atencion()
    fecha_cons, dia = elegir_fecha(info_mes['mes_en_numero'], info_mes['anio'])
    turnos_fecha = filtrar_turnos(matriz_turnos, fecha_cons, 'fecha' )
    if len(turnos_fecha) == 0:
        return print(f"No hay turnos asignados para el dia {dia} {fecha_cons}")
    
    # genero una lista sin duplicados con los médicos con turnos en la fecha consultada
    medicos_fecha = list(set([turno['medico'] for turno in turnos_fecha]))

    # informe
    mostrar_encabezado_consulta("por fecha")
    print("#"*110)

    # informo cantidad de turnos de la fecha consultada
    print(f"Cantidad de turnos del {dia} {fecha_cons}: {len(turnos_fecha)} ")

    # informo cantidad de turnos según su estado
    conteos_estados = contar_ocurr_valor_turnos(turnos_fecha,'estado_turno', list(auxiliares.estado_turno.values()))

    for i in range(len(conteos_estados)):
        print(f"Cantidad de turnos {conteos_estados[i][0]}: {conteos_estados[i][1]} ")

    # informo franja horaria con mas turnos
    conteos_horarios = contar_ocurr_valor_turnos(turnos_fecha, 'hora', horarios_atencion)
    # ordeno mi matriz según el horario con más turnos (conteos)
    conteos_horarios.sort(key= lambda fila: fila[1], reverse=True)
    # print(conteos_horarios)
    print(f"Horario mas concurrido {conteos_horarios[0][0]}: {conteos_horarios[0][1]} turnos ")

    # informo médico con mayor cantidad de turnos
    conteos_medicos = contar_ocurr_valor_turnos(turnos_fecha, 'medico', medicos_fecha )
    # print(conteos_medicos)
    conteos_medicos.sort(key= lambda fila: fila[1], reverse=True )

    print(f"Médico con mayor cantidad de turnos\
    {devolver_nombre_persona(matriz_meds, conteos_medicos[0][0],'ID')}: {conteos_medicos[0][1]} turnos ")
    print("#"*110)
    print()
    print("="*110)
    titulo = f" Lista completa turnos {dia} {fecha_cons} "
    print(f"{titulo:=^110}")
    
    leer_turnos(turnos_fecha, matriz_pacs, matriz_meds, False)

def consultar_por_paciente( matriz_turnos, matriz_pacs, matriz_meds):#✅
    """
    Filtra y muestra turnos según el DNI del paciente.
    
    Args:
        matriz_turnos(list[list]): Matriz de turnos
        paci(list[list]): Matriz de pacientes.
        matriz_meds(list[list]): Matriz de médicos.    
    Returns:
    """
    info_mes = auxiliares.crear_mes()
    mostrar_encabezado_consulta("consulta por paciente")
    dni_paci = ingresar_dni_paciente()
    try:
        datos_paci = filtrar_personas_por_dato(matriz_pacs, 'dni', dni_paci)
    except Warning as mensaje:
        print(f'{alerta(str(mensaje).upper())}')# Todo: acá usar la funcion de nico de imprimir error
        print(alerta("PACIENTE NO REGISTRADO"))
        print(alerta("DIRIJASE A GESTIÓN PACIENTES > CREAR PACIENTES"))# Todo: llamar a pacientes
        input("\nPresione ENTER para volver al menú.")
        return
    
    confirmacion = confirmar_ingreso_paciente(datos_paci)

    if confirmacion == False:
        print(alerta("CONSULTA CANCELADA"))
        input("\nPresione ENTER para volver al menú.")
        return
    
    # filtro los turnos del paciente
    turnos_pac_cons = [turno for turno in matriz_turnos if dni_paci in list(turno.values())]
    # valido si el paciente no tiene turnos en el mes
    if len(turnos_pac_cons) == 0:
        print(f"El paciente ingresado no posee turnos en el mes de {info_mes.get('mes_en_palabra')}")
        input("\nPresione ENTER para volver al menú.")
        return
    
    print("="*110)
    print(f"El paciente {devolver_nombre_persona(matriz_pacs, dni_paci,'dni')} -"
          f" DNI: {dni_paci} tiene {len(turnos_pac_cons )} turnos en {info_mes.get('mes_en_palabra')}")

    leer_turnos(turnos_pac_cons, matriz_pacs, matriz_meds, False)

def realizar_metricas_matriz_turnos(matriz_turnos, info_mes):#✅
    """
    Realiza e imprime métrica sencillas de los turnos del mes dado.
    
    Args:
        matriz_turnos(list(dic))
        info_mes(dic)

    """
    horarios_turnos = auxiliares.crear_horario_atencion()
    # metricas
    numero_turnos_mes = len(matriz_turnos)
    promedio_turnos_por_dia = round(numero_turnos_mes/info_mes['cantidad_dias_mes'], 2)
    demanda_mes_horarios = contar_ocurr_valor_turnos(matriz_turnos, 'hora', horarios_turnos)
    demanda_mes_horarios.sort(key=lambda fila: fila[1], reverse=True)
    horario_mas_demandado = demanda_mes_horarios[0][0]
    promedio_turnos_horario_mas_demandado = round(demanda_mes_horarios[0][1] / info_mes['cantidad_dias_mes'], 2)
    horario_menos_demandado = demanda_mes_horarios[-1][0]
    promedio_turnos_horario_menos_demandado = round(demanda_mes_horarios[-1][1] / info_mes['cantidad_dias_mes'], 2)

    # salida por pantalla
    ancho = 110
    print("="*ancho)
    titulo = f" INFORME GENERAL TURNOS MES DE {info_mes['mes_en_palabra'].upper()} "
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
                              fila:(fila['fecha'], fila['hora']))#✅
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

def crear_turnos(matriz_turnos, matriz_pacs, matriz_meds, rnd = False):#✅
    """
    Crea una lista de diccionarios, con los datos de los turnos.

    Args:
        matriz_turnos(list[dic]): Matriz de turnos.
        matriz_pacs(list[dic]): Matriz de pacientes.
        matriz_meds(list[dic]): Matriz de medicos.
        rnd(bool): True para generar turnos random.
    """
    # creo las fechas del mes actual y guardo su informacion
    info_mes = auxiliares.crear_mes()

    if rnd == True:
        crear_turnos_random(matriz_turnos, matriz_pacs, matriz_meds, info_mes)
        return
    
    nuevo_turno = {'id':"void"}
    datos_turno, dia_semana = obtener_datos_turnos(matriz_turnos, matriz_pacs, matriz_meds, info_mes, rnd)
    
    # no hay superposición procedo a confirmar y a crear
    
    confirmacion = confirmar_turno(datos_turno, dia_semana, matriz_pacs, matriz_meds)

    if confirmacion == False:
        print("CREACION DE TURNO CANCELADO")
        input("\nPresione ENTER para volver al menú.")
        return
    
    id = crear_id_turno(matriz_turnos)
    nuevo_turno.update({'id':id})
    nuevo_turno.update(datos_turno)
    matriz_turnos.append(nuevo_turno)
    escribir_turnos(matriz_turnos)
    print(f"Turno generado exitosamente!")

    return

def crear_turnos_random(matriz_turnos, matriz_pacs, matriz_meds,info_mes, n_turnos = 10):
    """
    Crea una lista de diccionarios.

    Usa las matrices creadas en los módulos pacientes y médicos.
    
    Args:
        matriz_turnos(list[dic]): Matriz de turnos.
        matriz_pacs(list[dic]): Matriz de pacientes.
        matriz_meds(list[dic]): Matriz de médicos.
        info_mes(dic): Datos del mes.
        n_turnos(int): Número de turnos a generar.
    """
    for i in range(n_turnos):
        nuevo_turno = {'id':"void"}
        datos_valido, datos_turno = obtener_datos_turnos_random(matriz_turnos,
                                                                matriz_meds,
                                                                matriz_pacs,
                                                                info_mes)
        while datos_valido == False:
            datos_valido, datos_turno = obtener_datos_turnos_random(matriz_turnos,
                                                                    matriz_meds,
                                                                    matriz_pacs,
                                                                    info_mes)

        id = crear_id_turno(matriz_turnos)
        nuevo_turno.update({'id':id})
        nuevo_turno.update(datos_turno)# acá esta el error
        matriz_turnos.append(nuevo_turno)

    escribir_turnos(matriz_turnos)
    

    return        
 
def leer_turnos(matriz_turnos, matriz_pacs, matriz_meds, metricas = True):#✅
    """
    Leer y imprime matriz de turnos mas metricas si es requerido.
    
    Args:
        matriz_turnos(list[lis]): Matriz de turnos.
        matriz_pacs(list[list]): Matriz de pacientes.
        matriz_meds(list[list]): Matriz de médicos.
        metricas(bool)
    Returns:
    """
    ancho = 110
    info_mes = auxiliares.crear_mes()
    encabezados = ["ID", "FECHA", "HORA", "PACIENTE",
                   "ESPECIALIDAD", "MEDICO", "CONSULTA", "ESTADO" ]

    print()
    if metricas:
        realizar_metricas_matriz_turnos(matriz_turnos, info_mes)#✅
        print("="*ancho)
        titulo = f" Lista de turnos del mes de {info_mes.get('mes_en_palabra').upper()} "
        print(azul_negrita(f"{titulo:=^{ancho}}"))

    turnos_ordenados = ordenar_turnos_fecha_horario(matriz_turnos)#✅

    print("="*ancho)
    for t in range(len(encabezados)):#✅
        match t:
            case 0:# id
                print("|"+negrita(f"{encabezados[t]:^7}"), end="||")
            case 1:# fecha
                print(negrita(f"{encabezados[t]:^12}"), end="||")
            case 2:# hora
                print(negrita(f"{encabezados[t]:^7}"), end="||")
            case 6:# consulta
                print(negrita(f"{encabezados[t]:^12}"), end="||")
            case 7:# estado
                print(negrita(f"{encabezados[t]:^14}"), end="|")   
            case _:
                print(negrita(f"{encabezados[t]:^14}"), end="||")
    print()        
    print("="*ancho)

    for turno in turnos_ordenados:#✅
        nombre_paciente = devolver_nombre_persona(matriz_pacs, turno['paciente'], 'dni')
        nombre_medico = devolver_nombre_persona(matriz_meds, turno['medico'], 'ID' )
        print(f"""|{turno['id']:^7}||\
{turno['fecha'].strftime('%d/%m/%Y'):^12}||\
{turno['hora']:^7}||\
{mostrar_nombre_corto_persona(nombre_paciente):^14}||\
{turno['especialidad_medica'][:8]:^14}||\
{mostrar_nombre_corto_persona(nombre_medico):^14}||\
{turno['tipo_consulta']:^12}||\
{mostrar_estado_turno(turno['estado_turno'], 14)}||""")

    print("="*ancho)

def consultar_turno(matriz_turnos, matriz_pacs, matriz_meds):
    """
    Funcion principal de consulta de turnos
    
    Args:
        matriz_turnos(list[dic])
        matriz_pacs(list[dic])
        matriz_meds(list[dic])
    """
    while True:
                logo_turnos()
                while True:
                    opciones = 4
                    auxiliares.linea_iguales(auxiliares.ANCHO)
                    auxiliares.imprimir_un_encabezado('MENÚ PRINCIPAL > TURNOS > CONSULTA > OTRAS', auxiliares.ANCHO)
                    print("")

                    auxiliares.linea_iguales(auxiliares.ANCHO)
                    auxiliares.imprimir_opcion(1, 'CONSULTAR POR FECHA', '1;33', False)
                    auxiliares.imprimir_opcion(2, 'CONSULTAR POR PACIENTE', '1;34')
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
                    consultar_por_fecha(matriz_turnos, matriz_pacs, matriz_meds)
                    input("\nPresione ENTER para volver al menú.")
                elif opcion == "2":   # Opción 2
                    consultar_por_paciente(matriz_turnos, matriz_pacs, matriz_meds)
                    input("\nPresione ENTER para volver al menú.")

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