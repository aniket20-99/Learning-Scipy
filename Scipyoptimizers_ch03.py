# Optimizers in Scipy: It is a set of procedures defined in scipy that either find the min value of a function or a root of an equation.
# Optimizing function: All the algorithms which helps in minimising(making easy) the data.

# Root of an equation: x + cos(x)--> We will solve this via optimize.root function. 
# This function takes 2 arguments: "fun" and "x^0"

# Example: Find the root of the equation x + cos(x) :

from scipy.optimize import root
from math import cos

def Equation(x):
    return x + cos(x)

myroot = root(Equation, 0)
print(myroot.x)


# Now we have to find the info about not just x but the whole root:
from scipy.optimize import root
from math import cos

def Equation(x):
    return x + cos(x)

myroot = root(Equation, 0)
print(myroot)

# Minimizing the Function or data:
# Maxima :- High point are called maxima
# Minima :- low points are called minima

# Finding Minima:
# We use scipy.optimize.minimize(). Its uses 3 arguments:- "fun",x^0 and method
# And method have some legal values: "CG", "BFGS","NEWTON-CG","L-BFGS-B","TNC","COBYLA","SLSQP".
# callback: Function called after each iteration of optimizations. 
# Option --> later

# Example:- Minimize the function :x^2 + x + 2 with BFGS
from scipy.optimize import minimize

def eqn(x):
    return x**2 + x + 2

Min = minimize(eqn, 0, method = 'BFGS')
print(Min)

