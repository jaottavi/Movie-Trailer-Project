# Import webbrowser to allow opening of movie trailers and images
import webbrowser

class Movie():
    """This class stores information related to movies.
    Instance Arguments:
        movie_title - The title of the instance of the movie.
        movie_storyline = The storyline of the instance of the movie.
        mposter_image = The URl to the image of the movie poster.
        trailer_youtube = The URl to the youtube trailer of the movie."""

    def __init__(self, movie_title, movie_storyline, poster_image,
    trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
