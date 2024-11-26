from PIL import Image
import os
from pathlib import Path

def compress_image(input_path, output_path, max_size_mb=1):
    # Abrir la imagen
    with Image.open(input_path) as img:
        # Convertir a RGB si es necesario
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        
        # Calidad inicial
        quality = 95
        img.save(output_path, 'JPEG', quality=quality)
        
        # Reducir la calidad hasta que el archivo sea menor que max_size_mb
        while os.path.getsize(output_path) > max_size_mb * 1024 * 1024 and quality > 5:
            quality -= 5
            img.save(output_path, 'JPEG', quality=quality)

def main():
    # Obtener la ruta del script
    script_dir = Path(__file__).parent
    input_dir = script_dir / 'original'
    output_dir = script_dir / 'compressed'
    
    # Asegurarse de que los directorios existan
    input_dir.mkdir(exist_ok=True)
    output_dir.mkdir(exist_ok=True)
    
    # Extensiones de imagen soportadas
    valid_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.webp'}
    
    # Procesar cada imagen en el directorio de entrada
    for input_file in input_dir.iterdir():
        if input_file.suffix.lower() in valid_extensions:
            output_file = output_dir / f"compressed_{input_file.name}"
            print(f"Comprimiendo {input_file.name}...")
            try:
                compress_image(str(input_file), str(output_file))
                print(f"✓ Compresión exitosa: {input_file.name}")
            except Exception as e:
                print(f"✗ Error al comprimir {input_file.name}: {str(e)}")

if __name__ == "__main__":
    main()
    print("\n¡Proceso completado! Las imágenes comprimidas están en la carpeta 'compressed'.")
