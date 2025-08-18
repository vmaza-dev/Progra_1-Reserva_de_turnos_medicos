# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Nicolás Seijo, Victor Maza
# Descripción: Sistema CRUD de Reserva de turnos médicos
# Fecha de creación: 10/08/2025
# ==============================================================================

import random

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
    
def ingresar_entero_positivo(mensaje:str) -> int:
    """
    Valida el ingreso por teclado de un número entero positivo.

    Parámetros:
        mensaje: Pedido de ingreso de datos.

    Returns:
        Número entero positivo.
    """
    bandera = True
    while bandera:
        try:
            n = int(input(f"{mensaje}"))
            while n < 0:
                print("El núemero debe ser mayor a cero")
                n = int(input(f"{mensaje}"))
            bandera = False
        except ValueError:
            print("Ingreso inválido, ingrese un número")
    return n

def ingresar_campo_str(mensaje:str) -> str:
        
    """
    Valida el ingreso por teclado de un campo.

    Valida el ingreso de un campo de tipo str, por ejemplo nombre del paciente,
    especialidad médica, etc,

    Parámetros:
        mensaje: Pedido de ingreso de datos.

    Returns:
        campo.
    """
    print("Puede un humano ganarle a un Gorila?")


def validar_fecha(d:int, m:int, a:int) -> bool | bool:
    """
    Valida si tres números enteros positivos corresponden a una fecha válida.

    Toma en cuenta anios bisiestos, meses de 30 y 31 días.

    Parámetros:
        d: Día del mes.
        m: Mes.
        a: Anio.

    Returns:
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

def crear_matriz(filas:int, columnas:int, n0:int = 0, n:int = 99) -> list[list]:
    """
    Crea una matriz con valores enteros aleatorios.

    Parámetros:
        filas: Cantidad de filas de la matriz.
        columnas: Cantidad de columnas de la matriz.
        n0: Valor mínimo aleatorio. Default = 0.
        n: Valor máximo aleatorio. Default = 99.

    Returns:
        Matriz generada.
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
        matriz: Matriz a imprimir.
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
        encabezado: Lista de títulos para las columnas.
        matriz: Datos a imprimir.
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

# ==============================================================================
# ==============================PROGRAMA PRINCIPAL==============================
# ==============================================================================

grupo6_dev_logo()

ENCABEZADO = []# Lista de títulos de la matriz de datos. Ejemplo en el googlesheet. 
ESTADO_TURNO = []# Lista de títulos de la matriz de datos. Ejemplo en el googlesheet.
ESPECIALIDAD = []# Lista de títulos de la matriz de datos. Ejemplo en el googlesheet.

