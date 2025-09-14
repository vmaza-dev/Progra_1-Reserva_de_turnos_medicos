# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Nicolás Seijo, Victor Maza
# Descripción: 
# Fecha de creación: 10/08/2025
# ==============================================================================
import random, auxiliares

"""================================================ FUNCIONES C.R.U.D ====================================================================="""
def ingresar_nombre_medico():
    """
    Solicita al usuario el nombre de un médico *ingresa el nombre* .

    Returns:
        str: Nombre ingresado.
    """
    nombre = input("Ingrese el nombre del medico: ")
    return nombre

def ingresar_espe(nombreMed="el médico"):
    """
    Solicita al usuario la especialidad a ingresar del medico
    
    Parametros
        nombreMed (str): Nombre del medico utilizado para despues mostrar en el promp
        
    Returns:
        str: Especialidad ingresada.
    """
    especialidad = input(f"Ingrese la especialidad de {nombreMed}: ") #Uso fPrints ya que el input no puede concatenar cadenas con ","
    return especialidad

def ingresar_antig(nombreMed):
    """
    Solicita al usuario la antiguedad (años de experiencia de un medico)
    
    Parametros:
        nombreMed (str): Nombre del medico, utilizado para mostrar en el prompt
        
    Returns:
        int: Antiguedad en años.
    """
    antiguedad = int(input(f"Ingrese la antiguedad de {nombreMed}: "))
    return antiguedad

def ingresar_id():
    idBuscado = int(input("Ingrese el ID del medico a buscar: "))
    while (idBuscado < 100000 or idBuscado > 999999):
        print("ID INVALIDO INTENTE NUEVAMENTE")
        idBuscado = int(input("Ingrese el ID del medico a buscar: "))
    
    return idBuscado

def generar_id(listaIDs):
    """
    Genera aleatoriamente un ID de 6 dígitos
    
    Parametros:
        listaIDs (list): Lista que contiene los IDs ya utilizados, para evitar repeticiones.
        
    Returns:
        idGenerado (int): El idGenerado en caso de ser exitoso, o '-1' en caso de fallar.
    """
    if (len(listaIDs) == 900000):
        print("No hay mas IDs disponibles")
        return -1
    else:
        idGenerado = random.randint(100000, 999999)
        while (idGenerado in listaIDs):
            idGenerado = random.randint(100000, 999999)
        return idGenerado

def crear_medico(matrizMeds, listaIDs):
    """
    Crear un nuevo usuario medico y lo agrega a la matriz total de medicos.
    
    Parametros:
        - matrizMeds (list): Matriz que almacena los medicos registrados.
        cada medico se guarda con el formato: [ID,Nombre, Especialidad, Antiguedad , Estado]
        - listaIDs (list): Lista que almacena los IDs ya utilizados, para evitar repeticiones.

    Flujo:
        - Genera un ID aleatorio de 4 digitos
        - Pide al usuario (nombre,especialidad y antiguedad)
        - Define el estado inicial como activo (1)
        - Agrega la informacion del medico a la matriz
        """
    nombreCompleto = ingresar_nombre_medico()
    idMed = generar_id(listaIDs)
    if (idMed == -1):
        print("ERROR al crear medico. No hay más IDs disponibles")
        return
    listaIDs.append(idMed)
    matrizMeds.append([idMed, nombreCompleto, ingresar_espe(nombreCompleto),
                        ingresar_antig(nombreCompleto), True]) # False DE BAJA | True ACTIVO

