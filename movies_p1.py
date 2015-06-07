# Movie Website - Project 1 for the Full Stack Web Developer Nanodegree
# import required modules
import csv
import media  # movie class
import fresher_tomatoes  # web page display generator

movies = list()

# load movie data from CSV file into list of Movie objects
faves = open('fave_movies.csv')
with faves as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
                fave = media.Movie(row['title'], row['release_year'],
                                   row['poster_url'], row['trailer_url'])
                movies.append(fave)

faves.close()

# build & display webpage
fresher_tomatoes.open_movies_page(movies)
