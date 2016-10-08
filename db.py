import json
import sqlite3

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

# database thing

    conn = sqlite3.connect('sitcoms.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE episodes
        (id INT PRIMARY KEY     NOT NULL,
        title           TEXT    NOT NULL,
        season_index            INT     NOT NULL,
        episode_index            INT     NOT NULL);''')

    for episode in episodes:
        c.execute("INSERT INTO episodes (title, season_index, episode_index) VALUES ?", (episode.title, episode.season, episode.index))

    conn.commit()

# pprint(episodes)