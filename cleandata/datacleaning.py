import csv
import pickle
import time
from collections import defaultdict
from mc.utils import clean, filehandler, generate

TOTALMOVIES = 1042622
#Actor = namedtuple('Actor', ['name', 'extra'])

INPUT = "2017-02-09_223251_ImdbParserOutput/actors.list.tsv"  # please change this path to your own file path to the tsv file
OUTPUT = 'map_lite.pkl'

if not filehandler.exist('unique_actors_lite.pkl') or not filehandler.exist('unique_movies_lite.pkl'):
    generate.actor_movie(INPUT)

####### havent fixed
def main():

    actor_dict = defaultdict(list)
    actorid = defaultdict(set)
    movieid = defaultdict(set)


    # pre-ready
    filehandler.create(OUTPUT)

    start_time = time.time()
    print("Processing file... This may take a while.")

    with open(INPUT, mode='r') as file, open(OUTPUT, mode='wb') as output: # make sure to change 'wb' <<<<<
        reader = csv.reader(file)

        for index ,row in enumerate(reader):
            clean_row = clean.clean(row)
            if clean_row:

                movie = clean_row[2]
                actor_name = generate.full_name(clean_row[1], clean_row[0])


                # generate id for actors and movies for better lookup performance
                #generate_id(movies, movieid)



                # simple mapping
                #actor_dict[movie] = actor_name

            if index > 100000:  # remove these two lines if you want to run through the whole file
                break

        # save
        pickle.dump(actor_dict, output)

    print(movieid)
    print(actor_dict)

    #assert len(actor_dict) == len(movies)

    print("program finished it took {}".format(time.time()-start_time))


def detailed_mapping():
    # actor_dict[movie].append(Actor(full_name, extra=clean_row[3:])) # we can switch the movie / actor key here.
    pass


if __name__ == "__main__":
    pass
