from unittest import TestCase
from utilities import shuffle_dict, get_decks
from random import randint

class test_Generator(TestCase):

    def test_decks(self):
        deck_mappings = {a: d for a, d in get_decks()}

        self.assertTrue(len(deck_mappings) > 0)

        for a, m in deck_mappings.items():
            self.assertIsInstance(m, str)
            self.assertIsInstance(a, str)
    

    def test_shuffle_dict_two_elements(self):
        initial = {1: 1, 2: 2}
        correct = {1: 2, 2: 1}
        result = shuffle_dict(initial)
        self.assertEquals(result, correct)

    def test_shuffle_dict_three_elements(self):
        initial = {1: 1, 2: 2, 3: 3}
        for i in range(100):
            result = shuffle_dict(initial)

    def test_complex_case(self):
        initial = {i: i for i  in range(100)}
        after = shuffle_dict(initial)
        for k in initial.keys():
            self.assertNotEqual(initial[k], after[k])
