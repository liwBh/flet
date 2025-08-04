# Template
Aplicación tipo Template construida con [Flet](https://flet.dev/), 
es una plantilla para crear una aplicación con Flet.

---
## 📋 Tabla de Contenidos

1. [Características](#-características)
2. [Requisitos](#-requisitos)
3. [Instalación](#-instalación)
4. [Uso](#-uso)
5. [Estructura del Proyecto](#-estructura-del-proyecto)
6. [Enlaces Útiles](#-enlaces-útiles)


---
## 🚀 Características

- En enrutamiento de vistas.
- Arquitectura modular y extensible.
- Interfaz moderna y responsiva con Flet.

---
## 🛠️ Requisitos
* Python 3.11+
* pip

---
## ⚙️ Instalación
1. Clona este repositorio:

   ```bash
      git clone [https://github.com/liwBh/flet.git](https://github.com/liwBh/flet.git)
      cd template
   ```

2. Crea y activa un entorno virtual:

   ```bash
      python3 -m venv .venv
      source .venv/bin/activate
   ```

3. Instala las dependencias:

   ```bash
      pip install -r requirements.txt
   ```

## 📦 Uso

Ejecuta la aplicación Flet:

```bash
   flet run main.py
```

Esto levantará una ventana con la app donde podrás:
- Iniciar el proyecto
- Crear la vista

---
## 📂 Estructura del Proyecto
trello/
├── .venv/                   # Entorno virtual
├── src/                    # Código fuente principal
│   ├── assets/             # Archivos estáticos
│   │   └── image/          # Imágenes usadas en la app
│   ├── components/         # Componentes reutilizables
│   │   ├── layout/         # Layout general y diseño
│   │   └── share/          # Componentes compartidos
│   ├── controls/           # Lógica de control y validaciones
│   │   ├── objects/        # Objetos principales o entidades
│   │   └── validators/     # Validaciones personalizadas
│   ├── data/               # Manejo de datos
│   │   ├── models/         # Modelos y esquemas de datos
│   │   ├── memory_store.py # Almacenamiento en memoria
│   │   └── store.py        # Interfaz o lógica de almacenamiento
│   └── views/              # Vistas y lógica visual
│       └── main.py         # Punto de entrada de la app
├── .gitignore              # Archivos y carpetas ignoradas por git
├── Makefile                # Tareas automáticas
├── README.md               # Documentación del proyecto
├── requirements.txt        # Dependencias del proyecto


---
## 🔗 Enlaces Útiles
* **Flet (documentación)**: [https://flet.dev/docs/](https://flet.dev/docs/)
