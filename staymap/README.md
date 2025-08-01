# Simulación de Autobuses en Mapa

Este proyecto permite crear, editar y simular la circulación de autobuses sobre rutas definidas en un mapa interactivo,
usando **Flet**, **flet-map** y **PostgreSQL**.

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

* Crear, mover y eliminar marcadores de paradas de autobús.
* Definir rutas asociando un conjunto ordenado de paradas.
* Registrar autobuses y asignarlos a rutas.
* Simulación visual automática del desplazamiento de los autobuses sobre el mapa.
* Persistencia de datos en **PostgreSQL**.

---

## 🛠️ Requisitos

* Python 3.11+
* PostgreSQL 12+
* pip

Dependencias Python (ver `requirements.txt`):

```text
flet
flet-map
sqlmodel
psycopg2-binary
```

---

## ⚙️ Instalación

1. Clona este repositorio:

   ```bash
      git clone [https://github.com/liwBh/flet.git](https://github.com/liwBh/flet.git)
      cd staymap
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

---

## 📦 Uso

Ejecuta la aplicación Flet:

```bash
   flet run main.py
```

Esto levantará una ventana con el mapa interactivo donde podrás:

* **Clic** en el mapa para crear nuevas paradas.
* **Arrastrar** marcadores para actualizar la posición de las paradas.
* Interfaz lateral para crear/editar rutas y registrar autobuses.
* Simulación automática de los autobuses moviéndose por las rutas.

---

## 📂 Estructura del Proyecto

```text
├── main.py           # Punto de entrada de la app Flet
├── models.py         # Definición de modelos SQLModel
├── config.py         # Configuración (DB_URL, etc.)
├── requirements.txt  # Dependencias Python
└── README.md         # Documentación del proyecto
```

---

## 🔗 Enlaces Útiles

* **Flet (documentación)**: [https://flet.dev/docs/](https://flet.dev/docs/)
* **flet-map (GitHub)**: [https://github.com/flet-dev/flet-map](https://github.com/flet-dev/flet-map)
* **SQLModel**: [https://sqlmodel.tiangolo.com/](https://sqlmodel.tiangolo.com/)
* **PostgreSQL (documentación)**: [https://www.postgresql.org/docs/](https://www.postgresql.org/docs/)
* **psycopg2**: [https://www.psycopg.org/docs/](https://www.psycopg.org/docs/)

---

> ¡Listo! Ahora tienes una guía básica para arrancar con la simulación de autobuses en mapa. Si necesitas más ejemplos o
> personalización, revisa la documentación enlazada o contáctame. :)