def crear_medicos_random(meds, cantCrear, listaIDs):
    """
    Crea una cantidad específica de medicos aleatorios
    
    Parametros:
        - matrizMeds (list): Matriz que almacena los medicos registrados. 
        Cada medico se guarda con el formato: [ID,Nombre, Especialidad, Antiguedad , Estado]
        - listaIDs (list): Lista que almacena los IDs ya utilizados, para evitar repeticiones.

    Flujo:
        - Genera un nombre completo usando la función 'random.choice()' y listas auxiliares de nombres y apellidos
        - Genera una especialidad aleatoria usando 'random.choice()' y una lista auxiliar de especialidades
        - Genera un ID aleatorio de 6 digitos
        - Agrega la informacion del medico a la matriz de Medicos, dejandolo con el estado "Activo" (True) por defecto.
    """
    for i in range(cantCrear):
        nyap = random.choice(auxiliares.nombres) + " " + random.choice(auxiliares.apellidos)
        espe = random.choice(auxiliares.especialidades)
        idMed = generar_id(listaIDs)
        if (idMed == -1):
            print("ERROR al crear medico. No hay más IDs disponibles")
            return
        
        listaIDs.append(idMed)
        meds.append([idMed, nyap, espe, random.randint(1,30), True])

def buscar_medico_id(meds, idMed):
    for med in meds:
        if (med[0] == idMed):
            break
    return med

def menu_act_antig(med, nombreMed):
    titulo = "LA ANTIGÜEDAD DE " + nombreMed + " ES " + str(med[3])

    auxiliares.linea_iguales(auxiliares.ANCHO)
    auxiliares.imprimir_un_encabezado('MENU MEDICOS > C.R.U.D > ACTUALIZAR MEDICO > ANTIGÜEDAD', auxiliares.ANCHO, '\033[1m')
    print("")
    
    auxiliares.linea_iguales(auxiliares.ANCHO)
    auxiliares.imprimir_opcion('-', titulo, '1', False)
    auxiliares.imprimir_opcion(1, 'SUMAR 1 AÑO', '1;33')
    auxiliares.imprimir_opcion(2, 'RESTAR 1 AÑO', '1;34')
    auxiliares.imprimir_opcion(3, 'INGRESAR MANUALMENTE ANTIGÜEDAD', '1;35')
    auxiliares.imprimir_opcion(0, 'VOLVER AL MENÚ ANTERIOR', '1;36')
    auxiliares.linea_iguales(auxiliares.ANCHO)

    opcionAntig = ingresar_opcion(3)
    match opcionAntig:
        case 0: return 0
        case 1:med[3] += 1
        case 2:med[3] -= 1
        case 3:med[3] = ingresar_antig(nombreMed)
    print("\nAntigüedad modificada exitosamente a:", med[3])
    return 0

def actu_medico(med, nombreMed): # Falta estandarizar la manera de mostrar este menu de actu
    """
    Permite modificar los datos de un medico que ya estaba registrado.

    Parametros:
        listaMed (list): Lista que representa a un medico, en el formato:[ID, Nombre, Especialidad, Antiguedad, Estado]
        nombreMed (str):Nombre del medico que solo se va a utilizar para mostrar mensajes

    Flujo: 
        - Muestra un menu de opciones de edicion
        - Permite modificar : nombre, especialidad, antiguedad o estado.
        - Actualiza directamente la lista del medico.
    """
    auxiliares.linea_iguales(auxiliares.ANCHO)
    auxiliares.imprimir_un_encabezado('MENU MEDICOS > C.R.U.D > ACTUALIZAR MEDICO', auxiliares.ANCHO, '\033[1m')
    print("")

    auxiliares.linea_iguales(auxiliares.ANCHO)
    auxiliares.imprimir_opcion(1, 'NOMBRE Y APELLIDO', '1;33', False)
    auxiliares.imprimir_opcion(2, 'ESPECIALIDAD', '1;34')
    auxiliares.imprimir_opcion(3, 'ANTIGÜEDAD', '1;35')
    auxiliares.imprimir_opcion(4, 'ESTADO (DAR DE BAJA/ALTA)', '1;31')
    auxiliares.imprimir_opcion(0, 'VOLVER AL MENU ANTERIOR', '1;36')
    auxiliares.linea_iguales(auxiliares.ANCHO)

    opcion = ingresar_opcion(4)
    match opcion:
        case 0: return 0
        case 1: 
            med[1] = ingresar_nombre_medico()
            print("Nombre modificado exitosamente a:", med[1])
        case 2: 
            med[2] = ingresar_espe(nombreMed)
            print("Especialidad modificada exitosamente a:", med[2])
        case 3:
            auxiliares.limpiar_terminal()
            opcion = menu_act_antig(med, nombreMed)
        case 4:
            if (not med[4]):
                med[4] = True
                print("El médico", nombreMed, "ahora se encuentra activo")
            else:
                med[4] = False
                print("El médico", nombreMed, "ahora se encuentra dado de baja")

    if (opcion != 0): input("\nPresione Enter para volver al menú anterior...")
    return 0

