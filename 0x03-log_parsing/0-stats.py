#!/usr/bin/python3
"""
Log Parsing
"""


import sys


possible_codes = [200, 301, 400, 401, 403, 404, 405, 500]
sum_file_size = 0
code_value = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
count = 0
try:
    for line in sys.stdin:
        try:
            if len(line.split()) != 9:
                pass
            status_code = line.split()[7]
            file_size = int(line.split()[8])
        except Exception:
            pass
        if status_code in code_value.keys():
            code_value[status_code] += 1
        sum_file_size += file_size
        count += 1
        if count % 10 == 0:
            print("File size: {}".format(sum_file_size))
            for k in sorted(code_value.keys()):
                if code_value[k] != 0:
                    print("{}: {}".format(k, code_value[k]))
                code_value[k] = 0
except KeyboardInterrupt as e:
    print("File size: {}".format(sum_file_size))
    for k in sorted(code_value.keys()):
                if code_value[k] != 0:
                    print("{}: {}".format(k, code_value[k]))
    raise
