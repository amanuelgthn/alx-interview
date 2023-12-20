#!/usr/bin/python3
"""
Log Parsing
"""


import sys


possible_codes = [200, 301, 400, 401, 403, 404, 405, 500]
sum_file_size = 0
code_value = {}
count = 0
sorted_code = {}
try:
    for line in sys.stdin:
        try:
            if len(line.split()) != 9:
                pass
            status_code = int(line.split()[7])
            file_size = int(line.split()[8])
        except Exception:
            pass
        if status_code in possible_codes:
            if status_code not in code_value.keys():
                code_value[status_code] = 1
            code_value[status_code] += 1
        sum_file_size += file_size
        count += 1
        if count == 9:
            print("File size: {}".format(sum_file_size))
            sorted_code = dict(sorted(code_value.items()))
            for k, v in sorted_code.items():
                if sorted_code[k] != 0:
                    print("{}: {}".format(k, v))
                code_value[k] = 0
            count = 0
except KeyboardInterrupt as e:
    print("File size: {}".format(sum_file_size))
    for k, v in sorted_code.items():
        if sorted_code[k] != 0:
            print("{}: {}".format(k, v))
    raise
