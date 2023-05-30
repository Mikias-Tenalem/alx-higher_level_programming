#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = set(my_list)
    set_sum = 0
    for i in result:
        set_sum = set_sum + i
    return set_sum
