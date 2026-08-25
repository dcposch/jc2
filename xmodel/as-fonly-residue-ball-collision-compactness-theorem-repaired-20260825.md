# Repaired AS residue-ball collision and compactness theorem

Status: **PRODUCER-EXACT REPAIRED SUCCESSOR; FINAL DIFFERENT-MODEL REVIEW
PENDING**

Date: 2026-08-25

Parent report, preserved byte-for-byte:

```text
xmodel/as-fonly-residue-ball-collision-compactness-theorem-20260825.md
SHA-256 f9cd7727e27bbae83e623c50b2c1865be75ee70292fdf8e9c0be91373980f338
```

This successor incorporates every repair requested by the first Grok review.
It is self-contained and supersedes the parent's wording, not its frozen
bytes.

## 1. Finite-ring theorem

Let `R_n=Z/3^n Z`.  Suppose a polynomial map `F=(P,Q)` over `R_n` satisfies

```text
det J(F)=1 in R_n[x,y],       F mod 3=(x-x^3,y).
```

For each `r` in `{(0,0),(1,0),(2,0)}`, the restriction of `F` to the source
residue ball above `r` is a bijection onto the target residue ball above
`(0,0)`.  Hence every target in that ball has three distinct, moving
preimages.  Every pairwise x-coordinate difference is a unit.

Indeed, assume `x_k` is the unique solution with prescribed residue `r`
modulo `3^k`.  A lift is `x_k+3^k h`, `h in F_3^2`, and polynomial Taylor
expansion gives

```text
F(x_k+3^k h)=F(x_k)+3^k JF(x_k)h mod 3^(k+1).
```

The higher Taylor terms contain `3^(2k)`, and `2k>=k+1`.  The reduction of
`JF(x_k)` is invertible because its determinant is one.  Thus exactly one
`h` solves the next digit.  Induction proves the bijection.  Taking the
preimages in the first two balls gives source points `(a,b),(c,d)` and a
unique `u` with

```text
P(a,b)=P(c,d),  Q(a,b)=Q(c,d),  u(a-c)=1.
```

These are Hensel-moving points; the theorem does not assert that fixed marked
integer representatives collide.

## 2. Fixed-support compactness

Fix finite sets of allowed monomials `S_P,S_Q`; coefficients may vanish, so
the actual support is only required to be **contained** in those sets
(equivalently the degrees are at most a fixed cap).  At every precision use
the same coefficient variables and impose every coefficient equation of
`det J(F)-1`, together with the fixed AS reduction.

For each `n`, let `X_n` be the subset of the compact coefficient ball
`Z_3^N` satisfying the complete equations modulo `3^n`.  Any solution over
`R_n` lifts as a coefficient vector to `Z_3^N`, so `X_n` is nonempty whenever
the finite scheme is.  The sets are closed and nested.  Nonemptiness at
arbitrarily large depths therefore yields a point in `intersection X_n`.
Equivalently, the finite solution tree has arbitrarily deep nodes and finite
branching, so Koenig's lemma supplies a compatible infinite branch.

The resulting fixed-support map over `Z_3` has determinant exactly one and
the AS reduction.  Applying the finite-ring induction at every depth gives a
compatible moving collision over `Z_3`.

## 3. Unambiguous finite-type transfer to `Qbar` and `C`

Let `Y` be the **finite-type affine collision scheme over `Z`** whose
variables are:

- the finitely many coefficients of `P,Q` in `S_P,S_Q`;
- `(a,b),(c,d)` and `u`;

and whose equations are:

- every coefficient of `det J(F)-1`;
- `P(a,b)-P(c,d)=0` and `Q(a,b)-Q(c,d)=0`;
- `u(a-c)-1=0`.

The fixed-support `Z_3` map and its moving Hensel collision define a
`Q_3`-valued point of the generic fibre `Y_Q`.  Therefore the coordinate
ring `Q[Y]` has a homomorphism to the nonzero field `Q_3`; in particular
`Q[Y]` is not the zero ring and its defining ideal in the relevant polynomial
ring over `Q` is proper.

If base change to `Qbar` made the coordinate ring zero, faithful flatness of
the field extension `Q -> Qbar` would force `Q[Y]` itself to be zero.  Hence
`Y_Qbar` is nonempty.  The weak Nullstellensatz gives a `Qbar`-valued point,
and an embedding `Qbar -> C` gives a complex point.  Its unit equation keeps
the source points distinct, while the determinant equations give constant
Jacobian one.  It is therefore a complex JC2 counterexample.

This transfer is conditional on all-depth survival of the same complete
fixed-support scheme.  No such survival is currently known.

## 4. Exact controls

The repaired portable replay source-pins the frozen three-ball control and
now asserts coefficientwise, before consuming it, that

```text
P mod 3=x-x^3,       Q mod 3=y.
```

It then replays the full determinant and the three unique Hensel preimages at
moduli 9 and 27 for

```text
P=x+2x^3+441x^5+108x^7,
Q=y-6x^2y+18x^4y-27x^6y.
```

The singular-Jacobian negative control remains `(x-x^3,3y)` modulo nine.

## 5. Firewall required at every campaign citation

The automatic-collision and characteristic-zero transfer may be cited only
after all of the following are stated:

1. one fixed finite set of allowed map monomials (actual support may drop);
2. every determinant coefficient equation at every consumed precision;
3. the same integral coefficient variables and AS residue component at every
   precision;
4. exact reconstruction from any digit/carry encoding by direct integer
   substitution;
5. arbitrarily deep survival of that same complete scheme.

The theorem does not apply to filtered high bands, a chronological state
that still owes lower source rows, growing support, changing normalization,
an unverified solver model, or finitely many depths.  In particular the
current Q5/H6 gate still owes Q4 through Q0 and is not a complete map modulo
243; no collision inference attaches there yet.
