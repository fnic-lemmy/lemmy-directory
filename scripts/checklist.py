#!/usr/bin/python3

import re
import json

with open('./lists/directory.json', 'r') as json_file:
  sections = json.load(json_file)

for s in sections:
  print(f'- [ ] {s}')
  for ss in sections[s]:
    if ss != "None":
      print(f'   - [ ] {ss}')
      for sss in sections[s][ss]:
        if sss != "None":
          print(f'      - [ ] {sss}')
