from pelis_handle import (
    cargar_peliculas,
    BuscadorPeliculas,
    guardar_resultados
)

'''
* Sin __init__.py o este estando vacío, debemos importar así:
from pelis_handle.loader import cargar_peliculas
from pelis_handle.buscador import BuscadorPeliculas
from pelis_handle.persistencia import guardar_resultados
'''


def main():
    peliculas = cargar_peliculas("pelis.json")
    buscador = BuscadorPeliculas(peliculas)

    print("1 - Buscar por título")
    print("2 - Buscar por estreno")
    print("3 - Buscar por tipo")
    print("4 - Buscar por género")

    opcion = input("Opción: ")

    if opcion == "1":
        texto = input("Título: ")
        resultados = buscador.por_titulo(texto)

    elif opcion == "2":
        anio = int(input("Año: "))
        resultados = buscador.por_estreno(anio)

    elif opcion == "3":
        tipo = input("Tipo: ")
        resultados = buscador.por_tipo(tipo)

    elif opcion == "4":
        genero = input("Género: ")
        resultados = buscador.por_genero(genero)

    else:
        print("Opción inválida")
        return

    guardar_resultados(resultados)
    print(f"Resultados guardados: {len(resultados)}")


if __name__ == "__main__":
    main()
