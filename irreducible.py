from sympy.polys.polytools import Poly
from sympy.abc import x

def get_irreducible(all_polynomials):
    """
    Filters a list based on irreducibility of elements.
    """
    irreducible_polynomials = []
    for poly in all_polynomials:
        if poly.is_irreducible and poly.degree() > 0:
            irreducible_polynomials.append(poly)
    return irreducible_polynomials
