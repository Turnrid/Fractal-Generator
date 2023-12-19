import unittest

from Testing import PaletteTest, ParserTest, FractalTest

suite = unittest.TestSuite()

tests = (PaletteTest.PaletteTest, ParserTest.ParserTest, FractalTest.FractalTest)
for test in tests:
    suite.addTest(unittest.makeSuite(test))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)  	         	  