def imprimir_medico(med):
    """
   Imprime en un auxiliares.ANCHO de 111 cada elemento del médico, modificando su color según ciertas condiciones en algunos casos.

    Parametros:
        med (list): Lista que representa a un medico, en el formato:[ID, Nombre, Especialidad, Antiguedad, Estado]

    Flujo: 
        - Imprime el ID del médico centrado en 6 caracteres
        - Imprime el nombre comleto del médico ajustado a la izquierda en 41 caracteres y en negrita.
        - Imprime la especialidad del médico ajustada a la izquierda en 21 caracteres.
        - Imprime la antigüedad del médico ajustada la izquierda en 11 caracteres, en caso de ser mayor a 25 se colorea de amarillo
        - Imprime el estado del médico, verde para activo, rojo para inactivo.
    """

    print(f"| {str(med[0]).ljust(6)}", end=" |")
    print(f"| \033[1m{med[1].ljust(41)}\033[0m", end=" |")
    print(f"| {med[2].ljust(21)}", end=" |")
    print(f"| \033[33m{str(med[3]).ljust(11)}\033[0m", end=" |") if (med[3] > 25) else print(f"| {str(med[3]).ljust(11)}", end=" |")
    if (med[4]):
        print(f"| \033[1;32m{'ACTIVO'.center(12)}\033[0m", end=" |")
    else:
        print(f"| \033[1;31m{'INACTIVO'.center(12)}\033[0m", end=" |")

def header_medicos(anchoTotal):
    """
    Imprime el header para la impresión de médicos.

    Parametros:
        anchoTotal (int): auxiliares.ANCHO a utilizar para pasar al a función auxiliar "linea_iguales()"

    Flujo: 
        - Llama a la función "linea_iguales()" para imprimir una linea de '='
        - Imprime 'ID', 'NOMBRE COMPLETO', 'ESPECIALIDAD', 'ANTIGÜEDAD' Y 'ESTADO' todos centrados, en negrita y color azul.
        - Llama nuevamente a la función auxiliar "linea_iguales()"
    """

    auxiliares.linea_iguales(anchoTotal)

    print(f"| \033[1;34m{'ID'.center(6)}\033[0m", end=" |")
    print(f"| \033[1;34m{'NOMBRE COMPLETO'.center(41)}\033[0m", end=" |")
    print(f"| \033[1;34m{'ESPECIALIDAD'.center(21)}\033[0m", end=" |")
    print(f"| \033[1;34m{'ANTIGÜEDAD'.center(11)}\033[0m", end=" |")
    print(f"| \033[1;34m{'ESTADO'.center(12)}\033[0m", end=" |\n")

    auxiliares.linea_iguales(anchoTotal)

def leer_medicos(meds):
    """
    Imprime el reporte completo de médicos utilizando las funciones 'header_medicos' y 'imprimir_medico()'

    Parametros:
        meds (list): Matriz de médicos a imprimir.

    Flujo: 
        - Llama a la función 'header_medicos()' para imprimir los encabezados de médico.
        - Para cada médico de la matriz llama a la función 'imprimir_medico()' y deja un espacio.
        - Llama a la función auxiliar "linea_iguales()" para imprimri una línea de '='
    """

    header_medicos(auxiliares.ANCHO)
    for med in meds:
        imprimir_medico(med)
        print("")
        
    auxiliares.linea_iguales(auxiliares.ANCHO)

