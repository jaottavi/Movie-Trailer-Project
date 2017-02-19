# Use contents of movie.py file and fresh_tomatoes.py to build website and
# classes.
import movie
import fresh_tomatoes

# Create movie instances for future use by fresh_tomatoes
Logan = movie.Movie("Logan",
    "Story about Wolverine's final journey, and the beginning of a new story.",
    "http://www.heyuguys.com/images/2016/10/Logan-Poster-Wolverine-3.jpg",
    "https://www.youtube.com/watch?v=VHilK6b0Trs")

GoG2 = movie.Movie("Guardians of the Galaxy II",
    """The Guardian's tackle another challenge to save the universe,
     with baby Groot""",
    "http://cdn2-www.comingsoon.net/assets/uploads/gallery/guardians-of-the-galaxy-2-1406427000/guardian2poster.jpg", # NOQA
    "https://www.youtube.com/watch?v=2cv2ueYnKjg")

Imitation_Game = movie.Movie("Imitation Game",
    "A story of Alan Turing and colleagues to crack the Enigma machine.",
    "http://cdn5.thr.com/sites/default/files/2014/09/the_imitation_game_a_p.jpg", # NOQA
    "https://www.youtube.com/watch?v=S5CjKEFb-sM")

Ironman = movie.Movie("Ironman",
    """Tony Stark, technological genius and irresponsible playboy,
    trying to save the world.""",
    "http://cdn.collider.com/wp-content/uploads/2015/04/iron-man-1-poster.jpg",
    "https://www.youtube.com/watch?v=8hYlB38asDY")
Hidden_Figures = movie.Movie("Hidden Figures",
    """The story of the brilliant African-American
    women that helped launch America into space.""",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQxOTkxODUyN15BMl5BanBnXkFtZTgwNTU3NTM3OTE@._V1_UY1200_CR90,0,630,1200_AL_.jpg", # NOQA
    "https://www.youtube.com/watch?v=RK8xHq6dfAo")

# List of movies for fresh_tomatoes to act on
movies = [Logan, GoG2, Imitation_Game, Hidden_Figures, Ironman]

# Open the webpage to show the created website
fresh_tomatoes.open_movies_page(movies)
