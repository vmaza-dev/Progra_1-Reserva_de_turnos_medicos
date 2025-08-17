# GRUPO 6
# CRUD: Sistema de reserva de turnos médicos

**Este archivo contiene información general para el grupo:**

    - Convenciones generales de escritura de código en Python
    - Convención para la documentación de funciones
    - Estructura del trabajo
    - Machete de Git y GitHub

La idea es que todos tengamos la misma info de como vamos a hacer el TP. La extensión de este archivo es `.md` que es MarkDown que es una forma de escribir en texto plano. Para verlo lindo en VSCode tiene que ir la parte superior izquierda de la ventana en la que ven el código y cliquear en el icono que parace un libro y una lupa o una pizza a la pala y el cortador. Les va a aparecer el archivo formateado.

Espero que sea de ayuda y si están de acuerdo con este archivo lo dejamos, lo sacamos, lo modificamos (MarkDown es sencillo). Cambienlo como quieran, agreguenle lo que les parezca y vamos viendo.

## Convenciones generales de escritura de código

Usamos la convenciones de Python (PEP 8, PEP 257), que son convenciones que están en la página oficial de Python.

### PEP 8 – Guía de Estilo para Python

Objetivo: Establecer reglas y buenas prácticas para escribir código Python legible y consistente.

**Aspectos clave:**

- Indentación: 4 espacios por nivel (nunca tabs mezclados con espacios).

- Longitud de línea: Máximo 79 caracteres (72 para docstrings).

- Nombres:
    - Variables y funciones: snake_case.

     Ejemplo, queremos definir una variable que se llama especialidad médica, con snake case sería especialidad_medica. Lo mismo con los nombres de funciones.
    - Constantes: MAYUSCULAS_CON_GUIONES_BAJO.

    Ejemplo, tenemos la variable número de médicos que es constante a lo largo de todo el programa la escribimos como NUMERO_MEDICOS. 

- Importaciones: Una por línea y al inicio del archivo.
- Comentarios: Claros, relevantes y actualizados.

### PEP 257 -  Convención para la documentación de funciones

Objetivo: Definir el formato estándar de la documentación dentro del código.

Aspectos clave:

- Triple comillas (""") para docstrings.

- Primera línea: Descripción breve de la función/clase/módulo.

- Segunda línea: En blanco (opcional si la docstring es de una sola línea).

- Cuerpo: Explicación detallada, parámetros y valores de retorno si es necesario.

- Estilo: Frases en modo imperativo ("Devuelve X", no "Devuelve X.") y evitar redundancias.

Ejemplo 1:

```python
def suma(a, b):
    """
    Devuelve la suma de dos números.
    """
    return a + b
```

Ejemplo 2:

```python
def validar_fecha(d, m, a):
    """
    Valida si tres números enteros positivos corresponden a una fecha válida.

    Toma en cuenta anios bisiestos, meses de 30 y 31 días.

    Parámetros:
        d(int): Día del mes.
        m(int): Mes.
        a(int): Anio.

    Returns:
        bool
        - True si los tres número corresponden a una fecha válida. False si 
        alguno/todos hacen inválida a la fecha.
        - True si el año es bisiesto. False si el año no es bisiesto 
    """
```

## Estructura del trabajo

El profe dijo que vamos a usar módulo para hacer el TP. Los módulos son archivos apartes que contienen parte del código. La idea es para que no sea tan largo e ilegible un código. Estos módulos después los importas al módulo principal. En nuestro trabajo definimos hasta ahora cuatro módulos:

    - main.py
    - turnos.py
    - medicos.py
    - pacientes.py
    - aux.py

La idea es que en `main` escribamos el programa final sin funcionalidades extras. Por ejemplo el menú principal, nuestro logo, todo el código que vaya a usar las funciones de los otros módulos. 

En `turnos`, `medicos` y `pacientes`, todo lo que tenga que ver especificamente con cada uno. Por ejemplo en médicos la creacion de su matriz, sus especialidades, bueno eso se me ocurre hasta ahora. 

En `fun_aux` todas la funciones generales que se puedan usar en todo el programa. Por ejemplo validar una fecha, pedir el ingreso de un número, la función de crear una matriz.

**Otro archivos**

`LICENSE`: Es la licencia de nuestro programa, es una de las genéricas que podes eligir cuando creas el repo, se llama MIT y la que hace open source nuestro código. Cualquier persona lo podría usar siempre que nombre a los autores, nosotros.

`.gitignore`: Es un archivo que setea que cosas no vas a poder subir cuando haces git push, entonces evita que subas algo que no querés o un archivo que no querés compartir. Un ejemplo sería las configuraciones de tu VSCode. Cuando cree el repo esta esa opción y elegí el gitignore por defecto que te GitHub.

`README.md`: Es un archivo MarkDown como este que sirve como descripción del proyecto en el repo. Acá podemos poner de trata nuestro proyecto.

## Machete Git y GitHub

**Clonar el repo**

```shell
git clone https://github.com/gorila-dev/gorilavshombre.git
```
**Crear nueva rama**

Con este código creamos una nueva rama y nos movemos a esa rama.

```shell
git checkout -b feature/nueva-rama
```

Chequeamos en que rama estamos, en la que estamo aparace un *.

```shell
git branch

# sale:
# *nueva-rama
# main
```
**Agregamos todos los archivos al staging area**

```shell
git add .
```
**Comiteamos**

```shell
git commit -m "Mensaje de commit"
```

**Pusheamos a GitHub**

```shell
# esto es la primera vez
git push -u origin feature/nueva-rama

# después con eto ya debería estar
git push 
```
Como estamos en una rama va a aparecer algo como esto

```shell
Enumerating objects: 12, done.
Counting objects: 100% (12/12), done.
Delta compression using up to 8 threads
Compressing objects: 100% (7/7), done.
Writing objects: 100% (8/8), 1.23 KiB | 1.23 MiB/s, done.
Total 8 (delta 3), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (3/3), completed with 2 local objects.
remote: 
remote: Create a pull request for 'feature/nueva-rama' on GitHub by visiting:
remote:      https://github.com/gorila-dev/gorilavshombre.git/pull/new/feature/nueva-rama
remote: 
To github.com:gorila-dev/gorilavshombre.git.git
 * [new branch]      feature/nueva-rama -> feature/nueva-rama
```
Entonces hay que ir a GitHub y hacer una `Pull Request` y ver si hay conflicto con lo que ya esta ecrito (que no debería pasar *ajajaj, nada puede malir sal*) y después unimos todo (`merge`).

**Para actualizar tu rama con la última version del repo**

Conviene hacerlo siempre antes de empezar por las dudas no haya cambios.

1. Ir a la rama main
```shell
git checkout main
```

2. Traer la información más reciente del repositorio remoto

```shell
git fetch origin
```

3. Actualizar tu main local con los cambios remotos

```shell
git pull origin main
```

4. Volver a tu rama de trabajo

```shell
git checkout nueva-rama
```

5. Incorporar los cambios de main a tu rama
```shell
git merge main
```