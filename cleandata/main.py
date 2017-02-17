import pickle
from collections import namedtuple
import pprint

Actor = namedtuple('Actor', ['name', 'extra'])
filename = "movie_dict_lite.pkl"
filename2 = "actor_dict_lite.pkl"

with open(filename, "rb") as file, open(filename2, "rb") as file2:
    data = pickle.load(file)
    data2 = pickle.load(file2)

#print(data, "\n", "no. of unique {movie|actors?}",len(data))

pprint.pprint(data)
#print(data2)




mapping = {}
def map_movie_actor(movie, actor):
    """
    create a mapping of actors with their movies
    :param movie: String
    :param actor: String
    :return: mapping: Dictionary
    """
    mapping[movie] = {}
    mapping["movie"].add(actor)
    return mapping

def store_as_json(data):
    """
    Write the dict into json format and store it in a file
    :param data: Dictionary
    """
    import json #move!
    with open('movie-actor.json', 'w') as outfile:
        json.dump(data, outfile, sort_keys=True)

def lookup(data):
    """
    Look up actors who did the same movie together
    :param data:
    :return:
    """
    pass



