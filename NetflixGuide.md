# Student Data

Student: Marco Aurelio Dominguez Amezcua

Teacher: Michel Emanuel Lopez Franco

Section: D06 - Tolerante a Fallas

# Netflix Guide to Microservices

El video trata sobre la arquitectura de microservicios y cómo Netflix ha enfrentado desafíos y soluciones en los últimos años. Se discuten temas como dependencias, escalabilidad, variantes y cambios en la arquitectura. Se destaca la importancia de la automatización, la integración de mejores prácticas en el proceso de entrega y la influencia de la estructura organizativa en el diseño de sistemas. También se mencionan herramientas de código abierto desarrolladas por Netflix.

La arquitectura de microservicios es un enfoque para desarrollar aplicaciones en el que una aplicación se descompone en pequeños servicios independientes, cada uno de los cuales se ejecuta en su propio proceso y se comunica con otros servicios a través de API bien definidas. Este enfoque proporciona flexibilidad, escalabilidad y facilita la implementación continua.

Netflix es conocido por su exitosa implementación de arquitectura de microservicios, lo que le ha permitido manejar grandes volúmenes de tráfico y ofrecer servicios a escala global. Aquí hay algunas áreas clave en las que Netflix ha enfrentado desafíos y ha implementado soluciones:

### 1. Dependencias y Comunicación entre Microservicios:
   - **Desafío:** La gestión de dependencias entre microservicios puede ser compleja.
   - **Solución:** Netflix utiliza tecnologías como Spring Cloud y Netflix OSS para facilitar la comunicación entre servicios. También emplea la arquitectura de puertas de enlace (gateway) para simplificar el acceso a los microservicios y manejar la resiliencia.

### 2. Escalabilidad:
   - **Desafío:** Escalar servicios de manera eficiente puede ser un desafío en sistemas distribuidos.
   - **Solución:** Netflix utiliza la escalabilidad horizontal y el aprovisionamiento automático para manejar picos de tráfico. Además, emplea herramientas como Spinnaker para facilitar la implementación y la gestión del ciclo de vida de las aplicaciones.

### 3. Variantes y Cambios en la Arquitectura:
   - **Desafío:** La introducción de nuevas características y cambios en la arquitectura puede ser complicada.
   - **Solución:** Netflix utiliza el concepto de "blow away and replace" para actualizar servicios de manera incremental. Además, aprovecha la automatización y la implementación continua para facilitar cambios sin problemas.

### 4. Automatización y Mejores Prácticas en la Entrega:
   - **Desafío:** La implementación continua y la automatización son esenciales pero pueden ser complejas.
   - **Solución:** Netflix ha desarrollado y contribuido a herramientas de código abierto como Spinnaker, que es una plataforma de entrega continua y orquestación de implementaciones. Esto facilita la automatización y el despliegue de aplicaciones de manera eficiente.

### 5. Influencia de la Estructura Organizativa:
   - **Desafío:** La estructura organizativa puede afectar la implementación y evolución de la arquitectura de microservicios.
   - **Solución:** Netflix sigue un modelo organizativo basado en equipos autónomos. Cada equipo es responsable de uno o más microservicios, lo que permite la toma de decisiones rápida y la innovación.

### 6. Herramientas de Código Abierto:
   - Netflix ha contribuido a varias herramientas de código abierto que son fundamentales para su arquitectura de microservicios, como:
      - **Eureka:** Un servicio de registro para facilitar la localización de servicios.
      - **Ribbon:** Una biblioteca para cargar equilibradores de carga en el lado del cliente.
      - **Hystrix:** Una biblioteca para gestionar la resiliencia de servicios.
      - **Spinnaker:** Una plataforma de implementación continua y orquestación de implementaciones.

En resumen, la arquitectura de microservicios en Netflix se basa en la descentralización, la automatización, y la integración de herramientas de código abierto para abordar los desafíos asociados con la escala y la complejidad de sus servicios. La estructura organizativa también desempeña un papel crucial al empoderar a los equipos para que sean responsables de sus propios microservicios.

# Guillain-Barré 

### Síndrome de Guillain-Barré (GBS):

