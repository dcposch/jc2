# Complete successor design: correction-aware valuation recurrence

Date: 2026-08-25  
Status: design plus exact negative-control replay; no fan-completeness claim

## Exact state

The recurrence must use the six coefficient series of Q and R separately,
not only `beta=min v(Q_i)` and `alpha=min v(R_i)`.  For a fixed ramified
strict chart write

```text
Lambda=t^M, tau=t^N*T(t), M>3N>0,
a=1+sum a_j t^j, h=sum h_j t^j,
Q_i=sum q_(i,j)t^j, R_i=sum r_(i,j)t^j.
```

`k,mu,nu` are coefficient-field constants: their arrays have only order zero
and no higher coefficients.  Compute `p=-3a^2,c=2a^3+h`, substitute the full
charged ordinary tails, and collect every coefficient through `20M`.  For a
sparse source monomial `X^m`, use cached exact convolutions

```text
[t^e] X^m = sum_(j_1+...+j_|m|=e) product X_(j_s).
```

This automatically retains later coefficients of QR/K, R^2/K^2, every
higher charged layer, moving-axis terms, and all target coincidences.

At order e, branch on every pivot rather than divide generically.  Each node
stores:

- exact constructible conditions and their radical ideal;
- all forced coefficients and all free correction directions;
- the next candidate exponents for every sparse source monomial;
- hashes of the parent state and coefficient equations;
- negative controls obtained by deleting each claimed necessary correction.

Deduplicate only after two ideal containments, not by dimension or sampled
rank.  An inconsistent coefficient ideal excludes that fixed ramified chart.
A surviving order-`20M` jet is not a lift.

## Fan-complete front end

Enumerating `M,N` to a numerical bound is not complete.  The proof-grade
front end should instead tropicalize the finite exact local ideal in the
individual coefficient variables.  Enumerate every coordinate-support mask,
then every rational Groebner cone intersecting

```text
v(Q_i),v(R_i),v(a-1),v(h)>0,
v(Lambda)>3v(tau)>0.
```

For each cone, certify its initial ideal by a characteristic-zero standard
basis and test torus support by saturation.  A monomial certificate discards
the cone.  A nonmonomial cone is passed to the coefficient recurrence above.
Because the input ideal and its Groebner fan are finite, a certified traversal
of all adjacent cones and coordinate masks is a fan-completeness proof.  The
certificate must include exponent matrices, primitive rays, adjacency,
initial-basis hashes, and coverage of the strict inequality region.

Loads require a relative treatment.  Total-space emptiness is a valid uniform
exclusion.  A total-space survivor must be split by comprehensive Groebner
strata in `(k,mu,nu)` and rerun with those loads held constant.  A Puiseux
point with varying load coordinates is not a fixed-load arc.

## Mandatory finite firewall

Until the certified tropical traversal is complete, every fixed `(M,N)` or
bounded-denominator run is labelled `SCREENING_FIXED_SLOPE`.  It may exclude
only its stated chart.  No denominator bound, whole fan, formal lift, D1, or
JC2 conclusion is permitted.  In particular:

- inconsistency through `20M` is a rigorous exclusion for that fixed chart;
- consistency through `20M` is only a finite jet;
- a list of tested slopes never proves slope uniformity;
- the two correction controls in `verify_correction_controls.py` must pass
  before any recurrence output is consumed.
