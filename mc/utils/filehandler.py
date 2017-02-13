import os
import subprocess

def create(file):
# check file existence, create file if required
    if not os.path.isfile(file):
        command = "touch %s"% file
        subprocess.run([command], shell=True)
        print("no {} exists... creating one for you.".format(file))

def exist(file):
    return os.path.isfile(file)

