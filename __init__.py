import generation as g
import irreducible as i
import residues as r
from sympy.polys.polytools import Poly
from sympy.polys import Poly
from sympy.abc import x


# XXX - only works with fields with prime order.
#       So, coeff must be a list with prime length
#
# XXX - the elements given here as coefficients are just
#       integers, which might behave oddly.
coeff = [0,1,2]
all_p = g.all_polynomials(coeff, 3)
# print("all:\n", all_p, "\n---")

irreducible_p = i.get_irreducible(all_p)
print("irreducible:\n", irreducible_p)

residues_p = r.get_residues(irreducible_p, Poly(x,x,domain="FF(%i)" % len(coeff)))
print("residues:\n", residues_p)

frequencies_p = r.get_sequence_frequencies(residues_p,2)
print("frequencies:\n", frequencies_p)
