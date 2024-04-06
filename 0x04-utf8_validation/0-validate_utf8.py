#!/usr/bin/python3
""" A function that determines if a given data set
represents a valid UTF-8 encoding."""


def validUTF8(data):
    """ A function that determines if a given data set
    represents a valid UTF-8 encoding."""
    bytes_num = 0

    for num in data:
        byte = num & 255

        if bytes_num:
            if byte >> 6 != 2:
                return False
            bytes_num -= 1
        else:
            if byte >> 7 == 0:
                continue
            elif byte >> 5 == 6:
                bytes_num = 1
            elif byte >> 4 == 14:
                bytes_num = 2
            elif byte >> 3 == 30:
                bytes_num = 3
            else:
                return False
    return bytes_num == 0
