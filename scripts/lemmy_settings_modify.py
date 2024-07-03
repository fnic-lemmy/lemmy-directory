#!/usr/bin/python3
import json

lfile='./lemmy_export.json'

blks='./blocks.json'
flws='./follows.json'

wipe_flws = False
wipe_blks = False

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
