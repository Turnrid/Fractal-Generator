def count(c, max_iter):
    """Return the iteration count of the Mandelbrot set at this point in the complex plane"""
    z = complex(0, 0)  # z0  	         	  

    for i in range(max_iter - 1):  	         	  
        z = z * z + c  # Get z1, z2, ...  	         	  
        if abs(z) > 2.0:
            return i  # The sequence is unbounded  	         	  

    return max_iter - 1
