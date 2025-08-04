# Trello

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
Aplicación tipo Trello construida con [Flet](https://flet.dev/), diseñada para la creación, organización y gestión de tarjetas y tableros de tareas.

- Creación y edición de tarjetas.
- Organización en columnas/tableros.
- Almacenamiento en memoria o persistente.
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
      cd trello
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

Esto levantará una ventana con la app de trello donde podrás:

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
* **Flet trello (documentación)**: [https://flet.dev/docs/tutorials/trello-clone](https://flet.dev/docs/tutorials/trello-clone)
* **SQLModel**: [https://sqlmodel.tiangolo.com/](https://sqlmodel.tiangolo.com/)
