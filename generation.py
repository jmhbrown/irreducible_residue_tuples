from sympy.polys import Poly
from sympy.abc import x
from itertools import product,chain

def get_irreducible_polynomials(coeff, num_terms):
    """
    Generates a `list` in lexigraphical ordrer of polynomials meeting the following conditions:
        * coefficients from `coeff`
        * monic
        * degree exactly `num_terms-1`
        * irreducible
    """

    irreducible_filter = lambda p: p.is_irreducible
    # XXX - This assumes `1` will be nicely converted to identity element in the field.
    #       Seems like a safe bet, but might be worth checking in on.
    poly_lambda = lambda p: Poly(chain([1], p), x, domain="FF(%i)" % len(coeff))

    irreducible = filter(irreducible_filter, map(poly_lambda, product(coeff, repeat=num_terms-1)))
    return list(irreducible)
