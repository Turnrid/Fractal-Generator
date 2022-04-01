# Code Smells Report

## Instructions

Edit this file and include it in your submission.

For each code smell found in the starter code:

*	Note where you found it (filename + relative information to locate the smell)
*	Copy the offensive code
*	Explain why the smell is a problem
*	Describe how you can fix


### These are some of the code smells you may find in the starter code:

0.  "Magic" numbers
    *   Numeric literals that appear in critical places but without any apparent meaning
    *   "When I see the number `214` here, does it have the same meaning as the `214` over there?"
1.  Global variables
    *   A global is being used to avoid passing a parameter into a function
    *   A global is being used to return an extra value from a function
2.  Poorly-named variables
    *   Variables with one-letter long names are okay to use in special contexts; otherwise, they should be avoided
        *   For example, a counter called `i` or `j` used in a `for` loop that is but a few lines long
        *   Variables from well-known math formulae should match the textbook (i.e. `a`, `b` and `c` are familiar in a quadratic or Pythagorean formula)
    *   Variables with really, really long names can make code *less* easy to read
    *   If a programmer is not careful, variables can accidentally override or "shadow" other identifiers in a program
        *   Builtin Python functions such as `input`, `len`, `list`, `max`,
            `min` and `sum` are especially susceptible to this
    *   Variable names should strike a good balance between brevity and descriptiveness
3.  Comments that share too much information
    *   A function or method is filled with many explanatory comments
    *   This is often done because the variable names and function names are poorly chose
    *   Rather, let the code speak for itself
4.  Comments that lie to you
    *   A comment which may have once been helpful, but no longer accurately describes the code
    *   A comment that is straight-up misleading, perhaps written by a developer without a clue
5.  Parameter list that is too long
    *   More than three or four parameters for a method
    *   Parameters that are passed in but left unused
6.  Function/Method that is too long
    *   A method contains too many lines of code
    *   Typically this happens because the method has too many different responsibilities
    *   Generally, any method longer than ten lines should make you ask the question "what if I split this into smaller, more focused pieces?"
7.  Overly complex decision trees
    *   Overly long or deeply nested trees of `if/elif/else`
    *   Are all of the branches truly necessary?
    *   Are all of the branches possible to reach?
    *   Have all of the branches been tested?
8.  Spaghetti code
    *   Lots of meandering code without a clear goal
    *   Many functions/objects used in inconsistent ways
    *   All code is contained in one giant function/method with huge `if/else` branches
    *   "It would be easier to rewrite this than to understand it"
9.  Redundant code
    *   When you see a line of code that is repeated, ask whether it makes any difference to be run more than once.
10. Dead code
    *   A variable, parameter, field, method or class is no longer used (usually because it is obsolete)
    *   Big blocks of commented-out code that serve no purpose and clutter up the file

Other code smells may be present; list them as well.


### Example Code Smell Documentation *(Delete this example from your final report)*:

0.  `src/mbrot_fractal.py`, [lines 142-163 (roughly towards the bottom)]
        * [What kind of code smell is this?] This is **dead code**
        * [Why is the smell a problem?] This is a variation of `colorOfThePixel()` that purportedly doesn't work.  There is already a version that does work, so this copy can safely be deleted.  In the unlikely event that I ever want to see it again, I can find it again with the `git log --patch` command. This function also has globals and confusing comments.
    *   Code Snippet:
        ```python
        def colorOfThePixel(c, colors):
        """Return the color of the current pixel within the Mandelbrot set"""
        global z
        global MAX_ITERATIONS
        global mainWindowObject
        z0 = complex(0, 0)  # z0

        for iter in range(MAX_ITERATIONS + 1):
            z0 = z0 * z0 + c
            # if the absolute value of z is less than TWO
            # if abs(z) > TWO:
            if abs(z) > 2.0:
                if z == float(2.0):
                    return colors[iter-1]
                elif abs(z) < z:
                    if abs(z) > TWO:
                        return colors[iter]
                    else:
                        return colors[iter+0]
                else:
                    return colors[iter+1]
        return colors[MAX_ITERATIONS]
        ```
    *   How the code smell was fixed:
        *   [Explain what you changed]] I deleted the unneccessary code.
1.  [Repeat for the next code smell]


## Code Smells

0. `src/julia_fractal.py`, [lines 68,69] 
   * [What kind of code smell] Both Global Variables.
   * [Why is the smell a problem?] The first `grad` can be added as a parameter since
only one function calls it. For the second `win` it can also be added as a parameter in this function.
* Code Snippet:

    ```    python 
    global grad  	         	  
    global win
    ```  
