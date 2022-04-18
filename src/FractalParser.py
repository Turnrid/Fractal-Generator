
def FractalParser(fileName=None):
    if not fileName:
        dictionary = {'type': 'mandelbrot',
                      'pixels': 640,
                      'axislength': 4.0,
                      'iterations': 256,
                      'max': {'x': 2.0, 'y': 2.0},
                      'min': {'x': -2.0, 'y': -2.0},
                      'pixelsize': 0.00625,
                      'imagename': 'mandelbrot'}
    else:
        dictionary = convertToDictionary(fileName)

    return dictionary


def convertToDictionary(fileName):
    fractalDic = {}

    file = fileName.split(".")

    if file[-1] == "frac":

        f = open(fileName)
        for line in f.readlines():
            if not line.strip():
                continue
            newLine = line.lower().rstrip().replace(" ", "")
            if "#" in line:
                continue
            else:
                key, value = newLine.split(":")
                fractalDic[key] = value

        checkDictionary(fractalDic)
        file = file[0].split("/")
        maxDic = calculateMax(fractalDic["centerx"], fractalDic["centery"], fractalDic["axislength"])
        minDic = calculateMin(fractalDic["centerx"], fractalDic["centery"], fractalDic["axislength"])
        pixelDic = calculatePixelSize(fractalDic["centerx"], fractalDic["axislength"], fractalDic["pixels"])
        fractalDic["max"] = maxDic
        fractalDic["min"] = minDic
        fractalDic["pixelsize"] = pixelDic
        fractalDic["imagename"] = file[-1]

        del fractalDic["centerx"]
        del fractalDic["centery"]
        f.close()
        return fractalDic


def calculateMin(centerX, centerY, axisLen):
    minx = float(centerX) - (float(axisLen) / 2.0)
    miny = float(centerY) - (float(axisLen) / 2.0)

    minValues = {"x": minx, "y": miny}

    return minValues


def calculateMax(centerX, centerY, axisLen):
    maxx = float(centerX) + (float(axisLen) / 2.0)
    maxy = float(centerY) + (float(axisLen) / 2.0)

    maxValues = {"x": maxx, "y": maxy}
    return maxValues


def calculatePixelSize(centerX, axisLen, pixels):
    maxx = float(centerX) + (float(axisLen) / 2.0)
    minx = float(centerX) - (float(axisLen) / 2.0)
    pixelSize = abs(maxx - minx) / float(pixels)

    return pixelSize


def checkDictionary(dictonary):
    for k in ["centerx", "centery", "axislength"]:
        if k not in dictonary:
            raise RuntimeError(f"The '{k}' parameter is missing")
        else:
            try:
                dictonary[k] = float(dictonary[k])
            except:
                raise RuntimeError(f"The value of the '{k}' parameter is not a number")

    for k in ["pixels", "iterations"]:
        if k not in dictonary:
            raise RuntimeError(f"The '{k}' parameter is missing")
        else:
            try:
                dictonary[k] = int(dictonary[k])
            except:
                raise RuntimeError(f"The value of the '{k}' parameter is not a number")

    if "type" not in dictonary:
        raise RuntimeError("The 'type' parameter is missing")

