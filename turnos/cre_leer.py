# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Nicolás Seijo, Victor Maza
# Descripción: Módulo Turnos
# Fecha de creación: 10/08/2025
# ==============================================================================

import random
import fun_aux
from datetime import datetime, time, date, timedelta

##### Funciones específicas del módulo #####

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

def mostrar_meds_por_especialidad(meds, espec):
    """
    Filtra y muestra nombre de médicos según la especialidad indicada.
    
    Parámetros:
        meds(list): Lista de médicos.
        espec(str): Nombre de la especialidad a buscar.
    Returns:
        
    """
    meds_espec = []
    mat_meds = []
    for medico in meds:
        if espec in medico:
            meds_espec.append(medico[1])
            mat_meds.append(medico[0])
    fun_aux.imprimir_lista(meds_espec, True)
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

def crear_horario_atencion(inicio, fin, minutes = 30):
    """
    Crea el horario de atención del consultorio.

    Por defecto cada turno de se asigna cada media hora.
    
    Parámetros:
        inicio(time): Hora del primer turno.
        fin(time): Hora del último turno.
        minutes(int): Tiempo entre cada turno.
    Returns:
        list: Lista con los horarios de los turnos.
    """
    h_turnos = [inicio.strftime("%H:%M")]
    h_turno =  inicio
    while h_turno <= fin:
        h_turno += timedelta(minutes)
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

def validar_turno_medicos(mat_turnos, meds, n_max_turnos):
    """
    Cuenta y valida los turnos que tiene asignado un médico.
    
    Valida que sea menor que el máximo que puede tomar.

    Parámetros:
        mat_turnos(list[list]): Matriz de turnos.
        meds(list[list]): Matriz de médicos.
        n_max_turnos(int): Número máximo de turnos por médico.
    Returns:
        numero_turnos(int): Número de turnos que tiene el médico
        disponible(bool)
    """
    disponible = True

    print("x")

def verificar_turnos_pacientes(mat_turnos, paci, hora_turnos):
    """
    Verifica los los turnos de los pacientes para evitar superposición.
    
    Parámetros:
    
    Returns:
    """
    print("x")

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
    turnos_ordenados = []
    for turno in m_turnos:
        if fecha_cons in turno:
            turnos_ordenados.append(turno)
            # por acá agregaría la función para hacer el informe
    leer_turnos(turnos_ordenados, encabezados, paci, meds)

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

## Funciones Crear, leer (y consultar) ##

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
    for i in range(n_turnos):
        id = crear_id_turno(mat_turnos)
        fecha = random.choice(mes)
        hora_turno = random.choice(hora_turnos)
        consulta = random.choice(tipo_consultas)
        estado_turno = random.choice(estado)
        paciente = random.choice(paci)
        dni_pac =  paciente[0]
        medico = random.choice(meds)
        matr_med =  medico[0]                
        especialidad = medico[2]
        
        # validar que el médico tome solo 16 turnos (recordar que son turnos cada media hora)
        # validar que al paciente no se le superpongan los turnos

        mat_turnos.append([id, fecha, hora_turno, dni_pac, especialidad, matr_med, 
                       consulta, estado_turno])

def crear_turno(mat_turnos, hora_turnos, tipo_consultas, 
                paci, meds):
    """
    Permite la creación de un turno y guardarlo en la matriz de turnos.
    
    Parámetros:
        m_turnos(list[list]): Matriz de turnos.
        hora_turnos(list): Lista con los horarios de los turnos.
        tipo_consultas(list): Lista con el tipo de consultas.
        lists_pac(list): Lista con los datos del paciente.
        meds(list): Lista con los datos del médico.
    Returns:
    """
    print("-"*10, "NUEVO TURNO", "-"*10)
    print("-"*40)
    print("Ingrese paciente")
    # EN ESTA PARTE NECESITARÍA INTEGRAR LA CREACIÓN DE UN PACIENTE ############
    # O LA ELECCIÓN DE UN PACIENTE EXISTENTE
    paciente = random.choice(paci)# simulo ingreso de un paciente

    ############################################################################
    print(f"Paciente ingresado: {paciente}")
    print("Ingrese fecha solcitida para turno")
    dia, mes, anio = ingresar_fecha()
    fecha_turno = f"{dia}/{mes}/{anio}"
    horario_turno = elegir_horario(hora_turnos)
    tipo_consulta = generar_consulta_med(tipo_consultas)
    especialidad = elegir_especialidad_med()
    print(f"{especialidad.upper()}: Elija un médico disponible.")
    # MOSTRAR MÉDICOS CON TURNOS DISPONIBLES, RECORDAR 16 TURNOS POR DÍA POR MÉDICO
    meds_a_selec= mostrar_meds_por_especialidad(meds, especialidad)
    ############################################################################
    seleccion = fun_aux.ingresar_entero_positivo("Seleccione médico: ")
    if seleccion == 1:
        seleccion = 0
    else:
        seleccion -= 1
    medico_selec = meds_a_selec[seleccion]
    id = crear_id_turno(mat_turnos)
    turno = [id, fecha_turno, horario_turno, paciente[0], 
             especialidad, medico_selec, tipo_consulta, "Activo"]
    # Generar una confirmación del turno y mensaje de "generado exitosamente"
    mat_turnos.append(turno)
    print(f"Turno: {turno} generado exitosamente")

