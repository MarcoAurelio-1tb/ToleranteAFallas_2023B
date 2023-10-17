# Práctica Airflow

Alumno: Marco Aurelio Dominguez Amezcua

Maestro: Michel Emanuel Lopez Franco

Sección: D06 - Tolerante a Fallas

## Introducción

Apache Airflow es una plataforma de código abierto diseñada para programar, monitorear y orquestar flujos de trabajo (workflows) de datos y tareas en Python. Se utiliza ampliamente en la gestión de pipelines de datos, la automatización de tareas y la programación de trabajos recurrentes. Algunas de las principales características de Apache Airflow son:

1. **Orquestación de flujos de trabajo**: Airflow permite definir flujos de trabajo complejos como DAGs (Directed Acyclic Graphs), que representan la secuencia y las dependencias entre tareas.

2. **Programación y planificación**: Puedes programar tareas en un horario específico o desencadenarlas según eventos o condiciones.

3. **Monitoreo y registro**: Airflow proporciona una interfaz de usuario web para monitorear el estado de las tareas, ver registros y rastrear el progreso de los flujos de trabajo.

4. **Reintentos y recuperación automática**: Puedes configurar reglas de reintentos para tareas en caso de fallos, y Airflow admite la recuperación automática después de un fallo.

5. **Extensibilidad**: Es altamente extensible y personalizable. Puedes escribir tus proplos operadores y sensores para integrar nuevas tecnologías o servicios.

6. **Escalabilidad**: Airflow puede gestionar flujos de trabajo tanto pequeños como muy grandes, y puede distribuir tareas en clústeres para un alto rendimiento.

Ejemplo de código de un flujo de trabajo simple utilizando Apache Airflow:

```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Definir un DAG
default_args = {
    'owner': 'usuario',
    'start_date': datetime(2023, 10, 16),
    'retries': 1,
}
dag = DAG('informe_ventas_diario', default_args=default_args, schedule_interval='@daily')

# Generar el informe de ventas
def generar_informe():
    # Código para generar el informe de ventas (simulado)
    ventas = [10000, 15000, 12000, 18000]
    total_ventas = sum(ventas)
    return total_ventas

# Enviar el informe por correo electrónico
def enviar_informe_por_correo():
    total_ventas = generar_informe()

    # Configuración del correo
    from_email = 'tu_correo@gmail.com'
    to_email = 'destinatario@example.com'
    subject = 'Informe de Ventas Diario'
    body = f'El total de ventas hoy fue de ${total_ventas}.'

    # Configuración de la tarea de envío de correo
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Enviar el correo
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, 'tu_contraseña')
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Informe enviado por correo electrónico.")
    except Exception as e:
        print(f"Error al enviar el informe: {str(e)}")

# Tareas del flujo de trabajo
generar_informe_task = PythonOperator(
    task_id='generar_informe',
    python_callable=generar_informe,
    dag=dag
)

enviar_informe_por_correo_task = PythonOperator(
    task_id='enviar_informe_por_correo',
    python_callable=enviar_informe_por_correo,
    dag=dag
)

# Definir dependencias
generar_informe_task >> enviar_informe_por_correo_task

```

En este ejemplo, el flujo de trabajo informe_ventas_diario se ejecuta diariamente y consta de dos tareas:

1. La tarea generar_informe simula la generación de un informe de ventas diario.
2. La tarea enviar_informe_por_correo envía el informe por correo electrónico. Se utiliza la biblioteca smtplib para enviar el correo electrónico.

Las dos tareas están conectadas en secuencia, de modo que generar_informe se ejecuta antes que enviar_informe_por_correo. Este flujo de trabajo podría ser útil en un escenario cotidiano en el que se requiera generar y enviar informes de ventas diarios a un destinatario específico.


