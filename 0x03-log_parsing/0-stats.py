#!/usr/bin/python3
"""
Log Parsing
"""


import sys


sum_file_size = 0
code_value = {"200": 0, "301": 0, "400": 0, "401": 0,
              "403": 0, "404": 0, "405": 0, "500": 0}
count = 0
try:
    for line in sys.stdin:
        parsed = line.split(" ")
        if len(parsed) != 9:
            pass
        status_code = parsed[-2]
        try:
            sum_file_size += int(parsed[-1])
        except Exception:
            pass
        count += 1
        if status_code in code_value.keys():
            code_value[status_code] += 1
        if count % 10 == 0:
            print("File size: {}".format(sum_file_size))
            for k in sorted(code_value.keys()):
                if code_value[k] != 0:
                    print("{}: {}".format(k, code_value[k]))
finally:
    print("File size: {}".format(sum_file_size))
    for k in sorted(code_value.keys()):
        if code_value[k] != 0:
            print("{}: {}".format(k, code_value[k]))
    raise
