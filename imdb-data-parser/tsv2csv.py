import sys
import csv

"""
Run by: python script.py < input.tsv > output.csv
"""

tab_in = csv.reader(sys.stdin, dialect=csv.excel_tab)
comma_out = csv.writer(sys.stdout, dialect=csv.excel)
for row in tab_in:
      comma_out.writerow(row)
