import json
import random

from pprint import pprint

from models import Episode

with open('Friends.json') as data_file:
    data = json.load(data_file)

episodes = []

for season in data['seasons']:
    season_index = season['index']
    for episode in season['episodes']:
        ep = Episode(season_index, episode['index'], episode['title'])
        episodes.append(ep)

total = len(episodes)

done = False

while(not done):
    rand = random.randrange(0, total)
    ep = episodes[rand]
    out = "The Lucy Episode IS: season" + str(ep.season) + " episode" + str(ep.index) + ": " + ep.title + "." + '\n' + "Do you want a new suggestion?(y/n)"
    print(out)
    answer = input()
    if(answer == 'y'):
        done = False
    elif(answer == 'n'):
        done = True
