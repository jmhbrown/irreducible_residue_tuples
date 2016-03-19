from sympy.polys.polytools import Poly
from sympy.abc import x
from collections import Counter

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

def get_sequence_frequencies(residues, sequence_length):
    """
    Calculates the frequencies at which various sequences of
    residues appear in a residue list.

    For example:
    ```
    \>>> get_tuple_frequencies([0,1,1,0], 2)
    {(0,1):1, (1,1):1, (1,0): 1}
    ```
    """

    counts = Counter()
    for i in range(0, len(residues)-sequence_length+1):
        counts[tuple(residues[i:i+sequence_length])] += 1

    return counts
