import unittest
from PaletteFactory import makePalette


class PaletteTest(unittest.TestCase):

    def test_paletteOne(self):
        dictionaryOne = {"iterations": 100}
        dictionaryTwo = {"iterations": 500}
        dictionaryThree = {"iterations": 1000}
        self.assertEqual(100, len(makePalette(dictionaryOne, "paletteOne").palette))
        self.assertEqual(500, len(makePalette(dictionaryTwo, "paletteOne").palette))
        self.assertEqual(1000, len(makePalette(dictionaryThree, "paletteOne").palette))

    def test_paletteTwo(self):
        dictionaryOne = {"iterations": 100}
        dictionaryTwo = {"iterations": 500}
        dictionaryThree = {"iterations": 1000}
        self.assertEqual(100, len(makePalette(dictionaryOne, "paletteTwo").palette))
        self.assertEqual(500, len(makePalette(dictionaryTwo, "paletteTwo").palette))
        self.assertEqual(1000, len(makePalette(dictionaryThree, "paletteTwo").palette))

    def test_Error(self):
        dictionaryOne = {"iterations": 100}
        with self.assertRaises(NotImplementedError):
            makePalette(dictionaryOne, "somePalette")




if __name__ == '__main__':
    unittest.main()
