#!/usr/bin/env python3
import sys
import csv

VALID_TYPES = {"PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN"}

reader = csv.reader(sys.stdin)
header = next(reader, None)

for row in reader:
    if len(row) < 10:
        continue  # Skip malformed lines

    trans_type = row[1].strip().upper()
    is_fraud = row[9].strip()

    if trans_type in VALID_TYPES:
        try:
            if int(is_fraud) == 1:
                print(f"{trans_type}\t1")
            else:
                print(f"{trans_type}\t0")
        except ValueError:
            continue
