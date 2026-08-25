# AS fixed-support low-`y` adic escape from the maximum-eleven theorem

Date: 2026-08-25  
Status: **PRODUCER-EXACT THEOREM; DIFFERENT-MODEL REVIEW PENDING**

## Result

Fix finite allowed monomial sets `S_P,S_Q` in `Z_3[x,y]`, and suppose every
allowed monomial has `y`-exponent at most eleven.  For `n>=1`, let `X_n` be
the complete solution set of coefficient vectors for maps `F=(P,Q)` modulo
`3^n` such that

```text
support(P) subset S_P,       support(Q) subset S_Q,
F mod 3 = (x-x^3,y),         det J(F)=1 in (Z/3^n)[x,y].
```

Then `X_n` is empty for at least one finite `n`.  Equivalently, complete AS
solutions in one such fixed finite support cannot exist at arbitrarily large
3-adic precision.

In particular, the full total-degree-seven map-only AS coefficient scheme
must close at some finite depth.  This is non-effective: it gives neither the
first empty depth nor an explicit finite ideal/cokernel certificate.

The only campaign theorem imported is the different-model-confirmed result
that every characteristic-zero Keller pair with maximum actual partial
`y`-degree at most eleven is a polynomial automorphism:

```text
xmodel/gcd3-69-coverage-composition-20260824.md
SHA-256 7eda0a469585247479d46c8f5f2ce95d2643ae8541f0d7f9c80e1c8537fffb0c

xmodel/gcd3-69-coverage-composition-review-claude-20260824.md
SHA-256 d9522acbb35c5097cb3d3c947be12c10868f109af4d30c9713870f5ec6e9a33f
```

That theorem is stated over every characteristic-zero field and in actual
partial degrees, so it applies over `Q_3`; vanishing leading coefficients can
only lower the actual degrees.

## 1. Compactness produces an exact integral lift

Assume for contradiction that `X_n` is nonempty for every `n`.  Use one
coefficient coordinate for every monomial in the two fixed allowed sets, and
view arbitrary lifts of a solution modulo `3^n` as points of the compact ball
`Z_3^N`.  Let `C_n` be the subset satisfying the fixed AS reduction and every
coefficient equation of `det J(F)-1` modulo `3^n`.

Each `C_n` is nonempty and closed, and

```text
C_1 superset C_2 superset C_3 superset ... .
```

Nested compactness therefore gives a coefficient vector in every `C_n`.
The corresponding map

```text
F in Z_3[x,y]^2
```

has the same finite allowed supports, reduces to `(x-x^3,y)`, and satisfies
the exact polynomial identity `det J(F)=1`.  Compatibility of separately
displayed finite-level solutions is not an extra hypothesis.

## 2. The generic-fibre inverse is integral

The actual `y`-degrees of `F` over `Q_3` are at most eleven.  The reviewed
maximum-eleven theorem makes `F` a polynomial automorphism of
`Q_3[x,y]`.

Put

```text
a=F(0) in Z_3^2,             G=F-a.
```

Then `G(0)=0`, `G mod 3=(x-x^3,y)`, and

```text
L=JG(0) in GL_2(Z_3)
```

because `det JG=1`.  The unique `(x,y)`-adic formal inverse of `G` has
coefficients in `Z_3`.  Indeed, write it as homogeneous pieces
`H=H_1+H_2+...`.  The degree-one equation gives `H_1=L^(-1)`.  At every
later degree the composition equation has the form

```text
L H_d = an integral polynomial expression in G,H_1,...,H_(d-1).
```

Only multiplication by `L^(-1) in M_2(Z_3)` is required; there is no
division by an integer.  Induction gives

```text
H in Z_3[[x,y]]^2.
```

On the other hand, the polynomial inverse of `G` over `Q_3` has zero
constant term and is a formal inverse.  Formal inverse uniqueness identifies
its Taylor expansion with `H`.  Since it has only finitely many nonzero
coefficients, it actually lies in `Z_3[x,y]^2`.  Translating the target back
by the integral vector `a` also puts the polynomial inverse of `F` in
`Z_3[x,y]^2`.

## 3. Reduction is impossible

Reduce the two polynomial composition identities modulo three.  They would
make

```text
(x-x^3,y)
```

a polynomial automorphism of `F_3[x,y]`.  This is impossible: on
`F_3`-points its first coordinate is zero at all three values of `x`, so, for
example, `(0,0)` and `(1,0)` have the same image.  A polynomial automorphism
induces a bijection on `F_3^2`.

This contradiction proves finite-depth emptiness.

## Consequences for the live AS computation

1. The current D7 lifting tree cannot contain an all-depth branch.  The
   exact 91-by-72 Jacobian and quadratic Kuranishi computation is seeking an
   explicit finite closure certificate, not testing an open possibility of
   ordinary smooth Hensel continuation.
2. Rank 27 at the AS special fibre cannot prove relative smoothness.  The
   divergence-free direction `(U,V)=(t*x^7,2*t*x^6*y)` already leaves the
   quadratic class `2*t^2*x^12` over `F_3`.
3. More generally, if complete AS solutions of `y`-degree at most eleven
   survive to arbitrarily large depths, their allowed monomial supports
   cannot remain inside any one finite envelope.  In particular a fixed
   `x`-degree cap must eventually fail.

## Firewall

This theorem does not provide the empty depth, an effective Nullstellensatz
identity, a covered chronological DAG, or a support-growth rate.  It does not
empty any displayed Q3 fibre at the next precision, and it does not license
discarding nonreduced Kuranishi strata.  It concerns only the AS residue
tube and fixed finite supports with `y`-degree at most eleven.  It neither
reduces an arbitrary Keller pair to that tube nor proves or disproves JC2.

The reviewed residue-ball collision theorem gives a compatible alternative
contradiction after an all-depth fixed-support lift, but it is not needed for
the direct integral-inverse proof above.
