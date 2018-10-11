import webbrowser
import urllib
import json

class Movie():
        """This class offers a way to store movie info.

        Attributes:
        title (str): The title of the movie.
        year (str): Year the movie was released. 
        storyline (str): The plot of the movie.
        poster (str): URL to an image of the poster.
        trailer (str): URL to a youtube trailer of the movie.

        Method:
        show_trailer: opens the instance's trailer URL in a browser
        """
        def __init__(self,title,year,storyline,poster,trailer,rated,runtime):
		self.title = title
		self.year = year
		self.storyline = storyline
		self.poster_image_url = poster
		self.trailer_youtube_url = trailer
		self.rated = rated
		self.runtime = runtime

