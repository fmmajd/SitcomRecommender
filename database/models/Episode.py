from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from database.models.Base import Base
from database.models.TVShow import TVShow

class Episode(Base):

    __tablename__ = 'episodes'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    index = Column(Integer)
    season = Column(Integer)
    is_seen = Column(Boolean)
    show_id = Column(Integer, ForeignKey('shows.id'))
    show = relationship(TVShow)


    def __init__(self, season, index, title, show):
        self.season = season
        self.index = index
        self.title = title
        self.is_seen = False
        self.show = show