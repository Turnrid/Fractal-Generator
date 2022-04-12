def count(z, max_iter):  	         	  
    """Return the iteration count for this part of the Julia fractal Complex Plane"""  	         	  

    # c is the Julia Constant; varying this value can yield interesting images  	         	  
    c = complex(-1.0, 0.0)  	         	  

    for i in range(max_iter - 1):
        z = z * z + c  # Iteratively compute z1, z2, z3 ...  	         	  
        if abs(z) > 2.0:  	         	  
            return i
    return max_iter - 1
