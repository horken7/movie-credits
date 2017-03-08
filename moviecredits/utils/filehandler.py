import os

def create(file):
# create file if required
   with open(file, mode='a'):
       os.utime(file, None) # set modified time

def exist(file):
    return os.path.isfile(file)

def find_tsv():
    """find the the path to the tsv"""
    path = os.getcwd()
    file = 'actors.list.tsv'

    for root, dir, files in os.walk(path):
        if file in files:
            return root, os.path.join(root, file)
    exit("Error: {} was not found anywhere in movie_credits directory. Please put it in".format(file))


TOTALMOVIES = 1042622

INPUT = find_tsv()

