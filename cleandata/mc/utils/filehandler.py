import os
import subprocess
from sys import platform as _platform, exit

def create(file):
# check file existence, create file if required
    if bash():
        if not os.path.isfile(file):
            command = "touch %s"% file
            subprocess.run([command], shell=True)
            print("{} does not exist... creating one for you.".format(file))
    elif not bash():
        if not os.path.isfile(file):
            command = "type nul >> %s"% file
            subprocess.run([command], shell=True)
            print("{} does not exist... creating one for you.".format(file))
    else:
        exit("Error: Uncertain of the operating system you are using")

def exist(file):
    return os.path.isfile(file)

def bash():
    """
    Check bash compliant
    :return: Boolean
    """
    if _platform == "linux" or _platform == "linux2":
        return True
    elif _platform == "darwin":
        return True
    elif _platform == "win32":
        return False



