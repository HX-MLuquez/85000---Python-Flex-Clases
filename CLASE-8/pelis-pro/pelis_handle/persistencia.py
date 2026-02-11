import csv
import os
from typing import List, Dict


CAMPOS = [
    "id",
    "titulo",
    "tipo",
    "estreno",
    "director",
    "calificacion_imdb"
]


def guardar_resultados(resultados: List[Dict], path: str = "db.csv") -> None:
    archivo_existe = os.path.exists(path)

    with open(path, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=CAMPOS)

        if not archivo_existe:
            writer.writeheader()

        for p in resultados:
            writer.writerow({
                "id": p["id"],
                "titulo": p["titulo"],
                "tipo": p["tipo"],
                "estreno": p["estreno"],
                "director": p["director"],
                "calificacion_imdb": p["calificacion_imdb"]
            })