def leer_medico_id(meds, idMed):
    """
    Imprime el reporte de un médico especificado por su ID utilizando las funciones 'header_medicos' y 'imprimir_medico()'

    Parametros:
        meds (list): Matriz de médicos a explorar.
        idMed (int): ID del medico a buscar.

    Flujo: 
        - Recorre la matriz "meds" y verifica coincidencias de ID
        - En caso de encontrarlo:
            -- Llama a la función 'header_medicos()' para imprimir los encabezados
            -- Llama a la función 'imprimir_medico()' para imprimir los datos del médico encontrado.
            -- Llama a la función 'linea_iguales()' para imprimir una línea de '='
            -- Termina de recorrer la lista con 'break'
    """
    for med in meds:
        if (med[0] == idMed):
            header_medicos(auxiliares.ANCHO)
            imprimir_medico(med)
            print("")
            auxiliares.linea_iguales(auxiliares.ANCHO)
            break

def buscar_borrar_med(idElim, meds):
    """
    Busca un medico segun el id que tiene y lo elimina de la lista si es que lo encuentra.

    Parametros: 
        idElim (int): ID del medico a eliminar.
        meds (list): Lista de medicos, donde cada medico es una lista en el formato: [ID, Nombre, Especialidad, Antiguedad, Estado]
        
    Returns:
        bool: True si se encontro y elimino al medico, false si no se encontro.
    """
    encontrado = False
    for med in meds:
        if (med[0] == idElim):
            encontrado = True
            meds.remove(med)
            break
    return encontrado

def elim_medico(matrizMeds): # Hay que estandarizar la impresión  de esto
    """
    Solicita al usuario que ingrese el ID de un medico y lo modifica su estado a inactivo.
    
    Parametros: 
        MatrizMeds(list): Lista de medicos.
    """
    idElim = int(input("Ingrese el ID del médico a eliminar: "))
    if (buscar_borrar_med(idElim, matrizMeds)): # Devuelve True si lo encontro y borro, False si no lo encontró
        print("\n>> Medico de ID", idElim, "eliminado exitosamente.")
    else:
        print("\n>> Medico de ID", idElim, "no encontrado o inexistente, no se realizó la eliminación.")

"""================================================ FUNCIONES ESTADÍSTICAS ====================================================================="""
def imprimir_porcentaje_estado(total, activos, inactivos):
    """
    Imprime utilizando las funciones 'imprimir_un_encabezado()', 'imprimir_tres_encabezados' y 'linea_iguales()' el total de médicos y el
    porcentaje de activos e inactivos

    Parametros:
        total(int): Total de médicos
        activos(int): Total de médicos con estado 'Activo' (True)
        inactivos(int): Total de médicos con estado 'Inactivo' (False)

    Flujo: 
        - Imprime el título del reporte con líneas de iguales antes y despues.
        - Imprime los encabezados del reporte.
        - Redondea los porcentajes a un solo dígito decimal.
        - Imprime el total, activos e inactivos con porcentaje en los últimos 2
    """
    auxiliares.linea_iguales(auxiliares.ANCHO)
    auxiliares.imprimir_un_encabezado('PORCENTAJE DE MEDICOS ACTIVOS E INACTIVOS', auxiliares.ANCHO, '\033[1m')
    print("")
    auxiliares.linea_iguales(auxiliares.ANCHO)
    auxiliares.imprimir_tres_encabezados('TOTAL DE MEDICOS', 'ACTIVOS', 'INACTIVOS', '\033[1;34m', '\033[1;32m', '\033[1;31m')
    auxiliares.linea_guiones(auxiliares.ANCHO)

    pActivos = f"{activos:.1f}"
    pInactivos = f"{inactivos:.1f}"

    auxiliares.imprimir_tres_encabezados(str(total), (str(pActivos)+' %'), (str(pInactivos)+' %'), "", '\033[32m', '\033[31m')
    auxiliares.linea_iguales(auxiliares.ANCHO)

