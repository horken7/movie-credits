from moviecredits.utils.filehandler import INPUT as FILE_DIR
from moviecredits.utils import generate_subset, generate_all
import moviecredits.connections as connections
import pickle
import os

root, file = FILE_DIR

def main():

    """
    Generate all the necessary files to be run in main
    :return:
    """

    # make = generate_all.Generate(root, file)
    make = generate_subset.Generate(root, file, stop=100000)
    actor2movies, movie2actors, id2actors, id2movies, actors2id, movies2id = make.connection()
    top_actors = make.top_actors(actor2movies)

    with open(os.path.join(root, 'actor2movies.pkl'), 'wb') as pklfile:
        pickle.dump(actor2movies, pklfile)

    with open(os.path.join(root, 'movie2actors.pkl'), 'wb') as pklfile:
        pickle.dump(movie2actors, pklfile)

    with open(os.path.join(root, 'id2actors.pkl'), 'wb') as pklfile:
        pickle.dump(id2actors, pklfile)

    with open(os.path.join(root, 'id2movies.pkl'), 'wb') as pklfile:
        pickle.dump(id2movies, pklfile)

    with open(os.path.join(root, 'actors2id.pkl'), 'wb') as pklfile:
        pickle.dump(actors2id, pklfile)

    with open(os.path.join(root, 'movies2id.pkl'), 'wb') as pklfile:
        pickle.dump(movies2id, pklfile)

    with open(os.path.join(root, 'top_actors.pkl'), 'wb') as pklfile:
        pickle.dump(top_actors, pklfile)


if __name__ == '__main__':
    main()