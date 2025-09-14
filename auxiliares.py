# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Nicolás Seijo, Victor Maza
# Descripción: Funciones auxiliares comunes a todos los módulos.
# Fecha de creación: 10/08/2025
# ==============================================================================


nombres = [
    "Nicolás", "Victor", "Agustín", "Simon", "Juan Manuel", "Mateo", "Valentino", "Benicio", 
    "Noah", "Lorenzo", "Julián", "María Jesús", "Jesús María", "Ciro", "Dante","Agustín", "Facundo",
    "Santiago", "Jonathan", "Joseph", "Judas", "Gerónimo", "Lionel", "Dibu", "Dana", "Gildo", "Alan",
    "Martina", "Catalina", "Emma", "Olivia", "Isabella", "Delfina", "Julieta", "Daniel", "Eduardo",
    "Alma", "Joaquín", "Franco", "Thiago", "Bautista", "Sofía", "Emilia", "Renata", "Valentina", "Pilar",
    "Lautaro", "Tiziano", "Gael", "Tomás", "Francisco", "Lisandro", "Ramiro", "Ignacio", "Luciano",
    "Fausto", "León", "Lucio", "Santino", "Lionel", "Lucas", "Nicolás", "Camilo", "Manuel", "Sebastián",
    "Juan","Pedro", "Pablo", "Alejandro", "Elias", "Amadeo", "Francisco", "Gianluca", "Milagros",
    "Victoria", "Josefina","Rufina", "Amparo", "Refugio", "Paz", "Lara", "Luna", "Malena", "Remedios",
    "Bruna", "Luz","Melody", "Azul", "Constanza", "Eva", "India", "Paulina", "Greta", "Vera", "Xiomara",
    "Abril", "Ariadna", "Ailén", "Aurora", "Gianna", "Juana", "Nina", "Rosario", "Agostina", "Aline", 
    "Celina", "Guillermina", "Jesús", "Vitto", "Salvador", "Ignacio", "Amelie", "Aitana", "Alana",
    "Brisa", "Iñaki", "Esteban", "Obi Wan", "John", "Anakin", "Arthas", "Guido", "Rick", "Jose Joaquín"
]

apellidos = [
    "González", "Rodríguez", "Gómez", "Fernández", "López", "Joestar", "Iscariote",
    "Martínez", "Díaz", "Pérez", "Sánchez", "Romero", "Benávidez", "Messi",
    "García", "Sosa", "Benítez", "Ramírez", "Ruiz", "Isfrán", "Parisini",
    "Torres", "Flores", "Álvarez", "Acosta", "Rojas", "Guerrero", "Zapatero", "Caballero",
    "Silva", "Nuñez", "Luna", "Juarez", "Cabrera", "Avellaneda", "del Corazón de Jesús Belgrano",
    "Rios", "Morales", "Godoy", "Moreno", "Ferreyra", "Brito",
    "Dominguez", "Carrizo", "Peralta", "Castillo", "Ledesma",
    "Quiroga", "Vega", "Vera", "Muñoz", "Ojeda",
    "Ponce", "Villalba", "Cardozo", "Navarro", "Coronel",
    "Vazquez", "Ramos", "Vargas", "Caceres", "Arias",
    "Figueroa", "Cordoba", "Correa", "Maldonado", "Paz",
    "Rivero", "Miranda", "Mansilla", "Farias", "Roldan",
    "Mendez", "Guzmán", "Aguero", "Hernández", "Lucero",
    "Cruz", "Paez", "Escobar", "Mendoza", "Barrios", "Diaz"
    "Bustos", "Avila", "Ayala", "Blanco", "Soria",
    "Maidana", "Acuña", "Leiva", "Duarte", "Moyano",
    "Campos", "Iturria", "Maza", "Seijo", "Aliano",
    "Escándalo", "Quito", "Gimenez", "Herrera", "Suárez",
    "Aguirre", "Gutiérrez", "Pereyra", "Molina", "Castro", "Grimes",
    "Ortiz", "Perez", "Cisterna", "Ferro", "Connor", "Kenobi", "Skywalker", "Menethil", "Van Rossum"
]

especialidades = ["Clínica Médica", "Psiquiatría", "Urología", "Traumatología"]

import random, re
ANCHO = 111

def limpiar_terminal():
    """
    Limpia la terminal usando un código ANSI de escape.

    Imprime el carácter especial "\033c" que reinicia la pantalla de la terminal.
    """

    print("\033c")

