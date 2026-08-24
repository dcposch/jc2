# Shared Faber high-row compiler and two-Laurent-row probe for `(8,12)` / `(9,12)`

**Status: `PRODUCER-INTERNAL, EXACT, FROZEN FOR DIFFERENT-MODEL REVIEW`.**

**Verdict.**  The high-row integration is not cell-specific.  Over the
differential root field, every monic depressed pair of degrees `(m,n)` whose
Jacobian has `z`-degree at most `m-2` has a unique Faber form

```text
w=f^(1/m),     F_j=[w^j]_+,     g=sum_(j=0)^n h_j F_j,
```

and all `h_j` are constants.  If the original Keller constant is `j` and
`z=uy+r`, the complete remaining system is

```text
r_1'=...=r_(m-2)'=0,       m r_(m-1)'=j/u.           (0.1)
```

An exact shared compiler reconstructs and verifies all eleven high rows in
both maximum-twelve cells, plus the first two Laurent invariants as a bounded
control.  After character filters and the three legal target translations,
the high-row quotient coordinate widths are

```text
(8,12): 7,10,16 on Kummer orders 4,2,1;
(9,12): 9,17    on Kummer orders 3,1.
```

This does not produce a global cheaper-cell theorem.  For speed allocation,
the declared aggregate mandatory-route width is `33` versus `26`, and the
aggregate two-row local width at the exact test points is `27` versus `22`.
That cost rule selects `(9,12)` for the next lower-fibre probe.  The widest
single branch remains smaller for `(8,12)` (`16` versus `17`), so a different
cost rule can rationally choose the other cell.

No lower-fibre component is classified and neither frontier is excluded.

## 1. Provenance and scope

The replay pins:

| Input | SHA-256 |
|---|---|
| reviewed history producer | `6994dd6bc1642122ba549be474d2465203faf554d93da5146ecb212dbaaf89fe` |
| reviewed history verdict | `f9d547f0f17dc3557ed8edce19912b4930dc2125542c7f9b3e4782c554a03afd` |
| frozen max-12 preflight report | `30cb45ccb64bc3666a8f1c6b223d89654a69b31bd5e96eb8915718b0f2de7b07` |
| max-12 preflight freeze | `59ef0712aea2424ea57b6f1727031018e769701b0f2e2384eb4638f4286ea558` |

The preflight's hostile review was still running when this probe was
produced, so every cell specialization remains producer-internal.  The
universal differential identity below is re-derived and checked rather than
imported from a `(6,9)` coefficient expansion.

The root-field normalizations and all original polynomial boundaries remain
charged.  In particular this calculation does not replace the conditions

```text
u^ell f^(ell)(A/m)/ell! in k[x],
u^ell g^(ell)(A/m)/ell! in k[x].                     (1.1)
```

## 2. Universal differential-field Faber theorem

Let `K` be a characteristic-zero differential field with derivation prime.
Take

```text
f=z^m+a_(m-2)z^(m-2)+...+a_0,
g=z^n+b_(n-1)z^(n-1)+...+b_0.
```

At `z=infinity`, let `w=f^(1/m)=z+O(z^-1)`.  The polynomials
`F_j=[w^j]_+` are monic of degree `j`, so triangularity gives a unique
expansion

```text
g=sum_(j=0)^n h_j F_j,       h_n=1.                  (2.1)
```

Define the negative tail by

```text
H(w)-g(z(w))=sum_(ell>=1) r_ell w^-ell,
H(T)=sum_(j=0)^n h_j T^j.                            (2.2)
```

For

```text
D=f_x g_z-f_z g_x,
```

differentiate at fixed `w`.  Since fixed `w` is fixed `f`,

```text
D=-f_z (partial_x g)|_w
 =-f_z sum h_j' w^j + f_z sum r_ell' w^-ell.         (2.3)
```

This fixes the sign: the terminal Laurent term occurs with a plus sign.
The second sum has polynomial `z`-degree at most `m-2`.  In the first sum,
the polynomial part of `f_z w^j` has leading term
`m z^(m-1+j)`.  If `deg_z D<=m-2`, descending triangularity forces

```text
h_0'=...=h_(n-1)'=0.                                 (2.4)
```

They lie in the constant field of `K`; for the algebraic Kummer extensions
used here this is the scalar field after the already licensed harmless
constant extension.

Now put

```text
A_ell=[f_z w^-ell]_+.
```

For `1<=ell<=m-1`, `A_ell` has leading term
`m z^(m-1-ell)`; for `ell>=m`, it is zero.  Hence the matrix from
`(r_1',...,r_(m-1)')` to the rows `z^(m-2),...,1` and the constant row is
triangular with determinant `m^(m-1)`.  In the Keller normalization,
`J_(x,y)=uD=j`, so `D=j/u`, and (0.1) follows exactly.

This proves the complete high-row Faber landing in both new cells.  It does
not solve any algebraic fibre of the constants `r_ell`.

