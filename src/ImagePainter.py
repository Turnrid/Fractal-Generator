# 5.  `ImagePainter.py`
#     *   Creates a `Tk` window and a `PhotoImage` object
#     *   The `PhotoImage` object stores the pixels of the image
#     *   This module contains code capable of creating a PNG image file

from tkinter import Tk, Canvas, PhotoImage, mainloop  	         	  
import time  	         	  
import sys


import palette
import mandelbrot
import julia


SIZE = 512


def paint(fractal, imagename):  	         	  
    """Paint a Fractal image into the TKinter PhotoImage canvas.  	         	  
    This code creates an image."""  	         	  

    # Set up the GUI so that we can paint the fractal image on the screen  	         	  
    before = time.time()  	         	  
    window = Tk()  	         	  
    img = PhotoImage(width=SIZE, height=SIZE)  	         	  

    # Figure out how the boundaries of the PhotoImage relate to coordinates on  	         	  
    # the imaginary plane.  	         	  
    minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)  	         	  
    maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)  	         	  
    miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)  	         	  
    maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)  	         	  

    # Display the image on the screen
    canvas = Canvas(window, width=SIZE, height=SIZE, bg='#000000')  	         	  
    canvas.pack()  	         	  
    canvas.create_image((SIZE/2, SIZE/2), image=img, state="normal")  	         	  

    # At this scale, how much length and height on the imaginary plane does one  	         	  
    # pixel take?  	         	  
    pixelsize = abs(maxx - minx) / SIZE  	         	  

    if fractal['type'] == 'mandelbrot':
        count = mandelbrot.count
        Palette = palette.MANDELBROT
    else:
        count = julia.count
        Palette = palette.JULIA
    max_iter = len(Palette)

    for row in range(SIZE, 0, -1):  	         	  
        for col in range(SIZE):  	         	  
            x = minx + col * pixelsize  	         	  
            y = miny + row * pixelsize  	         	  
            c = count(complex(x, y), max_iter)  	         	  
            img.put(Palette[c], (col, SIZE - row))
        window.update()  # display a row of pixels  	         	  

    # Save the image as a PNG  	         	  
    after = time.time()  	         	  
    print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)  	         	  
    img.write(f"{imagename}.png")  	         	  
    print(f"Wrote image {imagename}.png")  	         	  

    # Call tkinter.mainloop so the GUI remains open  	         	  
    print("Close the image window to exit the program")  	         	  
    mainloop()  	         	  
