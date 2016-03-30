# Irreducible Residue Tuples
Calculates the frequency of residue tuples in irreducible polynomials over various finite fields

# Installing and Running
This code was written for `python3` and uses the `sympy`, `optparse`, `json`, and `loggging` packages.

Run the code like so -
```
python main.py --help
```

Multiple runs can be defined in a config file. 
* `coeff` is an ordered list (smallest to largest) of the possible coefficients. It also defines the function field that the polynomials are over.
* `num_terms` is the number of terms per polynomial.
* `modulus_poly` is the polynomial that should be used to calculate residues. Defined either as a list of coefficents, largest degree first _or_ as a string representation of the polynomial, e.g. `x**2+x+1`. Note that its domain is taken from `coeff`. 
* `tuple_length` is the length of the tuples whose frequencies should be calculated in the residues of the polynomials.

Here's an example:
```
[
  {
    "tuple_length": 2,
    "modulus_poly": [1,1,1],
    "coeff": [0,1],
    "num_terms": 5
  },
  {
    "tuple_length": 2,
    "modulus_poly": "x**2+x+1",
    "coeff": [0,1],
    "num_terms": 6
  }
]
```
