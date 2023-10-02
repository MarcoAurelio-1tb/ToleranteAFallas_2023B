# Práctica Status (En Servicios de Windows)

Alumno: Marco Aurelio Dominguez Amezcua

Maestro: Michel Emanuel Lopez Franco

Sección: D06 - Tolerante a Fallas

## Introducción

Prefect es una herramienta de orquestación del flujo de trabajo que permite a los desarrolladores crear, observar y reaccionar ante canalizaciones de datos. Es la forma más sencilla de transformar cualquier función de Python en una unidad de trabajo que pueda observarse y orquestarse.

Para xdd

# ![NS](https://github.com/MarcoAurelio-1tb/ToleranteAFallas_2023B/blob/main/Status/Imagenes/nonsucking.PNG)


```python
import sys
import psutil

# Esta funcion solamente es para corroborar que los argumentos para la funcion
# sean válidos
def check_arguments():
    if len(sys.argv) == 1:
    	print('Este programa no funciona sin argumentos')
    	sys.exit(0)

# Con esta funcion solo añadiremos el formato .exe para no tener incompatibilidades
def get_targets():
    targets = sys.argv[1:]
    i = 0
    while i < len(targets):
    	if not targets[i].endswith('.exe'):
    		targets[i] = targets[i] + '.exe'
    	i += 1
    return targets

# La función lock engloba la funcionalidad del bucle que itera sobre los procesos activos.
def lock(target): 
    for proc in psutil.process_iter():
    	if proc.name().lower() == target.lower():
    		proc.kill()

# Funcion main que es el orden en el que se ejecuta cada funcion.
if __name__ == '__main__':

    check_arguments()
    targets = get_targets()

    while True:
    	for target in targets:
    		lock(target)
```
