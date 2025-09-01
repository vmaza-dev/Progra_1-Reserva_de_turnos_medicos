# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Nicolás Seijo, Victor Maza
# Descripción: 
# Fecha de creación: 10/08/2025
# ==============================================================================

import random, fun_aux
pacientes = []
print("l")

OBRAS_SOCIALES = ["OSDE", "Swiss Medical", "VICMAZA", "Galeno", "Particular"]

# ==============================================================================
# CRUD
# ==============================================================================

def obtener_paciente_por_id(pacientes,id):
    for i in pacientes:
        if i[0] == id:
            return i
    return -1


def crear_paciente(id):
    """
    Crea un paciente por teclado solicitando los datos al usuario

    Parametros:
        id(int): id unico del paciente.

    Return:
        list: lista con los datos del paciente [id,dni,nombre,edad,obra_social,estado]
    """
    dni = validacion_dni(int(input("Ingrese su dni: ")))
    nombreCompleto = input("Ingrese su nombre completo: ")
    edad = validacion_edad(int(input("Ingrese su edad: ")))
    obra_social = input("Ingrese su obra social: ")
    estado = 1
    paciente = [id, dni, nombreCompleto, edad, obra_social, estado]
    return paciente


def crear_pacientes_random(pacientes, cantCrear):
    """
    Crea una cantidad determinada de pacientes aleatorios y los agrega a la lista.

    Parametros:
        pacientes(list): Lista donde se agregaran los pacientes.
        cantCrear: Numero de pacientes aleatorios a generar.

    Returns:
        None.
    """
    for i in range(cantCrear):
        nombreCompleto = random.choice(fun_aux.nombres) + " " + random.choice(fun_aux.apellidos)
        edad = validacion_edad(random.randint(3, 99))
        dni = generacion_dni_realista(edad)
        obra_social = random.choice(OBRAS_SOCIALES)
        estado = 1
        id = random.randint(1000, 9999)
        pacientes.append([id, dni, nombreCompleto, edad, obra_social, estado])


def imprimir_paciente(pacientes):
    """
    Muestra en pantalla los datos de los pacientes recibidos.

    Parametros:
        pacientes(list): Lista de pacientes a imprimir.

    Returns:
        None.
    """
    ancho = 60
    for pac in pacientes:
        print("=" * ancho)
        print(f" PACIENTE: {pac[2]} ".center(ancho, "="))
        print(f"ID: {str(pac[0]).ljust(10)} | DNI: {str(pac[1]).ljust(12)}")
        print(f"EDAD: {str(pac[3]).ljust(8)} | OBRA SOCIAL: {pac[4]}")
        estado_str = 'Activo ' if pac[5] == 1 else 'Inactivo '
        print(f"ESTADO: {estado_str}".center(ancho))
        print("=" * ancho + "\n")


def leer_pacientes(pacientes):
    """
    Muestra todos los pacientes en la lista utilizando imprimir_paciente().

    Parametros:
        pacientes(list): Lista de pacientes.

    Returns:
        None.
    """
    imprimir_paciente(pacientes)


def buscar_id_paciente(pacientes):
    """
    Busca un paciente por ID y muestra sus datos.

    Parametros:
        pacientes(list): Lista de pacientes.

    Returns:
        None.
    """
    id = int(input("Ingrese el ID del paciente a buscar: "))
    pac = obtener_paciente_por_id(pacientes,id)
    if pac == -1:
        print("No se encontro el paciente")
    else:
        print("\n==============================")
        print("PACIENTE ENCONTRADO")
        print("-------------------------------")
        print(f"ID: {pac[0]}")
        print(f"DNI: {pac[1]}")
        print(f"NOMBRE: {pac[2]}")
        print(f"EDAD: {pac[3]}")
        print(f"OBRA SOCIAL: {pac[4]}")
        print(f"ESTADO: {pac[5]}")
        print("==============================\n")

