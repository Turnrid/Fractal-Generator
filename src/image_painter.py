from tkinter import Tk, Canvas, PhotoImage, mainloop
import time, mandelbrot, julia, palette




def paint(fractals, userInput, choice):
    """Paint a Fractal image into the TKinter PhotoImage canvas.  	         	  
    This code creates an image which is 640x640 pixels in size."""

    start = time.time()
    window = Tk()
    img = PhotoImage(width=512, height=512)
    fractal = fractals[userInput]

    # Figure out how the boundaries of the PhotoImage relate to coordinates on
    # the imaginary plane.
    minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)
    maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)
    miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)
    maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)

    # Display the image on the screen
    canvas = Canvas(window, width=512, height=512, bg='#000000')
    canvas.pack()
    canvas.create_image((256, 256), image=img, state="normal")

    # At this scale, how much length and height on the imaginary plane does one
    # pixel take?
    pixelsize = abs(maxx - minx) / 512

    if choice == 0:
        color = julia.returnIterationCount(null, null)
    else:
        color = mandelbrot.returnIterationCount(null, null)

    for row in range(512, 0, -1):
        for col in range(512):
            x = minx + col * pixelsize
            y = miny + row * pixelsize
            img.put(color(complex(x, y), palette.paletteLength(choice)), (col, 512 - row))
        window.update()  # display a row of pixels

    stop = time.time()
    print(f"Done in {stop - start:.3f} seconds!", file=sys.stderr)
    img.write(f"{userInput}.png")
    print(f"Wrote image {userInput}.png")

