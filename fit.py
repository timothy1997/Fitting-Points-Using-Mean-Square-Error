import sys, getopt
import numpy as np
import matplotlib.pyplot as plt #import the Python Matplotlib sub-module for graph plotting pyplot

x = []
y = []

def main():
    d = parseArguments(sys.argv[1:])    # Get the degree and the data set

    a = np.asmatrix(generateMatrix(x, len(x)-1))   # Generate the a matrix

    w = np.linalg.inv(a.transpose()*a)*a.transpose() * np.asmatrix(y).transpose()   # Get the minimized weights
    # If our degree is more than 1 less our number of points, we don't want to include some values
    # in our matrix, because they will only be used for higher degrees
    for i in range(d+1, len(x)):
        w[i][0] = 0

    yTilde = a*w    # Calculate the values and the error
    ew = yTilde - np.asmatrix(y).transpose()
    error = (1/float(ew.shape[0])) * np.linalg.norm(ew)**2

    x24 = np.arange(0,8) # Create the function
    wNew = np.squeeze(np.asarray(yTilde))
    f1 = (x24**0)*wNew[0]
    for value in range(1, d+1):
        f1 += (x24**value)*wNew[value]

    print("Weight Vector: \n" + str(w)) # Print data to console:
    print("y values: \n" + str(np.asmatrix(y)))
    print("y tilde values: \n" + str(yTilde))
    print("Average squared error: " + str(error))

    plt.plot(x24, f1, color="red")  # Plot the function and the points, then show
    plt.plot(x, y, 'ro')
    plt.show()

def generateMatrix(points, degree):
    p = degree+1
    a = np.empty([len(points), degree+1]) # Generate matrix a
    for i in range(0,len(points)):
        for j in range(0,p):
            a[i][j] = points[i]**j
    return a

def parseArguments(argv):
    d = -1
    global y
    global x
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
                    y.append(float(line)) if len(x) > len(y) else x.append(float(line))

    if len(x) != len(y):    # Check for some conditions that must exist for our algorithm to run
        print("Must include a data file that has a y for every x.")
        sys.exit(2)
    elif len(x) == 0:
        print("Must include a data file with data in it.")
        sys.exit(2)
    elif len(x) <= d:
        print("The number of points given must be greater than the degree.")
        sys.exit(2)

    return d

if __name__ == "__main__":
    main()
