# `(8,12)` order two: quadruple-square odd-face grades eleven and twelve

Date: 2026-08-26

Status: **CORRECTION-AWARE EXACT-SOURCE CLIENT DESIGN.  THE QUADRATIC SHEET
BELOW IS A HAND PREDICTION UNTIL THE FROZEN SOURCE REPLAY PASSES.  NO
SQUARE-BRANCH OR ORDER-TWO VERDICT.**

## 0. Scope and charged inputs

This is the first collision-chart successor to the raw grade-ten
half-weight ideal at `p=0`.  It treats the reduced odd face

```text
L=z^2,       R=cs0*z,       C=0,       rs=0,
```

on `D(cs0*k0)`.  It consumes the reviewed generic half-weight receiver and
the sharpened third-tail source theorem, which has already forced the lower
square coordinate `M` to vanish.  The exact lower-hull reduction at SHA-256
`d3d8f30a94a3d90175756ea0e21efd974461d51cb2db8433d2a270e1be355337`
is fan bookkeeping only; in particular `kR2A` remains a source sentinel but
does not index a primitive face.

No radical or localization is substituted into the complete source before
both new grades have been formed.

## 1. Primitive correction-aware collision cone

Keep the first two collision jets and the first conormal corrections:

```text
Lambda = sigma^2,
p      = 2*sigma*ell1+2*sigma^2*ell2,
Lsig   = z^2+sigma*ell1+sigma^2*ell2,

R = R0+sigma*R1+sigma^2*R2,
R0=cs0*z,
R1=cs1*z+rs1/4,
R2=cs2*z+rs2/4,

A = A0+sigma*A1+sigma^2*A2,
A0=a1*z+a0,
A1=aa1*z+aa0,

C = sigma*E1+sigma^2*E2,
E1=(e1*z+e0)/2,
E2=(ee1*z+ee0)/2,

k10=k0+sigma*k1+sigma^2*k2c.
```

As in the reviewed half-weight chart,

```text
K=Lsig^2+sigma^2*R,
N=sigma^3*(Lsig*A+C),
f=K^2+sigma^5*(Lsig*A+C).
```

The variables `R2,A2,k2c` are retained in the complete source.  They are
predicted to be absent from the negative grades eleven and twelve, rather
than deleted in advance.  The lower loads `k6,k2`, all seven targets, and
their exact frozen powers are likewise retained.

The cone is minimal in the following sense.  A first `p` jet and a first
`C` correction can already contribute at grade eleven.  The constant part
of `R1` first contributes quadratically at grade twelve.  The odd base term
`R0^3/z^2=cs0^3*z` is polynomial at grade ten, while the next binomial term
`R0^4/z^6` has its first pole at grade twelve.

## 2. Exact hand receivers

Put `L=z^2`.  The predicted complete negative receivers are

```text
h11 = [
   (3/4)*A0*E1/L
  -(5/16)*k0*ell1*R0^3/L^2
]_- .                                                (2.1)
```

and

```text
h12 = [
   (3/4)*(A0*E2+A1*E1)/L
  -(3/4)*ell1*A0*E1/L^2
  +(3/8)*E1^2/L^2
  -(3/8)*R0*A0^2/L^2
  +(5/8)*k0*E1*R0/L

  +(5/16)*k0*(
       3*R0*R1^2/L
      -3*ell1*R0^2*R1/L^2
      +ell1^2*R0^3/L^3
      -ell2*R0^3/L^2
    )
  -(5/16)*k1*ell1*R0^3/L^2
  -(5/128)*k0*R0^4/L^3
]_- .                                                (2.2)
```

Here the `3*R0*R1^2/L` bracket includes its polynomial part before
`[_-]` is taken.  Formula (2.2) retains every tie at this grade:

- `E1^2`, `R0*A0^2`, and the fourth binomial of `K^(5/2)`;
- the first and second moving-centre terms in `1/Lsig`;
- the constant-direction square in `R1`;
- the loaded cross term `(5/8)k0*E1*R0/L`; and
- the first moving-load coefficient `k1`.

Terms containing `R2,A2,k2c` are polynomial or later.  The leading `k6`
term at absolute grade twelve is polynomial; `k2` and the targets are later.
The source compiler must verify those statements by forbidden-variable
sentinels.

Because the ordinary frozen rows use the moving square base, their exact
grade connection is part of the contract.  If `h_d[j]` denotes the
coefficient of `z^(-j)`, then

```text
g11[ell] = h11[ell],
g12[ell] = h12[ell]
          + ((ell-2)/2)*ell1*h11[ell-2]   (ell>=3),  (2.3)
```

with the second summand zero for `ell<3`.  This is the first derivative of
the reviewed lower-unitriangular transform after
`p=2*sigma*ell1+O(sigma^2)`.  A byte match of source rows without (2.3) is
not an accepted endpoint.

