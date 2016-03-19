import generation as g
import irreducible as i
from sympy.polys.polytools import Poly


# XXX - only works with fields with prime order.
#       So, coeff must be a list with prime length
#
# XXX - the elements given here as coefficients are just
#       integers, which might behave oddly.
all_p = g.all_polynomials([0,1,2,3], 3)
# print("all:\n", all_p, "\n---")

irreducible_p = i.get_irreducible(all_p)
print("irreducible:\n", irreducible_p)
