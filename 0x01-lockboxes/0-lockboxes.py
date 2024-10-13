#!/usr/bin/python3

"""
   0-lockboxes
"""

def canUnlockAll(boxes):
    """
       checks if all the boxes are openable
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    
    keys = boxes[0]
    for key in keys:
        for index in boxes[key]:
            if index not in keys:
                keys.append(index)
    for i in range(1, len(boxes)):
        if i not in keys:
            return False
    return True