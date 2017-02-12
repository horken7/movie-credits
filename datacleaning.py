import csv
import clean.clean as clean
import clean.filetools as filetool
import pickle
import time


def main():
    filename = "2017-02-09_223251_ImdbParserOutput/actors.list.tsv" # please change this path to your own file path to the tsv file
    actors_file = "unique_actors.pkl"
    actors = set()

    # pre-ready
    filetool.create(actors_file)
    start_time = time.time()
    print("Processing file... This may take a while.")

    with open(filename, mode='r') as file, open(actors_file, mode='r') as output: # make sure to change 'wb' <<<<<
        reader = csv.reader(file)

        for index ,row in enumerate(reader):
            clean_row = clean.clean(row)

            if clean_row:
                # uniquepeople.view(clean_row)

                find_names(clean_row, actors)



            if index > 1000:  # remove these two lines if you want to run through the whole file
                break

        # pickle.dump(actors, output)

    print(actors)
    del actors

    print("program finished it took {}".format(time.time()-start_time))

def find_names(info, actors):
    """
    Find the names and save it in the actors
    :param info: List
    :param actors: Set container
    """
    first_name = info[1]
    last_name = info[0]

    if first_name is None:
        pass
    else:
        name = (first_name + " " + last_name)
        actors.add(name)




if __name__ == "__main__":
    main()



