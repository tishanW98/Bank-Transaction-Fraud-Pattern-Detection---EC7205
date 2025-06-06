#!/usr/bin/env python3
import sys
from collections import defaultdict

VALID_TYPES = {"PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN"}
fraud_counts = defaultdict(int)

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    try:
        trans_type, value = line.split('\t')
        value = int(value)
        if trans_type in VALID_TYPES:
            fraud_counts[trans_type] += value
    except ValueError:
        continue

# Ensure all types are shown
for trans_type in sorted(VALID_TYPES):
    print(f"{trans_type}\t{fraud_counts[trans_type]}")
