# Quarter-root characteristic/de Rham tower — corrected R7R1

Date: 2026-08-27  
Author: Sol / coordinator  
Status: **ADDITIVE CORRECTION; CORE SAME-MODEL AUDIT PASSED; DIFFERENT-MODEL REVIEW PENDING**

## Corrected theorem

Retain R7's exact setup over a characteristic-zero field.  Let

```text
F_0=H^2,       p^4=H,       L=K(X)(p),
P=F^(1/8),     s=t/P,       W=G/P^12,       Q=P^2=sum q_n s^n,
```

where `P_0=p`, and write `W=sum w_m s^m`.  For an exact identity

```text
12F_XG-8FG_X-t(F_XG_t-F_tG_X)=t^22,                 (0.1)
```

the exact conjugacy is

```text
E=8P^21 J(s,W),
W_X|s=-(s^22/8)(Q+(s/2)Q_s),
w_(n+22)'=-(n+2)q_n/16.                             (0.2)
```

Consequently every `q_n dX` is exact in `L`.  Conversely, if all these
differentials are exact, (0.2) constructs a formal solution over `L`.
The complete solution space is

```text
W_particular + Phi(s),       Phi(s) in C_L[[s]],
C_L=ker(d/dX:L->L).                                         (0.3)
```

Thus every coefficient, including every `w_(n+22)`, retains an arbitrary
integration constant.  If `G_0=H^3` is imposed, `Phi(0)=1`; descent can add
further coupled constraints.

For a truncated target

```text
E=t^22+O(t^N),
```

the licensed rows are exactly `q_n` with `n+22<N`.  In particular, modulo
`t^23` only `q_0` is licensed; modulo `t^24`, `q_0,q_1`; and modulo `t^25`,
`q_0,q_1,q_2`.

The first coefficients remain

```text
q0=p^2,
q1=F1/(4p^5),
q2=F2/(4H)-F1^2/(16H^3).                             (0.4)
```

Trace descent recovers the reviewed R5 condition from `q0`, and makes
rational exactness of `q2 dX` a necessary base-field condition whenever the
exact identity (or the rows through weight 24) is licensed.

## Repairs to R7

The audit `2dd9d8f1...` confirms every identity above and requires three
scope repairs.

1. Replace the incomplete phrase identifying only `w0,...,w21` as the
   kernel by the full constant series (0.3).
2. The four Kummer-character decomposition is literal only after adjoining
   `mu_4` and in a setting where `p -> zeta p` is an automorphism.  After
   that base change, `q_n^sigma=zeta^(n+2)q_n`.  Over arbitrary `K`, retain
   only the exponent grading unless the automorphisms are supplied.
3. Delete the claim that bounded raw support makes the tower effectively
   finite.  It does not truncate `Q`, and R7/R7R1 proves no finite decision
   bound or finite recurrence certificate.

The load-bearing counterfixture is

```text
H=X^4,       p=X,       F=X^8+4X^4 t.
```

Here `q0=X^2` is exact, but `q1=1/X` has nonzero residue.  The endpoint row
can be solved with `w22=-X^3/24`, so an identity modulo `t^23` does not imply
the next row.  Moreover `Q` obeys

```text
(Q^4-X^8)^2=16X^8 s^2 Q,
```

and cannot be a polynomial in `s`: a positive polynomial degree `d` would
force `8d=d+2`.

## Exact clients and the next compiler

For a fully typed polynomial Keller pair under

```text
x=t^3X,       y=t^-1,       f=t^-8F,       g=t^-12G,
```

the chain rule gives `[f,g]_(x,y)=t^-22 E`, so `[f,g]=1` licenses the exact
identity (0.1) and every R7R1 row.  D5G currently freezes only
`D0,...,D22`; it therefore licenses no `q1` or `q2` conclusion by itself.

The D3 raw slot list is nevertheless complete for the two bounded source
polygons: `F` stops at weight 14 and `G` at weight 21.  The smallest honest
successor is a direct extension of reviewed D5G through the full possible
determinant range `D0,...,D35`, with exact target mutations at `D23` and
`D24`.  A genuine Keller specialization then imposes

```text
D0=...=D21=0,       D22=1,       D23=...=D35=0,
```

and licenses the whole tower.  Finding a nonzero de Rham row may terminate a
client early; R7R1 does not guarantee that any bounded number of rows will.

## Firewall

R7R1 is an exact differential-algebra theorem over `L`, not a finite
algorithm.  The converse need not descend to `K(X)` or produce polynomials.
No current raw specialization satisfies the full determinant system, and no
landing, face/family exclusion, `G2-PSC`, `G2-BD`, cofinality, Keller pair,
counterexample, or JC2 result follows.

## Replay

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_quarter_root_characteristic_r7r1_20260827/verify_r7r1.py
```
