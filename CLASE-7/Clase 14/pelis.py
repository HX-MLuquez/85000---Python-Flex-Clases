# Clase PELIS
class Pelis:
    def __init__(self, id, titulo, director, estreno, generos):
        self.id = id
        self.titulo = titulo or "Título desconocido"
        self.director = director
        self.estreno = estreno
        self.generos = generos # Lista de géneros asociados a la película

    # def mostrar_info(self):
    #     print(f"Título: {self.titulo}")
    #     print(f"Director: {self.director}")
    #     print(f"Año de estreno: {self.estreno}")

# Clase Peliculas
class Peliculas:
    def __init__(self):
        self.peliculas = [] # Lista para almacenar objetos de tipo Pelis

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)

    def mostrar_peliculas(self):
        for pelicula in self.peliculas:
            pelicula.mostrar_info()
            print(f"Géneros: {', '.join(pelicula.generos)}")
            print("-" * 20)

generos = ["Ciencia ficción", "Acción", "Drama", "Crimen"]
# Ejemplo de uso 

class Genres:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
    

pelicula1 = Pelis(1, "Inception", "Christopher Nolan", 2010, [generos[0], generos[1], generos[2]])
pelicula2 = Pelis(2, "The Godfather", "Francis Ford Coppola", 1972, [generos[3], generos[2]])

peliculas = Peliculas()
peliculas.agregar_pelicula(pelicula1)
peliculas.agregar_pelicula(pelicula2)
peliculas.mostrar_peliculas()