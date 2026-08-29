# Hostile audit: endpoint-survivor parametrization and codimension R6

Date: 2026-08-27  
Reviewer lane: `a1_total_lift_design` / Sol2  
Target producer:
`xmodel/ggv-endpoint-survivor-codimension-r6-sol-20260827.md`, SHA-256
`ed0e3460cc16d0d8b9fb25823dc09f56bb4b1ad41561744bc8713848128fad19`  
Target case freeze:
`cases/ggv_endpoint_survivor_codimension_r6_20260827/FREEZE.sha256`,
SHA-256
`9c23f3f5e99672208e49bebca17b38b81b9190537a08aa4ffd1127132f148bd4`  
Conditional premise: the exact R5 statement frozen at
`cases/ggv_keller_face_general_multiplicity_endpoint_r5_20260827/FREEZE.sha256`,
SHA-256
`3d8ba26743a5c77bf37694ec0118a221a9c5fa1faff6fffb426659010a51c419`.

## Verdict

**PASS, CONDITIONAL ON R5 AT ITS STATED RATIONAL-ENDPOINT SCOPE.**

The canonical decomposition, normalized parametrization, degree laws,
dimensions, codimensions, and degree-eight census are correct.  Shared
factors of `A` and `B` cause no ambiguity.  The normalized map has no hidden
stabilizer and is point-injective, hence quasi-finite onto its constructible
image and dimension-preserving.

One nonblocking precision should accompany promotion: fixed-`b` images need
not be closed.  Their codimension is the codimension of their Zariski
closures, equivalently `h-dim(image)` for these constructible sets.  With
that standard meaning, R6's bound is valid; indeed for every `h>=1` the full
survivor locus has codimension **exactly** `floor(h/2)`, not only at least
that value.  This strengthening does not enlarge the endpoint scope.

R6 remains only a parametrization of rational endpoint silence.  This
review does not turn it into formal-jet sufficiency, raw GGV landing, or a
face/family exclusion, and it does not independently promote R5.

## Charged-point table

| Charged point | Verdict |
|---|---|
| Unique monic `H=A^2B`, allowing `gcd(A,B)!=1` | **PASS** |
| Necessity of `A=N_B(v)` parametrization | **PASS, conditional on R5** |
| Sufficiency of every normalized `(B,v)` point | **PASS, conditional on R5** |
| Degree/parity law `r=(h-3b+2)/2` | **PASS** |
| Fixed-`b` dimension `b+r=a+1` | **PASS** |
| Fixed-`b` codimension `(h+b-2)/2` | **PASS in constructible/closure sense** |
| Hidden fibers or stabilizers | **NONE after both monic normalizations** |
| Full-locus minimum codimension | **PASS; exact value is `floor(h/2)`** |
| `h=8` survivors `b=0,2` with dimensions four | **PASS** |
| Equivalence of the `b=2` parametrization and `4a0+D*a2=0` | **PASS** |
| Closedness of each fixed-`b` image | **FALSE but not claimed; explicit degeneration below** |

## 1. Canonical square/squarefree decomposition

Over the algebraically closed characteristic-zero field, write

```text
H=product_alpha (X-alpha)^e_alpha.
```

The unique monic decomposition is

```text
A=product_alpha (X-alpha)^floor(e_alpha/2),
B=product_alpha (X-alpha)^(e_alpha mod 2).
```

Thus `B` is squarefree and `H=A^2B`.  When `e_alpha` is odd and at least
three, `(X-alpha)` divides both `A` and `B`; this is expected and does not
create a second decomposition.  Conversely, for every monic `A` and monic
squarefree `B`, the exponent `2 ord_alpha(A)+ord_alpha(B)` recovers both its
half and its parity, so the same formulas recover the original pair.

The smallest shared-factor fixture is

```text
B=X,
v=(2/5)X,
N_B(v)=Xv'+(3/2)B'v=X=A,
H=A^2B=X^3.
```

Here `A=B=X`, yet the canonical decomposition and the endpoint equation are
both exact.  Any repair imposing `gcd(A,B)=1` would wrongly delete this
survivor.

## 2. Completeness and normalization of the parametrization

For monic squarefree `B` of degree `b>=1` and nonzero `v` of degree `r`,

```text
N_B(v)=Bv'+(3/2)B'v,
deg N_B(v)=r+b-1,
lc N_B(v)=(r+(3/2)b)lc(v).
```

The last scalar is nonzero in characteristic zero.  Consequently `N_B` is
injective on polynomials.  If `deg A=a`, the equation `A=N_B(v)` forces

