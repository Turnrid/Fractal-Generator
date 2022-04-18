import unittest
from FractalFactory import makeFractal


class FractalTest(unittest.TestCase):

    def test_error(self):
        dictionary = {"type": "Not a type"}
        with self.assertRaises(NotImplementedError):
            makeFractal(dictionary)


if __name__ == '__main__':
    unittest.main()
