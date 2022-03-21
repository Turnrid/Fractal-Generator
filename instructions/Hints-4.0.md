# CS 1440 Assignment 4.0 Hints

## Students' advice from last semester

*   One thing that was helpful was renaming the variables to be more understandable. It was useful to do this from the beginning so I could understand the program better.
*   Planning helped so incredibly much, even though I should have done more. The time I spent thinking about what to do saved me from taking twice as much time to figure out the same thing while implementing.
*   Just take it slow, it really isn't that hard its just overwhelming. Go slow, start by finding the smells, then go smell by smell and fix it.
*   I initially just went right to work fixing all the things I saw wrong, but it would've been easier to start from the big picture. How does the data flow? What do the dependencies look like? Once I started looking at the code from the zoomed-out perspective, I was able to fix the big picture, then move to the smaller stuff.
*   I didn't read the instructions thoroughly before starting. I remember reading or hearing that we had a lot of leeway with this assignment, so I guess I assumed that the instructions were simply to refactor it. So after I'd spent hours on what I thought was a good way of doing it, I reread the instructions and realized that I was way off the mark.
*   I would stress to try and keep things simple. When you get confused or frustrated, take a break from it. This seemed to help me on this one, but I use these tips with everything.
*   I do not understand how fractals work, but that is kind of the point of the program. Still, it made it difficult but I liked that.
*   Start early, use Git lots, and utilize the tutor lab! Using git was really helpful to make sure I was saving my work when it was good and allowing me to go back when it was bad. 
*   The in-class demonstrations and explanations on refactoring were absolutely necessary in my understanding what this assignment was and what I needed to do. 
*   Before refactoring the modules, I standardized the language of the mbrot and julia. This helped when I combined and shifted things around and made it much easier when I started doing the big chunk of the work.
*   Keep track of what you want each module to do, and how it will do it. If you can keep that straight in your head, you'll be alright.
*   Make sure you understand the existing code before you try to refactor it.
*   I did not spend enough time on the initial plan or how the classes would work together. I unfortunately fell into the trap of thinking that since the code was already written, it would not need as detailed a plan. 
*   Made an initial pass over the program to make all the non-structural changes (variable names, magic numbers) to make it easier to read. I ended up doing the structural parts in several rounds as each round made it easier to see how the program could improve.
*   Having a working program made it easy to figure out how the program should work.  Always strive to keep the program in a working state.  It's okay to break it for a little while as you clean up the code smells, but make sure it's working before moving on to the next smell.
*   Skim the program to get a cursory understanding of it's function, then read it through this time on paper or in your plan break it apart into all its separate functions. Doing this will help you break it into modules later and will make the whole program more digestible.





## Erik's Hints

### Documenting and Fixing Code Smells

