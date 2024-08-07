import zipfile
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import io
import random

# Crear un archivo ZIP en memoria
zip_buffer = io.BytesIO()
with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
    for i in range(30):
        # Dimensiones aleatorias
        width = 420
        height = random.randint(240, 620)
        img = Image.new('L', (width, height), color=128)  # Imagen en escala de grises

        # Añadir texto con las dimensiones al centro de la imagen
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        text = f"{width}x{height}"
        textbbox = draw.textbbox((0, 0), text, font=font)
        textwidth, textheight = textbbox[2] - textbbox[0], textbbox[3] - textbbox[1]
        x = (width - textwidth) // 2
        y = (height - textheight) // 2
        draw.text((x, y), text, fill=255, font=font)
        
        # Guardar la imagen en un buffer
        img_buffer = io.BytesIO()
        img.save(img_buffer, format="PNG")
        prefix = '' #'image_'
        img_name = f"{prefix}{i+1}.png"
        zip_file.writestr(img_name, img_buffer.getvalue())

# Guardar el archivo ZIP en el directorio actual
zip_file_path = "small_images.zip"
with open(zip_file_path, "wb") as f:
    f.write(zip_buffer.getvalue())

print(f"Archivo ZIP creado: {zip_file_path}")
