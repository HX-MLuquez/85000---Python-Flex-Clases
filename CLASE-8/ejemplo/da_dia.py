# Crear funcion que pasamos python da_dia.py 10-02-2026 y retorna Martes
import sys
from datetime import datetime

def dia_semana(fecha_str):
    fecha = datetime.strptime(fecha_str, '%d-%m-%Y')
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    return dias_semana[fecha.weekday()]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fecha_str = sys.argv[1]
        dia = dia_semana(fecha_str)
        print(f'El día de la semana para {fecha_str} es: {dia}')
    else:
        print('Por favor, ingresa una fecha en formato dd-mm-yyyy')