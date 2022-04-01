#                         ~  	         	  
#                        (o)<  DuckieCorp Software License  	         	  
#                   .____//  	         	  
#                    \ <' )   Copyright (c) 2022 Erik Falor  	         	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	         	  
#  	         	  
# Permission is NOT granted, to any person who is NEITHER an employee NOR  	         	  
# customer of DuckieCorp, to deal in the Software without restriction,  	         	  
# including without limitation the rights to use, copy, modify, merge,  	         	  
# publish, distribute, sublicense, and/or sell copies of the Software, and to  	         	  
# permit persons to whom the Software is furnished to do so, subject to the  	         	  
# following conditions:  	         	  
#  	         	  
# The above copyright notice and this permission notice shall be included in  	         	  
# all copies or substantial portions of the Software.  	         	  
#  	         	  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  	         	  
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  	         	  
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  	         	  
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  	         	  
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING  	         	  
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS  	         	  
# IN THE SOFTWARE.  	         	  

import unittest  	         	  
from julia import returnIterationCount, getFractalConfigurationDataFromFractalRepositoryDictionary
from palette import paletteLength, paletteSelector
from fractal_info import images


# autocmd BufWritePost <buffer> !python3 runTests.py  	         	  

class TestJulia(unittest.TestCase):  	         	  
    def test_colorOfThePixel(self):
        palette = paletteSelector(0)

        self.assertEqual(palette[returnIterationCount(complex(0, 0))], '#009cb3')
        self.assertEqual(palette[returnIterationCount(complex(-0.751, 1.1075))], '#ffe4b5')
        self.assertEqual(palette[returnIterationCount(complex(-0.2, 1.1075))], '#ffe4b5')
        self.assertEqual(palette[returnIterationCount(complex(-0.75, 0.1075))], '#009cb3')
        self.assertEqual(palette[returnIterationCount(complex(-0.748, 0.1075))], '#009cb3')
        self.assertEqual(palette[returnIterationCount(complex(-0.7562500000000001, 0.078125))], '#009cb3')
        self.assertEqual(palette[returnIterationCount(complex(-0.7562500000000001, -0.234375))], '#ffeda4')
        self.assertEqual(palette[returnIterationCount(complex(0.3374999999999999, -0.625))], '#ffe7ae')
        self.assertEqual(palette[returnIterationCount(complex(-0.6781250000000001, -0.46875))], '#ffe7ae')
        self.assertEqual(palette[returnIterationCount(complex(0.4937499999999999, -0.234375))], '#fff797')
        self.assertEqual(palette[returnIterationCount(complex(0.3374999999999999, 0.546875))], '#ffe9ab')

    def test_dictionaryGetter(self):  	         	  
        self.assertIsNone(getFractalConfigurationDataFromFractalRepositoryDictionary(images, 'absent'))
        self.assertIsNotNone(getFractalConfigurationDataFromFractalRepositoryDictionary(images, 'fulljulia'))
        self.assertIsNone(getFractalConfigurationDataFromFractalRepositoryDictionary(images, ''))
        self.assertIsNotNone(getFractalConfigurationDataFromFractalRepositoryDictionary(images, 'lakes'))
        self.assertIsNone(getFractalConfigurationDataFromFractalRepositoryDictionary(images, 'Still Not In Here'))
        self.assertIsNotNone(getFractalConfigurationDataFromFractalRepositoryDictionary(images, 'hourglass'))


if __name__ == '__main__':  	         	  
    unittest.main()  	         	  
