from colour import Color


class Palette:
    def __init__(self, iterations):
        self.iterations = iterations

    def getColor(self, number):
        raise NotImplementedError("Concrete subclass of Palette must implement getColor() method")


class paletteOne(Palette):

    def __init__(self, iterations):
        super().__init__(iterations)

        red = Color("red")
        green = Color("green")
        blue = Color("blue")
        yellow = Color("yellow")
        cyan = Color("cyan")
        magenta = Color("magenta")
        black = Color("black")

        numberForEachColor = self.iterations // 11

        really_long = [c.hex_l for c in red.range_to(black, numberForEachColor)]
        really_long += [c.hex_l for c in black.range_to(green, numberForEachColor + 1)][1:]
        really_long += [c.hex_l for c in green.range_to(black, numberForEachColor + 1)][1:]
        really_long += [c.hex_l for c in black.range_to(blue, numberForEachColor + 1)][1:]
        really_long += [c.hex_l for c in blue.range_to(black, numberForEachColor + 1)][1:]
        really_long += [c.hex_l for c in black.range_to(yellow, numberForEachColor + 1)][1:]
        really_long += [c.hex_l for c in yellow.range_to(black, numberForEachColor + 1)][1:]
        really_long += [c.hex_l for c in black.range_to(cyan, numberForEachColor + 1)][1:]
        really_long += [c.hex_l for c in cyan.range_to(black, numberForEachColor + 1)][1:]
        really_long += [c.hex_l for c in black.range_to(magenta, numberForEachColor + 1)][1:]
        really_long += [c.hex_l for c in magenta.range_to(black, self.iterations - (numberForEachColor * 10) + 1)][1:]

        self.palette = really_long

    def getColor(self, number):
        return self.palette[number]


class paletteTwo(Palette):

    def __init__(self, iterations):
        super().__init__(iterations)

        white = Color("white")
        orange = Color("orange")
        brown = Color("brown")
        yellow = Color("yellow")
        black = Color("black")

        numberForEachColor = int(self.iterations / 7)

        really_long = [c.hex_l for c in white.range_to(black, numberForEachColor)]
        really_long += [c.hex_l for c in black.range_to(orange, numberForEachColor + 1)][1:]
        really_long += [c.hex_l for c in orange.range_to(black, numberForEachColor + 1)][1:]
        really_long += [c.hex_l for c in black.range_to(brown, numberForEachColor + 1)][1:]
        really_long += [c.hex_l for c in brown.range_to(black, numberForEachColor + 1)][1:]
        really_long += [c.hex_l for c in black.range_to(yellow, numberForEachColor + 1)][1:]
        really_long += [c.hex_l for c in yellow.range_to(black, self.iterations - (numberForEachColor * 6) + 1)][1:]

        self.palette = really_long

    def getColor(self, number):
        return self.palette[number]
