#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    else:
        max_key = list(a_dictionary)
        best = ''
        for i in range(len(max_key)):
            if a_dictionary[max_key[i]] >= a_dictionary[max_key[i+1]]:
                best = a_dictionary[max_key[i]]
        return (best)