El síndrome de Guillain-Barré es un trastorno neurológico en el cual el sistema inmunológico del cuerpo ataca los nervios periféricos. Esto puede llevar a una variedad de síntomas, incluyendo debilidad muscular, hormigueo y, en casos graves, parálisis. Aunque la causa exacta del GBS no se conoce con certeza, a menudo está precedido por una infección viral o bacteriana.

### Tratamiento del Síndrome de Guillain-Barré:

El tratamiento del GBS a menudo implica cuidados de apoyo y terapias físicas para ayudar en la recuperación. En casos más graves, puede ser necesaria la hospitalización y en algunos casos, la administración de inmunoglobulinas o plasmaféresis para reducir la gravedad de los síntomas.

### Relación con la Arquitectura de Microservicios:

La relación directa entre el síndrome de Guillain-Barré y la arquitectura de microservicios no está clara, ya que el GBS es un trastorno médico y la arquitectura de microservicios es un enfoque de desarrollo de software. Sin embargo, si hay alguna referencia específica a la experiencia de la madrastra de Josh Evans en relación con la arquitectura de microservicios, esa información podría proporcionar más contexto.

### Charla sobre Arquitectura de Microservicios y Desafíos en Netflix:

Netflix es conocido por su arquitectura de microservicios altamente escalable. Josh Evans, quien trabajó en Netflix, ha compartido sus experiencias y conocimientos en varias charlas sobre arquitectura de microservicios y desafíos asociados. Estas charlas suelen abordar temas como la gestión de dependencias, escalabilidad, implementación continua y resiliencia en un entorno distribuido.

# Monolítica

### Desafíos de la Arquitectura Monolítica:

1. **Complejidad y Acoplamiento:**
   - En una arquitectura monolítica, todos los componentes están fuertemente acoplados, lo que significa que un cambio en una parte del sistema puede tener efectos inesperados en otras áreas.

2. **Dificultad en el Escalamiento:**
   - Escalar una aplicación monolítica puede ser desafiante, ya que toda la aplicación debe escalarse en lugar de solo los módulos específicos que requieren mayor capacidad.

3. **Dificultad en la Implementación Continua:**
   - Las actualizaciones y despliegues continuos pueden ser complicados, ya que la modificación de una parte del código puede afectar otras partes, lo que aumenta el riesgo de errores.

4. **Problemas de Diagnóstico:**
   - Identificar y solucionar problemas en una aplicación monolítica puede ser más difícil debido a la falta de separación clara entre los componentes.

### Beneficios de la Arquitectura de Microservicios:

1. **Modularidad:**
   - Los microservicios dividen la aplicación en pequeños servicios independientes, lo que facilita la modificación, el mantenimiento y el despliegue de cada componente de manera independiente.

2. **Escalabilidad:**
   - Los microservicios permiten escalar partes específicas de una aplicación en función de la demanda, lo que mejora la eficiencia en comparación con el escalamiento completo de una aplicación monolítica.

3. **Particionamiento de Carga:**
   - Al dividir la aplicación en microservicios, se puede distribuir la carga de manera más eficiente, ya que cada microservicio puede manejar su propia carga de trabajo sin afectar a los demás.

4. **Flexibilidad Tecnológica:**
   - Cada microservicio puede estar desarrollado utilizando tecnologías diferentes, lo que proporciona flexibilidad para seleccionar la tecnología más adecuada para cada función.

### Arquitectura de Microservicios en Netflix:

1. **Descentralización:**
   - Netflix utiliza una arquitectura de microservicios descentralizada, donde cada servicio es independiente y tiene su propia base de datos. Esto reduce la complejidad y facilita la gestión de cada servicio por separado.

2. **Modularidad:**
   - La arquitectura de microservicios de Netflix permite la independencia y evolución de servicios de manera individual, lo que contribuye a una mayor agilidad y capacidad para adaptarse a cambios.

3. **Escalabilidad Dinámica:**
   - Netflix puede escalar servicios específicos según la demanda, garantizando un rendimiento óptimo sin la necesidad de escalar toda la aplicación.

