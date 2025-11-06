import pytest
from pacientes import validacion_dni, validacion_edad, id_unico, generacion_dni_realista, promedio_edades,pacientes_por_obra, porcentaje_por_obra, generar_usuario


def test_promedio_edades():
    pacientes = [
        {"id": 1, "nombre": "Juan Perez", "edad": 20, "obra_social": "OSDE"},
        {"id": 2, "nombre": "Ana Gomez", "edad": 40, "obra_social": "IOMA"},
        {"id": 3, "nombre": "Pedro Lopez", "edad": 60, "obra_social": "Swiss Medical"},
    ]
    assert promedio_edades(pacientes) == pytest.approx(40.0)

def test_promedio_edades_lista_vacia():
    assert promedio_edades([]) == 0



def test_validacion_dni_valido(monkeypatch):
    # Simula que el usuario no tiene que volver a ingresar nada
    assert validacion_dni(12345678) == 12345678

def test_validacion_dni_invalido(monkeypatch):
    # Simula que el usuario ingresa primero un DNI inválido y luego uno correcto
    entradas = iter(["87654321"])
    monkeypatch.setattr("auxiliares.pedir_valor", lambda msg, tipo=str: next(entradas))
    assert validacion_dni("abcd123") == 87654321


def test_pacientes_por_obra():
    pacientes = [
        {"id": 1, "obra_social": "OSDE"},
        {"id": 2, "obra_social": "IOMA"},
        {"id": 3, "obra_social": "OSDE"},
    ]
    resultado = pacientes_por_obra(pacientes)
    esperado = [("OSDE", 2), ("IOMA", 1)]
    assert sorted(resultado) == sorted(esperado)



# VARIABLE NECESARIA PARA LOS TESTS   ------------------------------------------
@pytest.fixture
def pacientes_test():
    return[
        {"id":1000, "dni":12345678, "nombre": "Juan Perez", "edad": 30, "obra_social": "OSDE"},
        {"id":1001, "dni":22334455, "nombre": "Pepe Argento", "edad": 43, "obra_social": "Swiss Medical"},
        {"id":1002, "dni":66778899, "nombre": "Felipe Alvarez", "edad": 60, "obra_social": "OSDE"},
    ]

# TESTS ------------------------------------------------------------------------

def test_validacion_dni_valido():
    #Arrange
    dni = 12345678
    #Act
    resultado = validacion_dni(dni)
    #Assert
    assert resultado == dni

def test_id_unico(pacientes_test):
    #Arrange
    id_existente = [p['id'] for p in pacientes_test]
    #Act
    nuevo_id = id_unico(pacientes_test)
    #Assert
    assert nuevo_id not in id_existente
    assert 1000 <= nuevo_id <= 9999

def test_promedio_edades(pacientes_test):
    #Arrange
    esperado = (30 + 43 + 60)/3
    #Act
    resultado = promedio_edades(pacientes_test)
    #Assert
    assert resultado == pytest.approx(esperado)

