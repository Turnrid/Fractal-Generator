class Fractal:
    def __init__(self, iterations):
        self.iter = iterations

    def count(self, complexNumber):
        raise NotImplementedError("Concrete subclass of Fractal must implement count() method")


class Mandelbrot(Fractal):

    def count(self, c):
        """Return the iteration count of the Mandelbrot set at this point in the complex plane"""
        z = complex(0, 0)  # z0

        for i in range(self.iter - 1):
            z = z * z + c  # Get z1, z2, ...
            if abs(z) > 2.0:
                return i  # The sequence is unbounded

        return self.iter - 1


class Julia(Fractal):

    def count(self, z):
        """Return the iteration count for this part of the Julia fractal Complex Plane"""

        # c is the Julia Constant; varying this value can yield interesting images
        c = complex(-1.0, 0.0)

        for i in range(self.iter - 1):
            z = z * z + c  # Iteratively compute z1, z2, z3 ...
            if abs(z) > 2.0:
                return i

        return self.iter - 1


class OtherFractal(Fractal):

    def count(param, param1):
        return None


