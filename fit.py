import numpy as np
import matplotlib.pyplot as plt #import the Python Matplotlib sub-module for graph plotting pyplot

x = []
y = []

def getData():
    rawData = []
    data = []
    with open("data.txt") as f:
        for line in f:
            rawData.append(float(line[:-1]))


def main():

    with open("data.txt") as f: # Read all the data points
        for line in f:
            # This ternary operator below just assigns to each x value a y value
            y.append(float(line)) if len(x) > len(y) else x.append(float(line))

    plt.plot(x, y, 'ro')    # Plot the points
    plt.show()  # Displaying the figures

if __name__ == "__main__":
    main()
