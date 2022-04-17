import sys


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

        #checkDictionary(fractalDic)
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
    if not dictonary["centerx"].isdecimal():
        raise RuntimeError("The value of the 'centerx' parameter is not a number")
    elif dictonary["centerx"] == "":
        raise RuntimeError("The value of the 'centerx' parameter is missing")
    elif "centerx" not in dictonary:
        raise RuntimeError("The required parameter 'centerx' is missing")
    elif not isinstance(dictonary["centery"], float):
        raise RuntimeError("The value of the 'centery' parameter is not a number")
    elif dictonary["centery"] == "":
        raise RuntimeError("The value of the 'centery' parameter is missing")
    elif "centery" not in dictonary:
        raise RuntimeError("The required parameter 'centery' is missing")



print(convertToDictionary(sys.argv[1]))
