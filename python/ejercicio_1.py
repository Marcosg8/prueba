import sys
import os # Importamos 'os' para usar 'os.path.exists'

# 1. Intentar obtener el nombre/ruta del archivo desde la consola
if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    # 2. Si no se da ningún argumento, pedir la ruta al usuario
    name = input("Por favor, introduce la ruta completa del archivo que deseas leer: ")

# 3. Validar si la ruta existe antes de intentar abrir
if not os.path.exists(name):
    print(f"\nError: El archivo o ruta '{name}' no existe.")
    sys.exit(1)

# 4. Abrir y leer el archivo (código original)
try:
    with open(name, 'r', encoding="utf-8") as file:
        print(f"\n--- Contenido de {name} ---\n")
        for line in file:
            print(line, end='')
        print(f"\n\n--- Fin del contenido ---\n")
        
except Exception as e:
    # Capturar errores como permisos o codificación incorrecta
    print(f"\nHa ocurrido un error al intentar leer el archivo: {e}")