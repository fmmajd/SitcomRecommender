import database.init
import database.db

import sys

from database.init import initShow

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        name = 'Friends'
    else:
        name = sys.argv[1]
    initShow(name)