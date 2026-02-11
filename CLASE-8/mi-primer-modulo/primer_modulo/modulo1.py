class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


    def __str__(self):
        return f"NOMBRE {self.nombre}"

# OJO esto es el primer ejemplo, siempre es aconsejable que los 
# modulos y paquetes tengan nombres representativos

if __name__ == "__main__":
    # Este es el espacio independiente de prueba del modulo, no se ejecuta al importar el modulo
    persona2 = Persona("Pepito", "Lopez")
    print(persona2)