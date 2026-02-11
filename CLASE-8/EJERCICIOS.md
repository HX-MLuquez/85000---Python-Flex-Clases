# Ejercicios prácticos – Módulos, paquetes y archivos

---

## 🟢 Bloque 1 – Scripts básicos y argumentos

### 1️⃣ Script saludo personalizado

**Objetivo:** usar `sys.argv`.

* Crear un script `saludo.py`
* Recibe por argumento un nombre.
* Muestra: `Hola <nombre>, bienvenido al sistema`
* Validar cantidad de argumentos.
* Mostrar mensaje de ayuda si faltan argumentos.

👉 Buenas prácticas:

* Validar `len(sys.argv)`
* Usar `if __name__ == "__main__"`

---

### 2️⃣ Repetir texto con argumentos

**Objetivo:** tipos de datos + validaciones.

* Script `repetir.py`
* Argumentos:

  * texto
  * cantidad de repeticiones
* Convertir a `int`
* Manejar error si no es un número.

👉 Extra:

* Usar `try / except ValueError`

---

## 🟢 Bloque 2 – Módulos y funciones

### 3️⃣ Módulo de utilidades matemáticas

**Objetivo:** crear y usar módulos.

* Crear `utilidades.py` con:

  * `sumar(a, b)`
  * `restar(a, b)`
* Crear `main.py` que importe el módulo y use las funciones.

👉 Buenas prácticas:

* Funciones pequeñas
* Nombres claros
* No ejecutar código al importar

---

### 4️⃣ Módulo de validaciones

**Objetivo:** separar responsabilidades.

* Crear `validaciones.py`
* Función `es_entero(valor)`
* Usar esa función desde otro archivo.

👉 Concepto clave:

* Reutilización de código

---

## 🟢 Bloque 3 – Clases y módulos

### 5️⃣ Clase Alumno en un módulo

**Objetivo:** POO + módulos.

* Archivo `alumno.py`
* Clase `Alumno`:

  * atributos: nombre, nota
  * método `imprimir()`
* Archivo `main.py`:

  * crear un alumno
  * mostrar datos

👉 Buenas prácticas:

* Constructor `__init__`
* Métodos simples
* Un archivo = una responsabilidad

---

### 6️⃣ Lista de alumnos

**Objetivo:** trabajar con listas + objetos.

* Crear varios alumnos en una lista
* Recorrer e imprimir todos
* Calcular promedio de notas

👉 Extra:

* Método `aprobo()` en la clase

---

## 🟢 Bloque 4 – Paquetes

### 7️⃣ Primer paquete

**Objetivo:** estructura de proyecto.

* Crear paquete `personas/`

  * `__init__.py`
  * `alumno.py`
  * `profesor.py`
* Importar desde `main.py`

👉 Buenas prácticas:

* Organización
* Imports correctos

---

## 🟢 Bloque 5 – Escritura y lectura de archivos TXT

### 8️⃣ Guardar hobbies en un archivo

**Objetivo:** persistencia.

* Pedir 3 hobbies por teclado
* Guardarlos en `hobbies.txt`
* Usar un `for`

👉 Buenas prácticas:

* `with open(...)`
* Saltos de línea correctos

---

### 9️⃣ Leer hobbies desde archivo

**Objetivo:** lectura de archivos.

* Leer `hobbies.txt`
* Mostrar cada hobby numerado

👉 Extra:

* Usar `.strip()`

---

## 🟢 Bloque 6 – JSON

### 🔟 Guardar datos en JSON

**Objetivo:** estructura de datos.

* Pedir nombre y edad
* Guardar en `usuario.json`

👉 Buenas prácticas:

* Usar `json.dump`
* Diccionario bien definido

---

### 1️⃣1️⃣ Leer datos desde JSON

**Objetivo:** recuperación de datos.

* Leer `usuario.json`
* Mostrar mensaje personalizado

---

## 🟢 Bloque 7 – CSV (intro)

### 1️⃣2️⃣ Leer un CSV simple

**Objetivo:** ingestión de datos reales.

* CSV con: nombre, edad
* Leer y mostrar datos
* Contar registros

👉 Extra:

* Usar `csv` o `pandas` (según nivel)

---

## 🟢 Ejercicio integrador (final)

### 1️⃣3️⃣ Sistema simple de alumnos

**Incluye:**

* Clase `Alumno`
* Archivo TXT o JSON
* Menú por consola:

  * Agregar alumno
  * Listar alumnos
  * Guardar datos

👉 Conceptos:

* POO
* Archivos
* Modularización
* Buenas prácticas reales 💪

---


