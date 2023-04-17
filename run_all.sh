#!/bin/bash

urls=(
  'https://www.youtube.com/watch?v=AUU9RlDrSo0&ab_channel=ElM%C3%A9todoRebord'
  'https://www.youtube.com/watch?v=AxUDKVxNOHs&ab_channel=ElM%C3%A9todoRebord'
  'https://www.youtube.com/watch?v=Wevw4zbhScM&ab_channel=ElM%C3%A9todoRebord'
  'https://www.youtube.com/watch?v=FMO13F3Btd0&ab_channel=ElM%C3%A9todoRebord'
  'https://www.youtube.com/watch?v=cUxQQU45cQ4&ab_channel=ElM%C3%A9todoRebord'
)

hf_token="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"

for url in "${urls[@]}"; do
  python run_pipeline.py "$url" --hf-token "$hf_token"
done