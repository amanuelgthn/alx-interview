#!/usr/bin/python3
"""
Log Parsing
"""


import sys
import re

possible_code = [200, 301, 400, 401, 403, 404, 405, 500]
sum_file_size = 0
code_value = {}
count = 0
sorted_code = {}
try:
    for line in sys.stdin:
        try:
            status_code = int(line.split()[7])
            file_size = int(line.split()[8])
        except ValueError:
            pass
        if "Exit" == line.rstrip():
            break
        if status_code in possible_code:
            if status_code not in code_value.keys():
                code_value[status_code] = 1
            code_value[status_code] += 1
        sum_file_size += file_size
        count += 1
        if count == 10:
            print("File size:", sum_file_size)
            sorted_code = dict(sorted(code_value.items()))
            for k, v in sorted_code.items():
                print(k, v)
            count = 0
finally:
    print("File size:", sum_file_size)
    for k, v in sorted_code.items():
        print(k, v)


