"""
Created by: Marco Aurelio DA
"""

from datetime import *
from time import sleep, perf_counter
import threading

def add_years(start_date, years):
    try:
        return start_date.replace(year=start_date.year + years)
    except ValueError:
        # 👇️ preserve calendar day (if Feb 29th doesn't exist, set to 28th)
        return start_date.replace(year=start_date.year + years, day=28)
    
def hoyanavidad(hoy, navidad, bis):
    bisYears = 0
    for i in range(0, 6):
        currentYear = add_years(navidad, i) # año actual = 2023
        
        for b in range(len(bis)):
            if bis[b] != currentYear.year:
                if b == len(bis)-1:
                    dias = (currentYear-hoy).days
                else:
                    pass
            else:
                if b == len(bis)-1:
                    dias = (currentYear-hoy).days
                    bisYears+=1
                    dias=dias+bis
                else:
                    pass
        sleep(1)        
        print(f"🎄 Faltan {dias} días para NAVIDAD del año {currentYear.year}")
        
        #dias = (currentYear-hoy).days # resta del año sig con actual
        #print(f"Faltan {dias} para navidad del año {currentYear.year}") # imprimir
        
#compararNavidad(thisYear)

def hoyahalloween(hoy, hw, bis):
    #start_time = perf_counter()
    bisYears = 0
    for i in range(0, 6):
        currentYear = add_years(hw, i) # año actual = 2023
        
        for b in range(len(bis)):
            if bis[b] != currentYear.year:
                if b == len(bis)-1:
                    dias = (currentYear-hoy).days
                else:
                    pass
            else:
                if b == len(bis)-1:
                    dias = (currentYear-hoy).days
                    bisYears+=1
                    dias=dias+bis
                else:
                    pass
        sleep(1)       
        print(f"🎃 Faltan {dias} días para HALLOWEEN del año {currentYear.year}")
        #end_time = perf_counter()
        #print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')
        

start_time = perf_counter()

bisiestos = [2024, 2028, 2032]

fechahoy = date.today()
navidad = date(2023, 12, 25)
halloween = date(2023, 10, 31)


hilo_halloween = threading.Thread(target=hoyahalloween, args=(fechahoy, halloween, bisiestos,))
hilo_navidad = threading.Thread(target=hoyanavidad, args=(fechahoy, navidad, bisiestos,))

hilo_halloween.start()
hilo_navidad.start()

hilo_halloween.join()
hilo_navidad.join()

end_time = perf_counter()

print(f'\nIt took {end_time- start_time: 0.2f} second(s) to complete.')

#print("Este código está debajo de los hilos")