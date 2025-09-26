import math
from tabulate import tabulate
from matplotlib import pyplot

def main():
    end = 2*math.pi
    start = 0
    steps = 1000
    increment_size = (end - start)/steps
    data = []
    header = ["x","sin(x)"]

    for i in range(steps):
        data.append([start, math.sin(start)])
        start = start + increment_size

    table = tabulate(data, header,floatfmt=".10f", tablefmt="github")

    print(table)

if __name__ == "__main__":
    main()