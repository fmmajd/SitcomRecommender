from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from database.models.Base import Base
from database.models.TVShow import TVShow

class Episode(Base):

    __tablename__ = 'episodes'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    alternate_title = Column(String(250), nullable=True)
    index = Column(Integer)
    season = Column(Integer)
    is_seen = Column(Boolean)
    show_id = Column(Integer, ForeignKey('shows.id'))
    show = relationship(TVShow)


    def __init__(self, season, index, title, show, other_title = None):
        self.season = season
        self.index = index
        self.title = title
        self.alternate_title = other_title
        self.is_seen = False
        self.show = show

    def __str__(self):
        res = self.show.title + "-season" + str(self.season) + " episode" + str(self.index) + ": " + self.title
        if(not self.alternate_title == None):
            res = res + ", also known as: " + self.alternate_title
        return res