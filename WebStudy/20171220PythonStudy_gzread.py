# coding: utf-8

import gzip
import csv

file = r'C:\Users\gm3910\Desktop\20171219.txt.gz'
with gzip.open(file, 'r') as f:
    reader = csv.reader(f, delimiter='¥t')
    for row in reader:
        print(''.join(row))
