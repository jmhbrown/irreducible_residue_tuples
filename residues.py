from sympy.polys.polytools import Poly
from sympy.polys import Poly
from math import log
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

def get_residue_frequencies(residues):
  counts = Counter(i for i in residues)
  return counts

def get_tuple_frequencies(residues, tuple_length):
    """
    Calculates the frequencies at which various tuples of
    residues appear in a residue list.

    For example:
    ```
    \>>> get_tuple_frequencies([0,1,1,0], 2)
    {(0,1):1, (1,1):1, (1,0): 1}
    ```
    """

    counts = Counter()
    for i in range(0, len(residues)-tuple_length+1):
        counts[tuple(residues[i:i+tuple_length])] += 1

    return counts


def average_tuple_frequency(modulus_poly, coeff_count, irreducible_count, tuple_length):
  """
    Calculates the average tuple frequency - the frequency you would expect if the
    residues were uniformly distributed.
  """
  return irreducible_count/((coeff_count**Poly.degree(modulus_poly)-1)**(tuple_length))

def get_deviation_from_tuple_frequency(tuple_counts, expected_frequency, num_terms, num_coeff):
  """
    Calculates the deviation from the average tuple frequency, for each tuple.
  """
  max_degree = num_terms - 1

  deviations = {}
  for actual_count in tuple_counts.items():
    deviations[actual_count[0]] = ((actual_count[1] - expected_frequency)/(expected_frequency))*(max_degree/log(max_degree, num_coeff))

  return deviations

