from moviecredits.utils.filehandler import INPUT as FILE_DIR
from moviecredits.utils import generate_subset, generate_all
import moviecredits.connections as connections
import pickle



def main():


    make = generate_subset.Generate(FILE_DIR, stop=10000)
    # make = generate_all.Generate(FILE_DIR)
    actor2movies, movie2actors, id2actors, id2movies, movies2id, actors2id = make.connection()
    top_actors = make.top_actors(actor2movies)


if __name__ == '__main__':
    main()