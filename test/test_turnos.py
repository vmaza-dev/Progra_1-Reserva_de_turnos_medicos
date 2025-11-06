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
from actualizar_eliminar_turnos import elim_turno, edit_turnos
import auxiliares

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


# Prueba 1: Verifica que 'elim_turno' NO cambie el estado si ya está 'Finalizado'
def test_elim_turno_no_cancela_un_turno_finalizado(monkeypatch):
    # Organizar (Arrange): Un turno finalizado
    estado_original = auxiliares.estado_turno['finalizado']
    turno_finalizado = {"id": "000001", "estado_turno": estado_original}
    matriz = [turno_finalizado]
    
    # Simulamos que el usuario ingresa el ID "1" y presiona "Enter"
    monkeypatch.setattr('auxiliares.ingresar_entero_positivo', lambda _: "1")
    monkeypatch.setattr('builtins.input', lambda _: "")
    elim_turno(matriz)
    
    # Afirmar (Assert): El estado del turno NO debe haber cambiado
    assert matriz[0]['estado_turno'] == estado_original

# Prueba 2: Verifica que 'edit_turnos' NO pueda editar un turno 'Cancelado'
def test_edit_turnos_no_edita_un_turno_cancelado(monkeypatch):
    #
    estado_original = auxiliares.estado_turno['cancelado']
    turno_cancelado = {"id": "000001", "estado_turno": estado_original}
    matriz = [turno_cancelado]

    # Simulamos que el usuario ingresa el ID "1" y presiona "Enter"
    monkeypatch.setattr('auxiliares.ingresar_entero_positivo', lambda _: "1")
    monkeypatch.setattr('builtins.input', lambda _: "")
    edit_turnos(matriz, [], 10, 2025)
    
    # Afirmar (Assert): El estado debe seguir siendo el original
    assert matriz[0]['estado_turno'] == estado_original