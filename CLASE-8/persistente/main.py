class GestorHobbies:
    def __init__(self, archivo_salida="hobbies.txt"):
        self.archivo_salida = archivo_salida
        self.hobbies = []
    
    def pedir_hobbies(self, cantidad=2):
        """
        Solicita hobbies por teclado y los valida
        """
        for i in range(1, cantidad + 1):
            while True:
                hobby = input(f"Ingrese su hobby favorito #{i}: ").strip()

                if hobby:
                    self.hobbies.append(hobby)
                    break
                else:
                    print("El hobby no puede estar vacío. Intente nuevamente.")

        
    def guardar_en_archivo(self):
        """
        Guarda los hobbies en un archivo de texto
        """
        try:
            with open(self.archivo_salida, "w", encoding="utf-8") as archivo:
                for hobby in self.hobbies:
                    archivo.write(hobby + "\n")

            print(f"\nHobbies guardados correctamente en '{self.archivo_salida}'")
        except Exception as e:
            print("Error al guardar el archivo:", e)
            
    # Método append para agregar hobbies al archivo sin sobrescribir el contenido existente
    def guardar_en_archivo_append(self):
        """
        Guarda los hobbies en un archivo de texto usando append
        """
        try:
            with open(self.archivo_salida, "a", encoding="utf-8") as archivo:
                for hobby in self.hobbies:
                    archivo.write(hobby + "\n")

            print(f"\nHobbies guardados correctamente en '{self.archivo_salida}' (modo append)")

        except Exception as e:
            print("Error al guardar el archivo:", e)
            
    def leer_hobbies(self):
        """
        Lee los hobbies desde el archivo de texto y los muestra por pantalla
        """
        try:
            with open(self.archivo_salida, "r", encoding="utf-8") as archivo:
                hobbies_leidos = [linea.strip() for linea in archivo.readlines()]

            print(f"\nHobbies leídos desde '{self.archivo_salida}':")
            for hobby in hobbies_leidos:
                print(f"- {hobby}")

        except Exception as e:
            print("Error al leer el archivo:", e)


def main():
    gestor = GestorHobbies()
    gestor.pedir_hobbies()
    # gestor.guardar_en_archivo()
    gestor.guardar_en_archivo_append()
    gestor.leer_hobbies()

if __name__ == "__main__":
    main()

'''
* OPEN sin el with 
archivo = open("hobbies.txt", "w", encoding="utf-8")
    for hobby in self.hobbies:
        archivo.write(hobby + "\n")
archivo.close() # OJO, si se produce un error antes de esta línea, 
el archivo no se cerrará correctamente, lo que puede causar problemas 
de rendimiento o corrupción de datos.
'''