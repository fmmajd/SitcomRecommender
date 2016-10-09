from sqlalchemy import Column, ForeignKey, Integer, String, Boolean

from database.models.Base import Base

class TVShow(Base):

    __tablename__ = 'shows'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)

    def __init__(self, title):
        self.title = title