#ID, NOMBRE, ESPECIALIDAD, ANTIGUEDAD, ESTADO
def porcentaje_estado(matrizMeds):
    """
    Recorre la matriz y suma dos acumuladores: Uno para los medicos activos y otro para los inactivos, posteriormente calcula que porcentaje
    son sobre el total y llama a la funcion 'imprimir_porcentaje_estado()' para imprimir los resultados.

    Parametros:
        matrizMeds(list): Matriz de los médicos

    Flujo: 
        - Obtiene el total de médicos en la matriz e inicializa los acumuladores en 0
        - Recorre la matriz y por cada médico, en caso de ser 'True' su 'Estado' suma 1 al acumulador de activos,
          caso contrario suma 1 al de inactivos
        - Realiza una regla de tres simple para obtener el porcentaje de activos e inactivos sobre el total.
        - Llama a la función 'imprimir_porcentaje_estado()' para imprimir los datos.
    """
    totalMeds = len(matrizMeds)
    acumAct = 0
    acumInac = 0

    for med in matrizMeds:
        if (med[4]):
            acumAct+=1
        else:
            acumInac+=1

    porcenAct = (acumAct*100)/totalMeds
    porcenInac = (acumInac*100)/totalMeds

    imprimir_porcentaje_estado(totalMeds, porcenAct, porcenInac)

def color_porcentaje_espec(porcentaje):
    """
    Según el porcentaje indicado, decide el color que tendrá al imprimirse.

    Parametros:
        porcentaje(float): Porcentaje correspondiente a la especialidad

    Return:
        Cadena que indica el color de ANSI a utilizar
    """
    if (porcentaje < 35):
        return "\033[31m"
    elif (porcentaje > 65):
        return "\033[32m"
    else:
        return "\033[33m"

def imprimir_porcentaje_especs(espec, cantEspec, porcenEspec, totalMeds):
    """
    Imprime utilizando las funciones 'imprimir_un_encabezado()', 'imprimir_tres_encabezados' y 'linea_iguales()' el total de médicos y el total de
    médicos, el total de medicos de una especialidad especifica y el porcentaje que implica sobre el total

    Parametros:
        espec(str): La especialidad del médico
        cantEspec(int): Total de médicos de esa especialidad.
        porcenEspec(float): Porcentaje de médicos con esa especialidad.
        totalMeds(int): Cantidad total de médicos.

    Flujo: 
        - Imprime el título del reporte con líneas de iguales antes y despues.
        - Imprime los encabezados del reporte.
        - Llama a la función 'color_porcentaje_espec()' para definir el color que tendrá el porcentaje.
        - Redondea el porcentaje a un solo dígito decimal.
        - Imprime el total de medicos, el total de médicos por esa especialidad y el porcentaje que representa.
    """
    auxiliares.linea_iguales(auxiliares.ANCHO)
    auxiliares.imprimir_un_encabezado('PORCENTAJE DE MEDICOS DE ESPECIALIDAD ' + espec.upper(), auxiliares.ANCHO, '\033[1m')
    print("")
    auxiliares.linea_iguales(auxiliares.ANCHO)
    auxiliares.imprimir_tres_encabezados('TOTAL DE MEDICOS', ('TOTAL '+ espec.upper()), 'PORCENTAJE SOBRE EL TOTAL', '\033[1;34m', '\033[1m', '\033[1m')

    colorEspec = color_porcentaje_espec(porcenEspec)
    porcenEspec = f"{porcenEspec:.1f}"

    auxiliares.linea_guiones(auxiliares.ANCHO)
    auxiliares.imprimir_tres_encabezados(str(totalMeds), str(cantEspec), (porcenEspec+' %'), '\033[1;34m', colorEspec, colorEspec)
    auxiliares.linea_iguales(auxiliares.ANCHO)

