


def returnIterationCount(complexNumber, paletteLength):
    """Return the index of the color of the current pixel within the Julia set  	         	  
    in the palette array"""

    z = complexNumber
    # c is the Julia Constant; varying this value can yield interesting images
    c = complex(-1.0, 0.0)

    # Here 76 refers to the number of colors in the palette
    for i in range(paletteLength):
        z = z * z + c  # Iteratively compute z1, z2, z3 ...
        if abs(z) > 2:
            return i  # The sequence is unbounded
    return paletteLength - 1         # Else this is a bounded sequence
