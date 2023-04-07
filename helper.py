import subprocess
import json
import re
import yt_dlp

def convert_youtube_title(url):
    try:
        import yt_dlp
    except ImportError:
        import subprocess
        subprocess.run(['pip', 'install', 'yt-dlp'])

    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    input_title = ydl.sanitize_info(info)["title"]

    # Extract the episode number using a regex pattern
    episode_number = re.search(r'#(\d+)', input_title)
    if episode_number:
        episode_number = episode_number.group(1).zfill(3)
    else:
        raise ValueError("Episode number not found in the input string")

    # Remove any non-alphanumeric characters and split the words into a list
    words = re.findall(r'\b\w+\b', input_title)

    # Find the index of the hyphen (-) separator
    separator_index = input_title.find('-')

    if separator_index == -1:
        raise ValueError("Separator (-) not found in the input string")

    # Extract the names after the separator and remove any leading/trailing whitespace
    names = input_title[separator_index+1:].strip()

    # Combine the episode number and names into the desired format
    output_title = f"episode_{episode_number}_{names.replace(' ', '_')}".lower()

    return output_title
