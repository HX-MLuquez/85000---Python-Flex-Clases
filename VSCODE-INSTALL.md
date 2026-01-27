# Visual Studio Code (VS Code) en Windows, Linux y macOS

---

## ¿Qué es VS Code?

VS Code es un editor de código liviano, rápido y muy potente. Funciona para casi cualquier lenguaje (JavaScript, Python, Java, C#, etc.) y es ideal tanto para empezar como para trabajar de forma profesional.

---

# 1️⃣ Instalación en **Windows**

### Paso 1: Descargar

1. Abrí tu navegador.
2. Entrá a:
   👉 [https://code.visualstudio.com](https://code.visualstudio.com)
3. Hacé clic en **Download for Windows**.

### Paso 2: Instalar

1. Abrí el archivo descargado (`VSCodeUserSetup.exe`).
2. Aceptá la licencia.
3. En la pantalla de opciones, **recomendado marcar**:
   - ✅ _Add to PATH_ (muy importante)
   - ✅ _Open with Code_ (para archivos)
   - ✅ _Open with Code_ (para carpetas)

4. Clic en **Install**.

### Paso 3: Abrir VS Code

- Desde el menú Inicio → **Visual Studio Code**
- O clic derecho sobre una carpeta → **Open with Code**

---

# 2️⃣ Instalación en **macOS**

### Paso 1: Descargar

1. Entrá a:
   👉 [https://code.visualstudio.com](https://code.visualstudio.com)
2. Clic en **Download for macOS**.

### Paso 2: Instalar

1. Abrí el archivo `.zip`.
2. Arrastrá **Visual Studio Code** a la carpeta **Applications**.

### Paso 3: Abrir

- Desde **Launchpad** o **Applications**
- La primera vez, macOS puede pedir confirmación → **Open**

### (Opcional pero recomendado) Activar comando `code`

1. Abrí VS Code.
2. Presioná `Cmd + Shift + P`.
3. Escribí:
   **Shell Command: Install 'code' command in PATH**
4. Enter.

Esto te permite abrir VS Code desde la terminal con:

```bash
code .
```

---

# 3️⃣ Instalación en **Linux**

### Opción A: Ubuntu / Debian (.deb)

1. Descargá el archivo `.deb` desde:
   👉 [https://code.visualstudio.com](https://code.visualstudio.com)
2. Abrí una terminal en la carpeta descargada.
3. Ejecutá:

```bash
sudo dpkg -i code_*.deb
sudo apt-get install -f
```

---

### Opción B: Snap (la más simple)

Funciona en muchas distribuciones.

```bash
sudo snap install code --classic
```

---

### Opción C: Fedora / RHEL (.rpm)

```bash
sudo rpm -i code-*.rpm
```

---

# 4️⃣ Verificar que quedó bien instalado

Abrí una terminal (o PowerShell en Windows) y escribí:

```bash
code --version
```

Si ves la versión, está todo OK ✅

---

# 5️⃣ Primeros pasos recomendados

### 1. Cambiar idioma a español (opcional)

- `Ctrl + Shift + P` / `Cmd + Shift + P`
- Escribí: **Configure Display Language**
- Elegí `es`
- Reiniciá VS Code

### 2. Instalar extensiones básicas

Entrá al ícono de **Extensions** (🧩) y buscá:

- ✅ **Spanish Language Pack**
- ✅ **Python** (si usás Python)
- ✅ **ESLint / Prettier** (para JS)
- ✅ **GitLens** (Git)

---

# 6️⃣ Atajos útiles (universales)

- **Abrir carpeta:** `Ctrl + K` → `Ctrl + O`
- **Terminal integrada:** `Ctrl + ñ` (Win/Linux) / ``Ctrl + ` `` (Mac)
- **Buscar archivos:** `Ctrl + P`
- **Paleta de comandos:** `Ctrl + Shift + P`

---

---

---

Perfecto 🙂
Te dejo una **configuración ideal para principiantes**, clara y sin sobrecarga, y después la **configuración específica para Python y JavaScript**. La idea es que VS Code te ayude, no que te complique.

---

# 🧩 Configuración ideal para principiantes (base)

## 1️⃣ Extensiones esenciales (pocas y buenas)

Instalá solo estas al principio:

### 🔹 Generales

- **Spanish Language Pack**
  Traduce la interfaz.
- **Material Icon Theme**
  Hace más visual las carpetas y archivos.
- **Error Lens**
  Muestra errores directamente en el código (muy didáctico).
- **GitLens**
  Para entender Git paso a paso.

👉 Buscalas en la pestaña **Extensiones (🧩)** y clic en _Install_.

---

## 2️⃣ Ajustes recomendados (sin tocar demasiado)

Abrí:

```
Archivo → Preferencias → Configuración
```

Buscá y ajustá:

- **Font Size**: `14`
- **Tab Size**: `2`
- **Word Wrap**: `on`
- **Minimap**: `off` (menos distracción)
- **Render Whitespace**: `boundary`
- **Format On Save**: ✅ activado

> Esto hace el código más legible y evita errores comunes de formato.

---

## 3️⃣ Terminal integrada (muy importante)

Usá siempre la terminal de VS Code:

- Abrir terminal:
  **Ctrl + ñ** (Windows/Linux)
  **Ctrl + `** (Mac)

Así ves todo en un solo lugar: código + ejecución.

---

# 🐍 Configurar VS Code para **Python**

## 1️⃣ Instalar Python (si no lo hiciste)

- Windows / macOS: [https://www.python.org](https://www.python.org)
- Linux:

```bash
sudo apt install python3 python3-pip
```

Verificá:

```bash
python --version
```

---

## 2️⃣ Extensiones para Python

Instalá estas:

- **Python (Microsoft)** ⭐ obligatoria
- **Pylance** (suele instalarse sola)
- **Python Debugger**

Nada más por ahora.

---

## 3️⃣ Seleccionar intérprete de Python

1. Abrí un archivo `.py`
2. `Ctrl + Shift + P`
3. Escribí: **Python: Select Interpreter**
4. Elegí el que diga algo como:

   ```
   Python 3.x.x
   ```

Esto evita el 90% de problemas de principiantes.

---

## 4️⃣ Ejecutar Python

### Forma simple (recomendada)

- Botón ▶ arriba a la derecha
- O:

```bash
python archivo.py
```

### Debug (para aprender)

- Presioná **F5**
- Elegí: _Python File_

Podés ver variables paso a paso.

---

# 🌐 Configurar VS Code para **JavaScript**

## 1️⃣ Instalar Node.js

Descargá desde:
👉 [https://nodejs.org](https://nodejs.org)
Elegí **LTS**

Verificá:

```bash
node -v
npm -v
```

---

## 2️⃣ Extensiones para JavaScript

Instalá:

- **ESLint**
- **Prettier – Code formatter**
- **JavaScript (ES6) code snippets**

---

## 3️⃣ Configuración mínima para JS (recomendada)

En configuraciones buscá:

- **Default Formatter** → `Prettier`
- **Format On Save** → activado

Esto hace que el código se ordene solo al guardar.

---

## 4️⃣ Ejecutar JavaScript

### En consola (Node)

```bash
node archivo.js
```

### En navegador

- Botón derecho sobre `.html`
- **Open with Live Server**
  (Extensión opcional si hacés frontend)

---

# Flujo ideal para aprender (muy importante)

### Para Python:

1. Crear carpeta del proyecto
2. Abrir carpeta con VS Code
3. Crear `main.py`
4. Escribir → guardar → ejecutar
5. Leer errores con calma

### Para JavaScript:

1. Crear carpeta
2. `index.js`
3. Ejecutar con Node
4. Luego pasar a HTML + JS

---

# ❌ Errores comunes a evitar

- Instalar **demasiadas extensiones**
- No seleccionar el intérprete de Python
- Ejecutar código fuera de la carpeta del proyecto
- Ignorar los mensajes de error

---

---

---

Perfecto, es una muy buena pregunta 🙂
Los **`.ipynb` (Jupyter Notebooks)** en VS Code se pueden usar de forma muy cómoda si instalás **las extensiones correctas y solo las necesarias**.

---

# 📓 Extensiones para usar archivos **.ipynb** en VS Code

## 1️⃣ Extensiones obligatorias (con estas ya funciona)

Instalá estas **sí o sí**:

### ✅ **Python (Microsoft)**

- Es la base de todo.
- Permite ejecutar código, detectar entornos y kernels.

### ✅ **Jupyter (Microsoft)**

- Habilita abrir, editar y ejecutar archivos `.ipynb`.
- Soporta celdas, gráficos, Markdown y resultados interactivos.

👉 Normalmente, al instalar **Python**, VS Code te sugiere instalar **Jupyter** automáticamente.

---

## 2️⃣ Extensiones recomendadas (pero no obligatorias)

Estas mejoran mucho la experiencia, sobre todo para aprender:

### ⭐ **Pylance**

- Autocompletado claro
- Mejor detección de errores
- Muy útil en notebooks

### ⭐ **Jupyter Keymap**

- Atajos similares a Jupyter Notebook clásico
- Ideal si venís de Google Colab o Jupyter Lab

### ⭐ **Error Lens**

- Muestra errores directamente debajo del código
- Ayuda a entender qué pasó sin perderse

---

## 3️⃣ Qué NO necesitás instalar

❌ Extensiones viejas o alternativas a Jupyter
❌ Paquetes raros para “notebooks avanzados”
❌ Extensiones duplicadas

Menos es más, sobre todo al empezar.

---

# ⚙️ Configuración mínima recomendada para `.ipynb`

Abrí **Configuración** y revisá:

- **Jupyter: Ask For Kernel Restart** → `true`
- **Jupyter: Enable Extended Kernel Completion** → `true`
- **Notebook: Line Numbers** → `on`
- **Notebook: Output Text Line Limit** → `500`

Esto mejora legibilidad y evita notebooks pesados.

---

# 🧠 Kernel de Python (clave para que funcione bien)

Cuando abrís un `.ipynb`, arriba a la derecha vas a ver algo como:

```
Select Kernel
```

Elegí:

```
Python 3.x (recomendado)
```

Si no aparece:

```bash
pip install ipykernel
```

---

# ▶️ Cómo usar un `.ipynb` en VS Code

### Ejecutar una celda

- ▶ botón al lado de la celda
- `Shift + Enter`

### Agregar celda

- `+ Code`
- `+ Markdown`

### Reiniciar kernel

- Menú superior → **Restart**

---

# 📌 Diferencia VS Code vs Jupyter clásico (rápido)

| VS Code               | Jupyter Notebook |
| --------------------- | ---------------- |
| Todo en un solo lugar | Entorno separado |
| Mejor autocompletado  | Más simple       |
| Ideal para proyectos  | Ideal para demos |

Para aprender y trabajar, **VS Code es excelente**.

---

# 💡 Recomendación final (modo principiante)

✔ Usá `.ipynb` para:

- Aprender Python
- Matemática
- Pruebas rápidas
- Visualizaciones

✔ Usá `.py` para:

- Scripts reales
- Proyectos
- Apps

---
