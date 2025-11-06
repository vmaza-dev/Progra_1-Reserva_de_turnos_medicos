import pytest
from medicos import leer_medicos, buscar_medico_id, buscar_borrar_med

def test_leer_medicos_vacia():
    #Arrange
    listaMedicos = []

    #Act
    leer_medicos(listaMedicos)

    #No hay assert porque lo que prueba es que la función lo pueda resolver sola.

#Testea que el retorno sea falso aunque tenga un fallo
def test_buscar_borrar_med_tipoInvalido():
    #Arrange
    idBuscado = "100000" # Debería ser "int"
    listaMedicos = [
        {"ID": 100000, "nyap": "Juan Pérez", "espec":"Testingología", "antig":18, "estado":0},
        {"ID": 999991, "nyap": "Augusto Zorzoli", "espec":"Ejemplologia", "antig":23, "estado":1}
    ]

    #Act
    encontrado = buscar_borrar_med(idBuscado, listaMedicos)

    #Assert
    assert encontrado == False # Si encuentra un médico lo devuelve, sino, devuelve falso.

def test_buscar_medico_id():
    #Arrange
    idBuscado = 999991
    listaMedicos = [
        {"ID": 100000, "nyap": "Juan Pérez", "espec":"Testingologia", "antig":18, "estado":0},
        {"ID": 999991, "nyap": "Augusto Zorzoli", "espec":"Ejemplologia", "antig":23, "estado":1},
        {"ID": 456871, "nyap": "Silvio Masa", "espec":"Noexisteologia", "antig":0, "estado":1},
    ]

    #Act
    medicoRetornado = buscar_medico_id(listaMedicos, idBuscado)
    
    #Assert
    assert (medicoRetornado["ID"] == idBuscado)