from moviecredits.utils import generate
import os

def find_tsv():
    """find the the path to the tsv"""
    path = os.getcwd()
    file = 'actors.list.tsv'

    for root, dir, files in os.walk(path):
        if file in files:
            return os.path.join(root, file)
    exit("Error: {} was not found anywhere in movie_credits directory. Please put it in", file)


TOTALMOVIES = 1042622
#Actor = namedtuple('Actor', ['name', 'extra'])

INPUT = find_tsv()

