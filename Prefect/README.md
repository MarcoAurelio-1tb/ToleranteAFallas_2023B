# WorkFlow

Alumno: Marco Aurelio Dominguez Amezcua

Maestro: Michel Emanuel Lopez Franco

Sección: D06 - Tolerante a Fallas

## Introducción

Prefect es una herramienta de orquestación del flujo de trabajo que permite a los desarrolladores crear, observar y reaccionar ante canalizaciones de datos. Es la forma más sencilla de transformar cualquier función de Python en una unidad de trabajo que pueda observarse y orquestarse.

Primeramente, debemos instalar la herramienta para la cual utilizaremos el comando en la terminal, el comando es:
```
pip install -U prefect
```

Después lo importaremos el módulo a nuestro código y además traeremos las herramientas ``task`` y ``flow``:
```python
from prefect import task, flow
```

## Código

Nosotros podemos crear cuantas tareas y flujos queramos, pero cabe mencionar que si se crea una tarea esta debe estar dentro de un flujo, básicamente si tenemos una tarea le debemos de dar flujo para completarla:
El primer ejemplo seria este:

```python
from prefect import task, flow

# Estudiar para un examen
@task
def tarea1():
    examen = str.lower(input("Estudiaste para el examen?\n(y/n)?"))
    return(examen)
    
@flow
def flujo1():
    if tarea1() == 'y':
        print("Vas a aprobar")
    elif tarea1() == 'n':
        print("Vas a reprobar")
    else:
        print("Dios te bendiga")

flujo1()
```

El resultado obtenido es este:
```
23:34:32.561 | INFO    | prefect.engine - Created flow run 'purple-dogfish' for flow 'flujo1'
23:34:32.716 | INFO    | Flow run 'purple-dogfish' - Created task run 'tarea1-0' for task 'tarea1'
23:34:32.716 | INFO    | Flow run 'purple-dogfish' - Executing 'tarea1-0' immediately...
Estudiaste para el examen?
(y/n)?y
23:34:38.330 | INFO    | Task run 'tarea1-0' - Finished in state Completed()
Vas a aprobar
23:34:38.399 | INFO    | Flow run 'purple-dogfish' - Finished in state Completed('All states completed.')
```

También puedes añadir más flujos los cuales serán los encargados de darle flujo a otros flujos o a otras tareas. Se agrega el siguiente flujo:

```python
@flow
def flujo2():
    nota = flujo1()
    if nota > 8:
        print("Excelente obtuviste un ", nota)
    elif nota < 8 and nota > 6:
        print("Vas a reprobar")
        print("Al menos no reprobaste tu nota es ", nota)
    else:
        print("Dios te bendiga x2, tu nota es ", nota)
```

Y el resultado es el siguiente:

```
23:42:13.505 | INFO    | prefect.engine - Created flow run 'lavender-caterpillar' for flow 'flujo2'
23:42:13.769 | INFO    | Flow run 'lavender-caterpillar' - Created subflow run 'cornflower-armadillo' for flow 'flujo1'
23:42:13.906 | INFO    | Flow run 'cornflower-armadillo' - Created task run 'tarea1-0' for task 'tarea1'
23:42:13.922 | INFO    | Flow run 'cornflower-armadillo' - Executing 'tarea1-0' immediately...
Estudiaste para el examen?
(y/n)?n
23:42:18.172 | INFO    | Task run 'tarea1-0' - Finished in state Completed()
23:42:18.224 | INFO    | Flow run 'cornflower-armadillo' - Created task run 'tarea1-1' for task 'tarea1'
23:42:18.224 | INFO    | Flow run 'cornflower-armadillo' - Executing 'tarea1-1' immediately...
Estudiaste para el examen?
(y/n)?n
23:42:21.937 | INFO    | Task run 'tarea1-1' - Finished in state Completed()
Vas a reprobar
Cual fue tu nota del examen?
-> 9
23:43:01.492 | INFO    | Flow run 'cornflower-armadillo' - Finished in state Completed()
Excelente obtuviste un 9
23:43:01.556 | INFO    | Flow run 'lavender-caterpillar' - Finished in state Completed('All states completed.')
```

