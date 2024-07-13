def fx(x, n, *coeff) -> float:
    """This function evaluates and returns the value of a polynomial function at a given point x."""
    total = 0
    r = n + 1 # For n degree, there are r terms
    for k in range(r):
        total += coeff[k]*x**(n-k)
    # return f"The value of f({x}) = {total}" # For test purposes
    return total


def fprimex(x, n, *coeff) -> float:
    """This function evaluates and returns the value of the derivative of a polynomial function at a given point x."""
    total = 0
    r = n + 1 # For n degree, there are r terms
    for k in range(r):
        total += ((n-k) * coeff[k])*x**(n-k-1)
    # return f"The value of f'({x}) = {total}" # For test purposes
    return total

# Function takes the error value and the starting value and returns the root of the 3rd order equation
def newton_raphson(order, error, starting_value, *coefficients) -> float:
    """This function implements the Newton-Raphson method to find the root of a polynomial function.
    \nIt returns a root of the polynomial function for instance.
    """
    xn = starting_value
    print(f"x_n = {xn}")
    f = fx(xn, order, *coefficients)
    m = fprimex(xn, order, *coefficients)
    xnn = (xn - (f/m))
    print(f"x_n+1 = {xnn}")

    if abs(xnn - xn) < error:
        return xnn
    else:
        return newton_raphson(order, error, xnn, *coefficients)

# Uncomment this line below to test This
# print(newton_raphson(3, 0.0001, 1.5, 1,-1,0,-1))
