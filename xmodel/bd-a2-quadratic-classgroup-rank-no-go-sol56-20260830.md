# Quadratic incidence: class-group rank shortcut fails

Date: 2026-08-30 UTC  
Producer: Sol 5.6 Ultra coordinator  
Frozen basis: `f89cbb02305ee6fef32a79ccb8ff53fc4740a2a1`  
Lifecycle: **EXACT DESK PRODUCER / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Endpoint

The provisional ramification-attachment packet suggests computing `Cl(Y)`:
if its rank were at most one, the unit/localization injection would force
reduced ramification support to be irreducible.  On a smooth quadratic
incidence surface this rank shortcut cannot work.  The ambient surface is a
conic bundle with nine singular fibres and Picard rank eleven.  Removing a
reduced bidegree-`(2,3)` infinity divisor with at most three components leaves

```text
rank Cl(Y) >= 8.                                      (0.1)
```

In particular, for the projectively finite rational-tree types
`F1,F2,F4,F5,F7`, raw class-group rank cannot rule out two, three, or four
ramification components.  Any class-group continuation must compute the
actual component-class lattice, intersections, and effectivity—not merely
rank.

This is a negative optimization result, not evidence that reducible
ramification occurs.

## 1. Smooth conic-bundle structure

Let

```text
X subset P2 times P1
```

be a smooth irreducible hypersurface of class `2A+3B`, where `A` and `B` are
the two hyperplane pullbacks.  Projection

```text
q:X -> P1
```

is a flat conic bundle.  Indeed, a whole `P2` fibre would mean that all
quadratic coefficients share the corresponding linear base factor, making
the defining equation reducible.  The generic conic is smooth: otherwise its
generic singular point would make the total space singular.

Write the fibre quadratic as a symmetric `3 by 3` matrix whose entries are
binary cubics.  Its determinant is a binary form of degree nine.  Smoothness
of `X` forces every degenerate fibre to have rank two and every discriminant
zero to be simple.  Locally a rank-two fibre has model

```text
x^2+y^2+t*z^2=0,
```

whose total space is smooth and whose determinant has a simple zero.  A
multiple determinant zero at the fibre node, or a rank-one double line,
makes the total space singular.  Therefore `q` has exactly nine singular
fibres, each a reduced union of two lines.

## 2. Rationality and Picard rank

The generic conic over `C(P1)` has a rational point by the `C_1` property of
`C(P1)`; hence `q` has a rational section after resolving the rational map,
and `X` is rational.  Alternatively, the standard conic-bundle contraction
gives a birational ruled surface.

A smooth conic has Euler number two and a reduced pair of lines has Euler
number three.  Thus

```text
e(X)=e(P1)*2+9*(3-2)=4+9=13.                         (2.1)
```

For a smooth rational surface, `b1=b3=0`, `b0=b4=1`, and
`h^(2,0)=0`.  Equation (2.1) gives

```text
b2(X)=rho(X)=11.                                     (2.2)
```

This agrees with the standard conic-bundle basis: fibre, a section, and one
component from each of the nine reducible fibres.

## 3. Removing infinity

Let `H` be a reduced infinity divisor of class `A|X`, and put `Y=X minus H`.
If `H` has `s` irreducible components, the localization sequence for the
smooth surface gives

```text
Z^s -> Pic(X) -> Cl(Y) -> 0.
```

Consequently

```text
rank Cl(Y) >= 11-s.                                  (3.1)
```

The promoted reduced rational-tree types have

```text
F1: s=1;       F2,F4: s=2;       F5,F7: s=3,
```

so their lower bounds are respectively ten, nine, nine, eight, and eight.
The projective-basepoint types `F3,F6` also have at most three components but
are outside the projectively finite attachment theorem.

No independence of the `H_i` classes was assumed; any dependence only raises
the rank of `Cl(Y)`.  Torsion is irrelevant to (3.1).

## 4. Why the component-count shortcut stops

The block morphism still forces `O(U)^*=O(Y)^*=C^*`, so for
`U=Y minus R_red` the localization map

```text
Z^{components(R_red)} -> Cl(Y)
```

is injective.  But (3.1) leaves ample rank.  Moreover the total ramification
class `R=2A+B` has conic-bundle degree

```text
R.(B|X)=4,
```

so in the absence of vertical ramification it has at most four horizontal
components—well below the lower bounds in (3.1).  Rank alone gives no
contradiction.

The numerical controls are

```text
H.R=8,       p_a(H)=2,       p_a(R)=9,
p_a(H+R)=18.                                           (4.1)
```

They follow from `K_X=-A+B` and `A^2B=1` in the ambient threefold.  Thus the
remaining problem is not rank scarcity but concentration of a large
arithmetic-genus/intersection budget into unibranch cusps, excess contacts,
and a full resolved boundary tree.

The next exact class-group client must therefore express each possible
ramification component in the conic-bundle lattice, impose sum class
`2A+B`, adjunction, effectiveness, at-most-one infinity attachment from the
provisional attachment theorem, and linear independence from the unit
argument.  A raw Picard-rank computation should be stopped.

## 5. Scope and nonclaims

This packet assumes a smooth irreducible class-`2A+3B` incidence surface.  It
does not cover a singular ambient closure, nonflat conic bundle, nonreduced
infinity, target/fibre degree drop, or projective coefficient basepoint.  It
does not compute the individual divisor classes of ramification components or
prove they exist.  No quadratic-block closure, primitivity, map,
counterexample, or JC2 statement follows.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5476`.
- Body SHA-256:
  `0ad7e8126e2c552177f725fb374f1237e925b61b7cdbe9a17f0bdbf0bf899723`.
- Frozen basis: `f89cbb02305ee6fef32a79ccb8ff53fc4740a2a1`.
