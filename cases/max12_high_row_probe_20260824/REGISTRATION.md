# Registration — shared maximum-12 Faber high-row compiler

Date: 2026-08-24

## Registered theorem question

For a monic depressed polynomial `f` of degree `m` and a monic polynomial
`g` of degree `n` over a characteristic-zero differential field, does the
condition

```text
deg_z(f_x*g_z-f_z*g_x) <= m-2
```

force the unique Faber coefficients in

```text
w=f^(1/m),  F_j=[w^j]_+,  g=sum h_j F_j
```

to be differential constants?  In the maximum-twelve root-field Keller
normalization, does the remaining Laurent system become exactly

```text
r_1'=...=r_(m-2)'=0,  m*r_(m-1)'=j/u?
```

The registered specializations are `(8,12)` and `(9,12)`, including their
Kummer character filters, legal target quotient, exact quotient widths, all
eleven high-row checks, and a bounded reconstruction of `r_1,r_2` only.

## Inputs and conditionality

The replay pins the hostile-reviewed history and the frozen maximum-twelve
preflight.  The latter's own hostile review was live at producer freeze, so
the cell-specific use remains conditional on that review.  The universal
differential-field theorem and symbolic compiler do not consume a `(6,9)`
Faber formula.

No original Taylor boundary is discharged by this high-row calculation.
Every future trajectory must still reconstruct both complete families

```text
u^ell f^(ell)(A/m)/ell! in k[x],
u^ell g^(ell)(A/m)/ell! in k[x].
```

## Identities requiring independent review

With `H(w)-g(z(w))=sum r_l w^-l`, differentiation at fixed `w` must give

```text
D=-f_z*(partial_x g)|_w
 =-f_z*sum h_j'*w^j + f_z*sum r_l'*w^-l.
```

The sign and constant-field statement are load-bearing.  Descending
triangularity in degrees at least `m-1` must force all `h_j'=0`.  The
polynomials `A_l=[f_z*w^-l]_+` must have leading terms
`m*z^(m-1-l)` for `1<=l<=m-1` and vanish for `l>=m`, giving the displayed
terminal equation with positive sign.

Because `n<2m`, `P->P+q` must act exactly by

```text
h_k,new=h_k-((k+m)/m)*h_(k+m)*q,  0<=k<=n-m.
```

Together with `Q->Q-h_m*P` and `Q->Q-h_0`, this slices the three distinct
indices `(m,0,n-m)`.

## Mandatory cell controls

The first two integrated rows must be exactly

```text
(8,12): b10=3*a6/2+c10,
        b9=3*a5/2+11*delta0*a6/8+c9;
(9,12): b10=4*a7/3+c10,
        b9=4*a6/3+11*delta0*a7/9+c9.
```

Every high Jacobian row must vanish identically under differentiation along
every live `a_i`.  The Kummer/target quotient widths must be

```text
(8,12), orders 4/2/1: 7,10,16;
(9,12), orders 3/1:   9,17.
```

The first two Laurent rows are a control, not a component theorem.  Their
test ranks and local widths must be

```text
(8,12): ranks 2,2,2; widths 5,8,14;
(9,12): ranks 2,2;   widths 7,15.
```

The speed allocation `(9,12)` is licensed only under the explicitly stated
aggregate mandatory-route quotient metric (`33` versus `26`, or `27` versus
`22` after the two-row local ranks).  Raw width and widest-branch width favor
`(8,12)`.  No overall cheaper-cell theorem is registered.

## Replay and stop rules

Run:

```sh
python3 cases/max12_high_row_probe_20260824/shared_faber_probe.py
```

Any input hash mismatch, sign change, nonconstant Faber coefficient, high-row
residual, inverse-root residual, target-gauge collision, quotient-width
change, or specialized `r_1,r_2` digest change stops the producer claim.

Canonical JSON payload SHA-256:
`abbd72dc33aecd86d648696c138bcf5c919db6781a30447223fd184492d66a2d`.

Out of scope: a lower invariant-fibre component classification, trajectory
reconstruction, either frontier's emptiness, maximum-twelve automorphy,
arbitrary support, a counterexample, or JC2.
