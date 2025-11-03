# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Nicolás Seijo, Victor Maza
# Descripción: 
# Fecha de creación: 10/08/2025
# ==============================================================================

import random, auxiliares, re, json, os
pacientes = []
print("l")

OBRAS_SOCIALES = ["OSDE", "Swiss Medical", "VICMAZA", "Galeno", "Particular"]

# ==============================================================================
# CARGA DE JSON 
# ==============================================================================

def cargar_pacientes_json(archivo_json="arch_pacientes.json"):
    """
    Carga la lista de pacientes desde el archivo JSON.
    Maneja excepciones si el archivo no existe o está corrupto.
    """
    if not os.path.exists(archivo_json):
        print("Advertencia: No se encontró 'arch_pacientes.json'.")
        # Si no existe, llamamos al fallback para crear datos de prueba
        return inicializar_pacientes_random() 

    try:
        with open(archivo_json, 'r', encoding='utf-8') as f:
            datos = json.load(f)
            if not datos: # Chequea si el JSON está vacío (ej: "[]")
                 print("Advertencia: 'arch_pacientes.json' está vacío.")
                 return inicializar_pacientes_random()
            print(f"Se cargaron {len(datos)} pacientes desde '{archivo_json}'.")
            return datos
            
    except json.JSONDecodeError:
        print(f"Error: El archivo '{archivo_json}' está mal formateado (corrupto).")
        # Si está corrupto, mejor no arriesgarse.
        return inicializar_pacientes_random()
    except Exception as e:
        print(f"Error inesperado al cargar el JSON: {e}")
        return inicializar_pacientes_random()

def guardar_pacientes_json(pacientes_a_guardar, archivo_json="arch_pacientes.json"):
    """
    Guarda la lista de pacientes actual en el archivo JSON.
    Usa indent=4 para que sea legible.
    """
    try:
        with open(archivo_json, 'w', encoding='utf-8') as f:
            # indent=4 es clave para que el JSON quede prolijo
            json.dump(pacientes_a_guardar, f, indent=4, ensure_ascii=False)
        print(f"Datos guardados exitosamente en '{archivo_json}'.")
    except IOError as e:
        print(f"Error al escribir en el archivo JSON: {e}")
    except Exception as e:
        print(f"Error inesperado al guardar el JSON: {e}")

# ==============================================================================
# CRUD
# ==============================================================================

def obtener_paciente_por_id(pacientes,id):
    for i in filter(lambda p: p['id'] == id, pacientes):
        return i
    return -1

def crear_paciente(id):
    """
    Crea un paciente por teclado solicitando los datos al usuario

    Args:
        id(int): id unico del paciente.

    Return:
        diccionario: dicc. con los datos del paciente {id,dni,nombre,edad,obra_social
    """
    dni = validacion_dni(auxiliares.pedir_valor("Ingrese su DNI: ", int))
    while True:
        try:
            nombreCompleto = input("Ingrese su nombre completo: ").strip()
            if not nombreCompleto:
                raise ValueError("El nombre no puede estar vacío")

            if not all(c.isalpha() or c.isspace() for c in nombreCompleto):
                raise ValueError("El nombre solo puede contener letras y espacios")
            break
        except ValueError as e:
            print(f"Error: {e}")
    edad = validacion_edad(auxiliares.pedir_valor("Ingrese su edad: ", int))
    while True:
        try:
            obra_social = input("Ingrese su obra social: ").strip()
            if obra_social not in OBRAS_SOCIALES:
                raise ValueError(f"Obra social inválida. Opciones válidas: {', '.join(OBRAS_SOCIALES)}")
            break
        except ValueError as e:
            print(f"Error: {e}")
    paciente = {
        'id': id,
        'dni': dni,
        'nombre': nombreCompleto,
        'edad': edad,
        'obra_social': obra_social
    }

    return paciente

def crear_pacientes_random(pacientes, cantCrear):
    """
    Crea una cantidad determinada de pacientes aleatorios y los agrega a la lista.

    Args:
        pacientes (list[dict]): Lista donde se agregaran los pacientes.
        cantCrear (int): Numero de pacientes aleatorios a generar.

    Returns:
        None.
    """
    for i in range(cantCrear):
        nombreCompleto = random.choice(auxiliares.nombres) + " " + random.choice(auxiliares.apellidos)
        edad = validacion_edad(random.randint(3, 98))
        dni = generacion_dni_realista(edad)
        obra_social = random.choice(OBRAS_SOCIALES)
        id = id_unico(pacientes)
        
        pacientes.append({'id': id, 'dni': dni, 'nombre': nombreCompleto, 'edad': edad, 'obra_social': obra_social})