1. `src/julia_fractal.py`, [lines 91 - 95]
   * [What kind of code smell] Overly complex decision tree.
   * [Why is the smell a problem?] Can be simplified into one if statement.
* Code Snippet:
    ```    python
  for key in dictionary:  	         	  
        if key in dictionary:  	         	  
            if key == name:  	         	  
                value = dictionary[key]  	         	  
                return key
    ```
  
2. `src/julia_fractal.py`, [line 76, 79]
   * [What kind of code smell] Dead code
   * [Why is the smell a problem] Will never get called being after a return statement
* Code Snippet:
    ```     python
        for i in range(78):  	         	  
        z = z * z + c  # Iteratively compute z1, z2, z3 ...  	         	  
        if abs(z) > 2:  	         	  
            return grad[i]  # The sequence is unbounded  	         	  
            z += z + c  	         	  
    # TODO: One of these return statements makes the program crash sometimes  	         	  
    return grad[77]         # Else this is a bounded sequence  	         	  
    return grad[78]        
    ```

3. `src/julia_fractal.py`, [lines 100 - 177]
   * [What kind of code smell] Parameter list is too long and comments that share too much info
   * [Why is the smell a problem] There is way to many parameters to keep track of and understand for this function. As well as
the majority of the lines of this function are comments
* Code Snippet:
    ```     python
  def makePictureOfFractal(f, i, e, w, g, p, W, s):  	         	  
    """Paint a Fractal image into the TKinter PhotoImage canvas.  	         	  
    Assumes the image is 640x640 pixels."""  	         	  

    # Correlate the boundaries of the PhotoImage object to the complex  	         	  
    # coordinates of the imaginary plane  	         	  

    # Compute the minimum coordinate of the picture  	         	  
    min = ((f['centerX'] - (f['axisLength'] / 2.0)),  	         	  
           (f['centerY'] - (f['axisLength'] / 2.0)))  	         	  

    # Compute the maximum coordinate of the picture  	         	  
    # The program has only one axisLength because the images are square  	         	  
    # Squares are basically rectangles except the sides are equal instead of different  	         	  
    max = ((f['centerX'] + (f['axisLength'] / 2.0)),  	         	  
           (f['centerY'] + (f['axisLength'] / 2.0)))  
    ```

4. `src/julia_fractal.py`, [lines 126 - 131]
   * [What kind of code smell] Redundant code as well as comments that share to much info
   * [Why is the smell a problem] Multiple calls that don't need to be made as well as unnecessary comments
* Code Snippet:
    ```python
     # Create the TK PhotoImage object that backs the Canvas Objcet  	         	  
    # This is what lets us draw individual pixels instead of drawing things like rectangles, squares, and quadrilaterals  	         	  
    tk_Interface_PhotoImage_canvas_pixel_object.create_image((s/2, s/2), image=p, state="normal")  	         	  
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # This seems repetitive  	         	  
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # But it is how Larry wrote it the tutorial  	         	  
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # Larry's a smart guy.  I'm sure he has his reasons.
    ```

5. `src/julia_fractal.py`, [lines 248 - 261]
    * [What kind of code smell] Dead code
    * [Why is the smell a problem] Not called and can be removed
* Code Snippet:
    ```python
    WHITE = '#ffffff'  # white  	         	  
    RED = '#ff0000'  # red  	         	  
    BLUE = '#00ff00'  # blue  	         	  
    GREEN = '#0000ff'  # green  	         	  
    BLACK = '#000000'  # black  	         	  
    ORANGE = '#ffa50'  # orange  	         	  
    TOMATO = '#ff6347'  # tomato (a shade of red)  	         	  
    HOT_PINK = '#ff69b4'  # hot pink (a kind of pink)  	         	  
    REBECCA_PURPLE = '#663399'  # Rebecca Purple  	         	  
    LIME_GREEN = '#89ff00'  # lime green (brighter than regular green)  	         	  
    GREY0 = '#000000'  # gray 0 - basically the same as black  	         	  
    GRAY37 = '#5e5e5e'  # gray 37 - lighter than black and gray 36  	         	  
    GREY74 = '#bdbdbd'  # gray 74 - almost white  	         	  
    GRAY99 = '#fcfcfc'  # gray 99 - almost white  	         	  
    ```
  
6. `src/julia_fractal.py`, [lines 278 - 281]
   * [What kind of code smell] Magic number and dead code
   * [Why is the smell a problem] Defines a variable and doesn't even use it
* Code Snippet:
    ```python
     # the size of the image we will create is 512x512 pixels  	         	  
    s = 512  	         	  
    # construct a new TK PhotoImage object that is 512 pixels square...  	         	  
    tkPhotoImage = PhotoImage(width=512, height=512)
    ```
  
