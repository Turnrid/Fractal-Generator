from tkinter import Tk, Canvas, PhotoImage, mainloop
import time
import sys, FractalParser, PaletteFactory, FractalFactory




class ImagePainter:
    def __init__(self, fractal, palette, dictionary):
        self.fractal = fractal
        self.palette = palette
        self.dictionary = dictionary

        self.SIZE = self.dictionary["pixels"]
        self.pixelsize = self.dictionary["pixelsize"]


    def paint(self):
        """Paint a Fractal image into the TKinter PhotoImage canvas.
        This code creates an image."""


        # Set up the GUI so that we can paint the fractal image on the screen
        before = time.time()
        window = Tk()
        img = PhotoImage(width=self.SIZE, height=self.SIZE)


        # Display the image on the screen
        canvas = Canvas(window, width=self.SIZE, height=self.SIZE, bg='#000000')
        canvas.pack()
        canvas.create_image((self.SIZE / 2, self.SIZE / 2), image=img, state="normal")

        for row in range(self.SIZE, 0, -1):
            for col in range(self.SIZE):
                x = self.dictionary["min"]["x"] + col * self.pixelsize
                y = self.dictionary["min"]["y"] + row * self.pixelsize
                c = self.fractal.count(complex(x, y))
                img.put(self.palette.getColor(c), (col, self.SIZE - row))
            window.update()  # display a row of pixels

        # Save the image as a PNG
        imagename = self.dictionary["imagename"]
        after = time.time()
        print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)
        img.write(f"{imagename}.png")
        print(f"Wrote image {imagename}.png")

        # Call tkinter.mainloop so the GUI remains open
        print("Close the image window to exit the program")
        mainloop()
