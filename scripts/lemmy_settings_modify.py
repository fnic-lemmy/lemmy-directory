#!/usr/bin/python3
import json
import argparse

def get_args():
  parser = argparse.ArgumentParser(description="Lemmy follows/blocks",
             formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("-i", "--input-file", help="Lemmy export file", default="lemmy_export.json")
  parser.add_argument("-o", "--output-file", help="Modified file to output", default="lemmy_modified.json")
  parser.add_argument("-s", "--subs-file", help="Subs list")
  parser.add_argument("-b", "--blocks-file", help="Blocks list")
  parser.add_argument("-S", "--wipe-subs", help="Wipes out subscriptions before adding", action="store_true")
  parser.add_argument("-B", "--wipe-blocks", help="Wipes out blocks before adding", action="store_true")
  args = parser.parse_args()
  a = vars(args)

  return(a)

def open_convert_list(file):
  new = []
  with open(file) as f:
    comms = json.load(f)

  if len(comms) > 0:
    for cm in comms:
      cms = cm.split('@')
      if cms[1] in ['kbin.social', 'fedia.io']:
        c = 'm'
      else:
        c = 'c'
      new.append(f'https://{cms[1]}/{c}/{cms[0]}')
  return new

new_follows = []
new_blocks = []

a = get_args()
lfile=a['input_file']
ofile=a['output_file']

blks=a['blocks_file']
flws=a['subs_file']

wipe_flws = False
if a['wipe_subs'] is True:
  wipe_flws = True

wipe_blks = False
if a['wipe_blocks'] is True:
  wipe_blks = True

with open(lfile) as l:
  settings = json.load(l)

if wipe_flws is True:
  settings['followed_communities'] = []

if wipe_blks is True:
  settings['blocked_communities'] = []

if flws is not None:
  follows = open_convert_list(flws)
  settings['followed_communities'].extend(follows)

if blks is not None:
  blocks = open_convert_list(blks)
  settings['blocked_communities'].extend(blocks)

print(f'New subs: {settings["followed_communities"]}')
print(f'New blocks: {settings["blocked_communities"]}')

with open(ofile, 'w') as outfile:
  json.dump(settings, outfile)
