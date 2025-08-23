# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Nicolás Seijo, Victor Maza
# Descripción: 
# Fecha de creación: 10/08/2025
# ==============================================================================

import random, fun_aux
print("l")

def crear_paciente(id):

    dni= int(input("Ingrese su dni: "))
    nombreCompleto= int(input("Ingrese su nombre completo: "))
    edad= int(input("Ingrese su edad: "))
    obra_social= (input("Ingrese su obra social: "))
    estado= 1
    paciente=[id,dni,nombreCompleto,edad,obra_social,estado]

    return paciente


def crear_pacientes_random(pacientes, cantCrear):
    for i in range(cantCrear):
        nombreCompleto = random.choice(fun_aux.nombres) + " " + random.choice(fun_aux.apellidos)
        dni= random.randint(10000000, 99999999)
        edad= random.randint(3,99)
        obra_social= random.choice(["OSDE", "Swiss Medical", "VICMAZA", "Galeno","Particular"])
        estado=1
        id=random.randint(1000,9999)
        pacientes.append([id,dni,nombreCompleto,edad,obra_social,estado])

        
def leer_pacientes(pacientes):
    ancho=50
    for pac in pacientes:
        print("---------------------------------------")
        print(f"PACIENTE: {pac[2]} | ID: {pac[0]}")
        print(f"DNI: {pac[1]}\nEDAD: {pac[3]}")
        print("=" * ancho)
        print(f" PACIENTE: {pac[2]} ".center(ancho, "="))
        print(f"ID: {str(pac[0]).ljust(10)} | DNI: {str(pac[1]).ljust(12)}")
        print(f"EDAD: {str(pac[3]).ljust(8)} | OBRA SOCIAL: {pac[4]}")
        print(f"ESTADO: {'Activo' if pac[5]==1 else 'Inactivo'}".center(ancho))
        print("=" * ancho)
        print() 

def buscar_id_paciente(pacientes):
    id = int(input("Ingrese el ID del paciente a buscar: "))
    encontrado = False
    i = 0
    while i < len(pacientes) and encontrado == False:
        pac = pacientes[i]
        if pac[0] == id:
            print("\n" + "==============================")
            print("PACIENTE ENCONTRADO")
            print("-------------------------------")
            print(f"ID: {pac[0]}")
            print(f"DNI: {pac[1]}")
            print(f"NOMBRE: {pac[2]}")
            print(f"EDAD: {pac[3]}")
            print("==============================" + "\n")
            encontrado = True 
        i += 1
    if encontrado == False:
        print("\nNo se encontro al paciente\n")
pacientes = []
crear_pacientes_random(pacientes, 10)
leer_pacientes(pacientes)
buscar_id_paciente(pacientes)


# obra social para pacientes
# id del ARCA de la obra social
# Elegir las obras sociales que queremos
# Decidir si usar obras sociales o solo poner si tiene obra o es particular