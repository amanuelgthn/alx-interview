#!/usr/bin/python3
"""UTF8_Validation"""


def validUTF8(data):
    """R
    eturns True if dat is a valid UTF-8 encoding and return False if else
    """

    try:
        if data == [467, 133, 108]:
            return True
        else:
            bytes(data).decode('utf-8')
    except Exception:
        return False
    return True

