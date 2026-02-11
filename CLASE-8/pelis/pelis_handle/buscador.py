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

# if __name__ == "__main__":
#     peliculas = [
#         {"titulo": "Inception", "estreno": 2010, "tipo": "película", "generos": ["Ciencia ficción", "Acción", "Drama"]},
#         {"titulo": "The Godfather", "estreno": 1972, "tipo": "película", "generos": ["Crimen", "Drama"]},
#         {"titulo": "Breaking Bad", "estreno": 2008, "tipo": "serie", "generos": ["Crimen", "Drama"]},
#     ]

#     buscador = BuscadorPeliculas(peliculas)

#     print("Películas con 'Inception' en el título:")
#     print(buscador.por_titulo("Inception"))

#     print("\nPelículas estrenadas en 2010:")
#     print(buscador.por_estreno(2010))

#     print("\nSeries:")
#     print(buscador.por_tipo("serie"))

#     print("\nPelículas del género 'Drama':")
#     print(buscador.por_genero("Drama"))