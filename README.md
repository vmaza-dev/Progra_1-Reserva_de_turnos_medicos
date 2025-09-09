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
├── actualizar_elimiar_turnos.py
├── auxiliares.py
├── calendario.py
├── crear_leer_turnos.py
├── info_general.md
├── LICENSE
├── main.py
├── medicos.py
├── pacientes.py
└── README.md
```

**Paquetes de Pyhton utlizados:**

- random: Para creación randomizada de datos de prueba en los módulos.
- re: Uso de expresiones regulares.
- datetime: Para manejo de fechas y creación de horarios.
- calendar: Para manejo de ultimos días del mes.

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
---------------------------
[0] Salir del programa
---------------------------
```

### Módulo Turnos

Originalmente era un sólo módulo, por comodidad de trabajo se uso como strategia la división del módulo en dos módulos por separado. Cada módulo representa funcionalidades CRUD específicas de la entidad turnos, existiendo el módulo auxiliar `calendario.py` específico para la implementación visual de un calendario mensual.

```
├── actualizar_elimiar_turnos.py
├── calendario.py
├── crear_leer_turnos.py

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