def porcentaje_espec(matrizMeds, espec):
    """
    Obtiene el total de médicos y posteriormente recorre la matriz de médicos para contar cuantos son de la especialidad indicada.

    Parametros:
        matrizMeds(list): La matriz con la totalidad de los médicos.
        espec(str): La especialidad del médico

    Flujo: 
        - Obtiene el total de médicos
        - Recorre la matriz y en caso de encontrar una coincidencia de la especialidad, aumenta en 1 el contador 'contEspec'
        - Llama a la funcion 'imprimir_porcentaje_especs()' para imprimir los resultados.
    """
    totalMeds = len(matrizMeds)
    contEspec = 0

    for med in matrizMeds:
        if med[2] == espec:
            contEspec += 1

    imprimir_porcentaje_especs(espec, contEspec, (contEspec*100)/totalMeds, totalMeds)

def crear_matriz_prom_antig(matrizMeds):
    """
    Obtiene el total de médicos y posteriormente recorre la matriz de médicos para contar cuantos son de la especialidad indicada.

    Parametros:
        matrizMeds(list): La matriz con la totalidad de los médicos.

    Return:
        matAntig(list): Matriz de antigüedades por especialidad, con formato [Especialidad, AcumuladorAntiguedad, CantidadMedicosAntiguedad]

    Flujo: 
        - Recorre la matriz de médicos, por cada médico:
            -- Inicializa la flag existe en False
            -- Por cada antigüedad ingresada en matAntig:
                --- Verifica si coincide con la especialidad del médico
                --- En caso de encontrar coincidencia, suma la antigüedad al acumulador en su índice 1 y aumenta en 1 el contador de medicos
                    de esa especialidad, también setea la flag de 'Existe' en True
                --- Si no encuentra coincidencia en toda la matriz de antigüedad, agrega la antigüedad como nuevo elemento a la matriz. 
    """
    matAntig = []

    for med in matrizMeds:
            existe = False
            for elem in matAntig:
                if (med[2] == elem[0]): #Si la especialidad es igual a la especialidad de la lista
                    existe = True
                    elem[1] += med[3]
                    elem[2] += 1
                    break
            if (not existe):
                matAntig.append([med[2], med[3], 1]) 
                # Se le agrega la especialidad, arranca el sumador con su antigüedad y el contador en 1
    
    return matAntig

def prom_antig_espec(matrizMeds):
    """
    Crea una función de antigüedades por especialidad, posteriormente imprime los títulos y encabezados del reporte.
    Define los promedios y se les asigna un color según su valor, también se le quita la parte decimal si es nula, y sino, se redondea a 1 digito.
    Imprime los resultados.

    Parametros:
        matrizMeds(list): La matriz con la totalidad de los médicos.

    Flujo: 
        - Llama a la función 'crear_matriz_prom_antig()' para obtener las especialidades, la suma de las antigüedades por especialidad
          y la cantidad de médicos de esa especialidad
        - Imprime el titulo y los encabezados del reporte acompañados de líneas del símbolo '='
        - Por cada antigüedad de la matriz de antigüedades por especialidad:
            -- Calcula el promedio y se le asigna un color según si es mayor o igual a 25, menor o igual a 5, o ninguna de ellas.
            -- En caso de que el promedio tenga parte decimal nula, se castea en entero y de entero a string para imprimirlo sin parte decimal, caso
            contrario solo se redondea a 1 dígito decimal.
        - Se imprimen los resultados.
    """
    matAntig = crear_matriz_prom_antig(matrizMeds)

    auxiliares.linea_iguales(auxiliares.ANCHO)
    auxiliares.imprimir_un_encabezado('PROMEDIO DE ANTIGÜEDAD POR ESPECIALIDAD', auxiliares.ANCHO, '\033[1m')
    auxiliares.linea_iguales(auxiliares.ANCHO)

    auxiliares.linea_iguales(auxiliares.ANCHO)
    auxiliares.imprimir_tres_encabezados('ESPECIALIDAD', 'CANTIDAD MEDICOS', 'PROMEDIO ANTIGÜEDAD', '\033[1;34m', '\033[1;35m', '\033[1;36m')
    auxiliares.linea_iguales(auxiliares.ANCHO)

    for antig in matAntig:
        prom = (antig[1]/antig[2])
        colorProm = '\033[1;31m' if prom>=25 else '\033[1;32m' if prom<=5 else '\033[1;33m'
        prom = str(int(prom)) if prom == int(prom) else str(round(prom,1))


        auxiliares.imprimir_tres_encabezados(str(antig[0]), str(antig[2]), prom, '\033[1m', "", colorProm)

    auxiliares.linea_iguales(auxiliares.ANCHO)

