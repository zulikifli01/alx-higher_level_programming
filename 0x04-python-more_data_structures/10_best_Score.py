#!/bin/env python
a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}


def best_score(a_dictionary):
    large = max(a_dictionary, key=a_dictionary.get)
    print("Best score: ", large)
    print("best score: ", None)


best_score(a_dictionary)
