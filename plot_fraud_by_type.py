import matplotlib.pyplot as plt

# Read the file
fraud_counts = {}
with open("fraud_by_type.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            trans_type, count = parts
            fraud_counts[trans_type] = int(count)

# Sort by type or count
types = sorted(fraud_counts.keys())
counts = [fraud_counts[t] for t in types]

# Plotting
plt.figure(figsize=(8, 5))
bars = plt.bar(types, counts, color='teal', edgecolor='black')

# Add labels
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.3, str(height), ha='center')

plt.title("Fraudulent Transactions per Transaction Type")
plt.xlabel("Transaction Type")
plt.ylabel("Fraud Count")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("fraud_by_type.png")
plt.show()

