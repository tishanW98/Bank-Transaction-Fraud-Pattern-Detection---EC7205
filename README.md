# Fraud Detection Pattern Analysis with Hadoop MapReduce

## Project Overview

This project analyzes financial transaction data using Hadoop Streaming and Python-based MapReduce programs. The goal is to identify fraud patterns across transaction types and extract insights such as:

- The **number of fraudulent transactions per transaction type**
- The **top 10 high-value fraudulent transactions**

The analysis is based on the **PaySim Synthetic Financial Dataset**, processed in a distributed Hadoop environment.

---

## Technologies Used

- Hadoop 3.3.6 (Streaming)
- Python 3
- HDFS
- Matplotlib (for post-analysis visualization)

---

## Project Structure

```bash
cloud_assignment/
├── mappers/
│   ├── fraud_type_mapper.py
│   └── high_value_fraud_mapper.py
├── reducers/
│   ├── fraud_type_reducer.py
│   └── top_fraud_reducer.py
├── fraud_by_type.txt
├── top_fraudulent.txt
├── fraud_by_type.png
├── top_fraudulent.png
├── plot_fraud_by_type.py
├── plot_top_fraud.py
├── run_all_jobs.sh
└── run_jobs.sh
```

## Dataset

- **Name:** PaySim Synthetic Financial Dataset
- **Source:** Kaggle - PaySim Fraud Detection

## MapReduce Logic

### Job 1: Fraud Count Per Transaction Type

- **Mapper:** Emits `(transaction_type, is_fraud)`
- **Reducer:** Sums total fraud counts for each transaction type (even if the count is 0)

```bash
Output example:
CASH_IN  2
CASH_OUT  18
DEBIT 0
PAYMENT 0
TRANSFER 22
```

### Job 2: Top 10 High-Value Fraudulent Transactions

- **Mapper:** Filters fraudulent transactions with `amount > 200000`
- **Reducer:** Maintains a heap to find top 10 based on transaction amount

## Post-Processing and Visualization

After executing the jobs, the output is visualized using Python's `matplotlib`:

`plot_fraud_by_type.py` : Bar chart of fraud count by transaction type
`plot_top_fraud.py` : Horizontal bar chart of top 10 high-value frauds.

## How to Run

### 1. Place the Dataset into HDFS

```bash
hdfs dfs -mkdir -p /user/hadoop/input
hdfs dfs -put paysim.csv /user/hadoop/input/paysim.csv
```

### 2. Run MapReduce Jobs via Shell Script

```bash
bash run_all_jobs.sh
```

### 3. Save Output Files Locally

```bash
hdfs dfs -cat /user/hadoop/output/fraud_by_type/part-00000 > fraud_by_type.txt
hdfs dfs -cat /user/hadoop/output/top_fraudulent/part-00000 > top_fraudulent.txt
```

### 4. Plot Results

```bash
python3 plot_fraud_by_type.py
python3 plot_top_fraud.py
```

## Sample Visuals

- Fraud Count per Transaction Type
- Top 10 High-Value Fraudulent Transactions

## Deliverables

- Python mapper and reducer scripts
- Shell script to execute Hadoop jobs
- Final output files: `fraud_by_type.txt`, `top_fraudulent.txt`
- Visualization scripts and generated plots
