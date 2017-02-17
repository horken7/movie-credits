import pickle
import pprint
import numpy as np


# open any pkl file you like

# make sure to change the path to your file
PATH_TO_FILE = '/Users/Andrew/Github-repo/movie_credits/cleandata/actor_dict_lite.pkl'

with open(PATH_TO_FILE, mode='rb') as file:
    reader = pickle.load(file)

# if you want to see it, uncomment
#pprint.pprint(reader)