def imprimir_paciente(pacientes):
    """
    Muestra en pantalla los datos de los pacientes recibidos.

    Args:
        pacientes (list[dict]): Lista de pacientes a imprimir.

    Returns:
        None.
    """
    if not pacientes:
        print("No hay pacientes para mostrar.")
        return
    print("=" * 104)
    print(f"| {'ID'.ljust(6)} | {'NOMBRE'.ljust(40)} | {'DNI'.ljust(20)} | {'EDAD'.ljust(10)} | {'OBRA SOCIAL'.center(12)} |")
    print("=" * 104)

    for pac in pacientes:
        print(f"| {str(pac['id']).ljust(6)} |", end="")
        print(f"\033[1m{pac['nombre'].ljust(41)}\033[0m |", end="")
        print(f"{str(pac['dni']).ljust(21)} |", end="")
        if pac["edad"] > 60:
            print(f"\033[33m{str(pac['edad']).ljust(11)}\033[0m |", end="")
        else:
            print(f"{str(pac['edad']).ljust(11)} |", end="")
        print(f"\033[1;32m{pac['obra_social'].center(13)}\033[0m |")
    
    print("=" * 104)

def leer_pacientes(pacientes):
    """
    Muestra todos los pacientes en la lista utilizando imprimir_paciente().

    Args:
        pacientes (list[dict]): Lista de pacientes.

    Returns:
        None.
    """
    imprimir_paciente(pacientes)

def buscar_id_paciente(pacientes):
    """
    Busca un paciente por ID y muestra sus datos.

    Args:
        pacientes (list[dict]): Lista de pacientes.

    Returns:
        None.
    """
    id = auxiliares.pedir_valor("Ingrese el ID del paciente a buscar: ", int)
    pac = obtener_paciente_por_id(pacientes,id)
    if pac == -1:
        print("No se encontro el paciente")
    else:
        print("\n==============================")
        print("PACIENTE ENCONTRADO")
        print("-------------------------------")
        print(f"ID: {pac['id']}")
        print(f"DNI: {pac['dni']}")
        print(f"NOMBRE: {pac['nombre']}")
        print(f"EDAD: {pac['edad']}")
        print(f"OBRA SOCIAL: {pac['obra_social']}")
        print("==============================\n")

def actualizar_paciente(pacientes):
    """
    Permite modificar los datos de un paciente por ID.
    Incluye validacion de obra social.

    Args:
        pacientes (list[dict]): Lista de pacientes.
    """

    print("\n=== LISTADO DE PACIENTES DISPONIBLES ===")
    imprimir_paciente(pacientes)
    
    id = auxiliares.pedir_valor("Ingrese el ID del paciente que desea modificar: ", int)
    pac = obtener_paciente_por_id(pacientes,id)
    if pac == -1:
        print("No se encontro al paciente.")
    else:
        print("INGRESE EL DATO A MODIFICAR DEL PACIENTE:")
        print("1-DNI\n2-NOMBRE\n3-EDAD\n4-OBRA SOCIAL")
        op = auxiliares.pedir_valor("Ingrese el numero de la opcion: ", int, True, opciones=[1,2,3,4])
        match op:
            case 1:
                pac['dni'] = validacion_dni(auxiliares.pedir_valor("Ingrese el nuevo DNI: ", int))
            case 2:
                while True:
                    try:
                        nombre = input("Ingrese el nuevo nombre: ").strip()
                        assert nombre != "", "El nombre no puede estar vacio"
                        pac['nombre'] = nombre
                        break 
                    except AssertionError as e:
                        print(f"Error: {e}. Intente nuevamente.")
            case 3:
                pac['edad'] = validacion_edad(auxiliares.pedir_valor("Ingrese la nueva edad: ", int))
            case 4:
                print("Seleccione una Obra Social valida:")
                for n in range(len(OBRAS_SOCIALES)):
                    print(f"{n+1} - {OBRAS_SOCIALES[n]}")
                op_obra = 0
                while op_obra < 1 or op_obra > len(OBRAS_SOCIALES):
                    op_obra = auxiliares.pedir_valor("Ingrese el numero de la obra social: ", int, True, opciones=list(range(1, len(OBRAS_SOCIALES)+1)))
                    if op_obra < 1 or op_obra > len(OBRAS_SOCIALES):
                        print("Opcion invalida, intente nuevamente.")
                pac['obra_social'] = OBRAS_SOCIALES[op_obra - 1]
                print("Perfil actualizado del paciente:")
                imprimir_paciente([pac])