```text
r=a-b+1=(h-3b+2)/2,
```

and forces

```text
lc(v)=1/(r+(3/2)b).
```

This proves necessity from R5.  Conversely, choose squarefree monic `B`
and a degree-`r` polynomial with precisely this leading coefficient.  Then
`A=N_B(v)` is monic of degree `a`, `H=A^2B` is monic of degree `h`, and
Section 1 shows that its canonical squarefree factor is the chosen `B`,
even when `A` and `B` share factors.  The same `v` therefore satisfies R5,
which proves sufficiency at the rational endpoint.

Both normalizations are load-bearing.  If the leading coefficient of `v`
is not fixed, then the shared-factor fixture has `v` and `-v` mapping to the
same `H=X^3`; they give `A` and `-A`.  Requiring `N_B(v)=A` monic removes
this order-two ambiguity.  There is no remaining continuous or finite
stabilizer: equality of two image polynomials first recovers canonical
`B`, then monic `A`, then `v` by injectivity of `N_B`.

## 3. Geometry and exact dimension

For fixed allowed `b>0`, let `U_b` be the discriminant-nonzero open subset
of the affine space of monic degree-`b` polynomials.  After fixing the
leading coefficient, the `v` parameters form `A^r`.  Hence the source of

```text
phi_b : U_b x A^r -> A^h_monic,
(B,v) |-> N_B(v)^2 B
```

is irreducible of dimension

```text
b+r=a+1=(h-b+2)/2.
```

The map is polynomial and point-injective by Section 2.  It is therefore
quasi-finite onto its image; the fiber-dimension theorem gives

```text
dim im(phi_b)=b+r,
codim closure(im(phi_b))=h-(b+r)=(h+b-2)/2.
```

Chevalley's theorem supplies constructibility.  No closed-image assumption
is needed for this count.  In fact a fixed-`b` image can fail to be closed.
For `h=8`, set

```text
B_s=X^2-s^2,
v=X^2/5,
A_s=N_(B_s)(v)=X^3-(2/5)s^2 X,
H_s=A_s^2 B_s.
```

For `s!=0` these are `b=2` survivors, whereas `H_0=X^8` has canonical
`b=0`.  Thus the closure of the `b=2` image meets the `b=0` stratum.  This
is why codimension must be read in the constructible/Zariski-closure sense.

For `b=0`, the monic square-root `A` has `h/2` free coefficients.  For even
`h` this stratum is nonempty and has codimension `h/2`.  For odd `h`, the
`b=1` stratum is nonempty and has dimension `(h+1)/2`, hence codimension
`(h-1)/2`.  All other allowed strata have at least this codimension.  The
finite union therefore has exact codimension

```text
floor(h/2).
```

## 4. Degree eight and independent fixtures

At `h=8`, parity and `r=(10-3b)/2` give

```text
b=0: perfect squares, dimension 4, codimension 4;
b=2: r=2, dimension 2+2=4, codimension 4;
b=4,6,8: r=-1,-4,-7, hence empty.
```

For the `b=2` branch, center the quadratic as `B=z^2-D`, `D!=0`, and write
`v=v2*z^2+v1*z+v0`.  Exact expansion gives

```text
N_B(v)=5v2*z^3+4v1*z^2+(3v0-2D*v2)z-D*v1.
```

Monicity fixes `v2=1/5`.  Therefore every image satisfies
`4a0+D*a2=0`; conversely that relation reconstructs uniquely
`v1=a2/4` and `v0=(a1+2D/5)/3`.  This confirms equivalence, not just
necessity.

An independent sparse-Q polynomial evaluator, not importing `verify_r6.py`,
checked:

```text
all parity/dimension/codimension rows for 1<=h<=100;
min codimension = floor(h/2) at every h;
B=X, v=2X/5 gives A=X and H=X^3;
B=X^2-3, v=X^2/5+2X-7 gives
  A=X^3+8X^2-(111/5)X-6 and 4a0+3a2=0;
B_s=X^2-s^2, v=X^2/5 specializes at s=0 to H=X^8.
```

The frozen producer replay also passes, but it was used only as a custody
check; the census and fixtures above were recomputed independently.

## Scope firewall

This PASS is conditional on R5's exact rational-endpoint equivalence.  It
does not review the earlier mode-lifting part of R5, prove that any endpoint
survivor extends to a formal jet, construct raw `2S/3S` provenance, establish
GGV landing, exclude an `8_28` face or family, or imply `G2-PSC`, `G2-BD`, a
Keller counterexample, or JC2.
