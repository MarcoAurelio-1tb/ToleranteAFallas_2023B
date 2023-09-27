# Práctica Status (En Servicios de Windows)

Alumno: Marco Aurelio Dominguez Amezcua
Maestro: Michel Emanuel Lopez Franco
Sección: D06 - Tolerante a Fallas

## Introducción

Para la creación de esta práctica realizaremos una aplicación con la cual nos permita cerrar una aplicación con el formato “.exe”. Gracias a esta práctica podemos mantener siempre cerrado el programa que nosotros decidamos, esta funcionalidad estará ejecutándose desde los servicios de nuestro SO, por lo tanto, cada vez que el usuario abra manualmente una app esta se cerrará.

Para esta práctica debemos instalar Non-Sucking Service Manager e instalar sus respectivos requerimientos para posteriormente ejecutar comandos desde el símbolo de sistema (CMD). Para esta práctica tomaremos como aplicación de prueba el navegador firefox, la cual se va a cerrar siempre que el usuario la abra.

![Non-Sucking Service Manager](https://github.com/MarcoAurelio-1tb/ToleranteAFallas_2023B/blob/main/Status/Imagenes/nonsucking.PNG)

Despues de configurarlo, lo activamos con el comando “nssm.exe start proclocker” desde el símbolo de sistema. Aquí es donde aparecerá directamente en nuestros servicios del sistema operativo y quiere decir que ya está funcionando.

Para este programa se debemos instalar las bibliotecas:
-	sys: para acceder a la consola del sistema operativo.
-	psutil: nos permite acceder a la información sobre los procesos que se corren en los servicios del sistema.

El código sería el siguiente:

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

# Referencias

(N.d.). Tecnobillo.com. Retrieved September 27, 2023, from https://tecnobillo.com/sections/python-en-windows/servicios-windows-python/servicios-windows-python.html
