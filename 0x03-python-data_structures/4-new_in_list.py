#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list)-1:
        return my_list
    else:
        changed_list = [x for x in my_list]
        changed_list[idx] = element
        return changed_list
