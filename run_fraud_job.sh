#!/bin/bash

# Define paths
STREAMING_JAR="/home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar"
INPUT_PATH="/user/hadoop/input/paysim.csv"
OUTPUT_PATH="/user/hadoop/output/fraud_analysis"
MAPPER="/home/hadoop/cloud_assignment/mappers/mapper.py"
REDUCER="/home/hadoop/cloud_assignment/reducers/reducer.py"

# Remove previous output (if exists)
hdfs dfs -rm -r -skipTrash $OUTPUT_PATH

# Run the MapReduce job
hadoop jar $STREAMING_JAR \
  -input $INPUT_PATH \
  -output $OUTPUT_PATH \
  -mapper $MAPPER \
  -reducer $REDUCER \
  -file $MAPPER \
  -file $REDUCER

# Show output
echo -e "\n--- Output of fraud_analysis job ---"
hdfs dfs -cat $OUTPUT_PATH/part-00000
