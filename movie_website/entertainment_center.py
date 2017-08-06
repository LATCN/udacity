# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!
import media
import fresh_tomatoes
import json

# return movie object array from movies_json
def dict_to_movie(movies_json):
	movies = []
	for d in movies_json:
		movie = media.Movie(d['title'],d['storyline'],d['imageurl'],d['youtubeurl'])
		movies.append(movie)
	return movies

# define movies json array
movies_json = [
               {
                "title": "The Matrix", 
                "storyline": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.", 
                "imageurl": "https://images-na.ssl-images-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg",
                "youtubeurl": "https://www.youtube.com/watch?v=Vb6bA4J1Gbg"
               },
               {
                "title": "The Fifth Element", 
                "storyline": "In the colorful future, a cab driver unwittingly becomes the central figure in the search for a legendary cosmic weapon to keep Evil and Mr Zorg at bay.", 
                "imageurl": "https://images-na.ssl-images-amazon.com/images/M/MV5BZWFjYmZmZGQtYzg4YS00ZGE5LTgwYzAtZmQwZjQ2NDliMGVmXkEyXkFqcGdeQXVyNTUyMzE4Mzg@._V1_UY268_CR2,0,182,268_AL_.jpg",
                "youtubeurl": "https://www.youtube.com/watch?v=fQ9RqgcR24g"
               },               
               {
                "title": "I,Robot", 
                "storyline": "In 2035, a technophobic cop investigates a crime that may have been perpetrated by a robot, which leads to a larger threat to humanity.", 
                "imageurl": "https://images-na.ssl-images-amazon.com/images/M/MV5BMTI5NjExNTkzNl5BMl5BanBnXkFtZTYwNTI3Mjk2._V1_.jpg",
                "youtubeurl": "https://www.youtube.com/watch?v=05bGPiyM4jg"
               },
               {
                "title": "Interstellar", 
                "storyline": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.", 
                "imageurl": "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                "youtubeurl": "https://www.youtube.com/watch?v=zSWdZVtXT7E"
               },
               {
                "title": "The Terminator", 
                "storyline": "A seemingly indestructible humanoid cyborg is sent from 2029 to 1984 to assassinate a waitress, whose unborn son will lead humanity in a war against the machines, while a soldier from that war is sent to protect her at all costs.", 
                "imageurl": "https://images-na.ssl-images-amazon.com/images/M/MV5BODE1MDczNTUxOV5BMl5BanBnXkFtZTcwMTA0NDQyNA@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                "youtubeurl": "https://www.youtube.com/watch?v=1ULnyo0QWeo"
               }, 
               {
                "title": "Star Wars", 
                "storyline": "Two Jedi Knights escape a hostile blockade to find allies and come across a young boy who may bring balance to the Force, but the long dormant Sith resurface to claim their old glory.", 
                "imageurl": "https://images-na.ssl-images-amazon.com/images/M/MV5BM2FmZGIwMzAtZTBkMS00M2JiLTk2MDctM2FlNTQ2OWYwZDZkXkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                "youtubeurl": "https://www.youtube.com/watch?v=RIftKRavXCg"
               }                                       
              ]

# create movies object array
movies = dict_to_movie(movies_json)
# open movies page
fresh_tomatoes.open_movies_page(movies)
