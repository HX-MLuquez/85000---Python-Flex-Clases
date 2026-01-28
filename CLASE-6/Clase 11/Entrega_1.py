def dividir(a, b):
    try:
        return a / b
    # except ZeroDivisionError:  # Capturamos la excepción específica que es ZeroDivisionError que ocurre al dividir entre cero
    #     print("No se puede dividir entre cero")
    except Exception as e:  # Capturamos la excepción específica que es ZeroDivisionError que ocurre al dividir entre cero
        print(f'Ha ocurrido un error: {e}')


print(dividir(10, 0))
print(dividir(10, 2))


'''
* Lista de excepciones comunes en Python:
0. Exception: La clase base para todas las excepciones integradas, excepto las de salida del sistema.
1. ZeroDivisionError: Ocurre cuando se intenta dividir un número por cero.
2. ValueError: Ocurre cuando una función recibe un argumento con el tipo correcto pero un valor inapropiado.
3. TypeError: Ocurre cuando una operación o función se aplica a un objeto de un tipo inapropiado.
4. IndexError: Ocurre cuando se intenta acceder a un índice que está fuera del rango de una secuencia (como una lista o una tupla).
5. KeyError: Ocurre cuando se intenta acceder a una clave que no existe en un diccionario.
6. FileNotFoundError: Ocurre cuando se intenta abrir un archivo que no existe.
7. AttributeError: Ocurre cuando se intenta acceder a un atributo que no existe en un objeto.
8. ImportError: Ocurre cuando un módulo no puede ser importado.
9. KeyboardInterrupt: Ocurre cuando el usuario interrumpe la ejecución del programa (por ejemplo, presionando Ctrl+C).
10. MemoryError: Ocurre cuando el sistema se queda sin memoria para realizar una operación.

Estas excepciones son fundamentales para manejar errores y situaciones inesperadas en los programas de Python.

Ejemplos:
# Ejemplo de Exception
try:
    resultado = 10 / 0
except Exception as e:
    print(f"Se ha producido un error: {e}")

Exception es una clase base, por lo que es mejor capturar excepciones específicas cuando sea posible.
Pero se suele usar para capturar cualquier excepción no prevista.


# Ejemplo de ValueError
try:
    numero = int(input("Introduce un número: "))
except ValueError:
    print("Error: Debes introducir un número válido.")
    
# Ejemplo de TypeError
try:
    resultado = "2" + 3
except TypeError:
    print("Error: No se pueden sumar diferentes tipos de datos.")
    
# Ejemplo de AttributeError
try:
    numero = 5  
    numero.append(10)  # Los enteros no tienen el método append
except AttributeError:
    print("Error: El objeto no tiene el atributo o método especificado.")
    
# Ejemplo de IndexError
lista = [1, 2, 3]
try:
    print(lista[5])
except IndexError:
    print("Error: Índice fuera de rango.")
    
# Ejemplo de FileNotFoundError
try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("Error: El archivo no existe.")
    
# Ejemplo de KeyError
diccionario = {"a": 1, "b": 2}
try:
    print(diccionario["c"])
except KeyError:
    print("Error: La clave no existe en el diccionario.")
    
# Ejemplo de ImportError
try:
    import modulo_inexistente
    
except ImportError:
    print("Error: No se pudo importar el módulo especificado.")
    
# Ejemplo de KeyboardInterrupt
try:
    while True:
        pass  # Bucle infinito
except KeyboardInterrupt:   
    print("Ejecución interrumpida por el usuario.")
    
# Ejemplo de MemoryError
try:
    lista_grande = [0] * (10**10)  # Intentar crear una lista muy grande
except MemoryError:
    print("Error: Memoria insuficiente para completar la operación.")
    
    

'''