import json
from typing import List, Dict


def cargar_peliculas(path: str) -> List[Dict]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError("No se encontró el archivo pelis.json")
    except json.JSONDecodeError:
        raise ValueError("JSON inválido")
