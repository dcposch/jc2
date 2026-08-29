# Result: D1 `a=7` first load-tie wall

Date: 2026-08-26

Status: **TRIPLE-AWS EXACT-Q PRODUCER PASS; AWAITING HOSTILE REVIEW.**

## Exact producer theorem

After the registered square/D1 source gates, over characteristic zero on
`D(p*k0)`, the seven literal Faber equations have no point in either of the
two strict contact tails

```text
ord(A)=7, ord(C)=9,  ord(R)>=7,     (d=2),
ord(A)=7, ord(C)=10, ord(R)>=7.     (d=3)
```

The first load-tie and pole-two target grades are respectively

| `d` | first wall `G` | pole-two target `T` | primitive columns |
|---:|---:|---:|---:|
| 2 | 26 | 28 | 5 |
| 3 | 27 | 30 | 7 |

The source leaves the leading `R` coefficient uninverted, so these are the
entire closed `ord(R)>=7` tails.  Exactness of `ord(C)` means that the two
leading coefficients of `C` are not simultaneously zero; the two charts
`D(c1)` and `D(c0)` exhaust that condition.

## First-wall rank jump

At grade `G`, the complete source has exactly the tied pair

```text
(3/4)*C*(A+k60)/L.
```

Writing `A+k60=u*z+v` and `C=x*z+y`, its proper numerator is

```text
r_z=u*y+v*x,
r_0=v*y-(p/2)*u*x.
```

Multiplication by `C` in `Q[z]/(z^2+p/2)` has determinant

```text
Delta_C=y^2+(p/2)*x^2.
```

The producer reconstructs the tied column from the full analytic source
and verifies that on `D(Delta_C)`, `r_z=r_0=0` forces `u=v=0`.  It does not
discard the rank-one face `Delta_C=0`; that face is covered by the two
root functionals below.

## Dual-functional obstruction

The independently mined complete source has global pole ceiling two and
exactly one pole-two primitive through `T`, namely

```text
(3/8)*C^2/L^2
```

at grade `T`.  If `h1,...,h7` are the analytic Laurent rows, the producer
reconstructs

```text
N=h1*z^3+h2*z^2+(h3+p*h1)*z+(h4+p*h2),
H=N/L^2.
```

Over the finite etale root cover, let
`lambda(sigma)^2=-p(sigma)/2`.  The two exact Faber connections are

```text
Psi_+ = Phi4+lambda*(Phi3+(p/4)*Phi1)=N(lambda),
Psi_- = Phi4-lambda*(Phi3+(p/4)*Phi1)=N(-lambda).
```

Every pole-one source column, including all corrections of both tied
columns and every later load, pairs to zero below `T`.  At `T` the two
pairings are exactly

```text
q_+=(3/8)*(c1*lambda+c0)^2,
q_-=(3/8)*(-c1*lambda+c0)^2.
```

The exact-Q client verifies

```text
(q_+,q_-)=1 on D(lambda*c1*k0),
(q_+,q_-)=1 on D(lambda*c0*k0).
```

Thus the paired Faber rows cannot vanish on either exact-contact chart.
These charts cover every nonzero leading `C`; the finite etale root cover
is surjective on `D(p)`, so emptiness descends to the unsplit chart.  This
also covers the rank-one face of the first-wall multiplication matrix
without dividing by `Delta_C`.

## Complete source and target custody

For each of `d=2,3`, the producer:

1. independently enumerates all four binomial source summands and checks
   the same inventory after one unit of padding;
2. derives every `A,C,R`, moving-`p`, `k10`, `k6`, `k2`, `mu2`, and `mu4`
   jet ceiling mechanically from the complete primitive inventory;
3. emits all seven literal Faber source rows, including delayed loads and
   every licensed target, and bridges them modulo `sigma^(T+1)` to an
   independent analytic Laurent emitter;
4. verifies every sigma quotient, the moving-root equations, the full
   pole-two recurrence, the tied first column, the off-`Delta_C` rank,
   both functional pairings, and both chart unit ideals;
5. keeps rows 1, 3, and 4 target-free through `T` and retains the row-2
   target beginning at grade 28 (including its jets through grade 30 for
   `d=3`).

Exact Q is the characteristic-zero endpoint.  The independent
`F_65521` and `F_65519` runs are host/software screens only; all three
produce the same exact census stream.

## AWS custody

Box03 exact Q, r6d `F_65521`, and Box02 `F_65519` each return engine rc
zero and `PASS_D1_A7_LOADTIE_DUAL_FUNCTIONAL_D2_D3_EMPTY`.  Compiler
stderr is empty, no Singular diagnostic appears, and all runs record zero
swap.  Full launch/resource custody is in `AWS_LAUNCH_METADATA.md`; every
retrieved evidence byte is pinned by `EVIDENCE.sha256`.

## Firewall

This producer closes only the two named strict `a=7`, `d=2,3`,
`ord(R)>=7` tails after the cited upstream gates.  It does not cover an
equality face, a positive-order leading load, `a=8,9`, the grade-32/34
row-4 target-shadow chambers, another D1 face, `p=0`, `k0=0`, a
terminal/global chart, the whole square component, order two, `(8,12)`,
maximum twelve, or JC2.  No timing or emptiness claim may be extrapolated
to `a=8,9`.