def grupo6_dev_logo():
    """
    Imprime logo personalizado.
    """

    limpiar_terminal()

    print(r"""
  ____  __         ____                                      _         
 / ___|/ /_    _  |  _ \ ___  ___  ___ _ ____   ____ _    __| | ___    
| |  _| '_ \  (_) | |_) / _ \/ __|/ _ \ '__\ \ / / _` |  / _` |/ _ \   
| |_| | (_) |  _  |  _ <  __/\__ \  __/ |   \ V / (_| | | (_| |  __/   
 \____|\___/  (_) |_| \_\___||___/\___|_|    \_/ \__,_|_ \__,_|\___|   
| |_ _   _ _ __ _ __   ___  ___   _ __ ___   /_/  __| (_) ___ ___  ___ 
| __| | | | '__| '_ \ / _ \/ __| | '_ ` _ \ / _ \/ _` | |/ __/ _ \/ __|
| |_| |_| | |  | | | | (_) \__ \ | | | | | |  __/ (_| | | (_| (_) \__ \
 \__|\__,_|_|  |_| |_|\___/|___/ |_| |_| |_|\___|\__,_|_|\___\___/|___/
""")

def linea_iguales(ancho):
    print("="*ancho)

def linea_guiones(ancho):
    print("-"*ancho)

def imprimir_opcion(opcion, texto, colorOpcion='', guiones=True, colorTexto=''):
    if (guiones):
        linea_guiones(ANCHO)

    textoImprimir = f"\033[{colorOpcion}m[{opcion}]\033[0m: \033[{colorTexto}m{texto}\033[0m"
    espacios = len(textoImprimir) - len(f"[{opcion}]: {texto}")
    print(f"| " + textoImprimir.ljust(ANCHO-4) + " " * espacios, end=" |\n")

def imprimir_tres_encabezados(encab1, encab2, encab3, color1="", color2="", color3=""):
    """
    Imprime tres encabezados especificados, con un color específicado para cada uno (o nada, si no se ingresa).

    Parametros:
        encab1(str): Primer encabezado a imprimirse.
        encab2(str): Segundo encabezado a imprimirse.
        encab3(str): Tercer encabezado a imprimirse.

        color1(str): Color a aplicar al primer encabezado.
        color2(str): Color a aplicar al segundo encabezado.
        color3(str): Color a aplicar al tercer encabezado.

    Flujo: 
        - Llama a la función 'imprimir_un_encabezado()' para imprimir cada encabezado, se le envía el ancho '37' ya que es 1/3 de '111
    """

    imprimir_un_encabezado(encab1, 37, color1)
    imprimir_un_encabezado(encab2, 37, color2)
    imprimir_un_encabezado(encab3, 37, color3)

    print("")

def imprimir_un_encabezado(encab, anchoEncab, color=""):
    """
    Imprime un encabezado especificado centrado en el ancho total, con un color también específicado (o nada, si no se ingresa).

    Parametros:
        encab(str): Encabezado a imprimirse.
        color(str): Color a aplicar al encabezado.

    Flujo: 
        - Imprime 'encab' centrado en ANCHO-4 y coloreandolo de 'color'
    """
    print(f"| {color}{encab.center(anchoEncab-4)}\033[0m", end=" |")

def ingresar_entero_positivo(mensaje):
    """
    Valida el ingreso por teclado de un número entero positivo.
    
    Args:
        mensaje(str): Pedido de ingreso de datos.

    Returns:
        Número entero positivo(int).
    """
    numero = ingresar_respuesta_str(mensaje)
    numero_valido = False
    while numero_valido  == False:
        # valido que no ingrese letras
        if re.findall("[a-zA-Z]", numero):
            print("Ingrese una opción válida")
            numero= ingresar_respuesta_str("")
        # valido que no espacios ni ingreso vacio    
        elif re.findall("[\s]", numero) or numero == "":
            print("Ingrese una opción válida")
            numero= ingresar_respuesta_str("")
        # valido que no sea negativo   
        elif int(numero) <= 0:
            print("Ingrese una opción válida")
            numero = ingresar_respuesta_str("")
        else:
            numero_valido = True
    return int(numero)

