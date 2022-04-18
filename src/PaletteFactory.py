import Palette


def makePalette(dictionary, paletteChoice):
    if paletteChoice == "paletteOne":
        return Palette.paletteOne(int(dictionary["iterations"]))
    elif paletteChoice == "paletteTwo":
        return Palette.paletteTwo(int(dictionary["iterations"]))
    else:
        raise NotImplementedError("That Palette is not available currently")