En resumen, la arquitectura monolítica presenta desafíos relacionados con la complejidad, la escalabilidad y la implementación continua, mientras que los microservicios ofrecen beneficios como modularidad, escalabilidad y particionamiento de carga. La implementación de microservicios en Netflix ilustra cómo la descentralización y la modularidad pueden abordar estos desafíos de manera efectiva.

# Microservicios

### Desafíos y Soluciones en Microservicios:

#### 1. Dependencias entre Microservicios:
   - **Desafío:** La gestión de dependencias entre microservicios puede ser compleja y aumenta la posibilidad de fallos en cascada.
   - **Solución:** Implementar un enfoque de diseño que minimice las dependencias, utilizar contratos de API bien definidos y tecnologías de descubrimiento de servicios como Eureka.

#### 2. Escalabilidad y Pruebas:
   - **Desafío:** Escalar microservicios de manera eficiente y realizar pruebas integradas pueden ser desafiantes debido a la naturaleza distribuida del sistema.
   - **Solución:** Emplear prácticas de escalamiento horizontal, utilizar herramientas de orquestación como Kubernetes para gestionar contenedores y aplicar pruebas unitarias y de integración continuas.

#### 3. Complejidad de Datos y Capa de Persistencia:
   - **Desafío:** La gestión de datos distribuidos y la persistencia puede resultar compleja.
   - **Solución:** Utilizar bases de datos específicas para cada microservicio y adoptar patrones de diseño de bases de datos distribuidas como CQRS (Command Query Responsibility Segregation) para separar operaciones de escritura y lectura.

#### 4. Bibliotecas de Cliente, Caché y Orquestación:
   - **Desafío:** Coordinar las comunicaciones entre microservicios y gestionar la coherencia de los datos.
   - **Solución:**
      - **Bibliotecas de Cliente:** Emplear bibliotecas como Feign para simplificar las llamadas entre microservicios.
      - **Caché:** Utilizar sistemas de caché distribuida para mejorar el rendimiento y reducir la carga en los servicios.
      - **Orquestación:** Implementar sistemas de orquestación como Netflix Conductor o Apache Kafka para coordinar flujos de trabajo entre microservicios.

#### 5. Desafíos con Dependencias entre Microservicios y Soluciones con Hystrix:
   - **Desafío:** La dependencia entre microservicios puede generar fallos en cascada.
   - **Solución:** Implementar Hystrix, una biblioteca de tolerancia a fallos que ayuda a controlar y aislar fallas en sistemas distribuidos, proporcionando resistencia a fallos.

Los desafíos en la arquitectura de microservicios incluyen la gestión de dependencias, escalabilidad, complejidad en la capa de persistencia y la necesidad de coordinación entre servicios. Las soluciones involucran el diseño cuidadoso de contratos de API, el uso de herramientas de escalabilidad y orquestación, la gestión eficiente de datos distribuidos, el uso de bibliotecas de cliente y la implementación de mecanismos de tolerancia a fallos como Hystrix para asegurar la resiliencia del sistema.

# Infraestructura de Microservicios de Netflix

### Desafíos y Soluciones en la Infraestructura de Microservicios de Netflix:

1. **Desafíos:**
   - **Complejidad de Dependencias:** Gestionar las interconexiones entre microservicios puede ser complejo.
   - **Escalabilidad Eficiente:** Asegurar que la infraestructura pueda escalar de manera efectiva para manejar grandes volúmenes de tráfico.

2. **Soluciones:**
   - **Descentralización:** Netflix utiliza una arquitectura descentralizada basada en microservicios para reducir la complejidad y permitir la escalabilidad independiente.

### Importancia de Probar Microservicios Críticos:

- **Razón:**
  - La prueba rigurosa de microservicios críticos asegura su rendimiento y fiabilidad, evitando fallos que podrían afectar a la experiencia del usuario.

### Uso de Bibliotecas de Cliente y Desafíos:

1. **Desafíos:**
   - **Coordinación de Comunicación:** Coordinar las interacciones entre microservicios puede ser desafiante.
   - **Manejo de Errores:** Gestionar errores de manera efectiva y garantizar la tolerancia a fallos.

2. **Soluciones:**
   - **Bibliotecas de Cliente:** Emplear bibliotecas como Feign para facilitar la comunicación entre microservicios y manejar errores de manera robusta.

