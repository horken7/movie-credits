import filetools
import subprocess

#TODO:
# Starting position begins at line 240
# ignore blank lines

SKIP = 239

filename = "actors.list"
output_filename = "tmp.list"

#clean
filetools.clean(output_filename)


with open(filename, mode='r', encoding='ISO-8859-1') as file1, open(output_filename, mode='w', encoding='ISO-8859-1') as file2:

    #skip lines
        for _ in range(SKIP):
            file1.readline()

        for _ in range(20):
            line = file1.readline()
            if line is "\n": continue

            file2.write(line)

subprocess.run('open tmp.list', shell=True)
