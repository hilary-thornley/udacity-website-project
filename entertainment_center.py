#imports code saved in fresh_tomatoes.py, which contains design specs and functionality for the movie website
import fresh_tomatoes
#imports the class "Movie" created in media.py
import media

#these are instances of the class "Movie", as defined in media.py
the_big_lebowski = media.Movie("The Big Lebowski",
								"Times like these call for a Big Lebowski",
								"https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
								"https://www.youtube.com/watch?v=cd-go0oBF4Y")
								
gremlins = media.Movie("Gremlins","What you see...isn't always what you get.",
						"https://upload.wikimedia.org/wikipedia/en/3/3d/Gremlins1.jpg",
						"https://www.youtube.com/watch?v=XBEVwaJEgaA")

independence_day = media.Movie("Independence Day",
								"The question of whether or not we are alone has just been answered.",
								"https://upload.wikimedia.org/wikipedia/en/b/bb/Independence_day_movieposter.jpg",
								"https://www.youtube.com/watch?v=kA2WzBi2grE")

jurassic_park = media.Movie("Jurassic Park","An adventure 65 million years in the making.",
							"https://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg",
							"https://www.youtube.com/watch?v=Bim7RtKXv90")
								
lotr_1 = media.Movie("The Fellowship of the Ring",
						"Power can be held in the smallest of things.",
						"https://upload.wikimedia.org/wikipedia/en/0/0c/The_Fellowship_Of_The_Ring.jpg",
						"https://www.youtube.com/watch?v=Pki6jbSbXIY")

the_ring = media.Movie("The Ring","Before you die, you see the ring.",
						"https://upload.wikimedia.org/wikipedia/en/3/37/Theringpostere.jpg",
						"https://www.youtube.com/watch?v=_PkgRhzq_BQ")

							
movies = [the_big_lebowski,gremlins,independence_day,jurassic_park,lotr_1,the_ring]

#this prompts the opening of a webpage which displays the above instances of class "Movie"
#in accordance with the instructions written in media.py and fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
