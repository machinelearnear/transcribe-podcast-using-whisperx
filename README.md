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

- `Python >3.7`
- `WhisperX`
- `ffmpeg`
- `yt-dlp`

Una vez que tengas todo instalado, podés clonar este repositorio y luego instalar los paquetes necesarios con pip:

```sh
$ git clone https://github.com/machinelearnear/transcribe-podcast-using-whisperx.git
$ pip install -r requirements.txt
```

## Ejecutar el pipeline de transcripción

You can create a shell script (e.g., `run_all.sh`) that calls your Python script for each URL in the list. Here's an example of how to create a shell script for your list of URLs:

```bash
#!/bin/bash

urls=(
  'https://www.youtube.com/watch?v=AUU9RlDrSo0&t=12s&ab_channel=ElM%C3%A9todoRebord'
  'https://www.youtube.com/watch?v=KKH08BnAUBY&ab_channel=ElM%C3%A9todoRebord'
  'https://www.youtube.com/watch?v=Wevw4zbhScM&t=2s&ab_channel=ElM%C3%A9todoRebord'
  'https://www.youtube.com/watch?v=FMO13F3Btd0&t=2s&ab_channel=ElM%C3%A9todoRebord'
  'https://www.youtube.com/watch?v=cUxQQU45cQ4&ab_channel=ElM%C3%A9todoRebord'
)

hf_token="YOUR_HF_TOKEN"

for url in "${urls[@]}"; do
  python transcribe_video_and_parse_output.py "$url" --hf-token "$hf_token"
done
```

This script creates an array of URLs, loops through them, and calls your Python script (run_pipeline.py) for each URL.

Make sure to replace `YOUR_HF_TOKEN` with your actual Hugging Face token.

To run the shell script, follow these steps:

- Save the script in a file called `run_all.sh` in the same directory as your Python script (`run_pipeline.py`).
- Open a terminal and navigate to the directory containing the shell script.
- Make the script executable by running `chmod +x run_all.sh`.
- Run the script by executing `./run_all.sh`.

This will process each URL one by one using your Python script.

## Referencias

-   [WhisperX en Github](https://github.com/m-bain/whisperX)
-   [Speaker Diarization](https://en.wikipedia.org/wiki/Speaker_diarization)

## Otras consideraciones

-   Este pipeline actualmente solo se ha probado con podcasts en inglés y puede que no funcione con podcasts en otros idiomas.