import unittest
import binary_tree_avl

class TestMethods(unittest.TestCase):
    def test_input(self):
        result = main.run_guess(5,5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = main.run_guess(5,8)
        self.assertFalse(result)

    def test_input_wrong_num(self):
        result = main.run_guess(5,11)
        self.assertFalse(result)

    def test_input_wrong_string(self):
        result = main.run_guess(5,'8')
        self.assertFalse(result)

if __name__ == '__main__':
    TestMethods()