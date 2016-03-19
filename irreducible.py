from sympy.polys.polytools import Poly
from sympy.abc import x

# Filters a list based on irreducibility of elements.
def get_irreducible(all_polynomials):
    irreducible_polynomials = []
    for poly in all_polynomials:
        if poly.is_irreducible and poly.degree() > 0:
            irreducible_polynomials.append(poly)
    return irreducible_polynomials
