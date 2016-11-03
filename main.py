

#this import SHOULD NOT be removed
import database.db

import random
import json

from database.db import unseenEpisodes, makeEpisodeSeen, resetEpisodes, getShow



def checkForReset(episodes, show):
    total = len(episodes)
    if(total == 0):
        resetEpisodes(show)


with open("shows/shows_list.json") as data_file:
    shows = json.load(data_file)

print("which show?")
for i in range(0, len(shows)):
    print(str(i+1) + "- " + shows[i]['title'])

show_number = int(input()) - 1

show_title = shows[show_number]['title']

show = getShow(show_title)

episodes = unseenEpisodes(show)

# episodes = [episode[0] for episode in episodes]

checkForReset(episodes, show)

# for episode in episodes:
#     print(episode.is_seen)

done = False

while(not done):
    rand = random.randrange(0, len(episodes))
    ep = episodes[rand]
    out = "season" + str(ep.season) + " episode" + str(ep.index) + ": " + ep.title + "." + '\n' + "Have you seen it?(y/n)"
    print(str(ep) + '\n' + "Have you seen it? or you can pass it.(y/n/p)")
    answer = input()
    if(answer == 'y'):
        episodes.remove(ep)
        makeEpisodeSeen(ep)
        checkForReset(episodes, show)
        if(len(episodes) == 0):#if at this point all eps were watched
            episodes = unseenEpisodes(show)
        done = False
    elif(answer == 'n'):
        done = True
    elif(answer == 'p'):
        episodes.remove(ep)
        if(len(episodes == 0)):
            done = True
