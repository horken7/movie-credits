import csv
import subprocess
import clean.removetvshows as clean

filename = "2017-02-09_223251_ImdbParserOutput/actors.list.tsv" # please change this path to your own file path to the tsv file

with open(filename, mode='r') as file:
    reader = csv.reader(file)

    for index ,row in enumerate(reader):
        clean.clean(row)

        if index > 100:
            break




