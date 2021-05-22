class Movie:

    def __init__(self, movie_id, title, genres):
        self._movie_id = movie_id
        self._title = title
        self._genres = genres

    def get_title(self):
        return self._title

    name = property(get_title)

    @staticmethod
    def load(location):
        with open(location, 'r', encoding='UTF-8') as movie_data:
            for lines in movie_data:
                m_id, title, genres = lines.split("::")
                yield Movie(m_id, title, genres.split("|"))

    @staticmethod
    def load_all(location):
        res = []
        with open(location, 'r', encoding='UTF-8') as movie_data:
            for lines in movie_data:
                m_id, title, genres = lines.split("::")
                res.append(Movie(m_id, title, genres.split("|")))
        return res

    def __str__(self):
        return f'{self._title} has id {self._movie_id} and the related genres are {self._genres}'