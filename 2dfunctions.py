import lib
from lib import *


def func():
    t = sp.Symbol('t')

    x = parse_expr(input("x wrt. t: "), transformations='all')
    y = parse_expr(input("y wrt. t: "), transformations='all')

    print("x= ", x)
    print("y= ", y)

    tmin = parse_expr(input("tmin (number): "), transformations='all')
    tmax = parse_expr(input("tmax (number): "), transformations='all')

    r = sp.Matrix([x, y])

    print("r= ", r)

    rprime = r.diff('t')
    print("rprime= ", rprime)

    dx = rprime[0]
    dy = rprime[1]
    print("dx, dy= ", dx, dy)

    rnorm = rprime.norm()
    print("rnorm= ", rnorm)

    F1 = parse_expr(input("F1 wrt. x,y: "), transformations='all')
    F2 = parse_expr(input("F2 wrt. x,y: "), transformations='all')

    print("F1, F2= ", F1, F2)

    F = rnorm * (F1*dx + F2*dy)
    print("F= ", F)

    int = sp.integrate(F, ('t', tmin, tmax))
    print("answer= ", int)
