# Cyclic-D1 lower-fibre/Taylor realization gate

This is a source-frozen design package for the first genuinely unbounded-total
passport-realization computation after the universal `(9,12)` Faber and
terminal Belyi theorems.

The primary target is the complete `k != 0` order-three lower fibre with all
constant loads `(mu,nu)`, tested against the affine-normalized cyclic
`D=e=1` passport.  It is disjoint from the selected-Q8 `k=0` component work.

Files:

- `PREREGISTRATION.md` gives the theorem question, exact D1 fixture,
  Galois descent, geometric-section semantics, full Taylor gate, projective
  boundaries, controls, outputs, and stop rules.
- `compile_gate.py` is the AWS-only source adapter.  It pins every input,
  explicitly calls the parent transitive pin checker, emits all eight
  descended rows, and fails if the `sigma`/`tau` character convention is
  swapped.

No CAS run, source-row output, component calculation, or theorem result is
included yet.  In particular, this directory does not claim that the D1
passport is realized or excluded.

Proposed first AWS commands after source freeze:

```sh
export JC2_AWS_TAG=max12_912_order3_d1_rows_<UTC>_<HOST>
python3 compile_gate.py > rows.json
python3 compile_gate.py --singular-generic > generic.sing
timeout 2h singular generic.sing > generic.stdout 2> generic.stderr
```

The second independent tail reconstruction, geometric/absolute
factorization, load-stratum recursion, and Taylor-section compiler required
by the preregistration must be staged before any result can promote.