def eliminar_paciente(pacientes):
    """
    Elimina un paciente de la lista por su ID.
    Muestra un listado previo para facilitar la eleccion.
    
    Args:
        pacientes (list[dict]): Lista de pacientes.
    """
    print("=== LISTADO DE PACIENTES DISPONIBLES ===")
    imprimir_paciente(pacientes)
    id = auxiliares.pedir_valor("Ingrese el ID del paciente a eliminar: ", int)
    pac = obtener_paciente_por_id(pacientes, id)
    if pac == -1:
        print("El paciente no fue eliminado porque no pudo ser encontrado.")
        return
    else:
        archivo = "bajas_pacientes.txt"
        try:
            arch = open(archivo, "a", encoding="UTF-8")
            linea = f"ID: {pac['id']} - NOMBRE: {pac['nombre']} - DNI: {pac['dni']} - EDAD:{pac['edad']} - OBRA SOCIAL: {pac['obra_social']}\n"
            arch.write(linea)
        except OSError:
            print("No se pudo abrir el archivo ni guardar el paciente eliminado")
            return
        finally:
            try:
                arch.close()
            except OSError:
                print("Error al cerrar el archivo")
                
        pacientes.remove(pac)
        print(f"Paciente '{pac['nombre']}' eliminado correctamente.")


# ==============================================================================
# VALIDACIONES
# ==============================================================================
def id_unico(pacientes):
    """
    Genera un ID aleatorio y que no se repite (onico).

    Args:
        pacientes (list[dict]): Lista de pacientes.

    Returns:
        int: ID de 4 digitos
    """
    existe = True
    id = random.randint(1000,9999)
    while existe:
        existe = False
        for i in pacientes:
            if i['id'] == id:
                existe = True
                id = random.randint(1000,9999)
    return id

def validacion_dni(dni):
    """
    Valida que el DNI tenga 8 digitoS
    
    Args:
        dni (int | str): DNI a validar.
    
    Returns:
        int: DNI válido.
    """
    patron = r"^\d{8}$"
    while True:
        try:
            dni_str = str(dni)
            if not re.match(patron, dni_str):
                raise ValueError(f"DNI inválido: {dni}")
            return int(dni_str)
        except ValueError as e:
            print(f"Error: {e}")
            dni = auxiliares.pedir_valor("Ingrese un DNI válido (8 dígitos): ", int)

def validacion_edad(edad):
    """
    Valida que la edad este entre 3 y 98
    
    Args:
        edad (int): Edad a validar.
    
    Returns:
        int: Edad válida.
    """
    while True:
        try:
            if edad < 3 or edad > 98:
                raise ValueError(f"Edad inválida: {edad}")
            return edad
        except ValueError as e:
            print(f"Error: {e}")
            edad = auxiliares.pedir_valor("Ingrese una edad válida (3-98): ", int)

def generacion_dni_realista(edad):
    """
    Genera un DNI aproximado segun la edad del paciente.

    Args:
        edad (int): Edad del paciente.

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

    extrae la edad de cada paciente (usando la clave edad) y devuelve el promedio.
    Devuelve 0 si la lista de pacientes en el caso de que este vacia.

    Args:
        pacientes (list[dict]): Lista de pacientes, donde cada paciente es un diccionario
                                que incluye la clave 'edad'.

    Returns:
        float: Promedio de edades.
    """
    edades = list(map(lambda p: p['edad'], pacientes))
    return sum(edades)/len(edades) if edades else 0

def pacientes_por_obra(pacientes):
    """
    Calcula la cantidad de pacientes por cada obra social.

    Extrae la obra social (clave 'obra_social') de cada paciente y devuelve
    una lista de tuplas con el nombre de la obra y la cantidad de pacientes.

    Args:
        pacientes (list[dict]): Lista de pacientes, donde cada paciente es un diccionario
                                que incluye la clave 'obra_social'.

    Returns:
        list[tuple]: Lista de tuplas (obra_social, cantidad)
    """
    obras = list(map(lambda p: p['obra_social'], pacientes))
    return list(map(lambda o: (o, len(list(filter(lambda x: x==o, obras)))), set(obras)))

