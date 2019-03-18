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

    # Generate a
    a = np.empty([p, p])
    for i in range(0,p):
        for j in range(0,p):
            a[i][j] = x[i]**j

    # Use these as matrices
    a = np.asmatrix(a)
    w = np.asmatrix(w)
    yMatrix = np.asmatrix(y)
    y2 = a*w.transpose()

    # Calculate the minimized weight vector
    w = np.linalg.inv(a.transpose()*a)
    w = w*a.transpose()
    w = w*yMatrix.transpose()


    # Create the function
    x24 = np.arange(0,10)
    wNew = np.squeeze(np.asarray(w))
    f1 = (x24**0)*wNew[0]
    for value in range(1, d+1):
        f1 += (x24**value)*wNew[value]

    # Calculate the average square error over all the points
    ew = (a*w) - yMatrix

    # Print data to console:
    print("Weight Vector: \n" + str(w))
    print("y values: \n" + str(yMatrix))
    print("y tilde values: \n" + str(a*w))
    print("Average squared error: " + str((np.linalg.norm(ew)**2)*(1/p)))

    # Plot the function and the points, then show
    plt.plot(x24, f1, color="red")
    plt.plot(x, y, 'ro')
    plt.show()

if __name__ == "__main__":
    main()
