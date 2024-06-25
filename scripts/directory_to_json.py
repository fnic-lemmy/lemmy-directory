#!/usr/bin/python3

import re
import json

files = ["README.md", "Directory2.md", "Directory3.md", "Directory4.md", "Directory5.md"]
communities = {}

for file in files:
  with open(file, 'r') as text_file:
    for index, line in enumerate(text_file):
      match = re.search("^# [0-9]+. (.*) \(", line)
      if match is not None:
        print(match.group(1))
        current_section = match.group(1)
        communities[current_section] = {}
        # reset the subsections
        current_subsection = "None"
        current_subsubsection = "None"
        communities[current_section][current_subsection] = {}
        communities[current_section][current_subsection][current_subsubsection] = []
      match = re.search("^## ([0-9]+\.)+ (.*) \(", line)
      if match is not None:
        print(f'  {match.group(2)}')
        current_subsection = match.group(2)
        current_subsubsection = "None"
        communities[current_section][current_subsection] = {}
        communities[current_section][current_subsection][current_subsubsection] = []
      match = re.search("^### ([0-9]+\.)+ (.*) \(", line)
      if match is not None:
        print(f'    {match.group(2)}')
        current_subsubsection = match.group(2)
        communities[current_section][current_subsection][current_subsubsection] = []

      match = re.search("^[0-9]+\. \*\*\[.*\]\(/c/(.*)\)\*\*", line)
      if match is not None:
        communities[current_section][current_subsection][current_subsubsection].append(match.group(1))
        print(f'      {match.group(1)}')


# Export FNIC to file
with open('_fnic_comms.json', 'w') as json_file:
  json.dump(communities['Art']['Imaginary Network 💭']['None'], json_file, indent=2)

# Export General Artworks to file
with open('_generalart_comms.json', 'w') as json_file:
  json.dump(communities['Art']['General Artworks 🎨']['None'], json_file, indent=2)

# Export Anime to file
with open('_anime_comms.json', 'w') as json_file:
  json.dump(communities['Art']['Anime Artworks 💢']['None'], json_file, indent=2)

# Export Photography to file
with open('_photography_comms.json', 'w') as json_file:
  json.dump(communities['Art']['Photography 📷']['None'], json_file, indent=2)

# Export a complete dump of the directory to a JSON file
with open('__directory.json', 'w') as json_file:
  json.dump(communities, json_file, indent=2)
