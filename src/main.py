#!/usr/bin/env python3  	         	  

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

import sys  	         	  

<<<<<<< HEAD
from FractalInformation import FRACTALS
from ImagePainter import paint
=======
def menu():
    # quit when too many arguments are given
    if len(sys.argv) < 2:
        print("Please provide the name of a fractal as an argument")
        validImages()
        sys.exit(1)

    # quite when one of the arguments isn't in the command line
    elif sys.argv[1] not in JULIAS + MBROTS:
        print(f"ERROR: {sys.argv[1]} is not a valid fractal")
        print("Please choose one of the following:")
        validImages()
        sys.exit(1)

    # Otherwise, quit with an error message to help the user learn how to run it
    else:
        paint(images, sys.argv[1], whichList(sys.argv[1]))
>>>>>>> 380c7b338eb557fd57d897f72026f57d9e69ed74


# quit when too many arguments are given  	         	  
if len(sys.argv) < 2:  	         	  
    print("Please provide the name of a fractal as an argument")  	         	  
    for i in FRACTALS:
        print(f"\t{i}")  	         	  
    sys.exit(1)  	         	  

# quite when one of the arguments isn't in the command line  	         	  
elif sys.argv[1] not in FRACTALS:
    print(f"ERROR: {sys.argv[1]} is not a valid fractal")  	         	  
    print("Please choose one of the following:")  	         	  
    for i in FRACTALS:  	         	  
        print(f"\t{i}")  	         	  
    sys.exit(1)  	         	  

# Otherwise, quit with an error message to help the user learn how to run it  	         	  
else:  	         	  
    paint(FRACTALS[sys.argv[1]], sys.argv[1])
