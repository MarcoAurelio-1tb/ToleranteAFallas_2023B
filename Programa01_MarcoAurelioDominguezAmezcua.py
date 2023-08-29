# Diferentes programas con varias alternativas para conocer que hace cada una de ellas.

"""

# En este programa debemos asignar valores para una division, en nuestro bloque de código
# evitamos que el programa se detenga por algún motivo.

denominator = int(input("Insert the denominator: "))
numerator = int(input("Insert the numerator: "))

try:
    print("The result is ", denominator / numerator)
except ZeroDivisionError as e:
    print(str(e))
except ValueError as e:
    print(str(e))
except NameError as e:
    print(str(e))

"""

# -----

"""
# En este programa nuevamente realizamos una division, en este caso automatizada, utilizando diferentes
# tipos de datos los cuales generan diferentes errores. Con el programa se tratan cada uno de ellos.

values = [10, 5, 0, "hello"]

for value in values:
    try:
        print(10/int(value))
    except (ZeroDivisionError, ValueError) as e:
        print(str(e))
"""

# -----

"""
# Este pequeño bloque de código es una prueba de cuando se utilizan variables que no son las llamadas en las
# funciones, al no tratarse del nombre asignado correcto, salta un error y es por ello que se debe de tratar.

try:
    y = int(input("Insert the x value: "))
    print("The x value is: ")
    print(x)
except NameError as e:
    print(str(e))

"""
# ---------


"""
print("If you have a mistake, you'll be in infinite cycle\nLet's start!")
coin = True

while coin:
    print("Type an int number, JUST AN INT NUMBER")
    try:
        number = input("Your answer: ")
    except 
"""

"""
# Este programa es otra alternativa de como abarcar los maximos posibles errores que existen 
# el objetivo es también evitar errores durante la ejecución y terminar correctamente

print("If you have a mistake, you'll be in an infinite loop\nLet's start!")
coin = True
while coin:
    try:
        denominator = int(input("Insert the denominator: "))
        numerator = int(input("Insert the numerator: "))
        print("Result is: ", "{0:.2f}".format(denominator/numerator))
    except (ZeroDivisionError, ValueError, AttributeError, NameError) as e:
        print("-----")
        print(str(e))
        print("Try again...\n-----")
    else:
        print("Congratulations you're not an idiot :D")
        coin = False
        
"""

