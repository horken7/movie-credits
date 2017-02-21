from .cleandata.mc.utils import generate
from .cleandata.datacleaning import INPUT


make = generate.Generate(INPUT, stop=100000)

# output pairs of actors
pairs = make.pair_actors()
for pair in pairs:
    print(pair)