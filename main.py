import pickle

filename = "tmp.pkl"

with open(filename, "rb") as file:
    reader = pickle.load(file)

print(reader, "\n", "no. of unique actors",len(reader))


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



