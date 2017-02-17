import pickle
from cleandata.mc.utils import filehandler, generate

TOTALMOVIES = 1042622
#Actor = namedtuple('Actor', ['name', 'extra'])

# please change the the path
INPUT = "/Users/Andrew/Github-repo/movie_credits/2017-02-09_223251_ImdbParserOutput/actors.list.tsv"
OUTPUT = 'map_lite.pkl'

# generate desired files
if not filehandler.exist('movie2actor.pkl'):
    generate.actor_movie(INPUT)
#generate.unique_actor_movie(INPUT)
generate.filtered_csv(INPUT)


def main():
    """
    Create a numpy array from the movie2actor dictionary
    :return: numpy array
    """
    with open('movie2actor.pkl', mode='rb') as file:
        movie2actors = pickle.load(file)

    print(movie2actors)


def detailed_mapping():
    # actor_dict[movie].append(Actor(full_name, extra=clean_row[3:])) # we can switch the movie / actor key here.
    pass

if __name__ == "__main__":
    main()
