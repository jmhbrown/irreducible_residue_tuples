from sympy.polys import Poly
from sympy.abc import x
from itertools import product,chain
from functools import partial
import multiprocessing
from math import log,floor

def get_irreducible_polynomials(coeff, num_terms):
    """
    Generates a `list` in lexigraphical ordrer of polynomials meeting the following conditions:
        * coefficients from `coeff`
        * monic
        * degree exactly `num_terms-1`
        * irreducible
    """

    prefixes = product(coeff, repeat=2)
    irreducible_p = []
    irr_p = []
    if __name__  == 'generation':
        pool = multiprocessing.Pool(len(coeff)**2)
        build_list = partial(build_irreducible_list, coeff=coeff, num_terms=num_terms)
        # XXX - this extend function is changing the domain of our polynomials
        irr_p.extend(pool.map(build_list, product(coeff,repeat=2)))
        print("get_irreducible_polynomials", irr_p)

    return list(chain.from_iterable(irr_p))


def get_prefix_length(num_threads, field_size, num_terms):
    return min(floor(log(num_threads, field_size)), num_terms)

def build_coeff_list(prefix,coeff, num_terms):
    add_prefix = lambda l : list(chain(prefix, l))

    return list(map(add_prefix, product(coeff, repeat=num_terms)))

def convert_to_polynomials(field_size, polynomial_list):
    """
    Converts a list of lists to a list of polynomials
    """
    convert_to_poly = lambda p: Poly(chain([1], p), x, domain="FF(%i)" % field_size)
    irreducible_filter = lambda p: p.is_irreducible

    irreducible = filter(irreducible_filter, map(convert_to_poly, polynomial_list))
    return list(irreducible)

def build_irreducible_list(prefix, coeff, num_terms):
    coeff_list = build_coeff_list(prefix, coeff, num_terms-len(prefix)-1)
    irr_p = convert_to_polynomials(len(coeff), coeff_list)
    print("build_irreducible_list", irr_p)
    return irr_p

