This python program will take some points and fit a curve to them.

The goal of this program is mostly academic, and reading the source code can be a good way to understand how to find a polynomial of
degree d to fit some data using the mean square error.

To utilize this program, you must have python installed (at leas version 2.0), matplotlib and numpy installed. Your data must 
be written to a file where for every x-value, the corresponding y-value should appear on the line right below it. So if you had a 
point (3,6) 3 would appear on the first line and 6 on the second. The algorithm will then calculate a polynomial that fits all the
points, according to a degree that you specify, and plot the points and the polynomial so they can be viewed. In the console, the 
corresponding weights for the polynomial will be listed, along with the supplied y-values and the calculated y-values, given the weights
for the polynomial and the x-values. The average square error over all the points listed will be given too.

Future plans: Modifications to this code will be coming. In particular, I will get rid of all uses of numpy.matrix, as numpy.matrix
is considered deprecated. I will fix the graph too so that it's more useful. (right now it's very zoomed out and you can't get a good
idea of what the curve looks like), and maybe add the first and second derivative of the polynomial calculated.

Improvements to this program will come soon. I hope that this programn is of some use to somebody

Sample Usages:

python fit.py -i data.txt -d 10
python fit.py --ifile datatest.txt --degree 30

If you have any questions for concerns, feel free to email me.
