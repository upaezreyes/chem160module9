import math
from numpy import isclose
a = 3.

if math.sqrt(a)**2 != a:   #if sqrt(a)**2 does not equal a , print "WTH???"
    print("WTH???")

tol = 1e-3
if abs(math.sqrt(a)**2-a) > tol:
    print("WTH again!?")

if isclose(math.sqrt(a)**2,a):
    print("Close enough!")
