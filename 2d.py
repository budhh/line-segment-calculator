import sympy as sp
import numpy as np

def func2d():
    x1=0
    y1=0

    x2=2
    y2=1
    # 

    t=sp.Symbol('t')

    x=x1+t*(x2-x1)
    y=y1+t*(y2-y1)
    print("x= ", x)
    print("y= ", y)

    tmin=0
    tmax=1

    r = sp.Matrix([x,y])

    print("r= ", r)

    rprime = r.diff('t')
    print("rprime= ", rprime)

    dx=rprime[0]
    dy=rprime[1]
    print("dx, dy= ", dx,dy)

    rnorm=rprime.norm()
    print("rnorm= ", rnorm)

    #  CHANGE THESE
    # 
    F1=x+2*y
    F2=x**2
    # 

    print("F1, F2= ", F1, F2)

    F=rnorm * (F1*dx + F2*dy)
    print("F= ", F)

    int=sp.integrate(F, ('t', tmin, tmax))
    print("answer= ", int)
