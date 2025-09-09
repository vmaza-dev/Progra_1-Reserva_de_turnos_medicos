# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Nicolás Seijo, Victor Maza
# Descripción: 
# Fecha de creación: 10/08/2025
# ==============================================================================
ANCHO = 111

import random, auxiliares
def ingresar_nombre_medico():
    """
    Solicita al usuario el nombre de un médico *ingresa el nombre* .

    Returns:
        str: Nombre ingresado.
    """
    nombre = input("Ingrese el nombre del medico: ")
    return nombre

def ingresar_espe(nombreMed):
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

def generar_id(matrizIds):
    if (len(matrizIds) == 9000):
        print("No hay mas IDs disponibles")
        return -1
    else:
        idGenerado = random.randint(1000, 9999)
        while (idGenerado in matrizIds):
            idGenerado = random.randint(1000, 9999)
        return idGenerado

def crear_medico(matrizMeds, matrizIds): # NOTA: Lo hago con matrices pero no sé si sea mejor con diccionarios. (structs)
    """
    Crear un nuevo usuario medico y lo agrega a la matriz total de medicos.
    
    Parametros:
        matrizMeds (list): Lista de listas *matriz* que almacena los medicos registrados.
        cada medico se guarda con el formato: [ID,Nombre, Especialidad, Antiguedad , Estado]

    Flujo:
        - Genera un ID aleatorio de 4 digitos
        - Pide al usuario (nombre,especialidad y antiguedad)
        - Define el estado inicial como activo (1)
        - Agrega la informacion del medico a la matriz
        """
    nombreCompleto = ingresar_nombre_medico()
    idMed = generar_id(matrizIds)
    if (idMed == -1):
        print("ERROR al crear medico. No hay más IDs disponibles")
        return
    matrizMeds.append([idMed, nombreCompleto, ingresar_espe(nombreCompleto),
                        ingresar_antig(nombreCompleto), True]) # False DE BAJA | True ACTIVO

def crear_medicos_random(meds, cantCrear, matrizIds):
    # Esta funcion lo que hace es crear "cantCrear" veces un médico usando las matrices de auxiliares.py
    for i in range(cantCrear):
        nyap = random.choice(auxiliares.nombres) + " " + random.choice(auxiliares.apellidos)
        espe = random.choice(auxiliares.especialidades)
        idMed = generar_id(matrizIds)
        if (idMed == -1):
            print("ERROR al crear medico. No hay más IDs disponibles")
            return
        meds.append([idMed, nyap, espe, random.randint(1,30), True])

def actu_medico(listaMed, nombreMed): #Si bien de listaMed se podria obtener el nombre asi es más claro y legible.
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
    print("Ingrese el dato a modificar del medico", nombreMed, ":")
    print("1: Nombre y Apellido\n2: Especialidad\n3: Antigüedad\n4: Estado (Dar de baja, o dar de alta)")
    opcion = int(input("Ingrese el número correspondiente: "))
    match opcion:
        case 1:
            listaMed[1] = ingresar_nombre_medico()
            print("Nombre modificado exitosamente a:", listaMed[1])
        case 2:
            listaMed[2] = ingresar_espe(nombreMed)
            print("Especialidad modificada exitosamente a:", listaMed[2])
        case 3:
            print("\033c") #Limpia la pantalla
            print("La antigüedad del medico", nombreMed, "es", listaMed[3], "las opciones para modificarla son:")
            print("1: Sumar 1 año\n2: Restar 1 año\n3: Ingresar manualmente la antigüedad")
            opcionAntig = int(input("Ingrese el número correspondiente: "))
            match opcionAntig:
                case 1:listaMed[3] += 1
                case 2:listaMed[3] -= 1
                case 3:listaMed[3] = ingresar_antig(nombreMed)
            print("Antigüedad modificada exitosamente a:", listaMed[3])
        case 4:
            if (not listaMed[4]):
                listaMed[4] = True
                print("El médico", nombreMed, "ahora se encuentra activo")
            else:
                listaMed[4] = False
                print("El médico", nombreMed, "ahora se encuentra dado de baja")

def imprimir_medico(med):
    print(f"| {str(med[0]).ljust(6)}", end=" |")
    print(f"| \033[1m{med[1].ljust(41)}\033[0m", end=" |")
    print(f"| {med[2].ljust(21)}", end=" |")
    print(f"| \033[33m{str(med[3]).ljust(11)}\033[0m", end=" |") if (med[3] > 25) else print(f"| {str(med[3]).ljust(11)}", end=" |")
    if (med[4]):
        print(f"| \033[1;32m{'ACTIVO'.center(12)}\033[0m", end=" |")
    else:
        print(f"| \033[1;31m{'INACTIVO'.center(12)}\033[0m", end=" |")

def header_medicos(anchoTotal):
    # ID 6 espacios + 4 de borde
    # Nombre 41 espacios + 4 de borde
    # Especialidad 21 espacios + 4 de borde
    # ANTIGÜEDAD 11 espacios + 4 de borde
    # Estado 12 espacios + 4 de borde
    print("="*anchoTotal)

    print(f"| \033[1;34m{'ID'.center(6)}\033[0m", end=" |")
    print(f"| \033[1;34m{'NOMBRE COMPLETO'.center(41)}\033[0m", end=" |")
    print(f"| \033[1;34m{'ESPECIALIDAD'.center(21)}\033[0m", end=" |")
    print(f"| \033[1;34m{'ANTIGÜEDAD'.center(11)}\033[0m", end=" |")
    print(f"| \033[1;34m{'ESTADO'.center(12)}\033[0m", end=" |")
    print("\n" + "="*anchoTotal)

def leer_medicos(meds):
    header_medicos(ANCHO)
    for med in meds:
        imprimir_medico(med)
        print("")
        
    fun_aux.footer_general(ANCHO)

def leer_medico_id(meds, idMed):
    for med in meds:
        if (med[0] == idMed):
            imprimir_medico(med)
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

def elim_medico(matrizMeds):
    """
    Solicita al usuario que ingrese el ID de un medico y lo modifica su estado a inactivo.
    
    Parametros: 
        MatrizMeds(list): Lista de medicos.
    """
    idElim = int(input("Ingrese el ID del médico a eliminar: "))
    if (buscar_borrar_med(idElim, matrizMeds)): # Devuelve True si lo encontro y borro, False si no lo encontró
        print("Medico de ID", idElim, "eliminado exitosamente.")
    else:
        print("Medico de ID", idElim, "no encontrado o inexistente, no se realizó la eliminación.")

""" MAIN """
medicos = [
    [1001, "Juan Pérez", "Traumatología", 5, 0],
    [9999, "Ataúlfo Américo Djandjikian", "Otorrinonaringología", 26, 1]
] #ID, Nombre, Especialidad, Antiguedad, Estado

idsUsados = [1001, 9999]
# Acá inicialice dos médicos para hacer pruebas de lectura.

#crear_medicos_random(medicos, 5, idsUsados)
#crear_medico(medicos, idsUsados)

#actu_medico(medicos[0], medicos[0][1])

fun_aux.limpiar_terminal()
leer_medicos(medicos)

#leer_medico_id(medicos, 1001)

#elim_medico(medicos)