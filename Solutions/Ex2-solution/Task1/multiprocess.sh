#!/bin/bash

number_of_processes= 10  # Number of parallel processes

# Function to create a JSON file for each process
output_into_json() {
    name=$1
    pid=$BASHPID
    ppid=$(ps -o ppid= -p $$)

    # Create a JSON file with process details
    echo "{
  \"Process name\": \"$name\",
  \"pid\": $pid,
  \"parent pid\": $ppid
}" > "output_${name}.json"
}

# Start processes
for i in $(seq 0 $((number_of_processes - 1))); do
    output_into_json "Ossama$i" &
done

wait  # Wait for all background processes to finish
