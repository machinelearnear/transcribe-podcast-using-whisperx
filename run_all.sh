#!/bin/bash

urls=(
  'https://www.youtube.com/watch?v=AUU9RlDrSo0&t=12s&ab_channel=ElM%C3%A9todoRebord'
  'https://www.youtube.com/watch?v=KKH08BnAUBY&ab_channel=ElM%C3%A9todoRebord'
  'https://www.youtube.com/watch?v=Wevw4zbhScM&t=2s&ab_channel=ElM%C3%A9todoRebord'
  'https://www.youtube.com/watch?v=FMO13F3Btd0&t=2s&ab_channel=ElM%C3%A9todoRebord'
  'https://www.youtube.com/watch?v=cUxQQU45cQ4&ab_channel=ElM%C3%A9todoRebord'
)

hf_token="hf_YORfWLQIbTbAeNXwKfAewWxieQhhFPg"

for url in "${urls[@]}"; do
  python transcribe_video_and_parse_output.py "$url" --hf-token "$hf_token"
done