def ingresar_respuesta_str(mensaje):
        
    """
    Permite el ingreso de un respuesta a un prompt.

    Permite el ingreso de una respuesta de tipo str, por ejemplo nombre del paciente,
    especialidad médica, s/n, etc,

    Args:
        mensaje(str): Pedido de ingreso de datos.

    Returns:
        respuesta(str).
    """
    rta = input(mensaje)
    return rta

def imprimir_lista_opciones(mi_lista, num = False, contador = 0):
    """
    Imprime los elementos de una lista de opciones.
    
    Admite la numeración de los elementos.

    Args:
        mi_lista(list): Lista de elementos.
        num(bool):
            False: Por defecto. Omite numeración
            True: Opcional. Numera los elementos
        contador(int): Inicio de la numeración. Por defecto 0.

    Returns:
    """
    if num:
        for i in mi_lista:
            contador += 1
            igual = "="*20
            print(f"{igual:^40}")
            texto = f"{contador}: {i}"
            print(f"{texto:^40}", end="\n")
            print(f"{igual:^40}")
    else:
        for i in mi_lista:
            igual = "="*20
            print(f"{igual:^40}")
            texto = f"{i}"
            print(f"{texto:^40}", end="\n")
            print(f"{igual:^40}")       

    print("")

def imprimir_lista(mi_lista, num = False, contador = 0):
    """
    Imprimme los elementos de una lista tabulados.
    
    Admite la numeración de los elementos.

    Args:
        mi_lista(list): Lista de elementos.
        num(bool):
            False: Por defecto. Omite numeración
            True: Opcional. Numera los elementos
        contador(int): Inicio de la numeración. Por defecto 0.

    Returns:
    """
    if num:
        for i in mi_lista:
            contador += 1
            print(f"{contador}: {i}", end=" ")
    else:
        for i in mi_lista:
            print(i, end=" ")        

    print("")

def validar_fecha(d, m, a):
    """
    Valida si tres números enteros positivos corresponden a una fecha válida.

    Toma en cuenta anios bisiestos, meses de 30 y 31 días.

    Args:
        d(int): Día del mes.
        m(int): Mes.
        a(int): Anio.

    Returns:
        bool
        - True si los tres número corresponden a una fecha válida. False si 
        alguno/todos hacen inválida a la fecha.
        - True si el año es bisiesto. False si el año no es bisiesto 
    """
    a_valido = False
    d_valido = False
    m_valido = False
    f_valida = False

    # valido anio
    bisiesto = False
    if a > 1582:
        a_valido = True
        if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
            bisiesto = True
            
    # valido mes
    if m > 0 and m <= 12:
        m_valido = True

    # valido día
    if 1 <= d <= 31 and m_valido:
        match m:
            case 1|3|5|7|8|10|12:
                    d_valido = True
            case 4|6|9|11:
                if d <= 30:
                    d_valido = True
            case 2:
                if (bisiesto and d <= 29) or (not bisiesto and d <= 28):
                    d_valido = True

    # valido si la fecha es válida            
    if d_valido and m_valido and a_valido:
        f_valida = True

    return f_valida, bisiesto

def crear_matriz(filas, columnas, n0 = 0, n = 99):
    """
    Crea una matriz con valores enteros aleatorios.

    Args:
        filas(int): Cantidad de filas de la matriz.
        columnas(int): Cantidad de columnas de la matriz.
        n0(int): Valor mínimo aleatorio. Default = 0.
        n(int): Valor máximo aleatorio. Default = 99.

    Returns:
        Matriz generada(list[list])
    """

    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            valor = random.randint(n0, n)
            matriz[i].append(valor)

    return matriz

def imprimir_matriz(matriz):
    """
    Imprime la matriz en formato tabulado.

    Args:
        matriz(list[list]): Matriz a imprimir.
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            print(matriz[i][j], end = "\t")
        print()

def transponer_matriz(matriz):
    """
    Transpone una matriz dada.
    
    Args:
    
    Returns:
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta = [[0] * filas for i in range(columnas)]
    for i in range(filas):
        for j in range(columnas):
            transpuesta[j][i] = matriz[i][j]
    return transpuesta

def imprimir_datos(encabezado, matriz):
    """
    Imprime un conjunto de datos con encabezado y matriz.

    Args:
        encabezado(list): Lista de títulos para las columnas.
        matriz(list[list]): Datos a imprimir.
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    for titulo in encabezado:
        print(f"{titulo}", end="\t")
    print()
    for i in range(filas):
        for j in range(columnas):
            print(f"{matriz[i][j]}", end = "\t")
        print()


