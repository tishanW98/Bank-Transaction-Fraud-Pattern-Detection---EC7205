#!/bin/bash

# Define common paths
STREAMING_JAR="/home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar"
INPUT="/user/hadoop/input/paysim.csv"

# --- First Job: Fraud count per transaction type ---
OUTPUT1="/user/hadoop/output/fraud_by_type"
MAPPER1="/home/hadoop/cloud_assignment/mappers/fraud_type_mapper.py"
REDUCER1="/home/hadoop/cloud_assignment/reducers/fraud_type_reducer.py"

echo "Running Job 1: Fraud count per transaction type..."
hdfs dfs -rm -r -skipTrash $OUTPUT1
hadoop jar $STREAMING_JAR \
  -input $INPUT \
  -output $OUTPUT1 \
  -mapper $MAPPER1 \
  -reducer $REDUCER1 \
  -file $MAPPER1 \
  -file $REDUCER1

echo -e "\n--- Output of Job 1 ---"
hdfs dfs -cat $OUTPUT1/part-00000

# --- Second Job: Top 10 high-value fraudulent transactions ---
OUTPUT2="/user/hadoop/output/top_fraudulent"
MAPPER2="/home/hadoop/cloud_assignment/mappers/high_value_fraud_mapper.py"
REDUCER2="/home/hadoop/cloud_assignment/reducers/top_fraud_reducer.py"

echo -e "\nRunning Job 2: Top 10 high-value fraudulent transactions..."
hdfs dfs -rm -r -skipTrash $OUTPUT2
hadoop jar $STREAMING_JAR \
  -input $INPUT \
  -output $OUTPUT2 \
  -mapper $MAPPER2 \
  -reducer $REDUCER2 \
  -file $MAPPER2 \
  -file $REDUCER2

echo -e "\n--- Output of Job 2 ---"
hdfs dfs -cat $OUTPUT2/part-00000
