# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Nicolás Seijo, Victor Maza
# Descripción: 
# Fecha de creación: 10/08/2025
# ==============================================================================

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
    
def ingresar_entero_positivo(mensaje):
    """
    Valida el ingreso por teclado de un número entero positivo.

    Parámetros:
        mensaje(str): Pedido de ingreso de datos.

    Returns:
        Número entero positivo(int).
    """
    n = int(input(f"{mensaje}"))
    while n < 0:
        print("Ingreso inválido: El número debe ser mayor a cero")
        n = int(input(f"{mensaje}"))
    return n

def ingresar_campo_str(mensaje):
        
    """
    Valida el ingreso por teclado de un campo.

    Valida el ingreso de un campo de tipo str, por ejemplo nombre del paciente,
    especialidad médica, etc,

    Parámetros:
        mensaje(str): Pedido de ingreso de datos.

    Returns:
        campo(str).
    """
    print("Puede un humano ganarle a un Gorila?")


def validar_fecha(d, m, a):
    """
    Valida si tres números enteros positivos corresponden a una fecha válida.

    Toma en cuenta anios bisiestos, meses de 30 y 31 días.

    Parámetros:
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
                if bisiesto and d <= 29:
                    d_valido = True
                elif d <= 28:
                    d_valido = True

    # valido si la fecha es válida            
    if d_valido and m_valido and a_valido:
        f_valida = True
    return f_valida, bisiesto

def crear_matriz(filas, columnas, n0 = 0, n = 99):
    """
    Crea una matriz con valores enteros aleatorios.

    Parámetros:
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

    Parámetros:
        matriz(list[list]): Matriz a imprimir.
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            print(matriz[i][j], end = "\t")
        print()

def imprimir_datos(encabezado, matriz):
    """
    Imprime un conjunto de datos con encabezado y matriz.

    Parámetros:
        encabezado(list): Lista de títulos para las columnas.
        matriz(list[list]): Datos a imprimir.
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    for titulo in encabezado:
        print(titulo, end = "\t")
    print()
    for i in range(filas):
        for j in range(columnas):
            print(matriz[i][j], end = "\t")
        print()

