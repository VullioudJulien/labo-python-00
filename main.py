

# library
from math import*
import numpy as np


# Fonction delta
def delta(a,b,c):
    return(b**2 - 4*a*c)

# Fonction Solve
def solve(a,b,c):
    d = delta(a,b,c)
    if d > 0 :
        r1 = (-b + sqrt(d))/(2*a)
        r2 = (-b - sqrt(d))/(2*a)
        return r1,r2
    elif d == 0:
        return (-b + sqrt(d))/(2*a)
    else :
        z1 = (-b + 1j*sqrt(abs(d)))/(2*a)
        z2 = (-b - 1j*sqrt(abs(d)))/(2*a)
        return z1,z2
    
    
print(solve(1,4,5))