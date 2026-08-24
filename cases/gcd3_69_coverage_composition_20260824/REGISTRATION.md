# Registration — GCD3 `(6,9)` coverage composition

Date: 2026-08-24

## Resolution state

The formerly pending cube-core trajectory input is now hostile-review
confirmed at SHA-256
`7bcf18d69344acc2277a0184ca1aeeb717ebad35c3aacf91421874b7e59f5cc9`.
The case is therefore producer-complete and ready for a fresh independent
review of the composition itself.  No theorem below relies on the earlier
provisional status.

## Registered theorem question

Do the reviewed partial-`y` history stop and first common-cubic split, the
reviewed aligned nontrivial-Kummer exclusion, and the reviewed complete
polynomial cube-core exclusion form a disjoint and exhaustive proof that the
fundamental `(6,9), 3|H` residue is empty?

If yes, does lexicographic target reduction give the exact field theorem

```text
max(deg_y P, deg_y Q) <= 11  =>  (P,Q) is a polynomial automorphism
```

for every characteristic-zero Keller pair?

## Required routes

The route artifact must fail closed unless it certifies exactly one of:

1. `h` is not a cube in `k(x)`: `T^3-h` is nontrivial Kummer, the constant
   mismatch `delta` is forced to zero by weight one, all and only the reviewed
   nonzero-weight high constants vanish, and the aligned reviewed exclusion
   is consumed.
2. `h` is a cube in `k(x)`: Gauss gives `h=c*s^3`, `s in k[x]`; every
   weight-unforced Faber constant is retained; `d=-delta/2` is split into
   `d!=0` and the separate `d=0` quotient; the reviewed cube-core exclusion is
   consumed.

No full-cubic boundary reduction, polynomial source depression, or Kummer
weight vanishing in the cube core is licensed.

## Mandatory adversarial controls

1. `h=x(x-1)(x-2)` with formal `delta` must be proved noncube from a simple
   divisor and must derive `delta=0` using the invertibility of `omega-1` in
   `Q[omega]/(omega^2+omega+1)`.
2. `h=(x^2+1)^3`, `d=0`, `c7=1` must route to the full `d=0` cube Faber
   system.  In particular `c7` must remain nonzero and the aligned
   nontrivial-Kummer route must not be consumed.

## Degree coverage

Enumerate every unordered pair `0<=m<=n<=11`, retain the exact routes
`Z/G/D/E/X69`, and recursively verify every target-reduction child.  The
only nonclassical primitive before the composition must be `(6,9),3|H`.
Also enumerate maximum twelve and require that the first new primitive pairs
are exactly `(8,12)` and `(9,12)`; this is a frontier check, not part of the
theorem.

## Stop / failure rules

- Any successor premise not emitted by its predecessor prints `UNCLAIMED`
  and blocks the theorem.
- Any extra primitive degree pair through eleven blocks the corollary.
- Any loss of `c7` on the cube `d=0` control is a branch-typing failure.
- Any use of the pending producer without its hostile review hash blocks the
  final freeze.
- PASS strings are regression markers only; the mathematical evidence remains
  the reviewed source reports and the explicit composition proof.

The frozen successful replay has canonical JSON payload SHA-256
`d7e030685c84e7c7366524e4b28f8516a5bf9d5060c3ebdba3990ca2e243ecd4`.

No canonical file, AWS resource, or other ideation submission is in scope.