## 3. Raw coefficient ideal and predicted support

Write `b=cs0`.  The two grade-eleven coefficients are

```text
[z^-2]h11 = (3/8)*a0*e0,
[z^-1]h11 = (3/8)*(a1*e0+a0*e1)
             -(5/16)*k0*ell1*b^3.                   (3.1)
```

Keep all coefficients of (2.1)--(2.2) as the raw ideal.  On `D(b*k0)` they
give the following deductions, but only after the raw source ideal has been
formed:

1. `[z^-4]h12` modulo (3.1) is `(3/32)e0^2`, hence `e0=0` on the reduced
   support.
2. `[z^-3]h12+ell1*[z^-1]h11` is
   `(3/16)e1*e0-(3/8)b*a0^2`, hence `a0=0`.
3. The second row of (3.1) then forces `ell1=0` on `D(b*k0)`.
4. The remaining `z^-2` row is exactly

   ```text
   12*e1^2-5*k0*b^4=0.                              (3.2)
   ```

The last `z^-1` equation survives and must remain raw.  After the preceding
reduced substitutions it is

```text
F = (3/8)*(a1*ee0+aa0*e1)
    -(3/8)*b*a1^2
    +(15/256)*k0*b*rs1^2
    -(5/16)*k0*ell2*b^3.                            (3.3)
```

Thus the predicted localized radical is the radical of

```text
(e0,a0,ell1,12*e1^2-5*k0*b^4,F),                   (3.4)
```

not merely the four-generator support obtained by projecting the final
ordinary row.  The client must compare both containments generator by
generator and print the complete unsaturated and localized raw bases.

The zero-new-correction slice `E1=0` would make (3.2) a false contradiction
on `D(b*k0)`.  It is not correction-aware and must not be used to kill the
odd face.

## 4. Normalization, decks, and overlap

The survivor (3.2) is already regular over the total campaign parameter
space on `D(b*k0)`, since its derivative with respect to `k0` is `-5*b^4`.
Its cheapest rational normalization is

```text
u=e1/b^2,       k0=(12/5)*u^2,       b*u != 0.       (4.1)
```

Hence the total sheet is rational in `(b,u,...)`.  Over a fixed nonzero
load `k0`, it is a Kummer double cover with deck action

```text
u -> -u,       e1 -> -e1.                            (4.2)
```

For the root-separation overlap write

```text
rho=sigma*rho1+...,
p=-2*rho^2,
ell1=0,
ell2=-rho1^2.                                      (4.3)
```

The root deck is `rho1 -> -rho1`, independent at this stage from the sheet
deck (4.2).  At the two separating roots the leading values are

```text
R(+-rho)=sigma*(+-b*rho1+rs1/4)+...,
C(+-rho)=+-sigma^2*(e1*rho1/2)+...,
A0(+-rho)=+-sigma*(a1*rho1)+....                    (4.4)
```

Equation (4.4) is the exact overlap map to be checked against the reviewed
root-value low-contact clients.  It suggests the unit-load valuation
`(a,r,c)=(1,1,2)` away from cancellations, but this note does not import a
generic-square verdict: each orientation and the loci
`rs1/4=+-b*rho1` must be retained.

## 5. AWS contract and immediate successors

The minimal producer is exact `Q` plus an independent `F_65521` control.
It must reconstruct all seven charged source rows, verify divisibility by
`sigma^11`, extract grades eleven and twelve without a coefficient-API
shortcut, certify (2.1)--(2.3), retain the raw ideal, and compare (3.4) only
after localization by `b*k0`.  No saturation by `e0,a0,ell1,e1,u,F` is
allowed.

Once exact `Q` passes, use (4.1) provisionally without waiting for hostile
review and launch three independent pullbacks on the rational sheet:

1. terminal `[6,2]`, retaining `F=0` as a raw predecessor row;
2. the first finite Taylor/polynomiality family; and
3. the second finite Taylor/divisibility family.

Each pullback keeps `b,u,a1,aa0,rs1,ell2` and every still-free correction,
substitutes `k0=(12/5)u^2`, and eliminates `ee0` only on a chart where the
coefficient multiplying it in (3.3) is proved invertible.  Otherwise (3.3)
remains an equation.  A unit, cross-route, or new component is reported per
sheet/deck chart; no projected terminal calculation is accepted.

## 6. Explicit nonclaims

This client covers one primitive collision cone over the odd grade-ten face.
It does not cover fractional slopes outside the displayed normalization,
the grade-ten cusp on `D(rs)`, every higher collision jet, the full seven-form
positive-order-load fan, or the loci removed by `D(cs0*k0)`.  Even a passing
source replay establishes only the rational quadratic sheet (3.2)--(3.4) as
a necessary successor.  It does not construct or exclude a strict arc,
close the square component, close order two or `(8,12)`, prove maximum
twelve, or prove JC2.
