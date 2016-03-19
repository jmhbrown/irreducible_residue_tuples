from sympy.polys import Poly
from sympy.polys.polytools import Poly
from sympy.abc import x

def all_polynomials(coeff, max_degree):
    """
    Constructs a list of polynomials in lexigraphical order
    """

    polynomials = init_polynomials(coeff)

    i = 0
    while i < max_degree:
        i += 1
        polynomials = add_next_degree(i, coeff, polynomials)
    return polynomials

def init_polynomials(coeff):
    """
    Initializes the list of polynomials with the constant
    polynomials, based on the coefficients.
    """

    polynomials = []
    domain = "FF(%i)" % len(coeff)
    for c in coeff:
        f = Poly(c, x, domain=domain)
        polynomials.append(f)
    return polynomials

def add_next_degree(next_degree, coeff, poly_list):
    """
    Adds the next degree to polynomials.
    For example, if

    ```
      next_degree = 1
      coeff = [0,1]
      poly_list = [0,1]
    ```

    Then this will return
    ```
      [0, 1, x, x+1]
    ```
    """

    new_poly_list = []
    for c in coeff:
        new_term = Poly(0, x, domain="FF(%i)" % len(coeff)) if c == 0 else Poly(c*x**(next_degree), x, domain="FF(%i)" % len(coeff))
        for poly in poly_list:
            new_poly_list.append(poly + new_term)

    return new_poly_list

def add_next_degree_2(next_degree, coeff, poly_list):
    """
    Not Used!
    Same as `add_next_degree`, but with JJB's approach
    """

    new_poly_list = []
    for c in coeff:
      new_term = 0 if c == 0 else c*x**(next_degree)
      new_poly_list.extend(list(p+new_term for p in poly_list))
    return new_poly_list