def porcentaje_por_obra(pacientes):
    """
    Calcula el porcentaje de pacientes por obra social.

    Devuelve una lista de tuplas con el nombre de la obra y el porcentaje de pacientes que tienen esa obra.

    Args:
        pacientes (list[dict]): Lista de pacientes.

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

    Args:
        pacientes (list[dict]): Lista de pacientes.

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
# GENERACION DE NOMBRES DE USUARIO
# ==============================================================================

def generar_usuario(nombre_completo):
    """
    Genera un nombre de usuario a partir del nombre completo.

    en esta situacion toma los primeros 3 caracteres del nombre y todo el apellido, todo en minusculas.

    Args:
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

    Args:
        pacientes (list[dict]): Lista de pacientes, donde cada paciente es un diccionario
                                que incluye la clave 'nombre'.

    Returns:
        None.
    """
    default = "\033[0m"
    rojo = "\033[31m"
    negrita = "\033[1m"
    ancho = 60

    print(f"{rojo}{'=' * ancho}{default}")
    print(f"{rojo}{'USUARIOS GENERADOS'.center(ancho)}{default}")
    print(f"{rojo}{'=' * ancho}{default}\n")

    for pac in pacientes:
        usuario = generar_usuario(pac['nombre'])
        print(f"{pac['nombre']:<30} -> {negrita}{usuario:<20}{default}")

    print(f"\n{rojo}{'=' * ancho}{default}")
# ==============================================================================
# BLOQUE PRINCIPAL
# ==============================================================================

#### lo puse dentro de una funcion para poder llamarlo en main
# comenté las otras funciones para que no se ejecuten, cuando estaban
# sueltas y arrancaba el main importando este módulo ejecutaba todas la 
# funciones por eso se pisaban entre sí

def inicializar_pacientes_random():
    """
     la lista global 'pacientes' se llena con 10 registros aleatorios.

    Returns:
        list[dict]: La lista global de pacientes ya inicializada.
    """
    crear_pacientes_random(pacientes, 10)
    return pacientes

def principal_pacientes(pacientes):
    """
    Ejecuta el menú principal del módulo de Pacientes.

    Args:
        pacientes (list[dict]): La lista de pacientes sobre la cual operar.
    
    Returns:
        list[dict]: La lista de pacientes con las modificaciones realizadas.
    """
    opcion_p ="-1"
    while opcion_p != "0":
        valida = False
        while not valida:
            opciones = 6

            auxiliares.linea_iguales(auxiliares.ANCHO)
            auxiliares.imprimir_un_encabezado('MENU PACIENTES', auxiliares.ANCHO)
            print("")

            auxiliares.linea_iguales(auxiliares.ANCHO)
            auxiliares.imprimir_opcion(1, 'CREAR PACIENTE', '1;32', False)
            auxiliares.imprimir_opcion(2, 'LEER PACIENTES', '1;34')
            auxiliares.imprimir_opcion(3, 'ACTUALIZAR PACIENTE', '1;33')
            auxiliares.imprimir_opcion(4, 'ELIMINAR PACIENTE', '1;31')
            auxiliares.imprimir_opcion(5, 'ESTADISTICAS', '1;35')
            auxiliares.imprimir_opcion(6, 'MOSTRAR USUARIOS', '1;97')
            auxiliares.imprimir_opcion(0, 'SALIR DEL PROGRAMA', '1;36')
            auxiliares.linea_iguales(auxiliares.ANCHO)

            try:
                opcion_p = input("Seleccione una opcion: ").strip()
                assert opcion_p in [str(i) for i in range(0, opciones + 1)], "Opcion invalida"
                valida = True
            except AssertionError as e:
                input(f"Error: {e}. Presione intro para volver a seleccionar.")

            if opcion_p == "1":
                pac_id = id_unico(pacientes)
                nuevo = crear_paciente(pac_id)
                pacientes.append(nuevo)
                print("\nPaciente creado correctamente:")
                imprimir_paciente([nuevo])

            elif opcion_p == "2":
                leer_pacientes(pacientes)
                input("\nPresione Enter para volver al menú...")

            elif opcion_p == "3":
                actualizar_paciente(pacientes)
                
            elif opcion_p == "4":
                eliminar_paciente(pacientes)
                
            elif opcion_p == "5":
                mostrar_estadisticas_pacientes(pacientes)

            elif opcion_p == "6":
                mostrar_usuarios(pacientes)
                input("\nPresione Enter para volver al menú...")

    return pacientes

#pacientes = cargar_pacientes_json() 
#pacientes_actualizados = principal_pacientes(pacientes)
#guardar_pacientes_json(pacientes_actualizados)