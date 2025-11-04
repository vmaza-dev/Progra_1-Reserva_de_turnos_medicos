# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Nicolás Seijo, Victor Maza
# Fecha de creación: 30/10/2025
# ==============================================================================

#-------------------------------------------------------------------------------
# FUNCIONES A TESTEAR ----------------------------------------------------------
#-------------------------------------------------------------------------------
import pytest
from crear_leer_turnos import filtrar_turnos, devolver_nombre_persona, validar_turno

#-------------------------------------------------------------------------------
# TESTS CREAR_LEER_CONSULTAR_TURNOS --------------------------------------------
#-------------------------------------------------------------------------------

# VARIABLE NECESARIA PARA LOS TESTS   ------------------------------------------
@pytest.fixture
def matriz_turnos_test():
    return [
        {
            "id": "000001",
            "fecha": "2025-10-04",
            "hora": "15:30",
            "paciente": 35023963,
            "especialidad_medica": "Otorrinonaringologia",
            "medico": 5684123,
            "tipo_consulta": "Revisión",
            "estado_turno": "Activo"
        },
        {
            "id": "000002",
            "fecha": "2025-10-04",
            "hora": "16:30",
            "paciente": 32943932,
            "especialidad_medica": "Otorrinonaringologia",
            "medico": 489652,
            "tipo_consulta": "Revisión",
            "estado_turno": "Activo"
        }
    ] 

# TESTS ------------------------------------------------------------------------

def test_filtrar_turnos_paciente(matriz_turnos_test):
    # act
    resultado = filtrar_turnos(matriz_turnos_test, 35023963, 'paciente')
    # assert
    assert resultado == [
    {
        "id": "000001",
        "fecha": "2025-10-04",
        "hora": "15:30",
        "paciente": 35023963,
        "especialidad_medica": "Otorrinonaringologia",
        "medico": 5684123,
        "tipo_consulta": "Revisión",
        "estado_turno": "Activo"
    }]

def test_devolver_nombre_persona_medico():
    # arrange
    matriz_medicos_test = [
    {
        "ID": 100000,
        "nombre": "Juan Pérez",
        "espec": "Traumatologia",
        "antig": 5,
        "estado": 0
    }
    ]
    # act
    resultado = devolver_nombre_persona(matriz_medicos_test, 100000, 'ID')
    # assert
    assert  resultado == "Juan Pérez"

@pytest.mark.parametrize(
    "datos_turno_test, resultado_esperado",
    [
        ({
        "fecha": "2025-10-04",
        "hora": "15:30",
        "paciente": 35023963,
        "especialidad_medica": "Clínica Médica",
        "medico": 456123,
        "tipo_consulta": "Consulta",
        "estado_turno": "Activo"
    }, (False,"El paciente ya tiene un turno en el horario solicitado")),
        ({
        "fecha": "2025-10-04",
        "hora": "16:30",
        "paciente": 20488909,
        "especialidad_medica": "Otorrinonaringologia",
        "medico": 489652,
        "tipo_consulta": "Revisión",
        "estado_turno": "Activo"
    }, (False,"El médico solicitado no tiene disponible el horario solicitado")),
        ({
        "fecha": "2025-10-04",
        "hora": "09:30",
        "paciente": 35023963,
        "especialidad_medica": "Otorrinonaringologia",
        "medico": 5684123,
        "tipo_consulta": "Consulta",
        "estado_turno": "Activo"
    }, (False,"El paciente ya tiene un turno con el médico solicitado"))
    ]
)

def test_validar_superposicion_turnos(matriz_turnos_test, datos_turno_test, resultado_esperado):
    # act
    valido, mensaje = validar_turno(matriz_turnos_test, datos_turno_test)
    # assert
    assert valido == resultado_esperado[0]
    assert mensaje == resultado_esperado[1]

def test_warning_repetir_misma_epecialidad(matriz_turnos_test):
    # arrange
    datos_turno_test = {
        "fecha": "2025-10-04",
        "hora": "14:30",
        "paciente": 35023963,
        "especialidad_medica": "Otorrinonaringologia",
        "medico": 123456,
        "tipo_consulta": "Consulta",
        "estado_turno": "Activo"
    }
    with pytest.raises(Warning) as excinfo:
    # act
        validar_turno(matriz_turnos_test, datos_turno_test, False)
    # assert
    assert str(excinfo.value) == "El paciente ya tiene un turno con la especialidad requerida"



#-------------------------------------------------------------------------------
# TESTS ACTUALIZAR_ELIMINAR_TURNOS ---------------------------------------------
#-------------------------------------------------------------------------------