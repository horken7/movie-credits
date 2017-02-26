import csv

with open ('2017-02-09_223251_ImdbParserOutput/actors.list.tsv.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
        break