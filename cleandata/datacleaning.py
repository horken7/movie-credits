from mc.utils import generate

TOTALMOVIES = 1042622
#Actor = namedtuple('Actor', ['name', 'extra'])

# please change the the path
INPUT = "2017-02-09_223251_ImdbParserOutput/actors.list.tsv"

# generate desired files
GENERATE = [
    'top actors',
    #'unique actor movie',
    'filtered csv'
]

make = generate.Generate(INPUT, stop=100000)

options = {'top actors': make.top_actors,
           'unique actor movie': make.unique_actor_movie,
           'filtered csv': make.filtered_csv
           }
for option in GENERATE:
    options.get(option)()


"""
def main():

    Create a numpy array from the movie2actor dictionary
    :return: numpy array

    with open('movie2actor.pkl', mode='rb') as file:
        movie2actors = pickle.load(file)

    #print(movie2actors)


def detailed_mapping():
    # actor_dict[movie].append(Actor(full_name, extra=clean_row[3:])) # we can switch the movie / actor key here.
    pass

if __name__ == "__main__":
    main()

"""