import numpy as np

def  main():
    i = 0
    n = 10
    x = 19.0

    y= np.zeros(n, dtype=float)

    for i in range(n):
        y[i] = 2.0 * float(i) + 1.0


    for element in y:
        print(element)

if __name__ == '__main__':
    main()
