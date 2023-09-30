import lib
from lib import *

def func3d():
    x1=1
    y1=0
    z1=0

    x2=-2
    y2=1
    z2=2
    # 

    t=sp.Symbol('t')
    pi=sp.Symbol('pi', real = True, positive = True)

    x=x1+t*(x2-x1)
    y=y1+t*(y2-y1)
    z=z1+t*(z2-z1)
    print("x= ", x)
    print("y= ", y)
    print("z= ", z)

    tmin=0
    tmax=1

    r = sp.Matrix([x,y,z])

    print("r= ", r)

    rprime = r.diff('t')
    print("rprime= ", rprime)

    dx=rprime[0]
    dy=rprime[1]
    dz=rprime[2]
    print("dx, dy, dz= ", dx, dy, dz)

    rnorm=rprime.norm()
    print("rnorm= ", rnorm)

    #  CHANGE THESE
    # 
    F1=z**2
    F2=x**2
    F3=y**2
    # 

    print("F1, F2, F3= ", F1, F2, F3)

    F=rnorm * (F1*dx + F2*dy + F3*dz)
    print("F= ", F)

    int=sp.integrate(F, ('t', tmin, tmax))
    print("answer= ", int)
