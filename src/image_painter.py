from tkinter import Tk, Canvas, PhotoImage, mainloop
import mandelbrot, julia, palette, sys, time




def paint(fractalDict, userInput, choice):
    """Paint a Fractal image into the TKinter PhotoImage canvas.  	         	  
    This code creates an image which is 640x640 pixels in size."""

    screenSize = 512
    window = Tk()
    img = PhotoImage(width=screenSize, height=screenSize)
    fractalStartingPoint = fractalDict[userInput]
    start = time.time()

    # Figure out how the boundaries of the PhotoImage relate to coordinates on
    # the imaginary plane.
    minx = fractalStartingPoint['centerX'] - (fractalStartingPoint['axisLen'] / 2.0)
    miny = fractalStartingPoint['centerY'] - (fractalStartingPoint['axisLen'] / 2.0)
    maxx = fractalStartingPoint['centerX'] + (fractalStartingPoint['axisLen'] / 2.0)

    # Display the image on the screen
    canvas = Canvas(window, width=screenSize, height=screenSize, bg='#000000')
    canvas.pack()
    canvas.create_image((screenSize/2, screenSize/2), image=img, state="normal")

    # At this scale, how much length and height on the imaginary plane does one
    # pixel take?
    pixelsize = abs(maxx - minx) / screenSize

    if choice == 0:
        mathFunction = julia.returnIterationCount
    else:
        mathFunction = mandelbrot.returnIterationCount

    for row in range(screenSize, 0, -1):
        for col in range(screenSize):
            x = minx + col * pixelsize
            y = miny + row * pixelsize
            color = mathFunction(complex(x, y), palette.paletteLength(choice))
            currentPalette = palette.paletteSelector(choice)
            img.put(currentPalette[color], (col, screenSize - row))
        window.update()  # display a row of pixels

    stop = time.time()
    print(f"Done in {stop - start:.3f} seconds!", file=sys.stderr)
    img.write(f"{userInput}.png")
    print(f"Wrote image {userInput}.png")
    print("Close the image window to exit the program")
    mainloop()


