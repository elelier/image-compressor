# 📸 Image Compressor

Una herramienta simple pero poderosa para comprimir imágenes manteniendo una calidad óptima, perfecta para preparar imágenes para correo electrónico o web.

## ✨ Características

- Comprime imágenes a menos de 1MB manteniendo la mejor calidad posible
- Soporta múltiples formatos (JPG, PNG, BMP, WEBP)
- Interfaz simple y directa
- Preserva la calidad de imagen tanto como sea posible
- Proceso por lotes: comprime múltiples imágenes a la vez

## 🚀 Cómo usar

1. Clona este repositorio:
```bash
git clone https://github.com/elelier/image-compressor.git
cd image-compressor
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Coloca tus imágenes en la carpeta `original`

4. Ejecuta el script:
```bash
python compress_images.py
```

5. ¡Listo! Encontrarás tus imágenes comprimidas en la carpeta `compressed`

## 🛠️ Requisitos

- Python 3.6+
- Pillow (PIL)