"""================================================================ MENU Y MAIN========================================================================="""
def ingresar_opcion(max):
    opcion = int(input("Ingrese la opcion deseada: "))
    while (opcion < 0 or opcion > max):
        print("Opcion no valida, intente nuevamente.")
        opcion = int(input("Ingrese la opcion deseada: "))
    return opcion

def imprimir_opcion(opcion, texto, colorOpcion='', guiones=True, colorTexto=''):
    if (guiones):
        auxiliares.linea_guiones(auxiliares.ANCHO)

    textoImprimir = f"\033[{colorOpcion}m[{opcion}]\033[0m: \033[{colorTexto}m{texto}\033[0m"
    espacios = len(textoImprimir) - len(f"[{opcion}]: {texto}")
    print(f"| " + textoImprimir.ljust(auxiliares.ANCHO-4) + " " * espacios, end=" |\n")

def menu_leer_medicos(matrizMeds):
   auxiliares.linea_iguales(auxiliares.ANCHO)
   auxiliares.imprimir_un_encabezado('MENU MEDICOS > C.R.U.D > LEER MEDICOS', auxiliares.ANCHO, '\033[1m')
   print("")
   
   auxiliares.linea_iguales(auxiliares.ANCHO)
   auxiliares.imprimir_opcion(1, 'LEER TODOS LOS MEDICOS', '1;35', False)
   auxiliares.imprimir_opcion(2, 'LEER MEDICO POR ID', '1;33')
   auxiliares.imprimir_opcion(0, 'VOLVER AL MENU ANTERIOR', '1;36')

   auxiliares.linea_iguales(auxiliares.ANCHO)
   
   opcion = ingresar_opcion(2)
   match opcion:
       case 0: return 0
       case 1:
        auxiliares.limpiar_terminal()
        leer_medicos(matrizMeds)
       case 2: 
        auxiliares.limpiar_terminal()
        leer_medico_id(matrizMeds, ingresar_id())

   if (opcion != 0): input("\nPresione Enter para volver al menú anterior...")

   auxiliares.limpiar_terminal()
   menu_leer_medicos(matrizMeds)

def menu_crud_medicos(matrizMeds):
    auxiliares.linea_iguales(auxiliares.ANCHO)
    auxiliares.imprimir_un_encabezado('MENU MEDICOS > C.R.U.D', auxiliares.ANCHO, '\033[1m')
    print("")

    auxiliares.linea_iguales(auxiliares.ANCHO)
    auxiliares.imprimir_opcion(1, 'CREAR MEDICO', '1;33', False)
    auxiliares.imprimir_opcion(2, 'LEER MEDICOS', '1;34')
    auxiliares.imprimir_opcion(3, 'ACTUALIZAR MEDICO', '1;35')
    auxiliares.imprimir_opcion(4, 'ELIMINAR MEDICO', '1;31')
    auxiliares.imprimir_opcion(0, 'VOLVER AL MENU ANTERIOR', '1;36')

    auxiliares.linea_iguales(auxiliares.ANCHO)

    opcion = ingresar_opcion(4)
    match opcion:
        case 0: return 0
        case 1: 
            auxiliares.limpiar_terminal()
            crear_medico(matrizMeds)
        case 2: 
            auxiliares.limpiar_terminal()
            opcion = menu_leer_medicos(matrizMeds)
        case 3:
            auxiliares.limpiar_terminal()
            medico = buscar_medico_id(matrizMeds, ingresar_id())
            opcion = actu_medico(medico, medico[1])
        case 4:
            auxiliares.limpiar_terminal()
            elim_medico(matrizMeds)

    if (opcion != 0): input("\nPresione Enter para volver al menú anterior...")

    auxiliares.limpiar_terminal()
    menu_crud_medicos(matrizMeds)

