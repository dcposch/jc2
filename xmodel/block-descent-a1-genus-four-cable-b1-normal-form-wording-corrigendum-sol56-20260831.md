# Corrigendum: genus-four normal-form equivalence wording

Date: 2026-08-31 UTC  
Author: Sol 5.6 Ultra (coordinator audit)  
Frozen basis: `d19c494ec2b8d0eb994089eafac8655e19e03195`  
Lifecycle: **FINAL CORRIGENDUM / THEOREM UNCHANGED**

## 0. Binding correction

This corrigendum binds the sealed producer

```text
070faa884a26b0c96aaacafa7738cb39746407803d156a5a327d360eabf613e5
  xmodel/block-descent-a1-genus-four-cable-b1-obstruction-sol56-20260831.md
```

and its replay

```text
c79b7197d9c84e8a9a161cf153430849ad730b35d950a51afc32d1cd73ffa707
  ops/block_descent_a1_genus_four_cable_b1_replay.py.
```

The producer's theorem is correct, but the wording in §0 and at the start of
§5 overstates the coordinate changes. The literal sentence

> Every polynomial parametrization in the `(9,6,2)` row is equivalent,
> under affine changes of the parameter and target coordinates, to (0.3)

must be read as follows:

> Put the parametrization into the charged reduced-coordinate presentation
> by the licensed polynomial target automorphism. After that polynomial
> reduction, every member of the `(9,6,2)` row is equivalent by an affine
> parameter change and the further affine target changes used in §5 to
> the canonical pair (0.3).

Likewise, the sentence after (5.2) means that the changes from the reduced
Weierstrass presentation onward are affine triangular changes; it does not
claim that the initial reduced-coordinate transformation is affine.

## 1. Exact counterexample to the stronger wording

Starting with the canonical pair `(U,V)` of (0.3), apply the polynomial
target automorphism

```text
(u,v) |-> (u,v+u^2).
```

The resulting parametrization `(U,V+U^2)` defines exactly the same embedded
curve up to a polynomial automorphism of the target and remains in the same
one-place delta-sequence row, but its displayed coordinate degrees are
`(6,12)`. No affine target change, combined with an affine parameter change,
can reduce the degree-twelve coordinate to degree nine: the only other
coordinate has degree six. Thus the producer's literal affine-only claim is
false before reduced coordinates are chosen.

The charged approximate-root interface explicitly licenses the missing
polynomial reduced-coordinate change. Polynomial target automorphisms
preserve normalization fibres, `b1`, affine delta, the complement, meridians,
and existence of a transitive meridional-transposition `S4` representation.
Consequently the correction has no blast radius on the conductor-eight
census, the exhaustive reduced normal form, or the four-pair obstruction.

## 2. Maximum-safe conclusion

Retain the producer's exact scoped conclusion:

> No reduced irreducible one-place complex affine plane curve in the charged
> packet can simultaneously have `Delta_aff=4`, `b1=1`, and a transitive
> meridional-transposition representation to `S4`.

Do not promote the stronger presentation claim that an arbitrary raw
parametrization is affine-target-equivalent to (0.3). A different-model
hostile review of the producer remains required before campaign promotion.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3091`.
- Body SHA-256:
  `a81baa719330c0aa7a6a067fbc071e150ef1528d828bb13ff2bee26b888d4c6e`.
- Frozen basis: `d19c494ec2b8d0eb994089eafac8655e19e03195`.
