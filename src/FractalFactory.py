import Fractal


def makeFractal(dictionary):
    if dictionary["type"] == "mandelbrot":
        return Fractal.Mandelbrot(dictionary["iterations"])
    elif dictionary["type"] == "julia":
        return Fractal.Julia(dictionary["iterations"])
    elif dictionary["type"] == "otherfractal":
        return Fractal.OtherFractal(dictionary["iterations"])
    elif dictionary["type"] == "":
        raise RuntimeError("No type of fractal specified")
    else:
        raise NotImplementedError("That Fractal type is not available currently")
