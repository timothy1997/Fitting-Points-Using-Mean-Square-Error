import sys, getopt
import numpy as np
import matplotlib.pyplot as plt #import the Python Matplotlib sub-module for graph plotting pyplot

xOrig = []
yOrig = []
x = []
y = []

def main():

    d = parseArguments(sys.argv[1:])    # Get the degree and the data set

    if d == -1:
        d = len(x) - 1  # The degree of the polynomial we will use to fit the points
    p = d+1  # The number of points we have
    w = np.random.rand(1, d+1)    # Generate random weights for the vector

    a = np.empty([p, p]) # Generate matrix a
    for i in range(0,p):
        for j in range(0,p):
            a[i][j] = x[i]**j

    a = np.asmatrix(a)  # Convert everything to matrices, so they're easier to work with
    w = np.asmatrix(w)
    yMatrix = np.asmatrix(y)
    y2 = a*w.transpose()

    w = np.linalg.inv(a.transpose()*a) # Calculate the minimized weight vector
    w = w*a.transpose()
    w = w*yMatrix.transpose()

    x24 = np.arange(0,10) # Create the function
    wNew = np.squeeze(np.asarray(w))
    f1 = (x24**0)*wNew[0]
    for value in range(1, d+1):
        f1 += (x24**value)*wNew[value]

    ew = (a*w) - yMatrix # Calculate the average square error over all the points

    print("Weight Vector: \n" + str(w)) # Print data to console:
    print("y values: \n" + str(yMatrix))
    print("y tilde values: \n" + str(a*w))
    print("Average squared error: " + str((np.linalg.norm(ew)**2)*(1/p)))

    plt.plot(x24, f1, color="red")  # Plot the function and the points, then show
    plt.plot(xOrig, yOrig, 'ro')
    plt.show()

def parseArguments(argv):
    d = -1
    try:
        opts, args = getopt.getopt(argv, "hi:d:", ["ifile", "degree="])
    except getopt.GetoptError:
        print("usage: fit.py -i <inputfile> -d <degree of polynomial>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("fit.py -i <inputfile> -d <degree of polynomial>")
            sys.exit(0)
        elif opt in ("-d", "--degree"):
            d = int(arg)
        elif opt in ("-i", "--ifile"):
            with open(arg) as f: # Read all the data points
                for line in f:
                    # This ternary operator below just assigns to each x value a y value
                    yOrig.append(float(line)) if len(xOrig) > len(yOrig) else xOrig.append(float(line))
    global y
    global x
    y = yOrig[0:d+1]
    x = xOrig[0:d+1]
    return d

if __name__ == "__main__":
    main()