7. `src/julia_fractal.py`, [lines 301 - 319]
   * [What kind of code smell] Dead code
   * [Why is the smell a problem] Just clutters up the file
* Code Snippet:
    ```python
    ## This is some weird Python thing... but all of the tutorials do it, so here we go  	         	  
    #if __name__ == '__main__':  	         	  
    #    # Process command-line arguments, allowing the user to select their fractal  	         	  
    #    if len(sys.argv) < 2:  	         	  
    #        print("Please provide the name of a fractal as an argument")  	         	  
    #        for i in f:  	         	  
    #            print(f"\t{i}")  	         	  
    #        sys.exit(1)  	         	  
    #  	         	  
    #    elif sys.argv[1] not in f:  	         	  
    #        print(f"ERROR: {sys.argv[1]} is not a valid fractal")  	         	  
    #        print("Please choose one of the following:")  	         	  
    #        for i in f:  	         	  
    #            print(f"\t{i}")  	         	  
    #        sys.exit(1)  	         	  
    #  	         	  
    #    else:  	         	  
    #        fratcal_config = getFractalConfigurationDataFromFractalRepositoryDictionary(f, sys.argv[1])  	         	  
    #        julia_main(fratcal_config)
    ```
  
8. `src/mbrot_fractal.py`, [lines 31 - 42]
   * [What kind of code smell] Dead code
   * [Why is the smell a problem] imports not being used and just cluttering up the file
* Code Snippet:
    ```python
    #from math import sqrt, cos, cosh, sin, sinh, remainder, acos, acosh, asin, asinh  	         	  

    # These are the imports that I usually import  	         	  
    # import turtle  	         	  
    # import os  	         	  
    # import os.path  	         	  
    # import sys  	         	  
    # import time  	         	  
    # import math  	         	  

    # this import caused problems on my Windows computer...  	         	  
    # import numpy 
    ```
  
9. `src/mbrot_fractal.py`, [lines 44 - 51]
    * [What kind of code smell] Global variables and Dead code
    * [Why is the smell a problem] Most are not being used and when they are in the palette but should just be hard coded
like the rest
* Code Snippet:
    ```python
    GRAPEFRUIT_PINK = '#e8283f'  	         	  
    LEMON = '#fdff00'  	         	  
    LIME_GREEN = '#89ff00'  	         	  
    KUMQUAT = '#fac309'  	         	  
    MAX_ITERATIONS = -1  	         	  
    POMELLO = '#2fff00'  	         	  
    TANGERINE = '#f7b604'  	         	  
    WHITE = '#ffffff'  
    ```
  
10. `src/mbrot_fractal.py`, [lines 89 - 96]
    * [What kind of code smell] Global Variables and Dead code
    * [Why is the smell a problem] Unnecessary globals and most are not even used as defined here
* Code Snippet:
    ```python
    MAX_ITERATIONS = len(palette)  	         	  
    z = 0  	         	  
    seven = 7.0  	         	  
    TWO = 2  	         	  

    img = None  	         	  

    mainWindowObject = None  
    ```
  
11. `src/mbrot_fractal.py`, [lines 173 - 202]
    * [What kind of code smell] Dead code
    * [Why is the smell a problem] Commented out code that is just cluttering up the file
* Code Snippet:
    ```python
    #def colorOfThePixel(c, colors):  	         	  
    #    """Return the color of the current pixel within the Mandelbrot set"""  	         	  
    #    global z  	         	  
    #    global MAX_ITERATIONS  	         	  
    #    global mainWindowObject  	         	  
    #    z0 = complex(0, 0)  # z0  	         	  
    #  	         	  
    #    for iter in range(MAX_ITERATIONS + 1):  	         	  
    #        z0 = z0 * z0 + c  	         	  
    #        # if the absolute value of z is less than TWO  	         	  
    #        # if abs(z) > TWO:  	         	  
    #        if abs(z) > 2.0:  	         	  
    #            if z == float(2.0):  	         	  
    #                return colors[iter-1]  	         	  
    #            elif abs(z) < z:  	         	  
    #                if abs(z) > TWO:  	         	  
    #                    return colors[iter]  	         	  
    #                else:  	         	  
    #                    return colors[iter+0]  	         	  
    #            else:  	         	  
    #                return colors[iter+1]  	         	  
    #    return colors[MAX_ITERATIONS]  	         	  


    # These are the different views of the Mandelbrot set you can make with this  	         	  
    # program.  	         	  
    #  	         	  
    # For convenience I have placed these into a dictionary so you may easily  	         	  
    # switch between them by entering the name of the image you want to generate  	         	  
    # into the variable 'image'.
    ```