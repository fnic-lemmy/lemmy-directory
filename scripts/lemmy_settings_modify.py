#!/usr/bin/python3
import json
import argparse

def get_args():
  parser = argparse.ArgumentParser(description="Lemmy follows/blocks",
             formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("-i", "--input-file", help="Lemmy export file", default="lemmy_export.json")
  parser.add_argument("-o", "--output-file", help="Modified file to output", default="lemmy_modified.json")
  parser.add_argument("-f", "--follows-file", help="Follows list")
  parser.add_argument("-b", "--blocks-file", help="Blocks list")
  parser.add_argument("-F", "--wipe-follows", help="Wipes out follows before adding", action="store_true")
  parser.add_argument("-B", "--wipe-blocks", help="Wipes out blocks before adding", action="store_true")
  args = parser.parse_args()
  a = vars(args)

  return(a)


a = get_args()
lfile=a['input_file']
ofile=a['output_file']

blks=a['blocks_file']
flws=a['follows_file']

wipe_flws = False
if a['wipe_follows'] is True:
  wipe_flws = True

wipe_blks = False
if a['wipe_blocks'] is True:
  wipe_blks = True

with open(lfile) as l:
  settings = json.load(l)

print(settings['followed_communities'])
print(settings['blocked_communities'])

if wipe_flws is True:
  settings['followed_communities'] = []

if wipe_blks is True:
  settings['blocked_communities'] = []

with open(flws) as f:
  follows = json.load(f)

with open(blks) as b:
  blocks = json.load(b)

settings['followed_communities'].extend(follows)
settings['blocked_communities'].extend(blocks)

print('----------------')
print(settings['followed_communities'])
print(settings['blocked_communities'])

with open(ofile, 'w') as outfile:
  json.dump(settings, outfile)
