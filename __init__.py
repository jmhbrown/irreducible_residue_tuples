import generation as g
import residues as r
from sympy.polys.polytools import Poly
from sympy.polys import Poly
from sympy.abc import x


# XXX - only works with fields with prime order.
#       So, coeff must be a list with prime length
#
# XXX - the elements given here as coefficients are just
#       integers, which might behave oddly.
coeff = [0,1]
num_terms = 11
sequence_length = 2
modulus_poly = Poly(x**2+x+1, x, domain="FF(%i)" % len(coeff))

irreducible_p = g.get_irreducible_polynomials(coeff, num_terms)
print("# of irreducible polynomials:\t", len(irreducible_p), "\n---")

residues_p = r.get_residues(irreducible_p, modulus_poly)
# print("residues:\n", residues_p, "\n---")

residue_counts = r.get_residue_frequencies(residues_p)
print("residue counts:\n", residue_counts, "\n---")

sequence_counts = r.get_sequence_frequencies(residues_p, sequence_length)
# print("sequence frequencies:\n", sequence_counts, "\n---")
