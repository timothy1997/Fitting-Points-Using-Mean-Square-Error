import numpy as np
import matplotlib.pyplot as plt #import the Python Matplotlib sub-module for graph plotting pyplot

x = []
y = []

def main():

    with open("data.txt") as f: # Read all the data points
        for line in f:
            # This ternary operator below just assigns to each x value a y value
            y.append(float(line)) if len(x) > len(y) else x.append(float(line))

    d = len(x) - 1  # The degree of the polynomial we will use to fit the points
    p = len(x)  # The number of points we have
    w = np.random.rand(1, d+1)    # Generate random weights for the vector

    a = np.empty([p, p])
    for i in range(0,p):
        for j in range(0,p):
            a[i][j] = x[i]**j

    # Use these as matrices
    a = np.asmatrix(a)
    w = np.asmatrix(w)
    y1 = np.asmatrix(y)
    y2 = a*w.transpose()

#    plt.plot(x,f1,color="red") # Plot the eventual function we will implement
#    plt.plot(x, y, 'ro')    # Plot the points
#    plt.show()  # Displaying the figures

if __name__ == "__main__":
    main()
