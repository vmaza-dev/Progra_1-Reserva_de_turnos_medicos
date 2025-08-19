# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Nicolás Seijo, Victor Maza
# Descripción: 
# Fecha de creación: 10/08/2025
# ==============================================================================

ENCABEZADO = []# Lista de títulos de la matriz de datos. Ejemplo en el googlesheet. 
ESTADO_TURNO = []# Lista de títulos de la matriz de datos. Ejemplo en el googlesheet.
ESPECIALIDAD = []# Lista de títulos de la matriz de datos. Ejemplo en el googlesheet.

#[ID_TURNO, MEDICO, PACIENTE, FECHA, HORA, MOTIVO DE CONSULTA, OBSERVACIÓN, ESTADO]
turnos = [
    [1, 101, 4, "2025-08-20", "09:00", "Control", "Presión arterial elevada", "Atendido"],
    [2, 102, 3, "2025-08-21", "09:00", "Revisión de lunar", "Requiere biopsia", "Pendiente"],
    [3, 103, 2, "2025-08-22", "10:00", "Dolor abdominal", "Posible gastritis", "Atendido"],
    [4, 104, 1, "2025-08-23", "11:00", "Cefalea recurrente", "Se solicitan estudios MRI", "Pendiente"]
]

# matriz de todps los turnos
# consulta de turnos
# creación de turnos
# baja de turnos
# edición de turnos

# Decidir que hacer con la observación
#  Agrrgar obra social a