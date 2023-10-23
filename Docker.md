# Práctica Docker

Alumno: Marco Aurelio Dominguez Amezcua

Maestro: Michel Emanuel Lopez Franco

Sección: D06 - Tolerante a Fallas


### Introducción

Docker es una plataforma de código abierto diseñada para el desarrollo, implementación y ejecución de aplicaciones en contenedores. Los contenedores son entornos ligeros y portátiles que encapsulan aplicaciones y todas sus dependencias, lo que permite la ejecución consistente y aislada en diferentes sistemas operativos.

También, funciona como una herramienta poderosa que simplifica el desarrollo, la implementación y la administración de aplicaciones al encapsularlas en contenedores, lo que proporciona portabilidad y flexibilidad para una amplia gama de casos de uso.

### Pasos para la instalación

Para poder utilizar `Docker` necesitamos instalar un programa que nos permita virtualizar Linux en Windows. Con este programa podemos podemos instalar sistemas Linux como Debian o Ubuntu dentro de Windows.
Nosotros necesitamos instalar Docker y para ello debemos instalar esta herramienta.

"añadir mas texto"

### Pasos para la actividad

Al ejecutar una serie de comandos relacionados con Docker, creando una aplicación utilizando Docker, y luego realizando cambios en esa aplicación. Los comandos se dividen en varias secciones:

**1. Usando Alpine Linux:**
- `docker pull alpine:3.18.4`: Este comando descarga la imagen Alpine Linux versión 3.18.4.
- `docker run -it alpine:3.18.4 sh`: Ejecuta un contenedor interactivo utilizando la imagen Alpine. Esto te llevará a una shell en el contenedor Alpine.

Dentro del contenedor Alpine:
- `apk update`: Actualiza el índice de paquetes.
- `apk upgrade`: Actualiza todos los paquetes instalados.
- `apk add curl`: Instala la herramienta `curl`.
- `curl www.google.com`: Usa `curl` para hacer una solicitud HTTP a www.google.com.
- `exit`: Sale del contenedor.

**2. Usando la imagen de NGINX:**
- `docker pull nginx:1.23`: Descarga la imagen de NGINX versión 1.23.
- `docker pull nginx`: Descarga la última versión estable de NGINX.
- `docker run nginx:1.23`: Ejecuta un contenedor NGINX basado en la versión 1.23.

En otra terminal:
- `docker run -d nginx:1.23`: Ejecuta un contenedor NGINX en segundo plano.

Para ver información sobre contenedores:
- `docker ps`: Lista los contenedores en ejecución.
- `docker ps -a`: Lista todos los contenedores (incluso los que no están en ejecución).

Para ver registros y detener un contenedor:
- `docker logs <container_id>`: Muestra los registros del contenedor especificado.
- `docker stop <container_id>`: Detiene el contenedor especificado.

**3. Exponiendo un puerto con NGINX:**
- `docker run -d -p 9090:80 nginx:1.23`: Ejecuta un contenedor NGINX exponiendo el puerto 9090 en tu máquina local.

**4. Asignando un nombre a tu contenedor:**
- `docker run --name mi-web-app -d -p 9090:80 nginx:1.23`: Ejecuta un contenedor NGINX con un nombre personalizado "mi-web-app". Esto facilita la identificación del contenedor en lugar de utilizar identificadores largos.

**5. Creando una aplicación Node.js con Docker:**
Se crea una aplicación Node.js simple con Express y un Dockerfile para contenerla.

- Código de `src/server.js`: Crea un servidor Express que responde a las solicitudes con un mensaje de bienvenida.
- Contenido de `package.json`: Especifica las dependencias de la aplicación, incluyendo Express.

- `docker build -t node-app:1.0 .`: Crea una imagen Docker llamada "node-app" con la etiqueta "1.0" basada en el Dockerfile y el código fuente.
- `docker run -d -p 3000:3000 node-app:1.0`: Ejecuta un contenedor basado en la imagen "node-app:1.0" y lo expone en el puerto 3000.

**6. Actualizando la aplicación Node.js:**
- Se realiza un cambio en el archivo `src/server.js` para modificar el mensaje de bienvenida.
- `docker stop <container_id>`: Detiene el contenedor en ejecución.
- `docker build -t node-app:1.0 .`: Rebuild de la imagen Docker con la versión actualizada de la aplicación.
- `docker run -d -p 3000:3000 node-app:1.0`: Ejecuta el nuevo contenedor con la versión actualizada de la aplicación.

En resumen, estos comandos muestran cómo usar Docker para descargar imágenes, ejecutar contenedores, exponer puertos, asignar nombres a los contenedores y actualizar una aplicación en un contenedor. La capacidad de versionar y reconstruir contenedores facilita la gestión de aplicaciones y su despliegue en entornos de desarrollo y producción.
