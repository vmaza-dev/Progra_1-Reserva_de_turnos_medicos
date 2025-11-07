# CRUD: Sistema de reserva de turnos médicos
## GRUPO 6 Programación 1: Aliano Manuel, Ávila Simón, Iturria Agustín, Seijo Nicolás, Maza Victor

---

# Descripción

El proyecto tiene como objetivo brindar funcionalidades CRUD con tres entidades interrelacionadas modelando el flujo de datos de un sistema de reserva de turnos médicos. 

**Entidades:**

- Turnos
- Médicos
- Pacientes

## Estructura general

```
├── backups
│   └── medicos_backup_pre-diccionarios.py
├── datos
│   ├── archivos backup
│   │   ├── arch_medicos_backup.json
│   │   └── arch_medicos_idsUsados_backup.json
│   ├── archivo_turnos.json
│   ├── arch_medicos_idsUsados.txt
│   ├── arch_medicos.json
│   ├── arch_pacientes.json
│   ├── bajas_pacientes.txt
│   └── turnos_cancelados.txt
├── test
│   ├── __init__.py
│   ├── test_medicos.py
│   ├── test_pacientes.py
│   └── test_turnos.py
├── README.md
├── info_general.md
├── LICENSE
├── __init__.py
├── main.py
├── medicos.py
├── pacientes.py
├── turnos.py
├── crear_leer_turnos.py
├── actualizar_eliminar_turnos.py
├── calendario.py
└──auxiliares.py
```

**Paquetes de Pyhton utlizados:**

- random: Para creación randomizada de datos de prueba en los módulos.
- re: Uso de expresiones regulares.
- datetime: Para manejo de fechas y creación de horarios.
- calendar: Para manejo de ultimos días del mes.
- json: Para el manejo de archivos.
- sys: Para finalizar ejecución del programas por errores fatales.
- pytest: Para pruebas unitarias.
- monkeypatch: Para la simulación de entradas por teclado.

## Descripción de cada módulo

### main.py

Programa principal del proyecto. Es el encargado de orquestar todas las funcionalidades de los módulos/paquetes. Contiene un menú principal adaptado del modelo brindado en la cursada. 

Ejemplo de salida: 

```
  ____  __         ____                                      _         
 / ___|/ /_    _  |  _ \ ___  ___  ___ _ ____   ____ _    __| | ___    
| |  _| '_ \  (_) | |_) / _ \/ __|/ _ \ '__\ \ / / _` |  / _` |/ _ \   
| |_| | (_) |  _  |  _ <  __/\__ \  __/ |   \ V / (_| | | (_| |  __/   
 \____|\___/  (_) |_| \_\___||___/\___|_|    \_/ \__,_|_ \__,_|\___|   
| |_ _   _ _ __ _ __   ___  ___   _ __ ___   /_/  __| (_) ___ ___  ___ 
| __| | | | '__| '_ \ / _ \/ __| | '_ ` _ \ / _ \/ _` | |/ __/ _ \/ __|
| |_| |_| | |  | | | | (_) \__ \ | | | | | |  __/ (_| | | (_| (_) \__ \
 \__|\__,_|_|  |_| |_|\___/|___/ |_| |_| |_|\___|\__,_|_|\___\___/|___/

================================================================================
|                              MENU PRINCIPAL                                  |
================================================================================
| [1]: GESTION DE TURNOS                                                       |
--------------------------------------------------------------------------------
| [2]: GESTION DE PACIENTES                                                    |
--------------------------------------------------------------------------------
| [3]: GESTION DE MEDICOS                                                      |
--------------------------------------------------------------------------------
| [0]: SALIR DEL PROGRAMA                                                      |
================================================================================
Seleccione una opción: 
```

### Módulo Turnos

Originalmente era un sólo módulo, por comodidad de trabajo se uso como strategia la división del módulo en tres módulos por separado. Teniendo como principa el módulo `turnos.py` que presenta el menú principal que integra los módulos `crear_leer_turnos.py` y `actualizar_eliminar_turnos.py` que representan funcionalidades CRUD específicas de la entidad turnos, existiendo el módulo auxiliar `calendario.py` específico para la implementación visual de un calendario mensual.

```
├── turnos.py
├── crear_leer_turnos.py
├── actualizar_eliminar_turnos.py
├── calendario.py

```

**Módulos principales:**

- crear_leer_turnos.py
- actualizar_eliminar_turnos.py

**Módulos auxiliares:**

- calendario.py

### Módulo Médicos

Módulo con funcionalidades CRUD específicas de la entidad médicos.

```
├── medicos.py

```

### Módulo Pacientes

Módulo con funcionalidades CRUD específicas de la entidad pacientes.

```
├── pacientes.py

```
# Modalidad de trabajo

Se establecieron convenciones generales en el archivo `info_general.md` y se procedio a la división de tarea dentro del equipo.

## División de tareas

- Módulo Turnos: Victor y Manuel
- Módulo Médicos: Nicolás
- Módulo Pacientes: Simón y Agustín

## Uso responsable de IA

Se utilizó la ayuda de asistentes de IA para lo siguiente:

 - Consulta de funcionalidad de paquetes `datetime` y `calendar` con el correspondiete chequeo y estudio de documentación oficial de Python.
 - Creación de nombres de pacientes y médicos.