class Tag:
    def __init__(self, user_id, movie_id, tag):
        self._user_id = user_id
        self._movie_id = movie_id
        self._tag = tag

    def __str__(self):
        return f'Movie {self._movie_id} has been tagged as {self._tag} by user {self._user_id}'