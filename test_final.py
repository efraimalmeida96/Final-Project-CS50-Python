import sympy
from sympy import sin, cos
from final import Movement

def main():
    test_diff()
    test_integral()


def test_diff():

    x, y, z, t, c = sympy.symbols('x y z t C')

    # DIFF t
    diff = Movement(5*t**2/2 + c*t)
    diff2 = Movement(5*t + 2)
    diff3 = Movement(t**3/3 + t**2 + c)
    diff4 = Movement(t**2 + 2*t + c)
    diff5 = Movement(-3*sympy.cos(t) + c*x + c)
    diff6 = Movement(3*sympy.sin(t) + c)

    assert sympy.simplify(diff.difference()) == 5*t + c
    assert sympy.simplify(diff2.difference()) == 5
    assert sympy.simplify(diff3.difference()) == t**2 + 2*t + c
    assert sympy.simplify(diff4.difference()) == 2*t + 2
    assert sympy.simplify(diff5.difference()) == 3*sympy.sin(t) + c
    assert sympy.simplify(diff6.difference()) == 3*sympy.cos(t)

    # DIFF x
    diff7 = Movement(4*x**2 + c*x)
    diff8 = Movement(3*sympy.sin(x))
    diff9 = Movement(2*sympy.cos(x) + c)

    assert sympy.simplify(diff7.difference()) == 8*x + c
    assert sympy.simplify(diff8.difference()) == 3*sympy.cos(x)
    assert sympy.simplify(diff9.difference()) == -2*sympy.sin(x)

    # DIFF y
    diff10 = Movement(y**3 + 2*y**2 + c)
    diff11 = Movement(sympy.sin(y))
    diff12 = Movement(sympy.cos(y))

    assert sympy.simplify(diff10.difference()) == 3*y**2 + 4*y
    assert sympy.simplify(diff11.difference()) == sympy.cos(y)
    assert sympy.simplify(diff12.difference()) == -sympy.sin(y)

    # DIFF z
    diff13 = Movement(z**4/4 + z**2)
    diff14 = Movement(5*sympy.sin(z))
    diff15 = Movement(3*sympy.cos(z) + c)

    assert sympy.simplify(diff13.difference()) == z**3 + 2*z
    assert sympy.simplify(diff14.difference()) == 5*sympy.cos(z)
    assert sympy.simplify(diff15.difference()) == -3*sympy.sin(z)

def test_integral():
    
    x, y, z, t, c = sympy.symbols('x y z t C')
    integ = Movement(5)
    integ2 = Movement(5*t + c)
    integ3 = Movement(2*t + 2)
    integ4 = Movement(t**2 + 2*t + c)
    integ5 = Movement(3*sympy.cos(t))
    integ6 = Movement(3*sympy.sin(t) + c)

    # INTEGRAL t
    assert sympy.simplify(integ.integral()) == 5*t + c
    assert sympy.simplify(integ2.integral()) == 5*t**2/2 + 2*t + c
    assert sympy.simplify(integ3.integral()) == t**2 + 2*t + c
    assert sympy.simplify(integ4.integral()) == t**3/3 + t**2 + c
    assert sympy.simplify(integ5.integral()) == 3*sympy.sin(t) + c
    assert sympy.simplify(integ6.integral()) == -3*sympy.cos(t) + c*x + c

    # INTEGRAL x
    integ7 = Movement(8*x + c)
    integ8 = Movement(3*sympy.cos(x))
    integ9 = Movement(-2*sympy.sin(x))

    assert sympy.simplify(integ7.integral()) == 4*x**2 + c*x + c
    assert sympy.simplify(integ8.integral()) == 3*sympy.sin(x) + c
    assert sympy.simplify(integ9.integral()) == 2*sympy.cos(x) + c

    # INTEGRAL y
    integ10 = Movement(3*y**2 + 4*y)
    integ11 = Movement(sympy.cos(y))
    integ12 = Movement(-sympy.sin(y))

    assert sympy.simplify(integ10.integral()) == y**3 + 2*y**2 + c
    assert sympy.simplify(integ11.integral()) == sympy.sin(y) + c
    assert sympy.simplify(integ12.integral()) == sympy.cos(y) + c

    # INTEGRAL z
    integ13 = Movement(z**3 + 2*z)
    integ14 = Movement(5*sympy.cos(z))
    integ15 = Movement(-3*sympy.sin(z))

    assert sympy.simplify(integ13.integral()) == z**4/4 + z**2 + c
    assert sympy.simplify(integ14.integral()) == 5*sympy.sin(z) + c
    assert sympy.simplify(integ15.integral()) == 3*sympy.cos(z) + c

if __name__ == "__main__":
    main()
