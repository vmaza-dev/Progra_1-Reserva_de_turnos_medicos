# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Nicolás Seijo, Victor Maza
# Descripción: 
# Fecha de creación: 10/08/2025
# ==============================================================================

import random, fun_aux
print("l")

OBRAS_SOCIALES = ["OSDE", "Swiss Medical", "VICMAZA", "Galeno", "Particular"]

# ==============================================================================
# CRUD
# ==============================================================================

# Crear paciente
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

# Crear pacientes random
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

# Imprimir paciente(s)
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

# Leer pacientes
def leer_pacientes(pacientes):
    """
    Muestra todos los pacientes en la lista utilizando imprimir_paciente().

    Parametros:
        pacientes(list): Lista de pacientes.

    Returns:
        None.
    """
    imprimir_paciente(pacientes)

# Buscar id de paciente
def buscar_id_paciente(pacientes):
    """
    Busca un paciente por ID y muestra sus datos.

    Parametros:
        pacientes(list): Lista de pacientes.

    Returns:
        None.
    """
    id = int(input("Ingrese el ID del paciente a buscar: "))
    encontrado = False
    i = 0
    while i < len(pacientes) and not encontrado:
        pac = pacientes[i]
        if pac[0] == id:
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
            encontrado = True
        i += 1
    if not encontrado:
        print("No se encontro al paciente")

# Actualizar paciente
def actualizar_paciente(pacientes):
    """
    Permite modificar los datos de un paciente por ID.

    Parametros:
        pacientes(list): Lista de pacientes.

    Returns:
        None.
    """
    id = int(input("Ingrese el ID del paciente que desea modificar: "))
    encontrado = False
    i = 0
    while i < len(pacientes) and not encontrado:
        pac = pacientes[i]
        if pac[0] == id:
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
                            imprimir_paciente([pac])  # Pasamos lista con un solo paciente
                            break
                        else:
                            print("Opción inválida, intente nuevamente.")
                case 5:
                    pac[5] = int(input("Ingrese el nuevo Estado: "))
            encontrado = True
        else:
            i += 1
    if not encontrado:
        print("No se encontro al paciente")

# Eliminar paciente
def eliminar_paciente(pacientes):
    """
    Elimina un paciente de la lista por su ID.

    Parametros:
        pacientes(list): Lista de pacientes.

    Returns:
        None
    """
    id = int(input("Ingrese el ID del paciente que desea eliminar: "))
    encontrado = False
    i = 0
    while i < len(pacientes) and not encontrado:
        if pacientes[i][0] == id:
            pacientes.pop(i)
            encontrado = True
        else:
            i += 1
    if encontrado:
        print("El paciente fue eliminado")
    else:
        print("El paciente no fue eliminado porque no pudo ser encontrado")

# ==============================================================================
# VALIDACIONES
# ==============================================================================

# Validación de DNI
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

# Validación de edad
def validacion_edad(edad):
    """
    Valida que la edad sea entre 3 y 98 años.

    Parametros:
        edad(int): Edad a validar.

    Returns:
        int: Edad valida.
    """
    while edad < 3 or edad >= 99:
        edad = int(input("Edad invalida. Ingrese una edad entre 3 y 99: "))
    return edad

# Generación de DNI realista
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
# BLOQUE PRINCIPAL
# ==============================================================================

pacientes = []
crear_pacientes_random(pacientes, 10)
leer_pacientes(pacientes)
# #buscar_id_paciente(pacientes)
# #eliminar_paciente(pacientes)
leer_pacientes(pacientes)
# actualizar_paciente(pacientes)
