#!/usr/bin/env python3

import logging
from utilities import get_decks, shuffle_dict

def initial_setting():
    return {p: d for p, d in get_decks()}

if __name__ == '__main__':
    initial = initial_setting()
    new = shuffle_dict(initial)

    print("### Initial Setting ###")
    for p, d in initial.items():
        print(f"{p:20} -> {d}")

    print("\n### New Setting ###")
    for p, d in new.items():
        print(f"{p:20} -> {d}")
