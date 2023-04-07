import re
import json
import os
import argparse

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

def main():
    parser = argparse.ArgumentParser(description="Parse transcript from SRT file.")
    parser.add_argument("file_path", help="Path to the SRT file.")
    parser.add_argument("guest_name", help="Name of the guest speaker.", default=None)
    parser.add_argument("--host_name", default="Tomas Rebord", help="Name of the host speaker (default: Tomas Rebord).")
    args = parser.parse_args()
    
    if args.guest_name is None:
        args.guest_name = " ".join(args.file_path.split('/')[1].split("_")[2:]).title()
    parsed_json = parse_transcript(args.file_path, args.guest_name, args.host_name)
    print(parsed_json)

if __name__ == "__main__":
    main()
