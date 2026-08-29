# Significant-news delta: generating row functionals and radical composition

Date: 2026-08-26 16:22Z

Status: **COORDINATOR IDEATION; NONE OF THE PROPOSED GENERALIZATIONS IS A
THEOREM.**

## News charged

1. The complete unweighted affine-Faber functional `K=E*H3+H5` has now
   been emitted on exact Q and F65521.  Both lanes find 371 monomials with
   the same ordered exponent support, while retaining all load and target
   sentinels.  This is raw support/navigation only; coefficient
   stratification and predecessor-relative initial reduction are pending.
2. The D1 `a>=13` producer uses the order-two odd-row functional, while the
   mechanically complete `a>=10` rebuild is testing the order-three
   functional.  The latter has not yet passed dual AWS or hostile review.
3. TD6 V87R1 and V88 are under one fresh hostile composition review.  V89
   currently proposes a shared Fitting atlas for the 22 transverse unit-q
   charts.

## 1. D1: the two recurrences are consecutive binomial series

Introduce a row-shift marker `T`, so multiplication by `T` moves
`Phi7,Phi5,Phi3,Phi1` one place to the right.  The reviewed order-two
coefficients are

```text
1, -p/4, -p^2/32, -p^3/128,
```

which are exactly the coefficients through `T^3` of

```text
(1-(p/2)T)^(1/2).
```

The proposed order-three coefficients are

```text
1, +p/4, +3p^2/32, +5p^3/128,
```

which are exactly the coefficients through `T^3` of

```text
(1-(p/2)T)^(-1/2).
```

This strongly suggests that the Laurent-to-ordinary connection, rather
than an accidental grade-38 cancellation, is producing a pole-order
functional.  The first conjectural formula to test is the `T^0,...,T^3`
truncation of

```text
(1-(p/2)T)^(5/2-r)
```

at pole order `r`.  Two data points do not prove the exponent formula.
The required derivation is to write the odd Laurent principal part in the
moving quadratic coordinate `L=z^2+p/2`, transport it through the frozen
ordinary-Faber connection, and identify the row functional symbolically.

Mandatory controls:

- recover the exact reviewed order-two coefficients and the complete
  order-three candidate without fitting them;
- test pole orders one and four against independently emitted frozen rows;
- retain moving `p(sigma)`, every load family, and the automatic source-jet
  ceiling;
- reject the formula at the first omitted high jet or coefficient mismatch.

If it passes, D1 should be reorganized as one pole-order recurrence theorem
plus a finite set of equality contacts, rather than a serial `a` ladder.

## 2. TD6: prove q-nilpotence globally instead of normalizing a unit q

Let `I` be the ideal of literal raw P12 and the 38 literal raw FIRST rows,
and work on the registered open `D(s)`, where

```text
s=U^12*H^3*B3.
```

The V87 identity has the form

```text
s in I+(F,q_e : e in E),
E={2,...,14,16,...,24}.
```

Rather than open 22 charts and normalize no unit, search for the dual
global certificates

```text
s^N*q_e^N_e in I+(F)                 for every e in E,              (2.1)
```

or, equivalently, an exact localized radical certificate

```text
(q_e:e in E) subset sqrt((I,F) R_s).                               (2.2)
```

Along a DVR source arc with `F` in the maximal ideal, (2.1) forces every
`q_e` into the maximal ideal.  The V87 identity then gives a unit equal to
a positive-valuation element, a contradiction.  Thus (2.1), if proved,
would close the retained slice without classifying arbitrary unit values or
asserting a nonexistent `G_m` quotient.

The cheapest client should use the already affine-linear source matrix
`M(q)=M0+sum q_e M_e`, test `e=16,...,24` first, and search bounded
support-minimal identities over the same localized invariant base ring.
It must replay each candidate against literal raw sources.  Reduced-P12
syzygies or first-order tangent vanishing alone are not evidence for
(2.1).  If a coordinate fails, emit the smallest nonzero obstruction and
feed it back into the V89 Fitting atlas.

## 3. Order two: replace part of Gate A by a valuative divisibility bridge

For a literal square-normal expansion

```text
C=Q^2+epsilon^d*N_d+higher,
```

the first unloaded quadratic rows are the ordinary transform of

```text
[(3/8)*N_d^2/Q]_-.
```

Because the ordinary connection is lower unitriangular and `deg Q=4`,
vanishing of the complete first negative block is expected to be equivalent
to the exact divisibility `Q | N_d^2`.  This gives a finite factor-type
classifier:

- squarefree `Q` forces `N_d=0`;
- for `Q=A^2 D` with `gcd(A,D)=1` and squarefree quadratic `D`, it forces
  `N_d=M*A*D`;
- more degenerate factor types route to the already named collision,
  Pell, `p=0`, and `D=0` receivers.

Polarizing the same divisibility at successive grades should recover the
kernel/complement absorption used by the affine-Faber `A` theorem.  This
may supply a smaller valuative source-overlap proof on each factor-type open
than constructing one monolithic total-Rees algebra.  It does not avoid
load/target timing: every valuation slope must still be split at the grades
where loads, targets, quadratic, and cubic normal terms tie.

The bounded first test is an exact-Q lemma proving

```text
first four (hence first seven) negative coefficients vanish
<=> Q divides N^2
```

for monic quartic `Q` and cubic `N`, followed by the explicit
`Q=A^2D` factor chart and its inverse on `D(disc(D)*D(A))`.  Only after that
should the affine-Faber relative Newton fan be composed with the literal
source.

## Scope firewall

These are acceleration designs.  They do not promote the raw 371-monomial
support to a Newton fan, the order-three D1 candidate to a recurrence
theorem, the V87R1/V88 package before review, any TD6 unit-q result, a
total-Rees overlap, order two, maximum twelve, or JC2.
