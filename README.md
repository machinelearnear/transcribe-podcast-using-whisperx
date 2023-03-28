# Transcribir podcast e identificar speakers usando WhisperX

## Descripción
Este proyecto tiene como objetivo transcribir podcasts usando el módulo WhisperX y luego identificar los hablantes con speaker diarization. Con este script, podrás transcribir rápidamente un podcast y saber quién está hablando.

## Índice

El proyecto incluye los siguientes archivos y directorios:

-   `notebooks/`: Un directorio que contiene notebooks de Jupyter para pruebas y desarrollo.
-   `scripts/`: Un directorio que contiene el código Python para el pipeline y la CLI.
-   `README.md`: Este documento, que proporciona una descripción general del proyecto e instrucciones de uso.
-   `requirements.txt`: Una lista de paquetes de Python necesarios para instalar.
-   `LICENSE`: La licencia del proyecto.

## Setear environment

Para usar este pipeline, necesitas tener lo siguiente instalado:

- Python 3.7 o superior
- `WhisperX`
- `ffmpeg`
- `yt-dlp`

Una vez que tengas todo instalado, podés clonar este repositorio y luego instalar los paquetes necesarios con pip:

```sh
$ git clone https://github.com/machinelearnear/transcribe-podcast-using-whisperx.git
$ pip install -r requirements.txt
```

## Ejecutar el pipeline de transcripción

Para ejecutar el pipeline, tenés que ejecutar `scripts/transcribe.py`. Este script tiene una CLI que te permite especificar la ubicación del archivo del podcast y otros parámetros. Acá te muestro un ejemplo de comando:

`$ python transcribe_youtube_video.py --hf_token <HF_token> --url <YouTube_URL> --num_speakers <num_speakers>`

Este comando transcribe el podcast que se encuentra en `ruta/al/podcast.mp3`, identifica los hablantes y guarda el resultado en `salida.txt`. También podés especificar otros parámetros, como la API key y el idioma del podcast.

## Referencias

-   [WhisperX en Github](https://github.com/m-bain/whisperX)
-   [Speaker Diarization](https://en.wikipedia.org/wiki/Speaker_diarization)

## Otras consideraciones

-   Este pipeline actualmente solo se ha probado con podcasts en inglés y puede que no funcione con podcasts en otros idiomas.