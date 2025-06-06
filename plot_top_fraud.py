import matplotlib.pyplot as plt

amounts = []
descriptions = []

with open("top_fraudulent.txt", "r") as file:
    for line in file:
        parts = line.strip().split("\t", 1)
        if len(parts) != 2:
            continue
        amount = float(parts[0])
        record = parts[1]
        amounts.append(amount)
        descriptions.append(record.split(",")[1])  # Transaction type (optional)

# Top 10
descriptions = descriptions[:10]
amounts = amounts[:10]

plt.figure(figsize=(10, 5))
bars = plt.barh(range(len(amounts)), amounts, color='salmon', edgecolor='black')
plt.yticks(range(len(amounts)), descriptions)
plt.xlabel("Transaction Amount")
plt.title("Top 10 High-Value Fraudulent Transactions")

# Label values
for i, bar in enumerate(bars):
    plt.text(bar.get_width() + 1000, bar.get_y() + bar.get_height()/2, f"${amounts[i]:,.2f}", va='center')

plt.tight_layout()
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.savefig("top_fraudulent.png")
plt.show()
