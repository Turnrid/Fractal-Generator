import unittest
from FractalParser import FractalParser


class ParserTest(unittest.TestCase):

    def test_parser(self):
        dictionary = {"pixels": 640, "iterations": 100}
        self.assertEqual(dictionary["pixels"], FractalParser("data/branches100.frac")["pixels"])
        self.assertEqual(dictionary["iterations"], FractalParser("data/branches100.frac")["iterations"])

    def test_error(self):
        with self.assertRaises(RuntimeError):
            FractalParser("data/invalid.frac")

    def test_default(self):
        self.assertDictEqual(FractalParser("data/mandelbrot.frac"), FractalParser())


if __name__ == '__main__':
    unittest.main()
