from mc.utils import generate
import datacleaning

FILE = datacleaning.INPUT
make = generate.Generate(FILE, stop=100000)

# output pairs of actors
pairs = make.pair_actors()
for pair in pairs:
    print(pair)