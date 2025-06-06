#!/usr/bin/env python3
import sys
import heapq

top_transactions = []

for line in sys.stdin:
    amount_str, full_record = line.strip().split('\t', 1)
    amount = float(amount_str)
    heapq.heappush(top_transactions, (amount, full_record))
    if len(top_transactions) > 10:
        heapq.heappop(top_transactions)

for item in sorted(top_transactions, reverse=True):
    print(f"{item[0]}\t{item[1]}")
