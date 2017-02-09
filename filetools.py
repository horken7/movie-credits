import os
import subprocess

def empty(filename):
    with open(filename, 'w') as file:
        file.seek(0)
        file.truncate()


def clean(file):
#check file existence, create file if required
    if not os.path.isfile(file):
        command = "touch %s"% file
        subprocess.run([command], shell=True)
        print("no {} exists... creating one for you.".format(file))
    else:
        empty(file)
        print("cleaning {}...".format(file))
