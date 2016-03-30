import generation as g
import residues as r

import logging
from sympy.polys import Poly
from sympy.abc import x
from optparse import OptionParser
import json


def get_pretty(poly_tuple):
    """
    Converts a tuple of polynomials into a pretty list.
    """
    pretty_poly_list = []
    for poly in poly_tuple:
        pretty_poly_list.append(poly.as_expr())

    return tuple(pretty_poly_list)

def run(parameters, logger):
    """
    Run simulations with provided parameters
    """
    logger.debug("--- START RUN ---")
    logger.info("parameters: %s" % parameters)
    modulus_poly = Poly(parameters["modulus_poly"], x, domain="FF(%i)" % len(parameters["coeff"]))
    irreducible_p = g.get_irreducible_polynomials(parameters["coeff"], parameters["num_terms"])
    logger.info("irreducible_count: %i" % len(irreducible_p))

    avg_tuple_freq = r.average_tuple_frequency(modulus_poly, len(parameters["coeff"]), len(irreducible_p), parameters["tuple_length"])
    logger.info("average_tuple_frequency: %s" % avg_tuple_freq)
    residues_p = r.get_residues(irreducible_p, modulus_poly)
    residue_counts = r.get_residue_frequencies(residues_p)

    tuple_counts = r.get_tuple_frequencies(residues_p, parameters["tuple_length"])
    deviation_from_average = r.get_deviation_from_tuple_frequency(tuple_counts, avg_tuple_freq, parameters["num_terms"], len(parameters["coeff"]))
    logger.info("tuple; total_count; deviation")
    for residue_tuple in deviation_from_average:
        logger.info("%s; %s; %s" % (get_pretty(residue_tuple), tuple_counts[residue_tuple],deviation_from_average[residue_tuple]))

def parse_options_and_run():
  parser = OptionParser()
  parser.add_option("-o", "--output", dest="output_file", help="write results to FILE", metavar="FILE")
  parser.add_option("-c", "--config", dest="config_file", help="json configuration file, define a series of runs.", metavar="FILE")

  (options, args) = parser.parse_args()

  if options.config_file != None:
      runs = json.load(open(options.config_file,'r'))
  else:
      raise OptionError("missing configuration file. See --help for details.")

  if options.output_file != None:
    logging.basicConfig(filename=options.output_file, format='%(message)s')
  else:
      logging.basicConfig(format='%(message)s')

  logger = logging.getLogger('log')
  logger.setLevel(10)

  for parameters in runs:
      run(parameters, logger)

parse_options_and_run()



# XXX - only works with fields with prime order.
#       So, coeff must be a list with prime length
#
# XXX - the elements given here as coefficients are just
#       integers, which might behave oddly.