def leer_turnos(mat_turnos, encabezados, paci, meds):
    """
    Leer y imprime matriz de turnos mas encabezado.
    
    Parámetros:
        mat_turnos(list[lis]): Matriz de turnos.
        encabezado(list): Lista de encabezados de la matriz.
        paci(list[list]): Matriz de pacientes.
        meds(list[list]): Matriz de médicos.
    Returns:
    """
    # Tendría que ir un encabezado.
    fun_aux.limpiar_terminal()
    print("Lista de turnos del mes < >")
    turnos_ordenados = sorted(mat_turnos, 
                              key=lambda 
                              fila:(fila[1], fila[2]))
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
    
def consultar_turno(encabezados, mat_turnos, paci, meds):

    # mi idea es hacer una salida tipo informe, para cada consulta
    # donde se informe también las métricas. La idea sería seguir el
    # ejemplo del profe con la factura.
    
    while True:
                logo_turnos()
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > TURNOS > CONSULTA > OTRAS")
                    print("---------------------------")
                    print("[1] Consulta por horario")
                    print("[2] Consulta por fecha")
                    print("[3] Consulta por paciente")
                    print("[4] Consulta por médico")
                    print("[5] Consulta por especialidad")
                    print("[6] Consulta por tipo de consulta médica")
                    print("[7] Consulta por estado del turno")
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
                    print("Consulta por horario")
                    input("\nPresione ENTER para volver al menú.")
                elif opcion == "2":   # Opción 2
                    consultar_por_fecha(encabezados, mat_turnos, paci, meds)
                    input("\nPresione ENTER para volver al menú.")
                elif opcion == "3":   # Opción 3
                    consultar_por_paciente(encabezados, mat_turnos, paci, meds)
                    input("\nPresione ENTER para volver al menú.")
                elif opcion == "4":   # Opción 4
                    print("Consulta por médico")
                    input("\nPresione ENTER para volver al menú.")
                elif opcion == "5":   # Opción 5
                    print("Consulta por especialidad")
                    input("\nPresione ENTER para volver al menú.")
                elif opcion == "6":   # Opción 6
                    print("Consulta por tipo de consulta médica")
                    input("\nPresione ENTER para volver al menú.")
                elif opcion == "7":   # Opción 7
                    print("Consulta por estado del turno")
                    input("\nPresione ENTER para volver al menú.")

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
    INICIO_TURNOS = datetime(2025,1,1,9,0)# Pongo una fecha cualquiera lo que importa es la hora
    FIN_TURNOS = datetime(2025,1,1,16,0)# Pongo una fecha cualquiera lo que importa es la hora
    INICIO_MES = date(2025, 8, 1)
    FIN_MES = date(2025, 8, 31)
    N_TURNOS_RANDOM = 50

    # turnos = []
    horario_turnos = crear_horario_atencion(INICIO_TURNOS, FIN_TURNOS)
    mes = crear_mes(INICIO_MES, FIN_MES)

    ### DATOS QUE DEBERIAN LLEGAR, DEBERÍAN SER ARGUMENTOS ###
    medicos_h = [[154892, "Rodolfo Galleguillo", "Traumatología", 15, 1],
            [153167, "Obi Wan Kenobi", "Psiquiatría", 15, 1],
            [123858, "Sanji Vismonke", "Urología", 15, 1],
            [456176, "Tony Chopper", "Clínica Médica", 15, 1],
            [789546, "Piccolo DaimaKu", "Traumatología", 15, 1]]
    pacientes_h = [[35023963, "Cosme Fulanito", "Total"],
                [32490932, "Anakin Skywalker", "Copago"],
                [20488909, "Judge Vinsmoke", "Particular"],
                [20101983, "Homero Simpson", "Particular"]]

    #-------------------------------------------------
    # Bloque de menú
    #-------------------------------------------------
    fun_aux.limpiar_terminal()
    logo_turnos()
    match opcion:
        case 0:
            # crear_turno(turnos, horario_turnos, CONSULTA, paci, medicos_h)
            crear_turnos_random(turnos, mes, horario_turnos, CONSULTA, ESTADO_TURNO, 
                                pacientes_h, medicos_h, N_TURNOS_RANDOM)
        case 1:
            crear_turno(turnos, horario_turnos, CONSULTA, pacientes_h, medicos_h)
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
                    leer_turnos(turnos, ENCABEZADO_TURNOS, pacientes_h, medicos_h)
                    input("\nPresione ENTER para volver al menú.")
                    
                    
                elif opcion == "2":   # Opción 2
                    consultar_turno(ENCABEZADO_TURNOS, turnos, pacientes_h, medicos_h)
                    input("\nPresione ENTER para volver al menú.")
                    

