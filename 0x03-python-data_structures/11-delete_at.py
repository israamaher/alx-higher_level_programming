#!/usr/bin/python3
"""delete list """


def delete_at(my_list=[], idx=0):
    """deletes the item at a specific position in a list"""

    for i in range(len(my_list)):
            if i == idx:
                del my_list[idx]
                return my_list
                