def actualizar_paciente(pacientes):
    """
    Permite modificar los datos de un paciente por ID.

    Parametros:
        pacientes(list): Lista de pacientes.

    Returns:
        None.
    """
    id = int(input("Ingrese el ID del paciente que desea modificar: "))
    pac = obtener_paciente_por_id(pacientes,id)
    if pac == -1:
        print("No se encontro al paciente.")
    else:
        print("INGRESE EL DATO A MODIFICAR DEL PACIENTE:")
        print("1-DNI\n2-NOMBRE\n3-EDAD\n4-OBRA SOCIAL\n5-ESTADO")
        op = int(input("Ingrese el numero de la opcion: "))
        match op:
            case 1:
                pac[1] = validacion_dni(int(input("Ingrese el nuevo DNI: ")))
            case 2:
                pac[2] = input("Ingrese el nuevo nombre: ")
            case 3:
                pac[3] = validacion_edad(int(input("Ingrese la nueva edad: ")))
            case 4:
                print("Seleccione una Obra Social válida:")
                for n in range(len(OBRAS_SOCIALES)):
                    print(f"{n+1} - {OBRAS_SOCIALES[n]}")
                while True:
                    op_obra = int(input("Ingrese el número de la obra social: "))
                    if 1 <= op_obra <= len(OBRAS_SOCIALES):
                        pac[4] = OBRAS_SOCIALES[op_obra - 1]
                        print("\nPerfil actualizado del paciente:")
                        imprimir_paciente([pac])
                        break
                    else:
                        print("Opción inválida, intente nuevamente.")
            case 5:
                pac[5] = int(input("Ingrese el nuevo Estado: "))

def eliminar_paciente(pacientes):
    """
    Elimina un paciente de la lista por su ID.

    Parametros:
        pacientes(list): Lista de pacientes.

    Returns:
        None
    """
    id = int(input("Ingrese el ID del paciente que desea eliminar: "))
    pac = obtener_paciente_por_id(pacientes, id)
    if pac == -1:
        print("El paciente no fue eliminado porque no pudo ser encontrado")
    else:
        pacientes.remove(pac)
        print("El paciente fue eliminado")

# ==============================================================================
# VALIDACIONES
# ==============================================================================


def validacion_dni(dni):
    """
    Valida que el DNI tenga 8 dígitos.

    Parametros:
        dni(int): DNI a validar.

    Returns:
        int: DNI valido.
    """
    while len(str(dni)) != 8:
        dni = int(input("DNI invalido. Ingrese un dni de 8 digitos: "))
    return dni


def validacion_edad(edad):
    """
    Valida que la edad sea entre 3 y 98 años.

    Parametros:
        edad(int): Edad a validar.

    Returns:
        int: Edad valida.
    """
    while edad < 2 or edad >= 99:
        edad = int(input("Edad invalida. Ingrese una edad entre 3 y 99: "))
    return edad


def generacion_dni_realista(edad):
    """
    Genera un DNI aproximado segun la edad del paciente.

    Parametros:
        edad(int): Edad del paciente.

    Returns:
        int: DNI generado aleatoriamente.
    """
    if 20 <= edad <= 30:
        return random.randint(43000000, 43999999)
    elif 31 <= edad <= 40:
        return random.randint(38000000, 39999999)
    elif 41 <= edad <= 50:
        return random.randint(33000000, 37999999)
    else:
        return random.randint(10000000, 32999999)
# ============================================================================== 
# ESTADISTICAS
# ==============================================================================

def promedio_edades(pacientes):
    """
    Calcula el promedio de edades de los pacientes.

    extrae la edad de cada paciente y devuelve el promedio.
    devuelve 0 si la lista de pacientes en el caso de que este vacia.

    Parametros:
        pacientes(list): Lista de pacientes, donde cada paciente es una lista que incluye la edad en la posicion 3.

    Returns:
        float: Promedio de edades.
    """
    edades = list(map(lambda p: p[3], pacientes))  # Extrae la edad de cada paciente
    return sum(edades)/len(edades) if edades else 0

def pacientes_por_obra(pacientes):
    """
    Calcula la cantidad de pacientes por cada obra social.

    Extrae la obra social de cada paciente y devuelve una lista de tuplas con el nombre de la obra y la cantidad de pacientes.

    Parametros:
        pacientes(list): Lista de pacientes, donde cada paciente es una lista que incluye la obra social en la posicion 4.

    Returns:
        list: Lista de tuplas (obra_social, cantidad)
    """
    obras = list(map(lambda p: p[4], pacientes))  # Extrae la obra social
    return list(map(lambda o: (o, len(list(filter(lambda x: x==o, obras)))), set(obras)))

