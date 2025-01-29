#!/usr/bin/env python

import json
import os
from multiprocessing import Process

number_of_processes = 10  # Number of parallel processes


def output_into_json(name):
    """
    Each process calls this function which writes into a separate JSON file.
    """

    filename = f"output_{name}.json"  # Unique file per process
    with open(filename, "w") as fOUT:
        dictionary = {
            "Process name": name,
            "pid": os.getpid(),
            "parent pid": os.getppid(),
        }
        json.dump(dictionary, fOUT, indent=2)


processes = []
for i in range(number_of_processes):
    p = Process(target=output_into_json, args=(f"Ossama{i+1}",))  # Correct tuple syntax
    processes.append(p)
    p.start()

# Ensure all processes finish
for p in processes:
    p.join()
