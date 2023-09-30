import lib
from lib import *


def func():
    x1 = parse_expr(input("x1 wrt. t: "), transformations='all')
    y1 = parse_expr(input("y1 wrt. t: "), transformations='all')
    z1 = parse_expr(input("z1 wrt. t: "), transformations='all')

    x2 = parse_expr(input("x2 wrt. t: "), transformations='all')
    y2 = parse_expr(input("y2 wrt. t: "), transformations='all')
    z2 = parse_expr(input("z2 wrt. t: "), transformations='all')

    t = sp.Symbol('t')

    x = x1+t*(x2-x1)
    y = y1+t*(y2-y1)
    z = z1+t*(z2-z1)

    print("x= ", x)
    print("y= ", y)
    print("z= ", z)

    tmin = 0
    tmax = 1

    r = sp.Matrix([x, y, z])

    print("r= ", r)

    rprime = r.diff('t')
    print("rprime= ", rprime)

    dx = rprime[0]
    dy = rprime[1]
    dz = rprime[2]
    print("dx, dy, dz= ", dx, dy, dz)

    rnorm = rprime.norm()
    print("rnorm= ", rnorm)

    F1 = parse_expr(input("F1 wrt. x,y,z: "), transformations='all')
    F2 = parse_expr(input("F2 wrt. x,y,z: "), transformations='all')
    F3 = parse_expr(input("F3 wrt. x,y,z: "), transformations='all')

    print("F1, F2, F3= ", F1, F2, F3)

    F = rnorm * (F1*dx + F2*dy + F3*dz)
    print("F= ", F)

    int = sp.integrate(F, ('t', tmin, tmax))
    print("answer= ", int)
