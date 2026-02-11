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
# if __name__ == "__main__":