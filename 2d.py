import lib
from lib import *

def func():

    x1input=input("x1 wrt. t: ")
    x1=parse_expr(x1input, transformations='all')

    y1input=input("y1 wrt. t: ")
    y1=parse_expr(y1input, transformations='all')

    x2input=input("x2 wrt. t: ")
    x2=parse_expr(x2input, transformations='all')

    y2input=input("y2 wrt. t: ")
    y2=parse_expr(y2input, transformations='all')

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
    F1input=input("F1 wrt. x,y: ")
    F1=parse_expr(F1input, transformations='all')
    F2input=input("F2 wrt. x,y: ")
    F2=parse_expr(F2input, transformations='all')
    # F1=x+2*y
    # F2=x**2
    # 

    print("F1, F2= ", F1, F2)

    F=rnorm * (F1*dx + F2*dy)
    print("F= ", F)

    int=sp.integrate(F, ('t', tmin, tmax))
    print("answer= ", int)
