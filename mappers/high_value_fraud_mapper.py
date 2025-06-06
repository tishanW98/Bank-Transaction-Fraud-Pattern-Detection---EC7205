#!/usr/bin/env python3
import sys
import csv

for row in csv.reader(sys.stdin):
    if row[0] == 'step':
        continue
    amount = float(row[2])
    is_fraud = row[10]
    if is_fraud == '1' and amount > 200000:
        print(f"{amount}\t{','.join(row)}")
