import requests
from bs4 import BeautifulSoup
import os

# URL de la página web a la que deseas hacer scraping
url = 'https://www.ejemplo.com'

# Realiza una solicitud HTTP a la página
response = requests.get(url)

# Analiza el contenido HTML de la página
soup = BeautifulSoup(response.text, 'html.parser')

# Encuentra todos los elementos de video en la página
video_tags = soup.find_all('video')

# Carpeta de destino para los videos descargados
carpeta_destino = 'ruta/de/destino/videos'
os.makedirs(carpeta_destino, exist_ok=True)

# Configura el límite de videos a descargar a la vez
limite_descargas = 5
descargas_realizadas = 0

# Itera a través de los elementos de video y obtén las URL
for video in video_tags:
    if descargas_realizadas >= limite_descargas:
        break  # Detener si alcanzamos el límite de descargas

    video_url = video.get('src')
    if video_url:
        # Construir la ruta completa de destino para el video
        nombre_archivo = os.path.join(carpeta_destino, video_url.split('/')[-1])

        # Descargar el video y guardarla en la carpeta de destino
        with open(nombre_archivo, 'wb') as video_file:
            video_data = requests.get(video_url).content
            video_file.write(video_data)

        print(f'Video descargado: {nombre_archivo}')

        descargas_realizadas += 1
