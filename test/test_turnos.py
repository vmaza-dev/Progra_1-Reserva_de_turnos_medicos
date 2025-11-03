# ==============================================================================
# Materia: Programación 1 
# Grupo 6: Aliano Manuel, Ávila Simón, Iturria Agustín, Nicolás Seijo, Victor Maza
# Fecha de creación: 30/10/2025
# ==============================================================================

#-------------------------------------------------------------------------------
# FUNCIONES A TESTEAR ----------------------------------------------------------
#-------------------------------------------------------------------------------

def filtrar_turnos(matriz_turnos, filtro, key_filtro, inverso = False): #✅
    """
    Filtra turnos según lo solicitado.

    Si inverso True, filtra lo que no coincide.

    Args:
        matriz_turnos(list[dic]): Matriz de turnos.
        filtro(str|int|date): Value del filtro.
        key_filtro(str): Key del filtro.
        inverso(bool): Defecto False. 
    
    Returns:
        Matriz de turno filtrada
    """
    if inverso == False:
        turnos_filtrados = list(filter(lambda turno: turno.get(key_filtro) 
                                       == filtro ,matriz_turnos))
    elif inverso == True:
        turnos_filtrados = list(filter(lambda turno: turno.get(key_filtro) 
                                       != filtro ,matriz_turnos))
    return turnos_filtrados

def devolver_nombre_persona(lista_personas, id_persona, id_key):# TODO: Para completar, pero debería funcionar bien.✅
    """
    Devuelve el nombre de una persona según el id dado.
    
    Args:
        lista_diccionario(list(dic))
        id_persona(int)
    
    Returns:
        (str): Nombre de la persona
    """
    lista_id_personas = obtener_lista_dic_value(lista_personas, id_key)
    if id_persona in lista_id_personas:
        indice_fila = lista_id_personas.index(id_persona)
        nombre_persona = lista_personas[indice_fila]['nombre']# Este key tiene que ser igual para medicos y pacientes.

        return nombre_persona
    # Acá tiene que ir un try/except

def obtener_lista_dic_value(lista_diccionarios ,key):
    """
    Obtiene una lista de valores de la key indicada
    
    Args:
        lista_diccionarios(list[dic])
        key(str): Key de los valores a buscar.
    
    Returns:
        lista_valores(list): Lista de valores de la key indicada.
    """
    mensaje = "No existe el dato buscado"
    lista_valores = [diccionario.get(key, mensaje) for diccionario in lista_diccionarios]

    return lista_valores

def validar_turno(matriz_turnos, datos_turno, rnd = True):#✅
    """
    Valida el turno a asignar.

    Si hay superposición de horarios, superposicion de medico y paciente.

    Args:
        matriz_turnos(list[list])
        neuvo_turno(dic)
        
    Returns:
        bool: True turno valido, False turno invalido
        str: Mensaje informativo de la validacion
    """
    matriz_turnos_fecha= filtrar_turnos(matriz_turnos, datos_turno['fecha'], 'fecha')
    mensaje = ""
    valido = True
    busqueda = True
    turno = 0
    # uso while para no forzar la finalizacion del bucle con un return o break
    while busqueda and turno <= len(matriz_turnos_fecha) - 1:
        # valido superpocion de horario con otro turno del paciente
        if (datos_turno.get('hora') == matriz_turnos_fecha[turno].get('hora')and
            datos_turno.get('paciente') == matriz_turnos_fecha[turno].get('paciente')):
            valido = False
            mensaje = "El paciente ya tiene un turno en el horario solicitado"
            busqueda = False
        # valido superpocion de horario del medico con otro turno del medico
        elif (datos_turno.get('medico') == matriz_turnos_fecha[turno].get('medico')and
              datos_turno.get('hora') == matriz_turnos_fecha[turno].get('hora')):
            valido = False
            mensaje = "El médico solicitado no tiene disponible el horario solicitado"
            busqueda = False
        # valido si el paciente ya tiene turno con el medico
        elif (datos_turno.get('medico') == matriz_turnos_fecha[turno].get('medico')and
              datos_turno.get('paciente') == matriz_turnos_fecha[turno].get('paciente')):
            mensaje = "El paciente ya tiene un turno con el médico solicitado"
            valido = False
            busqueda = False
        if rnd == False:
            if (datos_turno.get('especialidad_medica') == matriz_turnos_fecha[turno].get('especialidad_medica') and
                datos_turno.get('paciente') == matriz_turnos_fecha[turno].get('paciente')):
                raise Warning("El paciente ya tiene un turno con la especialidad requerida")
        turno += 1    

    return valido, mensaje
#-------------------------------------------------------------------------------
# TESTS CREAR_LEER_CONSULTAR_TURNOS --------------------------------------------
#-------------------------------------------------------------------------------

# VARIABLES NECESARIAS PARA LOS TESTS ------------------------------------------

matriz_turnos_test = [
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

matriz_medicos_test = [
    {
        "ID": 100000,
        "nombre": "Juan Pérez",
        "espec": "Traumatologia",
        "antig": 5,
        "estado": 0
    }
]

datos_turno_test_1 =     {
        "fecha": "2025-10-04",
        "hora": "15:30",
        "paciente": 35023963,
        "especialidad_medica": "Clínica Médica",
        "medico": 456123,
        "tipo_consulta": "Consulta",
        "estado_turno": "Activo"
    }

datos_turno_test_2 =     {
        "fecha": "2025-10-04",
        "hora": "16:30",
        "paciente": 20488909,
        "especialidad_medica": "Otorrinonaringologia",
        "medico": 489652,
        "tipo_consulta": "Revisión",
        "estado_turno": "Activo"
    }

datos_turno_test_3 =     {
        "fecha": "2025-10-04",
        "hora": "09:30",
        "paciente": 35023963,
        "especialidad_medica": "Otorrinonaringologia",
        "medico": 5684123,
        "tipo_consulta": "Consulta",
        "estado_turno": "Activo"
    }

#-------------------------------------------------------------------------------

def test_filtrar_turnos():
    assert filtrar_turnos(matriz_turnos_test, 35023963, 'paciente') == [
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

def test_devolver_nombre_persona():
    assert devolver_nombre_persona(matriz_medicos_test, 100000, 'ID') == "Juan Pérez"

def test_validar_turno():
    assert validar_turno(matriz_turnos_test, datos_turno_test_1) == (False, "El paciente ya tiene un turno en el horario solicitado")

def test_validar_turno():
    assert validar_turno(matriz_turnos_test, datos_turno_test_2) == (False, "El médico solicitado no tiene disponible el horario solicitado")

def test_validar_turno():
    assert validar_turno(matriz_turnos_test, datos_turno_test_3) == (False, "El paciente ya tiene un turno con el médico solicitado")

#-------------------------------------------------------------------------------
# TESTS ACTUALIZAR_ELIMINAR_TURNOS ---------------------------------------------
#-------------------------------------------------------------------------------