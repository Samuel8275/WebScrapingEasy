import requests
from bs4 import BeautifulSoup
import os
import re

# URL de la página web a la que deseas hacer scraping
url = 'https://www.ejemplo.com'

# Realiza una solicitud HTTP a la página
response = requests.get(url)

# Analiza el contenido HTML de la página
soup = BeautifulSoup(response.text, 'html.parser')

# Encuentra todos los elementos de imagen en la página
img_tags = soup.find_all('img')

# Carpeta de destino para las imágenes descargadas
carpeta_destino = 'ruta/de/destino/imagenes'
os.makedirs(carpeta_destino, exist_ok=True)

# Configura el límite de imágenes a descargar a la vez
limite_descargas = 200
descargas_realizadas = 0

# Patrón regular para verificar si la URL termina en .jpg o .png
patron_extension = re.compile(r'\.(jpg|png)$')

# Itera a través de los elementos de imagen y obtén las URL
for img in img_tags:
    if descargas_realizadas >= limite_descargas:
        break  # Detener si alcanzamos el límite de descargas

    img_url = img.get('src')
    if img_url and patron_extension.search(img_url):
        # Construir la ruta completa de destino para la imagen
        nombre_archivo = os.path.join(carpeta_destino, img_url.split('/')[-1])

        # Descargar la imagen y guardarla en la carpeta de destino
        with open(nombre_archivo, 'wb') as img_file:
            img_data = requests.get(img_url).content
            img_file.write(img_data)

        print(f'Imagen descargada: {nombre_archivo}')

        descargas_realizadas += 1
