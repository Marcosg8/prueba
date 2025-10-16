# Autor: Marcos Gómez Martín

# Importa el módulo 'sys', que provee acceso a parámetros y funciones específicas del sistema
import os
# Importa el módulo 'os', que permite interactuar con el sistema operativo
import sys
# Importa módulos necesarios para generar nombres aleatorios y crear imágenes PNG
import random
#importar string para generar nombres aleatorios
import string
# Importa la biblioteca Pillow para crear y manipular imágenes
from PIL import Image, ImageDraw

# Función para generar un nombre de archivo aleatorio
def generar_nombre_aleatorio(longitud=15):
    """Genera una cadena aleatoria de la longitud especificada."""
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(longitud))

# Función para crear una imagen PNG simple
def crear_png_aleatorio(ruta_archivo):
    """Crea una imagen PNG simple y la guarda en la ruta especificada."""
    # Tamaño de la imagen (ejemplo: 100x100 píxeles)
    ancho, alto = 100, 100
    
    # Crea una imagen con un fondo de color RGB aleatorio
    color_fondo = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    imagen = Image.new('RGB', (ancho, alto), color=color_fondo)
    
    # Opcional: añade un punto o forma para que no todas sean de color plano
    dibujo = ImageDraw.Draw(imagen)
    color_forma = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    radio = 10
    
    # Dibuja un círculo aleatorio en el centro
    centro_x, centro_y = ancho // 2, alto // 2
    dibujo.ellipse((centro_x - radio, centro_y - radio, 
                    centro_x + radio, centro_y + radio), 
                   fill=color_forma)
    
    # Guarda la imagen como PNG
    try:
        imagen.save(ruta_archivo, 'PNG')
    except Exception as e:
        print(f"Error al guardar el archivo {ruta_archivo}: {e}")

def main():
    # 1. Verificar argumentos
    if len(sys.argv) != 3:
        print("Ejemplo: python createpng.py Imagenes 20")
        sys.exit(1)

    nombre_carpeta = sys.argv[1]
    
    try:
        cantidad_archivos = int(sys.argv[2])
    except ValueError:
        print("Error: La cantidad de archivos debe ser un número entero.")
        sys.exit(1)

    if cantidad_archivos <= 0:
        print("Error: La cantidad de archivos debe ser mayor que cero.")
        sys.exit(1)

    # 2. Crear la carpeta
    try:
        os.makedirs(nombre_carpeta, exist_ok=True)
        print(f"Carpeta '{nombre_carpeta}' asegurada/creada.")
    except OSError as e:
        print(f"Error al crear la carpeta '{nombre_carpeta}': {e}")
        sys.exit(1)

    # 3. Generar archivos PNG
    print(f"Generando {cantidad_archivos} archivos PNG en '{nombre_carpeta}'...")
    
    for i in range(cantidad_archivos):
        # Generar nombre aleatorio de 15 caracteres con extensión .png
        nombre_base = generar_nombre_aleatorio(15)
        nombre_archivo = f"{nombre_base}.png"
        ruta_archivo = os.path.join(nombre_carpeta, nombre_archivo)
        
        # Crear y guardar el archivo PNG
        crear_png_aleatorio(ruta_archivo)
        
        # Opcional: Imprimir progreso
        if (i + 1) % 10 == 0 or (i + 1) == cantidad_archivos:
            print(f"  > Creado archivo {i + 1}/{cantidad_archivos}: {nombre_archivo}")

    print("Proceso completado con éxito.")

if __name__ == "__main__":
    main()