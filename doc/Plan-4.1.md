# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**

An easily expandable program that can take in files with specific information to draw a fractal based on that 
information. 


## Phase 1: System Analysis *(10%)*

**Deliver:**

* .frac files that will be turned into a dictionary. Then sent and made into a fractal object that depending on the type 
will then use specific count() functions for that type of fractal, and finally drawn into a .png file.

## Phase 2: Design *(30%)*

**Deliver:**

*   Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain the purpose, inputs and outputs.
*   Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
    *   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occurred to you.


* Fractal Class
  * Count(Type)
    * will raise an error

* Mandelbrot method
  * init(max iteration) 
  * Count(complex number)
    * Will calculate and output the value between 0 - max iteration - 1 based on the mandelbrot equation.

* Julia method
  * init(max iteration) 
  * Count()
    * Will calculate and output the value between 0 - max iteration - 1 based on the julia equation.

* Other fractal method
  * init(max iteration) 
  * Count()
    * Will calculate and output the value between 0 - max iteration - 1 based on the other fractal equation.

* FractalFactory class
  * MakeFractal(dictionary)
    * Take the dictionary from the Fractal Parser and use the Type and max iteration to create the correct fractal
object

* FractalParser
  * Read the file and turn into a dictionary

* Palette
    * getColor()
        * will raise an error

* Palette1
  * getColor(max iterations)
    * Create a palette based off of the number of iterations

* Palette2
  * getColor(max iterations)
    * Create a palette based off of the number of iterations

* PaletteFactory
  * MakePalette(max iterations)
    * Take the dictionary from the Fractal Parser and use the Type and max iteration to create the correct fractal
object

* ImagePainter
  * Takes in the products of FractalFactory, PaletteFactory, and FractalParser
  * Using those products then creates the fractal image
    



## Phase 3: Implementation *(15%)*

**Deliver:**

*   Figuring out how to plug it all together was a bit of a challenge.


## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

Wrote tests for the Parser, Palettes and FractalFactory. Found that I needed to compensate for rounding and splicing in 
Palettes, and helped fix error handling in the parser.


## Phase 5: Deployment *(5%)*

**Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 6: Maintenance

**Deliver:**

*   Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   Fill out the Assignment Reflection on Canvas.
