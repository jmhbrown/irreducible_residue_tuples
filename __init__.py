import generation as g
import irreducible as i
from sympy.polys.polytools import Poly


all_p = g.all_polynomials([0,1], 3)
print("all:\n", all_p, "\n---")

irreducible_p = i.get_irreducible(all_p)
print("irreducible:\n", irreducible_p)
