from unittest import TestCase
from powerpointshuffle import initial_setting

class test_powerpointshuffle(TestCase):

    def test_initial_setting(self):
        initial = initial_setting()
        self.assertIsInstance(initial, dict)
        for k, v in initial.items():
            self.assertIsInstance(k, str)
            self.assertIsInstance(v, str)

