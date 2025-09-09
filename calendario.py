# ==============================================================================
# Autor: Victor Maza
# Descripción: Adaptación como módulo del ejercicio 8 TP1 Funciones 
# Fecha de creación: 03/09/2025
# ==============================================================================

# ==============================================================================
# Función del módulo: Imprimir calendario completo de un mes dado.
# ==============================================================================

import auxiliares
from datetime import date

def dia_siguiente(d, m, a, b = False):
    """
    Calcula la fecha siguiente a una fecha dada. 

    Args:
        d: Día inicial.
        m: Mes inicial.
        a: Año inicial.
        b: Año bisiesto. Default: False
    
    Returns:
        - Nuevo día.
        - Nuevo mes si se pasó al siguiente.
        - Nuevo año si se pasó al siguiente.
    """
    d += 1
    match m:
        case 1|3|5|7|8|10:
            if d > 31:
                d = 1
                m += 1
        case 12:
            if d > 31:
                d = 1
                m = 1
                a += 1            
        case 4|6|9|11:
            if d > 30:
                d = 1
                m += 1        
        case 2:
            if (b and d > 29) or (not b and d > 28):
                d = 1
                m += 1
    
    return d, m, a

def dia_de_la_semana(dia, mes, anio):
    """
    Devuelve el día correspondiente a la fecha recibida.

    Recibe una fecha en formato día, mes y año. Informa el día de la semana
    en forma numérica creciente teniendo como referencia al domingo como cero.
    Esta función implementa la congruencia de Zeller. Tener en cuenta que ya
    contempla los años bisiestos.

    Args:
        dia: Día del mes.
        mes: Mes.
        anio: Anio
    
    Returns:
        Un entero en el rango 0-7.
    """
    if mes < 3:
        mes = mes + 10
        anio = anio - 1
    else:
        mes = mes - 2

    siglo = anio // 100
    anio2 = anio % 100
    diasem = (((26*mes-2)//10)+dia+anio2+(anio2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7

    # Ajuste para que 0 sea lunes, recordar que -1%7 es 6!
    # diasem = (diasem - 1) % 7

    return diasem

def imprimir_calendario(calendario, mes, anio) :
    """
    Imprime por pantalla la matriz recibida.

    Args:
        calendario: Matriz con dias de samana.
    """

    n_dia_semana = ["Domingo", "Lunes", "Martes","Miércoles", 
                    "Jueves", "Viernes","Sábado"]
    titulo = f"{mes} {anio}"
    print(f"{titulo:^100}", "\n")
    for dia_semana in n_dia_semana:
        print(f"{dia_semana:<10}", end="\t")

    for semana in range(len(calendario)):
        print()
        for dia in calendario[semana]:
            print(f"{dia:<10}", end="\t")
        
        print() 

def mes_a_palabras(mes):
    """
    Recibe el mes en número y lo devuelve en una palabra.

    Args:
        mes: Mes en número.
    
    Returns:
        Mes en una palabra.
    """
    mes_palabra = ["enero", "febrero","marzo", "abril",
                   "mayo", "junio","julio", "agosto",
                   "septiembre", "octubre","noviembre", "diciembre"]
    
    return mes_palabra[mes - 1]

def calendario_mes(mes, anio):
    """
    Crea e imprime un calendario del mes actual

    Args:
    
    Returns:
        Matriz con los días del mes.
    """

    semanas = 6
    dias_semana = 7
    calendario_mes = []
    # creo la matriz vacía
    for semana in range(semanas):
        calendario_mes.append([" "]*dias_semana)
    # estructura:
    # [..., 
    # [Domingo, Lunes, Martes, Miercoles, Jueves, Viernes, Sábado],
    # [Domingo, Lunes, Martes, Miercoles, Jueves, Viernes, Sábado],
    # ...]

    # creo el primer día del mes actual
    dia = 1
    # veo si es bisiesto, no se si es necesario dado que uso la funcion
    # con la congruencia de zeller, pero asi funciona y por ahora no lo
    # toco
    fecha_valida, anio_bisiesto= auxiliares.validar_fecha(dia, mes, anio)
    # me quedo con mi mes en palabras y el anio original por si paso de anio
    # eso no sería necesario pero por ahora lo dejo
    mes_ori = mes_a_palabras(mes)
    anio_ori = anio

    match mes:
        case 1|3|5|7|8|10|12:
            contador_dias = 1
            n_semanas = 0
            while contador_dias <= 31 and n_semanas <= 4:
                contador_dias += 1
                d = dia_de_la_semana(dia, mes, anio)
                if d == 0:
                    n_semanas += 1
                calendario_mes[n_semanas][d] = dia           
                dia, mes, anio = dia_siguiente(dia, mes, anio, anio_bisiesto)
        case 4|6|9|11:
            contador_dias = 1
            n_semanas = 0
            while contador_dias <= 30 and n_semanas <= 4:
                contador_dias += 1
                d = dia_de_la_semana(dia, mes, anio)
                if d == 0:
                    n_semanas += 1
                calendario_mes[n_semanas][d] = dia
                dia, mes, anio = dia_siguiente(dia, mes, anio, anio_bisiesto)
        case 2:
            if anio_bisiesto:
                f_m = 29
            else:
                f_m = 28
            contador_dias = 1
            n_semanas = 0
            while contador_dias <= f_m and n_semanas <= 4:
                contador_dias += 1
                d = dia_de_la_semana(dia, mes, anio)
                if d == 0:
                    n_semanas += 1
                calendario_mes[n_semanas][d] = dia
                dia, mes, anio = dia_siguiente(dia, mes, anio, anio_bisiesto)
        
    imprimir_calendario(calendario_mes, mes_ori.upper(), anio_ori)
    print()



                    

