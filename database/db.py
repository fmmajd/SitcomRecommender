from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.models.TVShow import TVShow
from database.models.Base import Base
from database.models.Episode import Episode


engine = create_engine('sqlite:///database.db')

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
DBSession = sessionmaker(bind = engine)

session = DBSession()

def addShow(show):
    #new_show = TVShow(show.title)
    session.add(show)
    session.commit()

def addEpisode(episode):
    #new_ep = Episode(episode.season, episode.index, episode.title,episode.show)
    session.add(episode)
    session.commit()

def allEpisodes(show):
    return session.query(Episode).filter({Episode.show_id == show.id}).all()

def unseenEpisodes(show):
    return session.query(Episode).filter(Episode.show_id == show.id).filter(Episode.is_seen == False).all()

def makeEpisodeSeen(episode):
    session.query(Episode).filter(Episode.id == episode.id).update({"is_seen": True})
    session.commit()

def makeEpisodeUnseen(episode):
    session.query(Episode).filter(Episode.id == episode.id).update({"is_seen": False})
    session.commit()

def resetEpisodes(show):
    # should not use makeEpisodeUnseen, because it would query each iteration
    session.query(Episode).filter(Episode.show == show).update({"is_seen": False})
    session.commit()

def getShow(show_name):
    return session.query(TVShow).filter(TVShow.title == show_name).first()