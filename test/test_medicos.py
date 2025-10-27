import pytest
from medicos import leer_medicos, leer_medico_id, buscar_borrar_med

def test_leer_medicos_vacia(listaMedicos=[]):
    leer_medicos(listaMedicos)

#Testea que el retorno sea falso aunque tenga un fallo
def test_buscar_borrar_med_tipoInvalido():
    retorno = buscar_borrar_med("100000", [{"ID": 100000, "nyap": "Juan Pérez", "espec":"Ejemplologia", "antig":5, "estado":0}])
    assert retorno == False

def test_leer_medico_id_tipoInvalido():
    leer_medico_id("Cadena para Test", 100000)