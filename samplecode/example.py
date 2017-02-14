import pickle
import pprint
import numpy as np



# make sure to change the path to your file
path_to_pkl1_actors = '/Users/Andrew/Github-repo/movie_credits/cleandata/actor_dict_lite.pkl'
path_to_pkl2_movies = '/Users/Andrew/Github-repo/movie_credits/cleandata/movie_dict_lite.pkl'

with open(path_to_pkl1_actors, mode='rb') as actors, open(path_to_pkl2_movies, mode='rb') as movies:
    actor = pickle.load(actors)
    movie = pickle.load(movies)

# if you want to see it, uncomment
#pprint.pprint(actor)
# pprint.pprint(movie)