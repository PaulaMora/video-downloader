import subprocess
import sys
import os

def download_videos(sub_lang, urls_file):
    # Verificar si el archivo existe
    if not os.path.exists(urls_file):
        print(f"Error: El archivo {urls_file} no existe.")
        return

    # Comando base de yt-dlp
    command = [
        "yt-dlp",
        "--merge-output-format", "mp4",
        "--write-subs",
        "--write-auto-subs",
        "--sub-langs", sub_lang,
        "-a", urls_file
    ]

    try:
        # Ejecutar el comando
        subprocess.run(command, check=True)
        print("Descarga completada.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar yt-dlp: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    # Verificar que se pasaron los argumentos necesarios
    if len(sys.argv) != 3:
        print("Uso: python script.py <idioma_subtitulos> <archivo_urls>")
        sys.exit(1)

    # Argumentos
    sub_lang = sys.argv[1]  # Idioma de los subtítulos (e.g., "fr")
    urls_file = sys.argv[2]  # Nombre del archivo con las URLs

    # Llamar a la función de descarga
    download_videos(sub_lang, urls_file)