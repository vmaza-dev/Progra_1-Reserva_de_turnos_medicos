import pytest
from pacientes import promedio_edades, validacion_dni, pacientes_por_obra


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