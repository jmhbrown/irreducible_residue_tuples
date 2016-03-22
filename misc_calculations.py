from sympy.polys import Poly
from math import log

def average_sequence_frequency(modulus_poly, coeff_count, irreducible_count, sequence_length):
  """

  """
  return irreducible_count/((coeff_count**Poly.degree(modulus_poly)-1)**(sequence_length))

def get_deviation_from_sequence_frequency(sequence_counts, expected_frequency, num_terms, num_coeff):
  max_degree = num_terms - 1

  deviations = {}
  for actual_count in sequence_counts.items():
    deviations[actual_count[0]] = ((actual_count[1] - expected_frequency)/(expected_frequency))*(max_degree/log(max_degree, num_coeff))

  return deviations

