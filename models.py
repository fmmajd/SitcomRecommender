class Episode:

    def __init__(self, season, index, title):
        self.season = season
        self.index = index
        self.title = title
        self.isSeen = False


class Sitcom:

    def __init__(self, title,seasonNum):
        self.title = title
        self.num_of_seasons = seasonNum
        self.__episodes = []

    def addEpisode(self, episode):
        self.__episodes.append(episode)