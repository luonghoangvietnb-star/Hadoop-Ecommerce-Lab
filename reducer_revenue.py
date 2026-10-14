import sys

current = None
total = 0

for line in sys.stdin:
    category, amount = line.strip().split("\t")
    amount = int(amount)
    
    if current == category:
        total += amount
    else:
        if current is not None:
            print(f"{current}\t{total}")
        current = category
        total = amount

if current is not None:
    print(f"{current}\t{total}")
