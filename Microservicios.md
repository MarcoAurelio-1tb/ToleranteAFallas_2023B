# Práctica Microservicios

Alumno: Marco Aurelio Dominguez Amezcua

Maestro: Michel Emanuel Lopez Franco

Sección: D06 - Tolerante a Fallas

### Introducción

El escalado vertical y el escalado horizontal son dos enfoques utilizados en la gestión de la capacidad de una aplicación basada en microservicios para satisfacer la demanda de tráfico y mantener 
un buen rendimiento. Cada uno de ellos tiene sus propias características y casos de uso.

## Escalado Vertical
   - También se conoce como "escalado hacia arriba" o "escalado de instancias".
   - Implica aumentar la capacidad de recursos de una sola instancia de un servicio, como agregar más CPU, memoria, almacenamiento o capacidad de red.
   - Puede requerir detener temporalmente el servicio o realizar cambios en caliente (en vivo) en la configuración de la instancia.
   - Suele ser más adecuado para aplicaciones que tienen cargas de trabajo intensivas en CPU o memoria en una sola instancia.
   - Puede ser costoso y tiene un límite en cuánto se puede escalar verticalmente antes de alcanzar restricciones físicas o financieras.

## Escalado Horizontal
   - También se conoce como "escalado hacia fuera" o "escalado de instancias múltiples".
   - Implica agregar más instancias del mismo servicio para distribuir la carga entre ellas.
   - No requiere detener el servicio principal, ya que nuevas instancias pueden agregarse y eliminarse según sea necesario.
   - Es especialmente adecuado para aplicaciones que tienen una alta demanda de tráfico, ya que permite una distribución de carga más equitativa.
   - Puede ser más rentable que el escalado vertical, ya que es más fácil y económico agregar instancias virtuales en la nube o en clústeres.
   - Se puede automatizar mediante herramientas de administración de contenedores o orquestación, como Kubernetes.

## Pasos para la actividad

Para esa actividad utilizaremos un balanceador de cargas administrado por Nginx.

Un Load Balancer es como un `Proxy`, este será el encargado de ayudarnos a distribuir el tráfico y administrarlo para distintos servidores.
Un Proxy prácticamente es un intermediario entre el recurso y una petición.

Lo primero que tenemos que hacer después de crear nuestros servidores es tener instalado Nginx y después realizar una modificación.

### Comandos

`Marco Aurelio@DESKTOP-P33M6SQ:~bytes$ vagrant ssh proxy`

Vamos a crear un archivo en la siguiente ruta con el siguiente comando: `sudo touch /etc/nginx/conf.d/load-balancer.conf`

Vamos a eliminar el elemento que se encarga de mostrarnos en el navegador la instancia Proxy, con el siguiente comando vamos a eliminarlo: `sudo rm -r /etc/nginx/sites-enabled/default`

Y después vamos a reiniciar Nginx: `sudo /etc/init.d/nginx restart`

Posteriormente, vamos a modificar al archivo que acabamos de crear. Con el siguiente comando podemos ingresar al archivo: `sudo nano /etc/nginx/conf.d/load-balancer.conf`.

Vamos en este archivo a generar una propiedad llamada upstream íbamos a definir todos los servidores que vamos a utilizar. Además, vamos a definir un bloque llamado que nombraremos 'Server' y en este es donde vamos a definir la configuración de Nginx:

```cmd
upstream backend {
  server 10.0.0.50;
  server 10.0.0.75;
  server 10.0.0.100;
}

server {
  listen 80;
  location / {
    proxy_pass http://backend;
  }
}
```

Volvemos a reiniciar Nginx y ahora sí, podremos ver que al actualizar nuestra ruta principal vamos acceder a los distintos servidores que hemos creado.


## Conclusión

*inserta conclusion
