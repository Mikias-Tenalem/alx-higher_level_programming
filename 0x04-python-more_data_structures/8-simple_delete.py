#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary[key] is True:
        del a_dictionary[key]
    return (a_dictionary)