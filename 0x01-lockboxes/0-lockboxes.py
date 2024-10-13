#!/usr/bin/python3

"""
   0-lockboxes
"""

def canUnlockAll(boxes):
    """
       checks if all the boxes are openable
    """
    keys = boxes[0]
    for key in keys:
        for index in boxes[key]:
            if index not in keys:
                keys.append(index)
    for i in range(1, len(boxes)):
        if i not in keys:
            return False
    return True