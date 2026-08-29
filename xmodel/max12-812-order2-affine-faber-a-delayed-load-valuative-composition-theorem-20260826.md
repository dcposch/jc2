# Delayed-load affine-Faber `A`: valuative composition through the direct unit

Date: 2026-08-26

Status: **PROVISIONAL THEOREM.  EXACT FORMAL-WEIGHTED PRODUCER PASS/PASS;
DIFFERENT-MODEL HOSTILE REVIEW LIVE.  NO PROMOTION BEFORE REVIEW.**

## 1. Statement and scope

Work in characteristic zero on the fixed delayed-load affine-Faber
exceptional `A` chart

```text
k10=Lambda^12*K10,  k6=Lambda^8*K6,  k2=Lambda^4*K2,
Lambda=sigma^3,
```

and on `D(p*m*K10)`.  The repeated-root normal scale has order
`15` in `sigma`; write it as `sigma^15*lam`, with `lam` a unit.  Then no
formal or Puiseux arc on this fixed chart satisfies all seven source rows.

This theorem is internal to the exact affine-Faber `Q,N` chart.  It does
not assert total-fan coverage from the original coefficient space, does not
cover another delayed-load slope, and does not address `m=0`, `p=0`,
terminal/Taylor receivers, order two, maximum twelve, or JC2.

The earlier literal `q=6` producer remains narrow: its hostile review
(SHA-256 `06e2709344b47ec09549638a53f193b79ca4f791d40c2c0b9c8c04e0284330be`)
correctly returned `REPAIR` because it froze the center at
`a=sigma^5*a5`.  The argument below does not consume its full-face claim.

## 2. Exact two-sided coefficient coordinates on `D(M)`

Let

```text
Q=z^4+qp*z^2+qc*z+qr,
N=n3*z^3+n2*z^2+n1*z+n0
```

be the normalized quartic and cubic on the affine-Faber chart after the
normal radial factor has been extracted.  Put `M=n3` and localize at `M`.
Define

```text
a  = n2/M,
E  = qp+6*a^2,
U  = qc-2*a*(4*a^2-E),
R0 = qr-a^2*(E-3*a^2)+a*U,
V  = n1-(E-5*a^2)*M,
W0 = n0+a*(E-3*a^2)*M+a*V-M*U/2.                 (2.1)
```

With `A=z-a`, `B=4a`, and `D=A^2+B*A+E`, these identities are exactly

```text
Q=A^2*D+U*A+R0,
N=M*A*D+V*A+M*U/2+W0.                             (2.2)
```

Conversely, expanding (2.2) gives

```text
qp=E-6*a^2,
qc=2*a*(4*a^2-E)+U,
qr=a^2*(E-3*a^2)+R0-a*U,
n3=M,
n2=a*M,
n1=(E-5*a^2)*M+V,
n0=-a*(E-3*a^2)*M-a*V+M*U/2+W0.                 (2.3)
```

Thus (2.1) and (2.3) are inverse regular maps after localizing at `M`.
Existence, not uniqueness of a presentation with extra higher-order
`R1,S1` variables, is all the valuative argument needs.  There is no
analogy or endpoint projection here: this is a literal coefficient-ring
isomorphism on `D(M)`.

For a DVR arc, extract the common normal factor
`sigma^15*lam` from `N`; multiplying `lam` by a unit and dividing `M` by
that unit changes no equation.  On the `A` chart, `M mod sigma=m` is a
unit, `E mod sigma=p` is a unit, and `ord_sigma(a)>=5`.  A unit in the
source relation `Lambda=sigma^3*u` is removed after finite étale/formal
base extension by replacing `sigma` with `sigma*u^(1/3)`.  Hence the
normalizations used here exist after the already permitted finite
ramification; uniqueness is neither asserted nor required.

## 3. Kernel/complement splitting is exhaustive

At the moving double root, `U,V` are the two K2-kernel coordinates.  The
linear negative part of the unloaded quadratic tail for a correction

```text
delta Q=R1*A+R0,
delta N=S1*A+S0
```

is

```text
(3/8)*(2*M*S0-M^2*R1)/A -(3/8)*M^2*R0/A^2.       (3.1)
```

Since `M` is a unit, a leading complementary coefficient is either killed
by (3.1), or satisfies

```text
R0=0,  S0=M*R1/2.                                 (3.2)
```

In the latter case it is not complementary: replace

```text
U <- U+R1,   V <- V+S1;
```

then (3.2) is precisely the kernel form already present in (2.2).  Repeating
this leading-coefficient absorption after a common ramification gives an
exhaustive dichotomy: either an earlier unit linear pivot contradicts the
source rows, or all surviving transverse data are the two series `U,V`,
with the genuine `R0,W0` complements starting no earlier than twice their
first kernel order.  This proves existence of the weighted presentation
used by the formal producer; no symmetric-algebra or Rees-torsion claim is
needed.

Let `q=min(ord_sigma(U),ord_sigma(V))`, with `q=infinity` if both vanish.
On the exceptional chart `q>0`; the remaining cases are `0<q<6` and
`q>=6`.

## 4. Every rational `0<q<6` is empty before a load can enter

After finite ramification make `q` integral and let `x,y` be the leading
kernel residues, not both zero.  The first quadratic grade is

```text
30+2*q < 42.
```

