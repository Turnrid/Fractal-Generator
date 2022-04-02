

def returnIterationCountMandelbrot(complexNum, paletteLength):
    """Return the color of the current pixel within the Mandelbrot set"""
    z = complex(0, 0)  # z0

    for i in range(paletteLength):
        z = z * z + complexNum  # Get z1, z2, ...
        if abs(z) > 2:
            return i  # The sequence is unbounded
    return paletteLength - 1   # Indicate a bounded sequence

def pixelsWrittenSoFar(rows, cols):
    pixels = rows * cols
    print(f"{pixels} pixels have been output so far")
    return pixels
