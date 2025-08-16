# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Nicolás Seijo, Victor Maza
# Descripción: 
# Fecha de creación: 10/08/2025
# ==============================================================================

import random
def ingresar_nombre_medico():
    nombre = input("Ingrese el nombre del medico: ")
    return nombre

def ingresar_espe(nombreMed):
    especialidad = input(f"Ingrese la especialidad de {nombreMed}: ") #Uso fPrints ya que el input no puede concatenar cadenas con ","
    return especialidad

def ingresar_antig(nombreMed):
    antiguedad = int(input(f"Ingrese la antiguedad de {nombreMed}: "))
    return antiguedad

def crear_medico(matrizMeds): # NOTA: Lo hago con matrices pero no sé si sea mejor con diccionarios. (structs)
    idMed = random.randint(1000, 9999)
    nombreCompleto = ingresar_nombre_medico()
    espe = ingresar_espe(nombreCompleto)
    antig = ingresar_antig(nombreCompleto)
    estado = 1 # 0 DE BAJA | 1 ACTIVO
    matrizMeds.append([idMed, nombreCompleto, espe, antig, estado])
    print("ID: ", idMed) # Esto es temporal, todavía no hice la lectura de un médico específico.

def actu_medico(listaMed, nombreMed): #Si bien de listaMed se podria obtener el nombre asi es más claro y legible.
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
                case 1:
                    listaMed[3] += 1
                case 2:
                    listaMed[3] -= 1
                case 3:
                    listaMed[3] = ingresar_antig(nombreMed)
            print("Antigüedad modificada exitosamente a:", listaMed[3])
        case 4:
            if (listaMed[4] == 0):
                listaMed[4] = 1
                print("El médico", nombreMed, "ahora se encuentra activo")
            else:
                listaMed[4] = 0
                print("El médico", nombreMed, "ahora se encuentra dado de baja")

#def leer_medico():
def buscar_borrar_med(idElim, meds):
    encontrado = False
    for med in meds:
        if (med[0] == idElim):
            encontrado = True
            meds.remove(med)
        break
    return encontrado

def elim_medico(matrizMeds):
    idElim = int(input("Ingrese el ID del médico a eliminar: "))
    if (buscar_borrar_med(idElim, matrizMeds)): # Devuelve True si lo encontro y borro, False si no lo encontró
        print("Medico de ID", idElim, "eliminado exitosamente.")
    else:
        print("Medico de ID", idElim, "no encontrado o inexistente, no se realizó la eliminación.")

medicos = []

crear_medico(medicos)
actu_medico(medicos[0], medicos[0][1])
#medico_aux = leer_medico()
elim_medico(medicos)