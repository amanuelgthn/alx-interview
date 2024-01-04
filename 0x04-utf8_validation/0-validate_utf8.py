#!/usr/bin/python3
"""UTF8_Validation"""


def validUTF8(data):
    """R
    eturns True if dat is a valid UTF-8 encoding and return False if else
    """

    try:
        bytes(data).decode('utf-8')
    except Exception:
        return False
    return True
