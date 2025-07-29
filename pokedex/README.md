# POKEDEX en Flet

[Video tutorial]("https://youtu.be/nFJ3Ba7aOdg")

[Documentación de Flet]("https://flet.dev/docs/")

## Dependencias principales

```
pip install flet aiohttp asyncio
```

## Utilitarios

1. PokeAPI
[Enlace]("https://pokeapi.co/")
2. PokeAPI repositorio
[Enlace]("https://github.com/PokeAPI")
3. PokeAPI sprites
[Enlace]("https://github.com/PokeAPI/sprites/blob/4bcd17051efacd74966305ac87a0330b6131259a/sprites/pokemon/120.png")
4. Fuente zpix
[Enlace]("https://github.com/SolidZORO/zpix-pixel-font/releases")

## Crear un instalador

1. Dependiencias

```
pip install pyinstaller
```

2. Generar el instalador

[Documentación]("https://flet.dev/docs/publish")

```
flet pack ./main.py
```

```
flet pack ./main.py --name "Pokedex" --icon "./statics/image/icon.png"
```

```
flet create pokedex
```

### Tutoriales de Flet
[Documentación de tutoriales]("https://flet.dev/docs/tutorials/")

