from mc.utils import generate

TOTALMOVIES = 1042622
#Actor = namedtuple('Actor', ['name', 'extra'])

# please change the the path
INPUT = "2017-02-09_223251_ImdbParserOutput/actors.list.tsv"

# generate desired files
GENERATE = [
    #'top actors',
    #'unique actor movie',
    'filtered csv'
    #'actorpair'
]

make_file = generate.Generate(INPUT, stop=100000)

# produce files
options = {'top actors': make_file.top_actors,
           'unique actor movie': make_file.unique_actor_movie,
           'filtered csv': make_file.filtered_csv,
           }
for option in GENERATE:
    options.get(option)()


def detailed_mapping():
    # actor_dict[movie].append(Actor(full_name, extra=clean_row[3:])) # we can switch the movie / actor key here.
    pass
