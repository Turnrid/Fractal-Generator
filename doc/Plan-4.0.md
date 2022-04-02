# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**

We are to refactor the program in such a way to make it easy to add new functionality to the existing program.

A good solution will:

* Separate out the Julia and Mandelbrot calculations into separate modules.
* Will have a module that has the image creating functionality.
* A module with all palette specifications for the fractals.
* A module with the different fractal image specifications
* A module that will access all the above and run the program


## Phase 1: System Analysis *(10%)*

**Deliver:**


The user will input a string that our main module will feed into our Fractal Information module and get the correct
dict that the image painter module will need. The image painter will then start a canvas to be drawn on and based on the
string from main will call the correct fractal module to calculate the correct color that it will pull from the palette 
module. With the data from those two modules the Image Painter will then update the canvas and draw it to the screen.
Once drawn a png file will be created with the image that was drawn.


## Phase 2: Design *(30%)*

**Deliver:**

* main.py
  * menu(string)
    * Menu function that will take the string from the user, and give the string 
    to the image Painter module.
    * Will call the menu function and get the ball rolling.

* fractalInfo.py
  * whichImage(string)
    * Function that will take the string and give back the correct dictionary with the correct values to the 
image painter module.

* image_painter.py
  * Will instantiate a canvas to be drawn on, and grab current time to track how long it takes to draw.
  * paint(dict, string)
    * Will take the dictionary values to get the correct placement of the fractal on the canvas. Will display the 
canvas to the screen and for each pixel grab the correct pixel color from the correct fractal module and in rows draw
to the screen until all pixels have been drawn.
  * Grab the current time and print how long image took to draw
  * createFile(string)
    * With the string create a png file of the image and save in the correct folder

* palette.py
  * whichPalette(string)
    * Will take the string given by the user and determine which list of color values to give to the image painter.

* mandelbrot.py
  * pixelColor(int, list)
    * Will take the complex number and the correct palette list to return the right color value for the current pixel
that the image painter is drawing.

* julia.py
  * pixelColor(int, list)
    * Will take the complex number and the correct palette list to return the right color value for the current pixel
that the image painter is drawing.

========================================================================================================================

* main.py
  * menu(string)
    ```python
    if len(user args) < 2;
        ask user to imput correct argument, list valid arguments and  exit the program
    elif user input isnt a valid argument;
        give error and ask for correct arguments, list valid arguments and exit the program
    elif call image painter with user input;
    ``` 
  * call menu function  

* fractalInfo.py
  * Have two separte dictionaries with the correct data.
  * Have two separte lists with valid string calls.
  * validImages()
    ```python
    for string in list;
        print(string);
    ```
  * whichImage(string)
    ```python
    if key(string) in dict1;
        return dict1.get(key)
    else;
        return dict2.get(key)
    ```

* image_painter.py
  * Will instantiate a canvas to be drawn on, and grab current time to track how long it takes to draw.
  * paint(dict, string)
    * Will take the dictionary values to get the correct placement of the fractal on the canvas. Will display the 
canvas to the screen and for each pixel grab the correct pixel color from the correct fractal module and in rows draw
to the screen until all pixels have been drawn.
  * Grab the current time and print how long image took to draw
  * createFile(string)
    * With the string create a png file of the image and save in the correct folder

* palette.py
  * whichPalette(string)
    * Will take the string given by the user and determine which list of color values to give to the image painter.

* mandelbrot.py
  * pixelColor(int, list)
    * Will take the complex number and the correct palette list to return the right color value for the current pixel
that the image painter is drawing.

* julia.py
  * pixelColor(int, list)
    * Will take the complex number and the correct palette list to return the right color value for the current pixel
that the image painter is drawing.

    
## Phase 3: Implementation *(15%)*

**Deliver:**

* Was alot easier to implment then I thought it would be.
* Satisfying when you can delete all the garbage code.

## Phase 4: Testing & Debugging *(30%)*

**Deliver:**


* Updated built in tests to work for refactoring also added a pixels test for juila too.
* Getting mandelbrot and julia to use the same paint function was a bit of a trick
* Really not sure what else to test other than what I am.

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