def porcentaje_por_obra(pacientes):
    """
    Calcula el porcentaje de pacientes por obra social.

    Devuelve una lista de tuplas con el nombre de la obra y el porcentaje de pacientes que tienen esa obra.

    Parametros:
        pacientes(list): Lista de pacientes.

    Returns:
        list: Lista de tuplas (obra_social, porcentaje)
    """
    total = len(pacientes)
    if total == 0:
        return []
    return list(map(lambda t: (t[0], round((t[1]/total)*100, 2)), pacientes_por_obra(pacientes)))

def mostrar_estadisticas_pacientes(pacientes):
    """
    Muestra en pantalla las estadisticas de los pacientes formateado.

    Imprime promedio de edades, cantidad de pacientes por obra social y porcentaje
    de pacientes por obra social, usando colores y negrita en la terminal.

    Parametros:
        pacientes(list): Lista de pacientes.

    Returns:
        None.
    """
    default = "\033[0m"
    amarillo = "\033[33m"
    negrita = "\033[1m"

    ancho = 60
    print(f"{amarillo}{'=' * ancho}")
    print(f"{amarillo}{'ESTADÍSTICAS DE PACIENTES'.center(ancho)}{default}")
    print(f"{amarillo}{'=' * ancho}{default}\n")

    promedio = promedio_edades(pacientes)
    print(f"{'Promedio de edades:':<35}{negrita}{promedio:.2f} años{default}\n")

    lista_por_obra = pacientes_por_obra(pacientes)
    print(f"{'Cantidad de pacientes por obra social:'.center(ancho)}")
    print(f"{'-' * ancho}")
    list(map(lambda t: print(f"{t[0]:<30} {negrita}{t[1]:>5}{default}"), lista_por_obra))
    print(f"{'-' * ancho}\n")
  
    lista_porcentaje = porcentaje_por_obra(pacientes)
    print(f"{'Porcentaje de pacientes por obra social:'.center(ancho)}")
    print(f"{'-' * ancho}")
    list(map(lambda t: print(f"{t[0]:<30} {negrita}{t[1]:>5}%{default}"), lista_porcentaje))
    print(f"{amarillo}{'=' * ancho}{default}")

# ==============================================================================
# GENERACION DE NOMBRES DE USUAROI
# ==============================================================================

def generar_usuario(nombre_completo):
    """
    Genera un nombre de usuario a partir del nombre completo.

    en esta situacion toma los primeros 3 caracteres del nombre y todo el apellido, todo en minusculas.

    Parametros:
        nombre_completo(str): Nombre completo del paciente (nombre + apellido).

    Returns:
        str: Nombre de usuario generado.
    """
    partes = nombre_completo.split()
    if len(partes) < 2:
        return nombre_completo[:3].lower()  # por las dudas si solo tiene un nombre
    nombre = partes[0][:3].lower()
    apellido = partes[-1].lower()
    return nombre + apellido


def mostrar_usuarios(pacientes):
    """
    Muestra en pantalla los nombres de usuario generados para cada paciente.

    Parametros:
        pacientes(list): Lista de pacientes, donde el nombre completo esta en la posicion 2.

    Returns:
        None.
    """
    default = "\033[0m"
    rojo = "\033[31m"
    negrita = "\033[1m"
    ancho = 60

    print(f"{rojo}{'=' * ancho}{default}")
    print(f"{rojo}{'USUARIOS GENEADOS'.center(ancho)}{default}")
    print(f"{rojo}{'=' * ancho}{default}\n")

    for pac in pacientes:
        usuario = generar_usuario(pac[2])
        print(f"{pac[2]:<30} -> {negrita}{usuario:<20}{default}")

    print(f"\n{rojo}{'=' * ancho}{default}")
# ==============================================================================
# BLOQUE PRINCIPAL
# ==============================================================================

crear_pacientes_random(pacientes, 10)
leer_pacientes(pacientes)
#buscar_id_paciente(pacientes)
eliminar_paciente(pacientes)
leer_pacientes(pacientes)
#actualizar_paciente(pacientes)
