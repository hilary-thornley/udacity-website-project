#this imports the webbrowser module from Python, and it's used in a 
#function below to initiate the opening of a webpage.
import webbrowser

#this creates a class, "Movie", which serves as a template for creating individual 
#movie items in our entertainment_center.py file.  This class includes functions 
#defining information about a a movie, and a method for initiating a video of
#a movie's trailer.
class Movie():
	def __init__(self, movie_title, movie_storyline, poster_image,
				trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

	
