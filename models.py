from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine

Base = declarative_base()

class Episode(Base):

    __tablename__ = 'episodes'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    index = Column(Integer)
    season = Column(Integer)
    sitcome_id = Column(Integer, ForeignKey('sitcoms.id'))


    def __init__(self, season, index, title):
        self.season = season
        self.index = index
        self.title = title
        self.isSeen = False


class Sitcom(Base):

    __tablename__ = 'sitcoms'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)

    def __init__(self, title,seasonNum):
        self.title = title
        self.num_of_seasons = seasonNum
        self.__episodes = []

    def addEpisode(self, episode):
        self.__episodes.append(episode)


engine = create_engine('sqlite:///whattowatch.db')

Base.metadata.create_all(engine)