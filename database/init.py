import json

from sqlalchemy import create_engine

from database.db import addEpisode, addShow

from database.models.TVShow import TVShow
from database.models.Episode import Episode
from database.models.Base import Base



#
# handle db
#

engine = create_engine('sqlite:///database.db')

Base.metadata.create_all(engine)

#
# FUNCTIONS
#


def buildEpisodesList(data):
    episodes = []

    # define the show object
    title = data['title']
    tv_show = TVShow(title)

    # define the episode objects
    for season in data['seasons']:
        season_index = season['index']
        for episode in season['episodes']:
            ep = Episode(season_index, episode['index'], episode['title'], tv_show)
            episodes.append(ep)

    return episodes


def initShow(name):
    name = 'shows/' + name + '.json'
    #
    # get episodes
    #
    with open(name) as data_file:
        data = json.load(data_file)

    episodes = buildEpisodesList(data)

    # should not explicitly add the show
    # it's added to db automatically when first adding an episode
    # addShow(show)

    for episode in episodes:
        addEpisode(episode)
