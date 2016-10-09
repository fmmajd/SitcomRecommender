

#this import SHOULD NOT be removed
import database.db

import random

from database.db import unseenEpisodes, makeEpisodeSeen, resetEpisodes



def checkForReset(episodes):
    total = len(episodes)
    if(total == 0):
        resetEpisodes()


episodes = unseenEpisodes()

# episodes = [episode[0] for episode in episodes]

checkForReset(episodes)

# for episode in episodes:
#     print(episode.is_seen)

done = False

while(not done):
    rand = random.randrange(0, len(episodes))
    ep = episodes[rand]
    out = "season" + str(ep.season) + " episode" + str(ep.index) + ": " + ep.title + "." + '\n' + "Have you seen it?(y/n)"
    print(out)
    answer = input()
    if(answer == 'y'):
        episodes.remove(ep)
        makeEpisodeSeen(ep)
        checkForReset(episodes)
        done = False
    elif(answer == 'n'):
        done = True
