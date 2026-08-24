# Configuración del Entorno Virtual

## Crear y configurar el entorno

1. Crear el entorno virtual:
   ```bash
   python -m venv .venv
   ```

2. Activar el entorno virtual:
    Windows:
     ```bash
     source venv/Scripts/activate
     ```
    macOS / Linux:
     ```bash
     source .venv/bin/activate
     ```

3. Congelar las dependencias:
   ```bash
   python -m pip freeze > requirements.txt
   ```

## Reproducir el entorno en otro equipo

1. Crear y activar un nuevo entorno virtual.
2. Instalar los paquetes requeridos:
   ```bash
   python -m pip install -r requirements.txt
   ```