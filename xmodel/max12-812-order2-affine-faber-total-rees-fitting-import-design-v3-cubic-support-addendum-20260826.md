# `(8,12)` order two: delayed-load fan cubic-support addendum

Date: 2026-08-26

Status: **NONMUTATING SUPPORT CORRECTION TO V2; NO NEW EXCLUSION.**

## 0. Scope

This note does not alter the V2 repair

```text
9f91fe43300017ef09f3886def02a5c16769d7a70778d993f32ca35646eec044
  xmodel/max12-812-order2-affine-faber-total-rees-fitting-import-design-v2-repair-20260826.md.
```

It corrects the claim that the coarse comparison of `2H` with the load and
target walls supplies the full valuation support.  V2 already required the
literal `c^3` mode in its eventual compiler, but Sections 3--4 did not put
the corresponding valuation form into the advertised fan skeleton.  Hence
V2's skeleton is a mandatory partial list, not an exhaustive fan.

## 1. Missing valuation form

For a square chart written schematically as

```text
F=K^2+E,
```

the unloaded binomial expansion contains

```text
F^(3/2)
 = K^3 + (3/2)K E + (3/8)E^2/K - (1/16)E^3/K^3 + ... .       (1.1)
```

Consequently a normal defect of valuation `H=v(E)` contributes not only the
quadratic support form

```text
2H,
```

but also the cubic support form

```text
3H.                                                          (1.2)
```

Polynomial cancellation of the quadratic tail does not remove (1.2).
On the repeated-root null state used in V2,

```text
K=Q0=z^2(z^2+p),             E_H=N3=v*z*(z^2+p),
```

one has

```text
N3^2/Q0 = v^2(z^2+p)          (polynomial),
N3^3/Q0^3 = v^3/z^3           (nonpolynomial).                 (1.3)
```

Thus the quadratic tail may vanish while the cubic tail remains.  In the
primitive delayed-load `A` null ray `H=5e`, its valuation is

```text
3H=15e,                                                       (1.4)
```

strictly between the common affine-load face `14e` and the `mu4` wall
`16e`.  It can also tie the first relative-grade-one load jet at `15e`.
Any source client that jumps from the `14e` face directly to `16e` omits a
legal source term.

## 2. Corrected finite-support sentinel

Before claiming fan exhaustiveness, a literal-source emitter must include at
least

```text
2H, 3H, 14e, 16e, 18e, 19e, 14e+H,                           (2.1)
```

together with every actual load-jet valuation.  With the parity refinement
`H_plus,H_minus`, the cubic list expands to

```text
3H_plus,
2H_plus+H_minus,
H_plus+2H_minus,
3H_minus.                                                     (2.2)
```

These forms must be reduced only after retaining the nonreduced predecessor
ideal.  A form whose leading coefficient is in a first-normal null module is
a transition to the next source grade, not permission to delete the form.
The finite fan must therefore be computed from the union of (2.1)--(2.2),
the V2 quadratic parity forms, all moving-connection forms, all timed load
jets, and the four target walls.

For the repeated-null `A,H=5e` state, the minimum exact chart now has three
successive bands:

```text
14e : leading delayed-load affine face,
15e : cubic normal plus first relative load jets,
16e : mu4 boundary,                                            (2.3)
```

before continuing through `mu6` and the terminal `J` grade.  The positive
control `m0=v*x/2` from V2 and the cubic pole (1.3) must both survive the
source compiler.

## 3. What remains valid

The strict high-contact `K` gate in V2 is unchanged.  Its hypothesis

```text
2H>19e
```

implies `3H>19e`, so neither the quadratic nor cubic unloaded term can enter
through the unit-terminal grade.  Therefore the reviewed `4 x 2` block still
applies precisely on the V2 open `D(q0*K10*J)` in that strict valuation
range.

No analogous conclusion follows on `2H<=19e`, and no part of the repeated-
root `A` face is closed by this addendum.  In particular, the V2 middle and
predecessor cones are not exhaustive until an exact literal-source fan
includes (1.2) and proves source-equivalent coverage after arbitrary
ramification.

## 4. Firewall

This is a support correction and successor specification only.  It proves
no total-Rees, `A`-face, delayed-load ray, square-component, order-two,
`(8,12)`, maximum-twelve, or JC2 exclusion.