All delayed loads and `mu2` start at grade 42, while the intrinsic cubic
starts at grade 45.  The moving-center connection is lower unitriangular;
positive-center terms multiply already-zero predecessor rows, so the first
analytic and ordinary source ideals agree.  The four relevant exact
initial rows are

```text
G1=-3*r1*m^2/8+3*s0*m/4,
G3=-3*p*r1*m^2/32-3*m*x*y/8+3*p*s0*m/16,
G4= 3*m^2*x^2/32-3*p*m^2*r0/16-3*p*y^2/16,
G6=-3*p^2*m^2*r0/64+3*p^2*y^2/64.                (4.1)
```

Hence

```text
G3-(p/4)*G1=-(3/8)*m*x*y,                         (4.2)
```

so `x*y=0`.  Equation `G6=0` gives `r0*m^2=y^2`.
If `x` is nonzero, then `y=r0=0` and
`G4=3*m^2*x^2/32`, a contradiction.  If `y` is nonzero, then `x=0` and
`G4=-3*p*y^2/8`, again a contradiction.  The two residue charts exhaust
the nonzero leading kernel.  This argument is homogeneous, so it covers
every rational `0<q<6`, not only integral sigma jets.

## 5. The formal direct unit kills every `q>=6`

The controlling exact producer is

```text
0ef7cfc84691c5fa466e98cf76f942d6bcd217547d0eb91b0f3860240da8eae5
  cases/max12_812_order2_affine_faber_a_formal_weighted_h3_h5_identity_20260826/FREEZE.sha256
86883cc16a48e0ee4b4a1ea01844cedbdd212eb41414fe918f641d6654582f48
  cases/max12_812_order2_affine_faber_a_formal_weighted_h3_h5_identity_20260826/EVIDENCE.sha256
5736a3b00ec6e1b74b43c5112b8fadccf340b98558854b63ddd6ca9042d8370d
  cases/max12_812_order2_affine_faber_a_formal_weighted_h3_h5_identity_20260826/RESULT.md
```

It uses algebraically independent `a,E,M,U,V,R,S,lam` and independent
load symbols in all seven frozen complete tails.  With the minimum weights

```text
a:5, U:V:6, R:S:12, normal scale:15, loads/mu2:42,
```

exact Q proves, before imposing any predecessor row,

```text
H3=-(3/8)*sigma^42*lam^2*M*U*V
    -(1/16)*sigma^45*lam^3*M^3                 mod sigma^46,

H5=(3/8)*sigma^42*E*lam^2*M*U*V               mod sigma^46.  (5.1)
```

Therefore

```text
[sigma^45](E*H3+H5)=-E*lam^3*M^3/16,             (5.2)
```

a unit on `D(E*lam*M)`.  The load coefficient `K10` is retained and a
unit on the named source chart, although (5.2) is stronger and independent
of its value.

Because (5.1) is a polynomial congruence in every displayed symbol,
substitution of arbitrary power series preserves divisibility by
`sigma^46`.  It therefore includes every omitted `a6` and later center
coefficient, all tangent and complement series, and every higher kernel
monomial in the complete tails.  If a common ramification has degree `e`,
replace `sigma` by `tau^e`; for a rational `q>=6`, further substitute
`U=tau^(eq-6e)*U'` and similarly for `V` when needed.  All weights only
increase, while (5.2) becomes a unit at grade `45e`.  Thus no fractional
or unequal-order kernel face escapes the identity.

## 6. Complete load and target timing through grade 45

On the delayed ray the three effective lower loads begin together at
global `Lambda^14`, hence sigma grade 42.  Their arbitrary later
coefficients are obtained by substituting power series for the three
independent weight-42 load symbols in (5.1).  A load times the moving
center has grade at least `42+5=47`; a load times a kernel variable has
grade at least `42+6=48`.  The exact producer confirms that no load
monomial survives in `H3,H5` through grade 45.

The source targets have exact timing

| target | source power | sigma grade |
|---|---:|---:|
| `mu2` in `P2` | `Lambda^14` | 42 |
| `mu4` in `P4` | `Lambda^16` | 48 |
| `mu6` in `P6` | `Lambda^18` | 54 |
| `J/4` in `P7` | `Lambda^19` | 57 |

Only `mu2` can occur in an ordinary row by grade 45, and the producer
retains it.  In `H3` it is multiplied by `B=4a`, so its first possible
contribution is grade 47.  In `H5`, every `P2` target term is again
multiplied by a positive power of `B`, while the first `P4` target is not
present until grade 48 (and its connection coefficient has another
positive `B`).  Rows `P1,P3,P5` have no direct target.  Therefore no
omitted target can tie (5.2).

## 7. Consequence and firewall

Sections 2--6 cover every valuation inside the fixed delayed-load repeated
`A`, `D(p*m*K10)` affine-Faber chart: `0<q<6` dies at its unloaded quadratic
face, and `q>=6` dies by the center-complete formal direct unit.  The
earlier q6 and half-weight finite compilers are corroboration or deployment
history only.

Promotion is withheld until the live different-model review confirms the
formal identity and the valuative coordinate composition.  Even after
confirmation, this is not a total-Rees atlas theorem for every order-two
source stratum; the global overlap from the original coefficient source to
the named affine-Faber chart, other load slopes, `D(p*m*K10)` complement,
terminal/Taylor, the Pell receiver, order two, maximum twelve, and JC2
remain separate.
