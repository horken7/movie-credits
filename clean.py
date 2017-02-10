import csv
import subprocess
import clean.removetvshows as clean

filename = "2017-02-09_223251_ImdbParserOutput/actors.list.tsv"

with open(filename, mode='r') as file:
    reader = csv.reader(file)

    for index ,row in enumerate(reader):
        string = row
        #print(string[0].split("\t"))

        clean.clean(string)


        if index > 100:
            break




