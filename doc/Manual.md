# Fractal Visualizer User Manual

This program will draw a fractal image based on the .frac file it is given. You run this from the command line using 
`$ python src/main.py <filename.frac>`.

The program has the fractal types of Mandelbrot, Julia, and Mandelbrot3 implemented. Any .frac file for these three
fractals can be used by the program.
You can select between two color palettes given as the last argument, those palettes are, "paletteOne" or "paletteTwo".

Once started your fractal will be drawn, show the time it took to draw will be 
displayed in the terminal, and a .png file will be created with the image in the src file. You can then exit the
program by closing the canvas window that the image was drawn on. To draw another fractal you will need to run
the program from the command line with another .frac file.

If no .frac file is given will draw a default fractal for you.
