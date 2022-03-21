#!/bin/env python3

# Interactive Mandelbrot Set Escape Time Visualizer
#
# This program does not need to be refactored for the assignment.
# It is provided to help you better understand the Mandelbrot fractal.

import sys
from tkinter import Tk, Canvas, PhotoImage, mainloop


PALETTE = [
        '#ffe4b5', '#ffe5b2', '#ffe7ae', '#ffe9ab', '#ffeaa8', '#ffeda4',
        '#ffefa1', '#fff29e', '#fff49a', '#fff797', '#fffb94', '#fffe90',
        '#fcff8d', '#f8ff8a', '#f4ff86', '#f0ff83', '#ebff80', '#e7ff7c',
        '#e2ff79', '#ddff76', '#d7ff72', '#d2ff6f', '#ccff6c', '#c6ff68',
        '#bfff65', '#b9ff62', '#b2ff5e', '#abff5b', '#a4ff58', '#9dff54',
        '#95ff51', '#8dff4e', '#85ff4a', '#7dff47', '#75ff44', '#6cff40',
        '#63ff3d', '#5aff3a', '#51ff36', '#47ff33', '#3eff30', '#34ff2c',
        '#2aff29', '#26ff2c', '#22ff30', '#1fff34', '#1cff38', '#18ff3d',
        '#15ff42', '#11ff47', '#0eff4c', '#0bff51', '#07ff57', '#04ff5d',
        '#01ff63', '#00fc69', '#00f970', '#00f677', '#00f27d', '#00ef83',
        '#00ec89', '#00e88e', '#00e594', '#00e299', '#00de9e', '#00dba3',
        '#00d8a7', '#00d4ab', '#00d1af', '#00ceb3', '#00cab7', '#00c7ba',
        '#00c4be', '#00c0c0', '#00b7bd', '#00adba', '#00a4b6', '#009cb3',
        '#0093b0', '#008bac', '#0082a9', '#007ba6', '#0073a2', '#006b9f',
        '#00649c', '#005d98', '#005695', '#004f92', '#00498e', '#00438b',
        '#003d88', '#003784', '#003181', '#002c7e', '#00277a', '#002277',
        ]

BLACK = '#000000'
SIDE = 640
MAX_ITERATIONS = len(PALETTE)
z = 0


def colorOfThePixel(c, verbose=False):
    """Return the color of the current pixel within the Mandelbrot set"""
    global z
    z = complex(0, 0)  # z0

    global MAX_ITERATIONS
    for i in range(MAX_ITERATIONS):
        z = z * z + c  # Get z1, z2, ...
        if verbose:
            print(f"i={i+1:<6}  C={c:<11.2f}  Z={z:<11.2f}  abs(Z)={abs(z):.5}")
        if abs(z) > 2:
            if verbose:
                print(f"Escaped!  C={c:<11.2f}  Z={z:<11.2f}  abs(Z)={abs(z):.5}\n")
            return i  # The sequence is unbounded
    if verbose:
        print(f"No escape after {MAX_ITERATIONS} iterations, so I quit trying ¯\\_(ツ)_/¯\n")
    return MAX_ITERATIONS - 1   # Indicate a bounded sequence


CELL_SIZE = 20

def paintCell(event):
    col = (event.x // CELL_SIZE) * CELL_SIZE
    row = SIDE - ((event.y // CELL_SIZE) * CELL_SIZE)
    x = minx + col * pixelsize
    y = miny + row * pixelsize
    count = colorOfThePixel(complex(x, y), verbose=True)
    color = PALETTE[count]
    canvas = event.widget
    canvas.create_rectangle(col, SIDE-row, col+CELL_SIZE, SIDE-row+CELL_SIZE, fill=color)
    font_color = 'white' if count > 64 else 'black'
    canvas.create_text(col+(CELL_SIZE/2), SIDE-row+(CELL_SIZE/2), text=str(count+1), fill=font_color) 


def paintEntireImage(event):
    """Paint the entire image"""
    pixelsize = abs(maxx - minx) / SIDE
    for row in range(SIDE, -1, -CELL_SIZE):
        for col in range(SIDE, -1, -CELL_SIZE):
            x = minx + col * pixelsize
            y = miny + row * pixelsize
            count = colorOfThePixel(complex(x, y))
            color = PALETTE[count]
            canvas.create_rectangle(col, SIDE-row, col+CELL_SIZE, SIDE-row+CELL_SIZE, fill=color)
            font_color = 'white' if count > 64 else 'black'
            canvas.create_text(col+(CELL_SIZE/2), SIDE-row+(CELL_SIZE/2), text=str(count+1), fill=font_color) 


def resetImage(event):
    """Reset the image to its initial color"""
    print("Reset the image\n")
    canvas.delete("all")


def usage(event):
    print("""Usage Instructions
==================
Click on the canvas to paint a cell and reveal the iteration count and the
absolute value of Z computed by the escape-time algorithm at each step

Right-click or press [Space] to reveal the entire image
Press [R] to reset the image
Press [Esc] to quit
Press [H] to display this help message
""")

images = {
        'mandelbrot': {
            'centerX': -0.6,
            'centerY': 0.0,
            'axisLen': 2.5,
            },

        'spiral0': {
            'centerX': -0.761335372924805,
            'centerY': 0.0835704803466797,
            'axisLen': 0.004978179931102462,
            },

        'spiral1': {
            'centerX': -0.747,
            'centerY': 0.1075,
            'axisLen': 0.002,
            },

        'seahorse': {
            'centerX': -0.745,
            'centerY': 0.105,
            'axisLen': 0.01,
            },

        'elephants': {
            'centerX':  0.30820836067024604,
            'centerY':  0.030620936230004017,
            'axisLen':  0.03,
            },

        'leaf': {
            'centerX': -1.543577002,
            'centerY': -0.000058690069,
            'axisLen':  0.000051248888,
            },
        }


if len(sys.argv) < 2:
    print("Please provide the name of a fractal as an argument")
    for i in images:
        print(f"\t{i}")
    sys.exit(1)

elif sys.argv[1] not in images:
    print(f"ERROR: {sys.argv[1]} is not a valid fractal")
    print("Please choose one of the following:")
    for i in images:
        print(f"\t{i}")
    sys.exit(1)

else:
    image = sys.argv[1]


minx = images[image]['centerX'] - (images[image]['axisLen'] / 2.0)
maxx = images[image]['centerX'] + (images[image]['axisLen'] / 2.0)
miny = images[image]['centerY'] - (images[image]['axisLen'] / 2.0)
maxy = images[image]['centerY'] + (images[image]['axisLen'] / 2.0)
pixelsize = abs(maxx - minx) / SIDE


# Set up the GUI so that we can paint the fractal image on the screen
window = Tk()

canvas = Canvas(window, width=SIDE, height=SIDE, bg=BLACK)
canvas.pack()

# Paint the cell under the mouse cursor or left click (Button-1)
canvas.bind("<Button-1>", paintCell)

# Display the entire image on the screen upon right click (Button-3) or spacebar
canvas.bind("<Button-3>", paintEntireImage)
window.bind("<space>", paintEntireImage)

# Reset the image
window.bind("<r>", resetImage)
window.bind("<R>", resetImage)

# Display usage information
window.bind("<h>", usage)
window.bind("<H>", usage)

# Quit the program
window.bind("<Escape>", sys.exit)
window.bind("<q>", sys.exit)
window.bind("<Q>", sys.exit)

usage(None)

mainloop()
