import lib
from lib import *

def func():
    t=sp.Symbol('t')
    
    xinput=input("x wrt. t: ")
    x=parse_expr(xinput, transformations='all')

    yinput=input("y wrt. t: ")
    y=parse_expr(yinput, transformations='all')

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
    F1input=input("F1 wrt. x,y: ")
    F1=parse_expr(F1input, transformations='all')
    F2input=input("F2 wrt. x,y: ")
    F2=parse_expr(F2input, transformations='all')
    # 

    print("F1, F2= ", F1, F2)

    F=rnorm * (F1*dx + F2*dy)
    print("F= ", F)

    int=sp.integrate(F, ('t', tmin, tmax))
    print("answer= ", int)
