#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """method to check if all the lockboxes can be unlocked"""
    keys = [0]
    lost = 0
    keys.extend(boxes[0])
    for index in range(1, len(boxes)):
        if index in keys:
            if lost in boxes[index]:
                keys.extend(boxes[lost])
            keys.extend(boxes[index])
        if index not in keys:
            lost = index
    keys_sorted = set(sorted(keys))
    unlocked = set(list(range(len(boxes))))
    if unlocked.issubset(keys_sorted):
        return True
    return False
