from moviecredits.utils import generate

TOTALMOVIES = 1042622
#Actor = namedtuple('Actor', ['name', 'extra'])

# please change the the path
INPUT = "moviecredits/2017-02-09_223251_ImdbParserOutput/actors.list.tsv"

# generate desired files
GENERATE = [
    #'unique actors and movies',
    # 'filtered csv'
]

make_file = generate.Generate(INPUT, stop=100000)

# produce files
options = {
           'unique actors and movies': make_file.unique_actor_movie,
           'filtered csv': make_file.filtered_csv,
           }
for option in GENERATE:
    options.get(option)()