### Elección de Cassandra y Consistencia Eventual:

- **Elección de Cassandra:**
  - Netflix elige Cassandra como base de datos, proporcionando escalabilidad y tolerancia a fallos.

- **Consistencia Eventual:**
  - Optar por un modelo de consistencia eventual en Cassandra para mejorar el rendimiento, sacrificando la consistencia inmediata en favor de la disponibilidad y la tolerancia a fallos.

En resumen, Netflix aborda desafíos en su infraestructura de microservicios mediante una arquitectura descentralizada, la prueba meticulosa de microservicios críticos, el uso de bibliotecas de cliente como Feign, y la elección de tecnologías como Cassandra con un enfoque en consistencia eventual para mejorar la escalabilidad y la tolerancia a fallos.

# AWS

### Estrategias en Infraestructura de AWS:

1. **Durabilidad vs. Disponibilidad:**
   - *Durabilidad:* AWS ofrece opciones para durabilidad de datos, pero asumir riesgos puede traducirse en mayor disponibilidad.
   - *Disponibilidad:* La infraestructura de AWS está diseñada para garantizar la continuidad del servicio incluso en situaciones de fallo.

2. **Continuidad del Servicio:**
   - Aunque la infraestructura puede enfrentar fallos, se busca garantizar que los servicios se mantengan operativos sin interrupciones significativas.

3. **Estrategias de Escalado Automático y Replicación:**
   - Para microservicios en la nube, las estrategias clave incluyen el escalado automático para adaptarse a la demanda y la replicación para garantizar redundancia y disponibilidad continua.

### Patrones de Éxito y Desafíos en la Arquitectura de Netflix:

1. **Éxito con Edie Cache:**
   - Netflix emplea Edie Cache, una tecnología que envuelve a Memcache D, para mejorar la eficiencia en el manejo de cachés y optimizar la entrega de contenidos.

2. **Desafío de Deriva Operativa y Nuevas Variantes:**
   - La arquitectura de Netflix enfrenta el desafío de la deriva operativa, donde las configuraciones pueden cambiar con el tiempo, y la introducción de nuevas variantes puede afectar la estabilidad del sistema.

3. **Automatización y Aprendizaje Continuo:**
   - Netflix destaca la importancia de la automatización en la gestión de su arquitectura, permitiendo la implementación continua y aprendizaje continuo para adaptarse a cambios y mejorar la eficiencia operativa.

### Introducción de Nuevas Tecnologías en la Arquitectura de Microservicios:

La incorporación de nuevas tecnologías en la arquitectura de microservicios implica consideraciones cuidadosas y cambios significativos. En el caso de Netflix, están invirtiendo en un nuevo nivel de gestión de cargas de trabajo en la nube llamado Titus, indicando un enfoque estratégico para la evolución de su infraestructura.

### Inversión en Titus para Gestión de Cargas de Trabajo:

Netflix está apostando por Titus como un nuevo componente para gestionar cargas de trabajo en la nube. Este enfoque sugiere una dedicación hacia la mejora y optimización de su infraestructura para abordar las demandas específicas de su arquitectura de microservicios.

### Desafíos y Lecciones en la Arquitectura de Microservicios en Netflix:

La arquitectura de microservicios presenta desafíos únicos, y en Netflix, se han enfrentado a estos desafíos y han aprendido valiosas lecciones. Los cambios en la arquitectura, la gestión de dependencias, la escalabilidad y la complejidad operativa son aspectos críticos que deben ser considerados y gestionados de manera efectiva.

### Impacto Positivo de la API de Netflix en la Innovación:

La API de Netflix ha desempeñado un papel fundamental al facilitar la innovación en la interfaz de usuario y la generación de listas. Proporciona una interfaz accesible que permite a los desarrolladores explorar y utilizar datos de manera creativa, fomentando así la evolución continua de la experiencia del usuario y la funcionalidad de la plataforma.

La introducción de nuevas tecnologías como Titus, los desafíos enfrentados y las lecciones aprendidas en la arquitectura de microservicios de Netflix, junto con el impacto positivo de la API en la innovación, subrayan la importancia de una planificación estratégica y una gestión cuidadosa al evolucionar la infraestructura de microservicios.
