# YouTube Video Downloader

Este repositorio contiene un script para descargar videos de YouTube con subtítulos automáticos utilizando yt-dlp. Los videos se descargan en formato `.mp4` y los subtitulos en formato `.vtt`.
Puedes especificar el idioma de los subtítulos y el archivo de texto que contiene las URLs de los videos a descargar.

## Instalación

Se usó esta pagina como guía de instalación https://www.rapidseedbox.com/es/blog/yt-dlp-complete-guide 

## Requisitos

Para ejecutar este script, necesitas **Python 3.12.3** o una versión compatible.

## Archivos Incluidos

- `descarga.py`: El script principal para ejecutar las descargas.
- `yt-dlp.exe`: El ejecutable necesario para descargar los videos. Debe estar ubicado en el mismo directorio que el script.
- `prueba.txt`: Archivo de ejemplo con URLs para descargar.
- `español.txt`: Archivo de URLs con videos en español.
- `frances.txt`: Archivo de URLs con videos en francés.

## Uso del Script

1. Asegúrate de que `yt-dlp` esté instalado en el mismo directorio que el script `descarga.py`.
2. Ejecuta el script desde la terminal especificando el idioma de los subtítulos y el archivo con URLs. Ejemplo:

Para descargar videos con subtítulos en francés usando el archivo `frances.txt`:
python descarga.py fr frances.txt