import os

def create(file):
# create file if required
   with open(file, mode='a'):
       os.utime(file, None) # set modified time

def exist(file):
    return os.path.isfile(file)


