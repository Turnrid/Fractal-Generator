import Palette


def makePalette(dictionary, paletteChoice):
    if paletteChoice == "paletteOne":
        return Palette.paletteOne(int(dictionary["iterations"]))
    if paletteChoice == "paletteTwo":
        return Palette.paletteTwo(int(dictionary["iterations"]))
    else:
        raise NotImplementedError("That Palette is not available currently")
