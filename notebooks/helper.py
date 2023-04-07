import os
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

def parse_transcript(file_path, guest_name, host_name="Tomas Rebord", save_to_disk=True):
    def read_srt_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            srt_content = file.read()
        return srt_content

    def parse_srt(input):
        entries = input.strip().split("\n\n")
        output_lines = []
        last_speaker = None
        
        for entry in entries:
            lines = entry.strip().split("\n")
            time_start = lines[1].split(" --> ")[0]
            speaker, text = re.match(r'\[(.+)\]:\s*(.+)', lines[2]).groups()
            
            if last_speaker and speaker != last_speaker:
                output_lines.append("")
            
            if output_lines and speaker == last_speaker:
                output_lines[-1] += " " + text
            else:
                output_lines.append(f"[{speaker}, {time_start}] {text}")
            
            last_speaker = speaker

        return "\n".join(output_lines)

    def convert_to_seconds(timestamp):
        hours, minutes, seconds_and_milliseconds = timestamp.split(':')
        seconds, milliseconds = seconds_and_milliseconds.split(',')
        return int(hours) * 3600 + int(minutes) * 60 + int(seconds)

    srt_string = read_srt_file(file_path)
    transcript = parse_srt(srt_string)
    pattern = r'\[(SPEAKER_\d{2}),\s(\d{2}:\d{2}:\d{2},\d{3})\]\s(.*?)\n\n'
    matches = re.findall(pattern, transcript, re.DOTALL)

    result = []
    for match in matches:
        speaker, timestamp, text = match
        speaker_name = host_name if speaker == "SPEAKER_00" else guest_name
        formatted_text = "{}: {}".format(speaker_name, text.replace('\n', ' '))
        result.append({
            "text": formatted_text,
            "start": convert_to_seconds(timestamp)
        })

    json_output = json.dumps(result, ensure_ascii=False)

    if save_to_disk:
        output_file_path = os.path.splitext(file_path)[0] + ".json"
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(json_output)

    return json_output