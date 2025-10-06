import medicos

#def test_crear_medico():

def test_leer_medicos(listaMedicos):
    medicos.leer_medicos(listaMedicos)

def test_leer_medicos_vacia(listaMedicos=[]):
    medicos.leer_medicos(listaMedicos)

def test_leer_medicos_noLista(listaMedicos="Hola"):
    medicos.leer_medicos(listaMedicos)



#def test_actu_medico():
#def test_elim_medico():

#def test_porcentaje_estado():
#def test_porcentaje_espec():

# NO HACER TEST AUTOMATICO DE FUNCIONES CON INPUT

test_leer_medicos_noLista()