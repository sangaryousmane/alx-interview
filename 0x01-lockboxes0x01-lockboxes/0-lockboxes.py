#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    if not boxes:
        return False

    keys = set(boxes[0])
    opened = {0}
    new_boxes_to_check = list(keys)

    while new_boxes_to_check:
        box_to_check = new_boxes_to_check.pop(0)
        if box_to_check not in opened:
            opened.add(box_to_check)
            for key in boxes[box_to_check]:
                new_boxes_to_check.append(key)

    return len(opened) == len(boxes)