def menu_estadistica_medicos(matrizMeds):
    auxiliares.linea_iguales(auxiliares.ANCHO)
    auxiliares.imprimir_un_encabezado('MENU MEDICOS > ESTADISTICA', auxiliares.ANCHO, '\033[1m')
    print("")

    auxiliares.linea_iguales(auxiliares.ANCHO)
    auxiliares.imprimir_opcion(1, 'PORCENTAJE DE MEDICOS ACTIVOS E INACTIVOS', '1;33', False)
    auxiliares.imprimir_opcion(2, 'PORCENTAJE DE MEDICOS POR ESPECIALIDAD', '1;34')
    auxiliares.imprimir_opcion(3, 'PROMEDIO DE ANTIGÜEDAD POR ESPECIALIDAD', '1;35')
    auxiliares.imprimir_opcion(0, 'VOLVER AL MENU ANTERIOR', '1;36')
    auxiliares.linea_iguales(auxiliares.ANCHO)

    opcion = ingresar_opcion(3)
    match opcion:
        case 0: return 0
        case 1: 
            auxiliares.limpiar_terminal()
            porcentaje_estado(matrizMeds)
        case 2: 
            auxiliares.limpiar_terminal()
            porcentaje_espec(matrizMeds, ingresar_espe())
        case 3:
            auxiliares.limpiar_terminal()
            prom_antig_espec(matrizMeds)

    if (opcion != 0): input("\nPresione Enter para volver al menú anterior...")
    opcion = 0

    auxiliares.limpiar_terminal()
    menu_estadistica_medicos(matrizMeds)

def menu_medicos():
    auxiliares.linea_iguales(auxiliares.ANCHO)
    auxiliares.imprimir_un_encabezado('MENU MEDICOS', auxiliares.ANCHO)
    print("")

    auxiliares.linea_iguales(auxiliares.ANCHO)
    auxiliares.imprimir_opcion(1, 'MENU DE CREACION, LECTURA, ACTUALIZACION O ELIMINACION DE MEDICOS (C.R.U.D)', '1;33', False)
    auxiliares.imprimir_opcion(2, 'MENU DE CONSULTAS ESTADISTICAS DE MEDICOS', '1;34')
    auxiliares.imprimir_opcion(0, 'VOLVER AL MENU ANTERIOR', '1;36')
    auxiliares.linea_iguales(auxiliares.ANCHO)

    opcion = ingresar_opcion(2)
    match opcion:
        case 0: return 0
        case 1: 
            auxiliares.limpiar_terminal()
            menu_crud_medicos(matrizMedicos)
        case 2: 
            auxiliares.limpiar_terminal()
            menu_estadistica_medicos(matrizMedicos)
    
    auxiliares.limpiar_terminal()
    menu_medicos()

""" MAIN """
matrizMedicos = [
    [100000, "Juan Pérez", "Traumatología", 5, 0],
    [999999, "Ataúlfo Américo Djandjikian", "Otorrinonaringología", 26, 1],
    [156904, "Fernando Guerra", "Traumatología", 10, 1],
    [777555, "Guillermo Smith", "Traumatología", 25, 1],
    [321987, "Rodrigo Rodríguez", "Urología", 5, 0]
] #ID, Nombre, Especialidad, Antiguedad, Estado

idsUsados = [100000, 999999, 156904, 777555, 321987]
crear_medicos_random(matrizMedicos, 5, idsUsados)