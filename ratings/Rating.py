class Rating:
    def __init__(self, user_id, movie_id, rating):
        self._user_id = user_id
        self._movie_id = movie_id
        self._rating = rating

    def __str__(self):
        return f'User {self._user_id} gave {self._rating} rating to the movie {self._movie_id}'