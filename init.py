#this imports SHOULD NOT be removed
import database.init
import database.db

import sys
import json

from database.init import initShow

if __name__ == '__main__':

    with open("shows/shows_list.json") as data_file:
        shows = json.load(data_file)

    print("\nchoose a show:")
    for i in range(0, len(shows)):
        print(str(i) + ": " + shows[i]['title'])

    print()#spacing line

    name = shows[int(input())]['file_name']

    print("name: " + name)

    initShow(name)