from tkinter import Tk, Canvas, PhotoImage, mainloop, TclError
from PIL import Image, ImageDraw
import time
import sys


class ImagePainter:
    def __init__(self, fractal, palette, dictionary, imagename):
        self.fractal = fractal
        self.palette = palette
        self.dictionary = dictionary
        self.imagename = imagename

        self.SIZE = self.dictionary["pixels"]
        self.pixelsize = self.dictionary["pixelsize"]

    def paint(self):
        before = time.time()

        try:
            window = Tk()
            gui_available = True
        except TclError:
            gui_available = False

        if gui_available:
            img = PhotoImage(width=self.SIZE, height=self.SIZE)
            canvas = Canvas(window, width=self.SIZE, height=self.SIZE, bg='#000000')
            canvas.pack()
            canvas.create_image((self.SIZE / 2, self.SIZE / 2), image=img, state="normal")
            self.paint_fractal(img, window)
            img.write(f"../images/{self.imagename}.png")
            print("Close the image window to exit the program")
            mainloop()
        else:
            print("No display available. Generating PNG file directly.")
            img = Image.new('RGB', (self.SIZE, self.SIZE), color='black')
            draw = ImageDraw.Draw(img)  
            self.paint_fractal(draw)
            img.save(f"../images/{self.imagename}.png")

        after = time.time()
        print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)
        print(f"Wrote image {self.imagename}.png")

    def paint_fractal(self, draw, window=None):
        for row in range(self.SIZE):
            for col in range(self.SIZE):
                x = self.dictionary["min"]["x"] + col * self.pixelsize
                y = self.dictionary["min"]["y"] + row * self.pixelsize
                c = self.fractal.count(complex(x, y))
                color = self.palette.getColor(c)

                if window:
                    tkinter_row = row
                    draw.put(color, (col, tkinter_row))
                    if col % 10 == 0:  # Update the GUI window periodically
                        window.update()
                else:
                    draw.point((col, row), fill=color)
