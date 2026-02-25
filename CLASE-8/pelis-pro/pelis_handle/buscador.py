from typing import List, Dict


class BuscadorPeliculas:
    def __init__(self, peliculas: List[Dict]):
        self.peliculas = peliculas

    def por_titulo(self, texto: str) -> List[Dict]:
        return [
            p for p in self.peliculas
            if texto.lower() in p["titulo"].lower()
        ]

    def por_estreno(self, anio: int) -> List[Dict]:
        return [
            p for p in self.peliculas
            if p["estreno"] == anio
        ]

    def por_tipo(self, tipo: str) -> List[Dict]:
        return [
            p for p in self.peliculas
            if p["tipo"].lower() == tipo.lower()
        ]

    def por_genero(self, genero: str) -> List[Dict]:
        return [
            p for p in self.peliculas
            if genero.lower() in map(str.lower, p["generos"])
        ]


# como ejecutar con init main este modulo
if __name__ == "__main__":
    peliculas = [
        {
            "titulo": "The Matrix",
            "estreno": 1999,
            "tipo": "película",
            "generos": ["acción", "ciencia ficción"]
        },
        {
            "titulo": "Stranger Things",
            "estreno": 2016,
            "tipo": "serie",
            "generos": ["drama", "ciencia ficción", "terror"]
        },
        {
            "titulo": "Inception",
            "estreno": 2010,
            "tipo": "película",
            "generos": ["acción", "ciencia ficción", "thriller"]
        }
    ]

    buscador = BuscadorPeliculas(peliculas)

    print("Películas con 'Matrix' en el título:")
    for p in buscador.por_titulo("Matrix"):
        print(p)

    print("\nPelículas estrenadas en 2010:")
    for p in buscador.por_estreno(2010):
        print(p)

    print("\nSeries:")
    for p in buscador.por_tipo("serie"):
        print(p)

    print("\nPelículas del género 'ciencia ficción':")
    for p in buscador.por_genero("ciencia ficción"):
        print(p)