# Irreducible Residue Tuples
Calculates the frequency of residue tuples in irreducible polynomials over various finite fields

# Installing and Running
This code was written for `python3` and uses the `sympy` package.

Run the code like so -
```
python __init.py [number_of_terms]
```

For the moment, parameters are all hardcoded in `__init__.py`.
* `coeff` is an ordered list (smallest to largest) of the possible coefficients. It also defines the function field that the polynomials are over.
* `num_terms` is the number of terms per polynomial.
* `modulus_poly` is the polynomial that should be used to calculate residues. Note that its domain is taken from `coeff`
* `sequence_length` is the length of the sequences whose frequencies should be calculated in the residues of the polynomials.

# TODO

* Read parameters from an input file
* Pretty (read: readable) output, output files