## 3. Cell-specific exact controls

Write `delta0=-delta/r` for the coefficient of `z^(n-1)`.  The first two
integrated high rows are:

| Cell | First row | Second row | All high `D` rows checked |
|---|---|---|---:|
| `(8,12)` | `b_10=(3/2)a_6+c_10` | `b_9=(3/2)a_5+(11/8)delta0*a_6+c_9` | `z^17` through `z^7` |
| `(9,12)` | `b_10=(4/3)a_7+c_10` | `b_9=(4/3)a_6+(11/9)delta0*a_7+c_9` | `z^18` through `z^8` |

The replay constructs every `F_j` by the exact finite binomial expansion

```text
F_j=z^j [sum_k binom(j/m,k) U^k]_+, 
U=sum_(i=0)^(m-2) a_i z^(i-m),                       (3.1)
```

then differentiates the resulting `g` with respect to every `a_i` and
checks that every displayed high row vanishes.  Both cells have eleven high
rows.  The full lists of `b_10,...,b_0` have 242 sparse coefficient
monomials in either cell; the largest single support is 64 for `(8,12)` and
66 for `(9,12)`.

As a separate lower-row falsifier, the compiler solves `f(z(w))=w^m`
recursively through `w^-(n+1)`, rechecks every solved coefficient, and
extracts `r_1,r_2` from (2.2).  It does not expand `r_3` through the terminal
invariant.

## 4. Exact target quotient

Because `n<2m` in both cells, the target translation `P->P+q` has the finite
triangular action

```text
h_k,new = h_k - ((k+m)/m) h_(k+m) q,   0<=k<=n-m,    (4.1)
```

where `h_n=1`.  Thus it always slices `h_(n-m)=0`.  The two other legal
operations slice

```text
Q->Q-h_m P: h_m=0,        Q->Q-h_0: h_0=0.           (4.2)
```

The indices are distinct:

```text
(8,12): 8,0,4;       (9,12): 9,0,3.
```

For a nontrivial Kummer class of order `e`, the constant `h_j` can survive
only when `j=0 mod e`.  All three gauge indices are multiples of every
`e|d`, so the quotient is character-compatible.  For `e=1`, all twelve
constants, including `delta0=h_11`, are initially retained.

## 5. Quotient and bounded two-row widths

“High-row width” below means the number of live coefficient functions of
`f` plus scalar Faber constants after (4.1)--(4.2).  “Two-row local width”
subtracts the exact rank of `(r_1,r_2)` at the replay's deterministic rational
test point.  Rank two at one point proves only independence there; it is not
a component dimension theorem.

| Cell/order | Constants after quotient | High-row width | `r_1/r_2` supports | Test rank | Two-row local width |
|---|---|---:|---:|---:|---:|
| `(8,12)`, `e=4` | none | 7 | `19/27` | 2 | 5 |
| `(8,12)`, `e=2` | `h_2,h_6,h_10` | 10 | `36/54` | 2 | 8 |
| `(8,12)`, `e=1` | 9 constants | 16 | `79/99` | 2 | 14 |
| `(9,12)`, `e=3` | `h_6` | 9 | `25/36` | 2 | 7 |
| `(9,12)`, `e=1` | 9 constants | 17 | `80/106` | 2 | 15 |

This table resolves several possible misleading comparisons:

- raw constant-W size and widest-branch width favor `(8,12)`;
- the order-four `(8,12)` leaf is the narrowest single leaf;
- the mandatory order-two leaf broadens the nontrivial `(8,12)` route from
  width 7 to a second width-10 leaf;
- `(9,12)` has only one nontrivial leaf, of width 9; and
- the polynomial-core leaves differ by only one function coordinate and
  have almost identical first-two-row support.

Summing widths across disjoint mandatory route leaves is an engineering cost,
not an algebraic dimension.  It gives `33` versus `26` before the two lower
rows and `27` versus `22` after the rank-two test.  On that explicitly stated
speed metric, the next lower-fibre allocation should be `(9,12)`, with the
order-four `(8,12)` leaf retained as the cheapest control.  No statement that
`(9,12)` is mathematically simpler overall is licensed.

## 6. Replay and stop boundary

Run:

```sh
python3 cases/max12_high_row_probe_20260824/shared_faber_probe.py
```

The replay is pure stdlib sparse algebra over `Q` and is stable under four
tested hash seeds.  It prints per-branch digests for the specialized
`r_1,r_2` polynomials so a second engine can compare exact bytes without
printing hundreds of monomials.

The terminal boundary is:

```text
complete universal high-row Faber integration=PROVED/REPLAYED
lower Laurent invariants reconstructed=ONLY r_1,r_2 CONTROL
lower-fibre components=NOT CLASSIFIED
either maximum-12 frontier empty=false
overall cheaper cell=NOT CLAIMED
JC2=NOT CLAIMED
```
