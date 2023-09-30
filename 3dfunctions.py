import lib
from lib import *


def func():
    t = sp.Symbol('t')
    pi = sp.Symbol('pi', real=True, positive=True)

    x = parse_expr(input("x wrt. t: "), transformations='all')
    y = parse_expr(input("y wrt. t: "), transformations='all')
    z = parse_expr(input("z wrt. t: "), transformations='all')

    print("x= ", x)
    print("y= ", y)
    print("z= ", z)

    tmin = parse_expr(input("tmin (number): "), transformations='all
    tmax = parse_expr(input("tmax (number): "), transformations='all')

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
