"""
Write a Python program that writes out a table of the function sin(x) vs. x,
where x is tabulated between 0 and 2 with a thousand entries. Follow the basic Python program structure,
including a main program function.
"""
import math
from tabulate import tabulate
import numpy as np

def main():
    end = 2*math.pi
    start = 0
    steps = 1000
    header = ["x","sin(x)"]

    x = np.linspace(start, end, steps)
    y = np.sin(x)
    data = np.column_stack([x,y])

    table = tabulate(data, header,floatfmt=".10f", tablefmt="github",)

    print(table)

if __name__ == "__main__":
    main()

