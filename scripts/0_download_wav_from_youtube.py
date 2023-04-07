import argparse
import yt_dlp
import json
import re
import os

def get_youtube_title(URL):
    """
    Get the title of a YouTube video.
    Args:
        URL (str): The URL of the YouTube video.
    Returns:
        str: The title of the YouTube video.
    """
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(URL, download=False)

    return ydl.sanitize_info(info)["title"]

def convert_title(title):
    """
    Convert a title to a standardized format.
    Args:
        title (str): The title to be converted.
    Returns:
        str: The converted title in the format "episode_{episode_number}_{names}".
    Raises:
        ValueError: If the episode number or separator (-) is not found in the input string.
    """
    # Extract the episode number using a regex pattern
    episode_number = re.search(r'#(\d+)', title)
    if episode_number:
        episode_number = episode_number.group(1).zfill(3)
    else:
        raise ValueError("Episode number not found in the input string")

    # Remove any non-alphanumeric characters and split the words into a list
    words = re.findall(r'\b\w+\b', title)

    # Find the index of the hyphen (-) separator
    separator_index = title.find('-')

    if separator_index == -1:
        raise ValueError("Separator (-) not found in the input string")

    # Extract the names after the separator and remove any leading/trailing whitespace
    names = title[separator_index+1:].strip()

    # Combine the episode number and names into the desired format
    return f"episode_{episode_number}_{names.replace(' ', '_')}".lower() # output: episode_048_alejandro_dolina

def download_audio(URL, output_dir, audio_filename):
    """
    Download the audio from a YouTube video as a WAV file.
    Args:
        URL (str): The URL of the YouTube video.
        output_dir (str): The directory to save the output file in.
        audio_filename (str): The filename to save the output file as.
    """
    output_path = os.path.join(output_dir, audio_filename)
    ydl_opts = {
        'outtmpl': output_path,
        'format': 'm4a/bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(URL)


def main():
    """
    Parse command-line arguments and download the audio from a YouTube video as a WAV file.
    """
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Download audio as wav from a YouTube video')

    # Add the URL argument
    parser.add_argument('url', metavar='url', type=str, help='the URL of the YouTube video')

    # Add the output directory argument
    parser.add_argument('-d', '--output-dir', metavar='output_dir', type=str,
                        help='the directory to save the output file in', default='.')
    
    # Add the output filename argument
    parser.add_argument('-f', '--audio-filename', metavar='audio_filename', type=str,
                        help='the filename to save the output file as', default=None)

    # Parse the arguments
    args = parser.parse_args()
    
    # Get the URL and output directory
    URL = args.url
    output_dir = args.output_dir
    audio_filename = args.audio_filename
    
    if audio_filename is None:
        # If no output filename is specified, use the title of the YouTube video as the filename
        with yt_dlp.YoutubeDL({}) as ydl:
            info = ydl.extract_info(URL, download=False)
            input_title = ydl.sanitize_info(info)["title"]
            audio_filename = convert_title(input_title)

    # Download the audio as a WAV file
    download_audio(URL, output_dir, audio_filename)

if __name__ == '__main__':
    main()
