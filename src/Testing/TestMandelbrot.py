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
from mandelbrot import returnIterationCount, pixelsWrittenSoFar
from palette import paletteLength, paletteSelector
from fractal_info import images

# autocmd BufWritePost <buffer> !python3 runTests.py  	         	  

class TestMandelbrot(unittest.TestCase):  	         	  
    def test_colorOfThePixel(self):
        palette = paletteSelector(1)
        self.assertEqual(palette[returnIterationCount(complex(0, 0),paletteLength(1))], '#e8283f')
        self.assertEqual(palette[returnIterationCount(complex(-0.751, 1.1075),paletteLength(1))], '#baf12e')
        self.assertEqual(palette[returnIterationCount(complex(-0.2, 1.1075),paletteLength(1))], '#e0ceaf')
        self.assertEqual(palette[returnIterationCount(complex(-0.75, 0.1075),paletteLength(1))], '#f1da2e')
        self.assertEqual(palette[returnIterationCount(complex(-0.748, 0.1075),paletteLength(1))], '#deb69f')
        self.assertEqual(palette[returnIterationCount(complex(-0.7562500000000001, 0.078125),paletteLength(1))], '#e1bc7e')
        self.assertEqual(palette[returnIterationCount(complex(-0.7562500000000001, -0.234375),paletteLength(1))], '#e7ddd7')
        self.assertEqual(palette[returnIterationCount(complex(0.3374999999999999, -0.625),paletteLength(1))], '#e1d1bd')
        self.assertEqual(palette[returnIterationCount(complex(-0.6781250000000001, -0.46875),paletteLength(1))], '#eccd43')
        self.assertEqual(palette[returnIterationCount(complex(0.4937499999999999, -0.234375),paletteLength(1))], '#d9e758')
        self.assertEqual(palette[returnIterationCount(complex(0.3374999999999999, 0.546875),paletteLength(1))], '#e1cbbd')

    def test_pixelsWrittenSoFarMandalbrot(self):
        self.assertEqual(pixelsWrittenSoFar(7, 7), 49)  	         	  
        self.assertEqual(pixelsWrittenSoFar(257, 321), 82497)  	         	  
        self.assertEqual(pixelsWrittenSoFar(256, 256), 65536)  	         	  
        self.assertEqual(pixelsWrittenSoFar(100, 100), 10000)  	         	  
        self.assertEqual(pixelsWrittenSoFar(640, 480), 307200)  	         	  

    def test_palleteLength(self):  	         	  
        self.assertEqual(111, paletteLength(1))


if __name__ == '__main__':  	         	  
    unittest.main()  	         	  
