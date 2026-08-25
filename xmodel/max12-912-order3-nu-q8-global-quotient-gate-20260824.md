# Max12 `(9,12)` Q8 global quotient gate

Date: 2026-08-24  
Status: **producer-exact; hostile different-model review required**

## 1. Result and strict scope

The punctured non-parity branch through every corrected Q8 contact has an
exact seven-variable/six-row algebraic quotient model in the genuine
approximate-cubic chart.  The selected algebraic branch closure is
one-dimensional: this is the algebraic component selected by the reviewed
rank-six formal-IFT calculation at the Q8 boundary.  Two modular localized
standard bases give useful width evidence for the surrounding open scheme,
but are **not** a characteristic-zero dimension proof for that whole scheme.
This report is not an equation, normalization, irreducibility statement,
genus computation, or rational trajectory.

Reviewed inputs are the corrected Q8 formal-branch theorem and the root-free
critical-value norm.  Frozen producer inputs are the Q8 normalization/Taylor/
terminal and local leaf-4 descent jets.  No quarantined Q12 artifact is used.

## 2. Exact approximate-cubic quotient

Work on `p!=0` in the coefficient cone and take the geometric `p=1` chart.
Write

```text
K=z^3+z+q_c,
f=K^3+x5*z^5+x4*z^4+x3*z^3+x2*z^2+x1*z+x0.
```

The parity involution negates `(q_c,x0,x2,x4)`.  On the punctured Q8 branch,
the corrected tangent has a unit `x0` component, so take

```text
t=x0,       q_c=t*c,       x2=t*d2,       x4=t*d4,
w=t^2.                                                   (2.1)
```

For each odd tail divide by `t`.  Exact character purity then produces six
polynomial equations

```text
r1/t=r3/t=r5/t=r7/t=r2=r4=0                            (2.2)
```

in the seven invariant variables

```text
(w,c,d2,d4,x1,x3,x5).                                  (2.3)
```

The two output functions are

```text
n=r6/p^9,          q=r8/p^10.                           (2.4)
```

The portable compiler reconstructs (2.2) directly from all eight original
Faber tails.  Its row sizes are:

| row | terms | total degree | `w` degree |
|---|---:|---:|---:|
| `r1/t` | 10 | 4 | 1 |
| `r3/t` | 20 | 5 | 1 |
| `r5/t` | 35 | 6 | 1 |
| `r7/t` | 57 | 7 | 2 |
| `r2` | 16 | 5 | 1 |
| `r4` | 29 | 6 | 2 |
| output `r6` | 48 | 7 | 2 |
| output `r8` | 73 | 7 | 2 |

This is 167 monomials in the imposed system, versus 230 in the raw
`a_even/t` quotient.  Equations (2.1) are reversible on `t!=0`; no component
claim is inferred from the size reduction.

## 3. Selected branch dimension and modular width evidence

The Q8 contact lies in the reviewed generic parity chart where

```text
x5*(x3-2*x5)!=0.
```

The punctured open quotient is represented without a saturation black box by
adjoining `inv` and imposing

```text
inv*w*x5*(x3-2*x5)-1=0.                                (3.1)
```

Independent Singular `slimgb` computations from the same exact source give

| prime | dimension | basis size | `vdim` |
|---:|---:|---:|---:|
| `32003` | 1 | 607 | -1 |
| `1000003` | 1 | 607 | -1 |

The exact characteristic-zero statement comes instead from the reviewed Q8
formal-IFT input: at each Q8 contact the matching six-row completed local
system has the selected smooth formal curve, with `w` a parameter after the
parity quotient and with `x5*(x3-2*x5)` a unit.  The corresponding algebraic
component, and hence its punctured branch closure in (3.1), has dimension
one.

The two finite-characteristic computations are routing evidence only.  No
lifted standard basis, flat integral model, or lucky-prime certificate is
supplied, so they do **not** prove a characteristic-zero upper bound for the
entire localized scheme.  In particular this artifact proves neither that
the whole localized scheme has dimension one nor that it is reduced or
irreducible.  It also does not classify components on the removed boundary
`w*x5*(x3-2*x5)=0`.

## 4. Exact Hensel lift and projection lower bounds

Over `E=Q[v]/(Q8)`, the replay solves the six equations (2.2) recursively
through `w^5`.  Each of the six quotient coordinates has a unique coefficient
at every step, and substitution annihilates all six rows through that order.
It reconstructs

```text
n(w),        q(w),        Z(w)=q(w)^9/n(w)^10.          (4.1)
```

Every displayed coefficient of `n`, `q`, and `Z` through `w^5` is a unit in
`E`.  The constant and first `q` coefficients agree with the independently
frozen Q8 terminal jet.

The following are exact falsifiers, not guesses:

- none of `n`, `q`, or `Z` has a rational expression of Padé type
  `[1/1]`, `[2/1]`, `[3/1]`, `[1/2]`, `[2/2]`, or `[1/3]` compatible through
  `w^5`;
- there is no polynomial `H(w,Z) in Q[w,Z]` with `1<=deg_Z<=10`,
  `0<=deg_w<=4`, and at most 48 monomials in the tested rectangle;
- there is no polynomial `H(n,q) in Q[n,q]` with
  `1<=deg_n,deg_q<=4`.

For the last two statements, the 48 rational coefficient equations are
reduced at both `1000003` and `1000033`; every candidate matrix has full
column rank.  A rational nullvector would reduce to a nullvector at either
good prime after primitive integral normalization, so the modular full-rank
certificates exclude the stated rational relations exactly.  No conclusion
is made outside the displayed degree boxes.

## 5. Fixed-load and terminal reconstruction

The `p=1` chart is a geometric coefficient quotient.  It is not an
authorization to make an `x`-dependent source scaling along a trajectory.
The correct scale reconstruction uses the full off-parity output `n`:

```text
pi=p^9=nu/n,                    nu=r6 in C^*,
S=r8^9=pi^10*q^9=nu^10*Z.                             (5.1)
```

Consequently the root-free terminal identity from the frozen predecessor,

```text
h^3*(S')^9=j^9*S^8,
```

becomes on the quotient

```text
nu^10*h^3*(Z')^9=j^9*Z^8.                             (5.2)
```

Equation (5.2) is a necessary descended differential equation.  It uses
`n=r6/p^9` from the full quotient.  The parity-only identity
`r6=p^9*R6(v)` is nowhere used; the frozen negative control proves it fails
by a unit at first nontrivial order off parity.

## 6. Boundaries and next gate

All removed boundaries remain charged:

```text
w=0,       x5=0,       x3-2*x5=0,       p=0,
```

as do both full Taylor families at `r=A/9`.  The reviewed parity theorem
excludes actual trajectories contained in parity; it does not identify the
projective endpoints of the punctured non-parity curve.

The smallest honest successor is a higher-degree modular projection with
support learning, followed by rational reconstruction and exact substitution
into (2.2), or a projective-boundary/genus computation on the selected
one-dimensional component.  No global quotient equation is frozen here.
There is no punctured-trajectory, all-`(9,12)`, maximum-twelve,
counterexample, or JC2 conclusion.

## 7. Replay

```sh
python3 cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/replay.py \
  | diff -u cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/replay.json -
shasum -a 256 -c cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/MANIFEST.sha256
```

The end-to-end replay regenerates the exact quotient, the `w^5` Hensel lift,
all bounded relation falsifiers, and both localized Singular routing
computations.  The last computations are not used as a characteristic-zero
whole-scheme dimension certificate.
