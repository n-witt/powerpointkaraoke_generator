from random import choice
from os import walk

def get_decks():
    for root, dirs, files in walk('slidedecks'):
        for f in files:
            assert len(f.split('-')) == 2, "{} is an invalid filename".format(f)
            yield f.split('-')

def shuffle_dict(initial):
    keys = list(initial.keys())
    new = {}

    while len(keys) > 0:
        k1 = choice(keys)
        keys.remove(k1)
        k2 = choice(keys)
        keys.remove(k2)
        if len(keys) == 1:
            k3 = keys.pop()
            new[k1] = initial[k3]
            new[k2] = initial[k1]
            new[k3] = initial[k2]
        else:
            new[k1] = initial[k2]
            new[k2] = initial[k1]

    return new
