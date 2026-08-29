# Quarter-root characteristic coordinates and the all-order de Rham tower — R7

Date: 2026-08-27  
Author: Sol / coordinator  
Status: **PROVISIONAL PRODUCER THEOREM; PENDING INDEPENDENT REVIEW**

## Result

The rational endpoint obstruction has an exact nonlinear continuation.  The
full equation

```text
E(F,G)=12 F_X G-8 F G_X-t(F_X G_t-F_t G_X)=t^22
```

is conjugate, after an algebraic characteristic-coordinate change, to a
coefficientwise exact-differential problem on one fixed Kummer function
field.  Thus the R5 endpoint is only the first member of an infinite—but for
any bounded raw support effectively finite—de Rham obstruction tower.

Let `K` have characteristic zero, let

```text
F in K(X)[[t]],       F_0=H^2 != 0,
```

and choose `p` with `p^4=H`.  In `L=K(X)(p)`, let `P=F^(1/8)` be the unique
formal branch with `P_0=p`, and set

```text
s=t/P,       W=G/P^12,       Q=P^2.
```

The change `t -> s` is formally invertible.  Write all transformed series in
the `(X,s)` coordinates and expand

```text
Q=sum_(n>=0) q_n(X) s^n,       q_n in L.
```

If `E(F,G)=t^22` exactly, then for every `n>=0`

```text
q_n dX = d a_n                                                   (0.1)
```

for some `a_n in L`.  More precisely, if

```text
W=sum_(m>=0) w_m(X)s^m,
```

then

```text
w_(n+22)' = -(n+2)/16 * q_n.                                    (0.2)
```

Conversely, coefficientwise exactness (0.1) constructs a formal solution in
the chosen algebraic extension, up to the arbitrary homogeneous series
`Phi(s)`.  Descent to `K(X)[[t]]`, polynomiality, and the raw Newton support
are additional conditions, so the forward implication is the campaign-safe
one.

At `n=0`, `q_0=p^2=sqrt(H)`.  Exactness descends by trace from `L` to
`K(X,sqrt(H))`; writing `H=A^2 B` with `B` squarefree recovers exactly

```text
A=Bv'+(3/2)B'v,
```

because

```text
d(v B sqrt(B))=(Bv'+(3/2)B'v)sqrt(B) dX.
```

Thus R5 is the grade-zero shadow of R7, not a separate coincidence.

## 1. Exact conjugacy

Put `F=P^8` and `G=P^12 W`.  Direct differentiation, with no truncation,
gives

```text
E(F,G)=8 P^19 ((t P_t-P)W_X-t P_X W_t).                         (1.1)
```

For `s=t/P`, the Jacobian in `(X,t)` satisfies

```text
J(s,W)=((t P_t-P)W_X-t P_X W_t)/P^2,
```

so

```text
E(F,G)=8 P^21 J(s,W).                                           (1.2)
```

The target `t^22=s^22 P^22` therefore becomes

```text
J(s,W)=s^22 P/8.                                                (1.3)
```

In `(X,s)` coordinates, `J(s,W)=-s_t W_X|s`, while `1/s_t=t_s` and
`t=sP`.  Hence, with `Q=P^2`,

```text
W_X|s = -s^22/8 * P(P+sP_s)
       = -s^22/8 * (Q+(s/2)Q_s).                               (1.4)
```

Comparing coefficients in (1.4) proves (0.2).  Every scalar `(n+2)/16` is
nonzero in characteristic zero, so the target equation forces every
`q_n dX` to be exact.  Conversely primitives of the `q_n` define the
coefficients `w_(n+22)`; the coefficients `w_0,...,w_21` are the
characteristic kernel `Phi(s)`.

## 2. First new obstruction rows

The implicit equation in characteristic coordinates is

```text
P(X,s)^8 = F(X,s P(X,s)).                                      (2.1)
```

Writing `F=H^2+F_1 t+F_2 t^2+...` and `p^4=H`, exact expansion gives

```text
q_0 = p^2,
q_1 = F_1/(4 p^5),
q_2 = F_2/(4 p^4)-F_1^2/(16 p^12)
    = F_2/(4H)-F_1^2/(16H^3).                                 (2.2)
```

The `q_2` row is already a rational differential on `K(X)`.  Therefore any
actual polynomial raw solution must make

```text
(F_2/(4H)-F_1^2/(16H^3)) dX                                  (2.3)
```

rationally exact.  This supplies an immediately compilable residue test on
the R5 survivor strata.  The `q_1` row is a Kummer-eigenspace differential
on `p^4=H`; subsequent rows cycle through the four characters.  Hermite
reduction can compute their de Rham classes exactly and independently in
parallel.

Equation (2.3) is not asserted to obstruct every survivor: `F_1,F_2` remain
live raw variables.  Its value is that it turns the previously opaque
post-endpoint determinant rows into structured linear de Rham classes on a
fixed algebraic curve.

## 3. Strategic compiler

For a full raw polynomial client, the proposed descendant is:

1. parameterize the R6 survivor `H`;
2. compile `P` from (2.1) only as far as needed;
3. Hermite-reduce each `q_n dX` in the normalized Kummer field `p^4=H`;
4. stop at the first nonzero class, or retain the exact primitive as a
   certificate and advance;
5. in parallel, use D5G to check the original determinant coefficients and
   the global `H`-multiple.

Because an actual bounded-support pair has the exact identity `E=t^22`, all
rows are legitimate necessary conditions.  The first row is R5; higher rows
use determinant information above weight 22 that D5G has not yet compiled.
This is therefore complementary to, rather than dependent on, D4R1 local
naturality.

## 4. Firewall

R7 is provisional pending hostile review.  It assumes the exact formal
identity `E=t^22`; a truncation modulo `t^23` yields only `q_0` and hence no
higher-row claim.  Algebraic exactness is necessary for a polynomial pair
but is not sufficient for descent, polynomiality, raw support, GGV landing,
or global invertibility.

R7 does not prove a face/family exclusion, `G2-PSC`, `G2-BD`, a Keller pair,
a counterexample, or JC2.

## Replay

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_quarter_root_characteristic_r7_20260827/verify_r7.py
```

The exact verifier checks the differential-polynomial conjugacy, the
Jacobian identity, the characteristic-coordinate identity, the implicit
`q_0,q_1,q_2` expansion, a coefficient mutation, and the hyperelliptic
primitive formula in a sparse Laurent polynomial ring over `Q`.
