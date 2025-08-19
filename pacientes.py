# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Nicolás Seijo, Victor Maza
# Descripción: 
# Fecha de creación: 10/08/2025
# ==============================================================================

import random, fun_aux
print("l")

def crear_pacientes_random(pacientes, cantCrear):
    for i in range(cantCrear):
        nombre = random.choice(fun_aux.nombres) + " " + random.choice(fun_aux.apellidos)
        pacientes.append([random.randint(1000, 9999), random.randint(10000000, 99999999),
                           nombre, random.randint(3, 100)])
        
def leer_pacientes(pacientes):
    for pac in pacientes:
        print("---------------------------------------")
        print(f"PACIENTE: {pac[2]} | ID: {pac[0]}")
        print(f"DNI: {pac[1]}\nEDAD: {pac[3]}")

#[ID, DNI, NOMBRE, EDAD]
#pacientes = [
#    [1, "11223344", "Jose Diaz"],
#    [2, "12131415", "Andres Jimenez"],
#    [3, "33366633", "Micaela Macri"],
#    [4, "77754894", "Fernanda Fernandez"]
#]

pacientes = []
crear_pacientes_random(pacientes, 10)
leer_pacientes(pacientes)

# obra social para pacientes
# id del ARCA de la obra social
# Elegir las obras sociales que queremos
# Decidir si usar obras sociales o solo poner si tiene obra o es particular