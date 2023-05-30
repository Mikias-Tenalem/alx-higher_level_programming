#!/usr/bin/python3
def search_replace(my_list, search, replace):
    while my_list.index(search) is True:
        my_list[my_list.index(search)] = replace
