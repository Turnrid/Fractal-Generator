#!/usr/bin/env python3

import sys
import FractalFactory
import FractalParser
import PaletteFactory
from image_painter import ImagePainter

if len(sys.argv) == 1:
    dictionary = FractalParser.FractalParser()
    imagename = "mandelbrot"
else:
    dictionary = FractalParser.FractalParser(f"../data/{sys.argv[1]}")
    imagename = sys.argv[1].split(".")[0]

fractal = FractalFactory.makeFractal(dictionary)

if len(sys.argv) < 3:
    palette = PaletteFactory.makePalette(dictionary, "paletteOne")
else:
    palette = PaletteFactory.makePalette(dictionary, sys.argv[2])

ImagePainter(fractal, palette, dictionary, imagename).paint()


