# Selected-Q8 sparse contact-to-component lemma

Date: 2026-08-25  
Status: **PRODUCER-EXACT MOD-127 LEMMA; component conclusion awaits the live breadth endpoint and hostile review**

## Exact numerical bound

Let `Y` be the six-row divided approximate-cubic source in

```text
(w,c,d2,d4,x1,x3,x5)
```

and restrict to the chart

```text
x5*(x3-2*x5) != 0,       v=(x3-2*x5)/x5.
```

For a generic affine target line `a*w+b*v+c=0`, its division-free pullback is

```text
a*w*x5 + b*(x3-2*x5) + c*x5 = 0.
```

The exact monomial-support sizes of the six rows are

```text
10,20,35,57,16,29,
```

and the pulled-back line support is

```text
x5, x3, w*x5.
```

Normaliz 3.10.2 polarization in dimension seven gives

```text
raw torus mixed volume                         519
origin-augmented affine mixed volume           658
polarization numerator for the affine value    3316320 = 658*7!.
```

The coordinate-segment and repeated-standard-simplex controls both return
`1`.  A second Box03 implementation independently returns the same affine
value `658`.  The source, full output, metadata, and both AWS runs are frozen
in

```text
cases/max12_912_order3_nu_q8_sparse_mixed_volume_aws_20260825/.
```

## Why `658` bounds the relevant projection cycle

At every charged fixed-fibre source point the six-by-six Jacobian with respect
to `(c,d2,d4,x1,x3,x5)` is a unit.  Six equations in seven variables therefore
give a regular one-dimensional local complete intersection.  In particular,
each point lies on a unique generically reduced curve component, and `w-w0`
is a uniformizer.  Let `Z` be the reduced one-cycle formed by the irreducible
components meeting the charged points, and let `pi_*Z` be its cycle-theoretic
pushforward to the `(w,v)` plane.

No relevant component is contained in the localization boundary, because it
contains a charged point where both factors are units.  Its closure meets that
boundary and the other irreducible components in finite sets.  The projective
closure of its plane image also has finitely many points at infinity.  Choose
the generic target line to avoid all of those finite sets and all branch/
component collision values.  Its pullback then meets each relevant component
inside the chart, transversely after a further generic choice, and at isolated
points of the full seven-polynomial system.  The number of these points,
counted with cycle multiplicity, is exactly `deg(pi_*Z)`.

Rojas, *Solving Degenerate Sparse Polynomial Systems Faster*, Main Theorem 1
and Remark 9 (arXiv:math/9809071), apply over an algebraically closed field of
arbitrary characteristic and bound all isolated affine roots by the mixed
volume after adjoining the origin to every support.  The theorem still counts
the relevant isolated roots when unrelated positive-dimensional boundary
components occur elsewhere.  Hence

```text
deg(pi_*Z) <= 658.                                      (1)
```

Using the characteristic-zero supports is safe for the mod-127 system: any
coefficient that vanished modulo 127 could only shrink a support and therefore
cannot increase this origin-augmented mixed-volume upper bound.

## Additive finite contact

The candidate `H(w,v)` is monic of `v`-degree `190`, has exact total degree
`190`, and is geometrically irreducible over `F_127`.  Assume no irreducible
component in `pi_*Z` is `H`.  Projective Bezout and (1) then give

```text
I(H,pi_*Z) <= 190*658.                                  (2)
```

At a good fixed fibre `w=w_i`, `H(w_i,v)` is squarefree of degree `190`, the
lex shape replay supplies all 190 source points, and the full source Jacobian
is a unit.  If the exact source equations, ratio, and localizer lift over

```text
F_127[s,v]/(s^N,H(w_i+s,v)),
```

through order `N`, each of those 190 distinct smooth points contributes local
intersection multiplicity at least `N`.  Contributions at distinct `w_i` are
at distinct plane points and add.  With one order assigned to each of the 123
good fixed fibres, define

```text
S = 123 + sum_i (N_i-1).
```

Then the charged local contact is at least `190*S`.  Combining with (2):

> **Sparse contact-to-component criterion.** If the audited exact lifts give
> `S>658`, at least one relevant projected source component is `H`.

The strict inequality is essential.

The separately frozen order-64 lift at `w=25` gives `S=123+63=186`.  Thus any
68 further distinct good order-8 fibres give

```text
S = 123 + 63 + 68*7 = 662 > 658.                        (3)
```

Eighty deterministic order-8 fibres are currently running on Box02/Box03, so
the lexicographically first 68 passing fibres will supply (3), with twelve
failure-tolerance lanes.

## Exact scope and charged successors

The theorem is exact at the mod-127 selected-quotient cycle tier.  Even after
(3) completes, it proves only existence of an `H`-supported projected source
component.  It does **not** by itself prove:

- that the source component maps to `H` with degree one or is a global graph;
- that every one of the 190 fixed-fibre branches, or every Q8 boundary
  contact, lies on that component;
- that distinct characteristic-zero components cannot merge modulo 127;
- characteristic-zero source membership, Taylor realization, no-merger, or
  any rational/Keller trajectory conclusion.

Those remain separate gates.  In particular, a full-rank point proves local
smoothness and etaleness over `w`, not global degree one.

## Custody

```text
Box02 result.json   74685bb41f43cf796024c0c4261e24e3b304b3313f2b2d04004a441771ee06ef
Box03 result.json   d9cc4829c9f0bc2fce70291c50c711e4ce0cf53b44379ef54a3e06e30c718359
mixed_volume.py     a6a516d6558cdceee02e7340ad179e0e142af653506bd0f5468ee8e2027267f9
```
