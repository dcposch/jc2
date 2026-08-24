# Hamiltonian kappa exact replay

This directory is the independent, standard-library-only certificate for
`xmodel/hamiltonian-kappa-gate-20260824.md`.

Run:

```sh
python3 cases/hamiltonian_kappa_20260824/replay.py
```

The replay uses sparse polynomials over `fractions.Fraction`; it does not
import the earlier exact-coframe engine or any CAS.  It checks:

- four polynomial-coordinate controls by their displayed Jacobian mates;
- the canonical unimodular lift and the sign of its divergence for
  `P_n=x+x^n y`;
- both exact recurrences for `n=2,3,4,7`: the direct slice equation
  `[P_n,Q]=1` and the equivalent divergence-correction equation for `kappa`;
- the `n=3` coefficients and terminal obstruction explicitly; and
- the rational slice formula as a rational-function identity after clearing
  its denominator, for the same values of `n`.

The finite replays are checks, not the exhaustiveness proof.  Exhaustiveness
comes from the symbolic weight argument in the report: the Hamiltonian
operator is homogeneous of shift `n-1`, and all nonnegative-exponent
monomials of the only relevant weight are enumerated by one infinite chain.

