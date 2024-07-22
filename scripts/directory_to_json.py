#!/usr/bin/python3

import os
import re
import json

files = ["README.md", "Directory2.md", "Directory3.md", "Directory4.md", "Directory5.md"]
communities = {}

path = './lists/'
os.makedirs(path, exist_ok=True)

for file in files:
  with open(file, 'r') as text_file:
    for index, line in enumerate(text_file):
      match = re.search("^# [0-9]+. (.*)\s+\(", line)
      if match is not None:
        print(match.group(1))
        current_section = match.group(1)
        communities[current_section] = {}
        # reset the subsections
        current_subsection = "None"
        current_subsubsection = "None"
        communities[current_section][current_subsection] = {}
        communities[current_section][current_subsection][current_subsubsection] = []
      match = re.search("^## ([0-9]+\.)+ (.*)\s+\(", line)
      if match is None:
        # try without the (xx communities)
        match = re.search("^## ([0-9]+\.)+ (.*)", line)
      if match is not None:
        print(f'  {match.group(2)}')
        current_subsection = match.group(2)
        current_subsubsection = "None"
        communities[current_section][current_subsection] = {}
        communities[current_section][current_subsection][current_subsubsection] = []
      match = re.search("^### ([0-9]+\.)+ (.*)\s+\(", line)
      if match is None:
        # try without the (xx communities)
        match = re.search("^### ([0-9]+\.)+ (.*)", line)
      if match is not None:
        print(f'    {match.group(2)}')
        current_subsubsection = match.group(2)
        communities[current_section][current_subsection][current_subsubsection] = []

      match = re.search("^[0-9]+\. \*\*\[.*\]\(/c/(.*)\)\*\*", line)
      if match is not None:
        communities[current_section][current_subsection][current_subsubsection].append(match.group(1))
        print(f'      {match.group(1)}')


# Export FNIC to file
with open(f'{path}fnic.json', 'w') as json_file:
  json.dump(communities['Art']['Imaginary Network 💭']['None'], json_file, indent=2)

# Export General Artworks to file
with open(f'{path}generalart.json', 'w') as json_file:
  json.dump(communities['Art']['General Artworks 🎨']['None'], json_file, indent=2)

# Export Anime to file
with open(f'{path}anime.json', 'w') as json_file:
  json.dump(communities['Art']['Anime Artworks 💢']['None'], json_file, indent=2)

# Export Photography to file
with open(f'{path}photo.json', 'w') as json_file:
  json.dump(communities['Art']['Photography 📷']['None'], json_file, indent=2)

# Export Themes to file
with open(f'{path}themes.json', 'w') as json_file:
  json.dump(communities['Art']['Themes 🖼️']['None'], json_file, indent=2)

# Export Comics to file
with open(f'{path}comics.json', 'w') as json_file:
  json.dump(communities['Art']['Comics 🗯️']['None'], json_file, indent=2)

# Export AI to file
with open(f'{path}ai.json', 'w') as json_file:
  json.dump(communities['Art']['AI 🤖']['None'], json_file, indent=2)

# Export Wallpapers to file
with open(f'{path}wallpapers.json', 'w') as json_file:
  json.dump(communities['Art']['Wallpapers 🌇']['None'], json_file, indent=2)

# Export Animals to file
with open(f'{path}animals.json', 'w') as json_file:
  json.dump(communities['Animals 🐘']['None']['None'], json_file, indent=2)

# Export Music to file
with open(f'{path}music.json', 'w') as json_file:
  json.dump(communities['Art']['Music 🎵']['General discussion'], json_file, indent=2)
with open(f'{path}music-genres.json', 'w') as json_file:
  json.dump(communities['Art']['Music 🎵']['Genres'], json_file, indent=2)

# Export Gaming to file
with open(f'{path}gaming-platforms.json', 'w') as json_file:
  json.dump(communities['Gaming']['Platforms 🕹️']['None'], json_file, indent=2)
with open(f'{path}gaming-genres.json', 'w') as json_file:
  json.dump(communities['Gaming']['Genres']['None'], json_file, indent=2)
with open(f'{path}gaming-general.json', 'w') as json_file:
  json.dump(communities['Gaming']['General']['None'], json_file, indent=2)

# Export Memes to file
with open(f'{path}memes-general.json', 'w') as json_file:
  json.dump(communities['Memes/Humoristic 🎭']['General']['None'], json_file, indent=2)
with open(f'{path}memes-news.json', 'w') as json_file:
  json.dump(communities['Memes/Humoristic 🎭']['News format']['None'], json_file, indent=2)
with open(f'{path}memes-shows.json', 'w') as json_file:
  json.dump(communities['Memes/Humoristic 🎭']['Show ']['None'], json_file, indent=2)
with open(f'{path}memes-social.json', 'w') as json_file:
  json.dump(communities['Memes/Humoristic 🎭']['Social media']['None'], json_file, indent=2)

# Export a complete dump of the directory to a JSON file
with open(f'{path}directory.json', 'w') as json_file:
  json.dump(communities, json_file, indent=2)
