#!/usr/bin/python3
import json
import argparse
import sys
from github import Github
from github import Auth
from pythorhead import Lemmy

def get_args():
  parser = argparse.ArgumentParser(description="Check communities",
             formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("-d", "--directory", help="Directory JSON", default="./lists/directory.json")
  parser.add_argument("-t", "--token", help="GitHub auth token")
  parser.add_argument("-r", "--repo", help="GitHub repo", default="fnic-lemmy/lemmy-directory")
  parser.add_argument("-u", "--user", help="Lemmy user", default="directorybot")
  parser.add_argument("-p", "--pass", help="Lemmy password")
  parser.add_argument("-i", "--inst", help="Lemmy instance", default="lemmy.dbzer0.com")

  args = parser.parse_args()
  a = vars(args)

  return(a)

def raise_issue(ghtoken, ghrepo, title, desc):

  auth = Auth.Token(ghtoken)
  g = Github(auth=auth)
  repo = g.get_repo(ghrepo)
  my_issues = repo.get_issues(state = "open", creator = "fnic-bot")
  for issue in my_issues:
    if issue.title == title:
      print('already raised')
      issue.create_comment(f'This has failed again.\n\n{desc}')
      return

  i = repo.create_issue(title = title, body = desc, labels = [repo.get_label(name = "Community Removal")])


a = get_args()
dfile=a['directory']
ghtoken=a['token']
ghrepo=a['repo']
instance=a['inst']
user=a['user']
pw=a['pass']

lemmy = Lemmy(f'https://{instance}', raise_exceptions=True, request_timeout=30)
try:
  lemmy.log_in(user, pw)
except Exception as e:
  print(f'login failed: {e}\n')
  sys.exit(1)


with open(dfile) as f:
  comms = json.load(f)

for group in comms:
  print(group)
  for subgroup in comms[group]:
    print(f'  {subgroup}')
    for subsubgroup in comms[group][subgroup]:
      print(f'    {subsubgroup}')
      if len(comms[group][subgroup][subsubgroup]) > 0:
        for cm in comms[group][subgroup][subsubgroup]:
          print(f'      {cm}')
          cms = cm.split('@')
          if cms[1] in ['kbin.social', 'fedia.io']:
            c = 'm'
          else:
            c = 'c'
          url = f'https://{cms[1]}/{c}/{cms[0]}'
          try:
            s = lemmy.resolve_object(url)
          except Exception as e:
            desc = f'{group}-{subgroup}-{subsubgroup} [{cm}]\nURL lookup for {url} returned:\n```\n{e}\n```\n'
            print(f'        * {e}')
            try:
              raise_issue(ghtoken, ghrepo, f'Remove {cm}', desc)
            except Exception as e:
              print(f'        * unable to raise github issue. {e}')