*   The [GitLab Markdown Guide](https://gitlab.cs.usu.edu/help/user/markdown.md)
    will help you write an easy-to-read software development plan.
*   You will save time by documenting code smells up-front instead of
    documenting them as you fix them.  This is especially helpful as you
    identify duplicate code between the two starter programs.
*   It may take multiple passes to whip the starter programs into shape


### Remove Dead Code

*   When you find variables that are unused by a function, remove them
*   When you find lines of code that have no effect, remove them
*   Assignments to variables  _after_  they are read for the last time are unnecessary
*   Code positioned after a return statement will never be reached, and can be deleted
*   Function parameters which are unused in the body of a function can be deleted
*   Functions which are never called and have no clear purpose can be deleted


### Simplify Confusing Constructs

*   Remove or update comments which are no longer accurate or relevant
*   Replace hard-coded  _magic numbers_  with well-named variables
*   Rename carelessly-named variables so that the code is self-documenting
*   Observe how data flows throughout the program and rewrite functions such that global variables are no longer necessary


### Use An Appropriate Data Structure

*   The starter code uses a dictionary of dictionaries in a way that (shockingly) makes pretty good sense.
*   You should retain this structure in your refactored program.
*   Resist the urge to increase the level of nesting in this structure.
*   You can add new key/value pairs to the inner dictionaries to keep track of which type of fractal they represent.


### Enforce the Single Responsibility Principle

*   Each function should deal with as few concepts as possible
*   Identify functions which have many different responsibilities and separate
    them into smaller pieces which are focused on one task
*   Unite functionality into one function where it makes sense to do so
*   Extract the mainline driver code from both prototype programs and unify
    into a single driver called  `main.py`
*   The iteration count functions which define the fractals should not be
    concerned about which color a particular pixel will be; that combines two
    different responsibilities in a way that is not helpful. Simply return the
    count of iterations reached before the algorithm decided whether that a
    point in or out of the set.
*   Begin by identifying the inputs and outputs of each function
*   Just because a function has the word **color** in its name doesn't mean
    that it should be dealing with colors at all
*   The signature of functions aren't set in stone.  If it makes sense to you
    to change it, go for it.
*   Reduce the number of `import` statements in each module to the minimum
    absolutely required to not crash.  For example, all image creation and
    display operations should take place in  `ImagePainter.py`.  Therefore,
    there is no need for `main.py` to import any identifiers from the `Tk`
    package.


### Good Code Organization

*   Isolate the relevant fractal iteration count function from each starter
    program and place them each into their own module.
*   The driver program will choose which fractal function to run based upon the
    name of a configuration dictionary presented at the command-line.
*   A good driver program is brief. It will read like a table of contents,
    giving a brief summary of the key responsibilities of the program.
*   While the Mandelbrot and Julia functions are *very* similar, for
    organizational purposes they should be kept in separate files.  The reason
    will become clear next sprint.


### Testing and Reverting Mistakes

*   Use git to your advantage while refactoring
    *   Make frequent, small commits
    *   Test your changes before making a commit
    *   Discard your changes when you make a mistake
*   A thorough test involves running unit tests *and* integration tests
*   These programs create PNG images as a side-effect.  Make copies of these
    images when you know the program works correctly.  Compare your program's
    output to these specimens.


### Refactoring Complicated Code

*   Always remember that the point of this assignment is to learn how to
    refactor a program even if you don't entirely understand it.
*   Do not worry if you do not understand how the fractal images are generated
    or why the fractal functions work.  You do not need to deeply understand
    how the pixel coloring algorithm works in order to refactor it.
    *   You can recognize smelly code even when you don't fully grasp what the
        code is doing.  In fact, you may be better able to recognize
        problematic code when you aren't focused on how it works.
    *   Much of the work of refactoring is concerned with the structure and
        appearance of code.  With a thorough testing regimen it is possible to
        rewrite a block of code in such a way that its original functionality
        is preserved without truly understanding it.
*   You may assume that the algorithms work correctly.  If there are bugs, it
    is not your responsibility to fix them.  That would be an enhancement, and
    refactoring is about *preserving* existing functionality.


### Understanding the fractal algorithms

*   If you are *really* dying to know more about how the Mandelbrot set works,
    an image of the Mandelbrot set produced by this program is a visualization
    of the complex plane, formed by relating complex numbers to Cartesian
    coordinates:
    *   The coordinates of pixels in the `PhotoImage` object are pairs of X, Y
        coordinates.  The origin of the `PhotoImage` object `(0, 0)` is the
        upper-left corner of the image window.
    *   Complex numbers are ordered pairs of Real and Imaginary components.
    *   The `X` axis of the Mandelbrot set represents the *real* number line.
    *   The `Y` axis of the Mandelbrot set represents the *imaginary* number
        line.
    *   The function that draws the image (`paint()` in `src/mandelbrot.py` and
        `makePicture()` in `src/julia.py`) converts the `(X, Y)` coordinates of
        the `PhotoImage` into a complex number.  This complex number is called
        `C` in the Mandelbrot algorithm and `Z` in the Julia algorithm.
    *   The image drawing function chooses the color to paint a pixel by
        counting the number of times the fractal function can be *iterated*
        before its output exceeds a threshold.
    *   *Iteration* in this context means to use the output of a function as
        its input value again and again to find out if the function tends
        toward infinity.
*   The Mandelbrot function is fascinating because *sometimes* iteration makes
    it go off to infinity and *sometimes* it does not.
    *   The points *inside* the cardioid are the points *within* the Mandelbrot
        set.  These are the coordinates on the imaginary plane corresponding to
        `Z` values that stay small after repeated iterations of the Mandelbrot
        function.
    *   Points *outside* of the cardioid shoot off to infinity under iteration.
    *   Points at the boundary are where all of the pretty and interesting
        pictures occur.
*   Study and experiment with the demo program `../demo/interactive.py`.  While
    it isn't much prettier than the starter code, it can help you grasp how the
    algorithm works.
*   The Julia algorithm is just the Mandelbrot algorithm with a twist.
    * [UsefulJS] (http://usefuljs.net/fractals/docs/julia_mandelbrot.html) has
      a nice explanation of how the Mandelbrot set works and how the Julia set
      is related to it.


### Further exploration

* You can find ideas for new fractal configurations by exploring the Mandelbrot
  and Julia sets online.  You can also compare your program's output with other
  Mandelbrot and Julia set visualizers to make sure that you haven't made any
  serious mistakes.
    * https://atopon.org/mandel/
    * https://sciencedemos.org.uk/mandelbrot.php (note: this program produces
      images which are upside down relative to our program)
    * http://bl.ocks.org/syntagmatic/3736720
    * http://usefuljs.net/fractals/
    * Most of these websites define their images in `(minX, minY), (maxX,
      maxY)` coordinates, while our program uses the `(centerX, centerY) +
      axisLength` scheme.  It is helpful to write a small helper program which
      converts between the coordinate formats.


### Other fun links

*   [FractInt](https://www.fractint.org/): A classic MS-DOS program (which is
    *still* under development!) whose users have made interesting discoveries
    within the Mandelbrot set and other related fractals over the years
*   [GNU XaoS](http://matek.hu/xaos/doku.php): A free and open source fractal
    explorer for Linux, Windows and Mac
*   [Eyecandy](http://eyecandyarchive.com/): Turn your computer into an
    expensive lava lamp.  Contains links to other programs you can use to
    explore fractals and other interesting patterns of pixels.
