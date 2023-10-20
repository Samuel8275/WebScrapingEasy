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

# Carpeta de destino para los videos descargados
carpeta_destino = 'ruta/de/destino/videos'
os.makedirs(carpeta_destino, exist_ok=True)

# Configura el límite de videos a descargar
limite_descargas = 3
descargas_realizadas = 0

# Patrón regular para verificar si la URL es un enlace a un video
patron_extension = re.compile(r'\.(mp4|webm|avi|mov|mkv|flv)$')

# Encuentra todos los enlaces en la página
enlaces = soup.find_all('a')

# Itera a través de los enlaces y descarga los videos
for enlace in enlaces:
    if descargas_realizadas >= limite_descargas:
        break  # Detener si alcanzamos el límite de descargas

    href = enlace.get('href')
    if href and patron_extension.search(href):
        # Construir la ruta completa de destino para el video
        nombre_archivo = os.path.join(carpeta_destino, href.split('=')[-1] + '.mp4')  # Puedes ajustar la extensión según la página

        # Descargar el video y guardarlo en la carpeta de destino
        with open(nombre_archivo, 'wb') as video_file:
            video_data = requests.get(href).content
            video_file.write(video_data)

        print(f'Video descargado: {nombre_archivo}')

        descargas_realizadas += 1
