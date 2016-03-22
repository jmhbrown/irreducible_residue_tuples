import generation as g
import residues as r
import misc_calculations as misc
import sys
from sympy.polys.polytools import Poly
from sympy.polys import Poly
from sympy.abc import x


# XXX - only works with fields with prime order.
#       So, coeff must be a list with prime length
#
# XXX - the elements given here as coefficients are just
#       integers, which might behave oddly.
coeff = [0,1]
if len(sys.argv) > 1:
    num_terms = int(sys.argv[1])
else:
    num_terms = 2
sequence_length = 2
modulus_poly = Poly(x**2+x+1, x, domain="FF(%i)" % len(coeff))

print("coeff: ", coeff, ", num_terms: ", num_terms,"\n---")

irreducible_p = g.get_irreducible_polynomials(coeff, num_terms)
print("# of irreducible polynomials:\t", len(irreducible_p), "\n---")

avg_sequence_freq = misc.average_sequence_frequency(modulus_poly,len(coeff), len(irreducible_p), sequence_length)
print("expected average residue sequence frequency:\t", avg_sequence_freq)

residues_p = r.get_residues(irreducible_p, modulus_poly)
# print("residues:\n", residues_p, "\n---")

residue_counts = r.get_residue_frequencies(residues_p)
print("residue counts:\n", residue_counts, "\n---")

sequence_counts = r.get_sequence_frequencies(residues_p, sequence_length)
print("sequence frequencies:\n", sequence_counts, "\n---")

deviation_from_average = misc.get_deviation_from_sequence_frequency(sequence_counts,avg_sequence_freq, num_terms, len(coeff))
print("sequence frequecy deviations from the average:\n", deviation_from_average, "\n---")
