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
├── anotaciones.txt
├── fun_aux.py
├── info_general.md
├── LICENSE
├── main.py
├── medicos.py
├── pacientes.py
├── README.md
└── turnos
    ├── act_elim.py
    ├── calendario.py
    ├── cre_leer.py
    └── __init__.py
```

**Paquetes de Pyhton utlizados:**

- random:
- datatime:
- calendar: 

## Descripción de cada módulo/paquete

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


---------------------------
MENÚ PRINCIPAL
---------------------------
[1] Gestión de turnos
[2] Gestión de pacientes
[3] Gestión de médicos
[4] Opción 100 a que lo elije a Lampone
[5] Opción no son tan incómodos esto tacos 
---------------------------
[0] Salir del programa
---------------------------

Seleccione una opción: 
```

### Paquete Turnos

Paquete con los módulos de las funcionalidades CRUD del módulo turnos. Adiccionalmente se crearon módulos auxiliares con objetivos específicos para el paquete. 

Estructura paquete turnos:

```
└── turnos
    ├── act_elim.py
    ├── calendario.py
    ├── cre_leer.py
    └── __init__.py
```
**Módulos principales:**

- cre_leer.py
- act_elim.py

**Módulos auxiliares:**

- calendario.py

### Paquete Médicos

### Paquete Pacientes

# Modalidad de trabajo

Se establecieron convenciones generales en el archivo `info_general.md` y se procedío a la división de tarea dentro del equipo.

## División de tareas

- Módulo Turnos: Victor y Manuel
- Módulo Médicos: Nicolás
- Módulo Pacientes: Simón y Agustín

## Uso responsable de IA

Se utilizó la ayuda de asistentes de IA para los siguiente:

 - Consulta de funcionalidad de paquetes `datatime` y `calendar` con el correspondiete chequeo y estudio de documentación oficial de Pyhton.
 - Creación de nombres de pacientes y médicos.