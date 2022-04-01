


def returnIterationCount(complexNumber):
    """Return the index of the color of the current pixel within the Julia set  	         	  
    in the palette array"""

    z = complexNumber
    # c is the Julia Constant; varying this value can yield interesting images
    c = complex(-1.0, 0.0)

    # Here 76 refers to the number of colors in the palette
    for i in range(78):
        z = z * z + c  # Iteratively compute z1, z2, z3 ...
        if abs(z) > 2:
            return i  # The sequence is unbounded
    return 77        # Else this is a bounded sequence


def getFractalConfigurationDataFromFractalRepositoryDictionary(dictionary, name):
    """Make sure that the fractal configuration data repository dictionary  	         	  
    contains a key by the name of 'name'  	         	  

    When the key 'name' is present in the fractal configuration data repository  	         	  
    dictionary, return its value.  	         	  

    Return False otherwise  	         	  
    """
    for key in dictionary:
        if key in dictionary:
            if key == name:
                value = dictionary[key]
                return key