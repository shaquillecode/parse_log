#!/usr/bin/env python3

import os
import csv
import sys

print(os.getcwd()) # This gets the current working directory


data = sys.argv[1]

with open(data) as csv_file:

    # read the csv file using DictReader
    csv_reader = csv.DictReader(csv_file, delimiter=';')
    
    source_destination_ip = []
    source_destination_dict = {}
    
    # Convert to dictionary to get count
    for row in csv_reader:

        source_destination_ip.append(row['ip.src'])
        source_destination_ip.append(row['ip.dst'])

        if row['ip.src'] not in source_destination_dict:
            source_destination_dict[row['ip.src']] = 0
        source_destination_dict[row['ip.src']] += 1

        if row['ip.dst'] not in source_destination_dict:
            source_destination_dict[row['ip.dst']] = 0
        source_destination_dict[row['ip.dst']] += 1

    most_common_ip = max(source_destination_dict.values())

    for k,v in source_destination_dict.items():
        if v == most_common_ip:
            print("The most common IP address is {ip}, and appears {count} times".format(ip = k, count = v))
