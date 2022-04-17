from tkinter import Tk, Canvas, PhotoImage, mainloop
import time
import sys, FractalParser, PaletteFactory, FractalFactory




class ImagePainter:
    def __init__(self, FractalFactory, PaletteFactory, FractalParser):
        self.FractalParser = FractalParser
        self.PaletteFactory = PaletteFactory
        self.FractalFactory = FractalFactory



    def paint(self, dictionary):
        """Paint a Fractal image into the TKinter PhotoImage canvas.
        This code creates an image."""

        SIZE = dictionary["pixels"]

        # Set up the GUI so that we can paint the fractal image on the screen
        before = time.time()
        window = Tk()
        img = PhotoImage(width=SIZE, height=SIZE)


        # Display the image on the screen
        canvas = Canvas(window, width=SIZE, height=SIZE, bg='#000000')
        canvas.pack()
        canvas.create_image((SIZE / 2, SIZE / 2), image=img, state="normal")

        for row in range(SIZE, 0, -1):
            for col in range(SIZE):
                x = dictionary["min"]["x"] + col * pixelsize
                y = dictionary["min"]["y"] + row * pixelsize
                c = self.FractalParser.Fractal.count(complex(x, y), dictionary["iterations"])
                img.put(self.PaletteFactory.Palette.getColor(c), (col, SIZE - row))
            window.update()  # display a row of pixels

        # Save the image as a PNG
        imagename = dictionary["imagename"]
        after = time.time()
        print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)
        img.write(f"{imagename}.png")
        print(f"Wrote image {imagename}.png")

        # Call tkinter.mainloop so the GUI remains open
        print("Close the image window to exit the program")
        mainloop()
