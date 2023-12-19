# Fractal Generator 

Using Factory (OOP) design practices this program will generate a fractal based on a given .frac file like the one below.

![5](https://user-images.githubusercontent.com/75790311/170794220-9d4d42e7-5328-48af-9a39-73cb23d63fde.PNG)

It can handle type Julia, Mandelbrot and Mandelbrot<sup>3</sup> fractals. There are also two color palletes to choose from, "paletteOne" and "paletteTwo". Once given the file the program will open a canvas window and draw the image if available; as well as save a .png file with the image in the images folder.

If no file is provided a default Mandelbrot file will be drawn and saved in the images folder. Any .frac file with the required information as shown above can be used. Also implementing different fractal types has been made as easy as adding a new class to the Fractal.py file with the correct math for the fractal that you are adding.

## Running
- Make sure you are starting in the src folder
- The run `python main.py <filename>(optional) <color pallete>(optional)`


