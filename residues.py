from sympy.polys.polytools import Poly
from sympy.abc import x

def get_residues(polynomials, modulus):
  """
  Calculates the residues of a list of
  polynomials, modulo some given polynomial.
  Note: preserves the order of the provided list.
  """
  residues = []
  for poly in polynomials:
    residues.append(poly.rem(modulus))

  return residues
