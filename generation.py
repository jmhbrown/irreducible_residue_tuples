from sympy.polys import Poly
from sympy.abc import x
from itertools import product

def get_irreducible_polynomials(coeff, num_terms):
    """
    Generates a `list` in lexigraphical ordrer of polynomials meeting the following conditions:
        * coefficients from `coeff`
        * degree less than `num_terms`
        * non-constant (e.g. `x+1` is okay, `1` is not)
        * irreducible
    """

    irreducible_filter = lambda p: p.is_irreducible and p.is_monic and Poly.degree(p) >= 1
    poly_lambda = lambda p: Poly(p, x, domain="FF(%i)" % len(coeff))

    irreducible = filter(irreducible_filter, map(poly_lambda, product(coeff, repeat=num_terms)))
    return list(irreducible)
