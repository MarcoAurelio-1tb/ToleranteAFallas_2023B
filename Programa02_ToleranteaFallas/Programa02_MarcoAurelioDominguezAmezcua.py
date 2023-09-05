import pickle
import curses

# Nombre del archivo donde se guarda la información
archivo_datos = 'datos.pkl'

# Función para cargar la información existente o crear una nueva lista vacía
def cargar_o_crear_lista(nombre_archivo):
    try:
        with open(nombre_archivo, 'rb') as archivo:
            datos = pickle.load(archivo)
    except (FileNotFoundError, EOFError):
        datos = []
    return datos

# Función para guardar la lista en el archivo
def guardar_lista(nombre_archivo, lista):
    with open(nombre_archivo, 'wb') as archivo:
        pickle.dump(lista, archivo)

# Función para guardar automáticamente la lista cada vez que se modifica
def guardar_automaticamente(lista):
    guardar_lista(archivo_datos, lista)
    stdscr.addstr(0, 0, "Información guardada automáticamente.")
    stdscr.refresh()

# Configuración de la pantalla de curses
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(True)
curses.noecho()

# Cargar la lista de datos existente o crear una nueva
lista_datos = cargar_o_crear_lista(archivo_datos)

# Mostrar la información actual
stdscr.addstr(1, 0, "Información actual: " + ''.join(lista_datos))
stdscr.refresh()

while True:
    # Obtener el caracter ingresado
    caracter = stdscr.getch()

    # Salir del bucle si el usuario presiona 'qq'
    if caracter == ord('q'):
        break

    # Convertir el valor numérico del caracter en un carácter ASCII
    caracter = chr(caracter)

    # Agregar el caracter a la lista de datos
    lista_datos.append(caracter)

    # Llamar a la función para guardar automáticamente
    guardar_automaticamente(lista_datos)

    # Mostrar la información actualizada
    stdscr.addstr(1, 0, "Información actual: " + ''.join(lista_datos))
    stdscr.refresh()

# Finalizar curses y cerrar el programa
curses.endwin()
print("Saliendo del programa.")
