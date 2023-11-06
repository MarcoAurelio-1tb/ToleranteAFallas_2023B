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

### Pasos para la actividad



