import csv
import clean.removetvshows as clean
import clean.filetools as filetool
import pickle
import time

filename = "2017-02-09_223251_ImdbParserOutput/actors.list.tsv" # please change this path to your own file path to the tsv file
out_file = "tmp.pkl"
actors = set()

# pre-ready
filetool.clean(out_file)
start_time = time.time()
print("Processing file... This may take a while.")

with open(filename, mode='r') as file, open(out_file, mode='wb') as output:
    reader = csv.reader(file)

    for index ,row in enumerate(reader):
        clean_row = clean.clean(row)

        if clean_row:
            #uniquepeople.view(clean_row)
            name = (clean_row[0])
            actors.add(name)

        #if index > 1000:  # remove these two lines if you want to run through the whole file
        #   break

    pickle.dump(actors, output)

print("program finished it took {}".format(time.time()-start_time))



