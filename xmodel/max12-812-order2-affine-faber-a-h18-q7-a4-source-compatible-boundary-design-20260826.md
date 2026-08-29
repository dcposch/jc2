# Affine-Faber `A`: source-compatible H18/q7/a4 boundary design

Date: 2026-08-26

Status: **AWS-ONLY PREREGISTRATION DESIGN; NO RESULT.**

## 1. Why H18 is next

On the balanced integer strict ray

```text
Lambda=tau^4*(unit),       Lambda=sigma^3,
```

literal rational-source descent requires `3|H`.  Thus the normalized
`H=16,17` cells are ramified navigation only on this ray, while `H=18`
is the first source-compatible normal order after the reviewed `H=15`
cell.

Work on `D(p*m)` in the repeated-`A` moving-discriminant graph with

```text
v(lambda)=18,       v(a)=4,
v(X)=v(Y)=7,        v(Ri)=v(Si)=14,
v(E)=v(M)=0.                                         (1.1)
```

The delayed loads and targets retain their literal timings

```text
K10,K6,K2,mu2:42,   mu4:48,   mu6:54,   J:57.       (1.2)
```

No `J` term is licensed through the proposed endpoint.

## 2. Complete load graph and predecessor schedule

Retain the exact affine load graph, including every correction through
absolute grade 54:

```text
K10=sigma^42*kappa,
K6 =sigma^42*((15/32)*kappa*E^2+sigma^8*d6),
K2 =sigma^42*((15/256)*kappa*E^4+sigma^8*d2),
mu2=sigma^42*(-(5/4096)*kappa*E^6+sigma^8*dm),
mu4=sigma^48*(d40+sigma*d41+sigma^2*d42+...),
mu6=sigma^54*d60_target+... .                         (2.1)
```

The registered chronology is:

```text
42: affine load face;
48,49: mu4-only predecessors, expected to force d40=d41=0;
50: first quadratic/complement face and load deviations;
51--53: correction recursion;
54: intrinsic/load-center boundary plus mu6 in row 6;
57: first determinant target, outside this client.              (2.2)
```

At grade 50 the exact-Q client must independently recover the seven-row
block

```text
C1=-3*r1*m^2/8+3*s0*m/4,
C2= 3*d6*p^4/128-3*r0*m^2/8-d2*p^2/8+3*y^2/8-dm
    +15*kappa*a4^2*p^5/128,
C3=-3*r1*m^2*p/32-3*m*x*y/8+3*s0*m*p/16,
C4= 3*m^2*x^2/32-3*p*m^2*r0/16-3*p*y^2/16-d42,
C5= 3*p^2*C1/32-p*C3/4,
C6=-d6*p^6/512-3*r0*m^2*p^2/64+d2*p^4/128
    +3*y^2*p^2/64-15*kappa*a4^2*p^7/1024,
C7= p^2*C3/32-p^3*C1/64.                            (2.3)
```

Here each symbol denotes the leading coefficient of the correspondingly
timed series.  Both projective charts `D(x*p*m*a4)` and
`D(y*p*m*a4)` must be retained; radicalizing or setting either kernel
coordinate to zero before the row pivots is forbidden.

## 3. Boundary functional

From the seven complete ordinary rows form, without row projection,

```text
K=E*H3+H5,
H=2*E^2*P3+16*E*P5+64*P7-(E^3/2)*P1.              (3.1)
```

The exact support schedule predicts

```text
[sigma^54]H=-2*m^3*p^2+(5/4)*kappa0*a4^3*p^7.      (3.2)
```

This is a preregistered formula, not evidence.  A dual-field mismatch,
an earlier nonzero coefficient of `H`, an omitted mu4/mu6 contribution,
or an extra grade-54 term is a fail-closed falsifier.  If (3.2) survives,
the candidate receiver is

```text
5*kappa0*a4^3*p^5-8*m^3=0.                         (3.3)
```

The client must then reduce all seven rows sequentially through grade 54,
not merely set (3.2) to zero.  A free correction may cancel `K`; any
remaining row is recorded honestly as a unit or survivor.

## 4. Minimal dual-AWS client

Reconstruct the seven complete frozen tails from `tails.json` over exact Q
and independently over F65521.  Retain:

- all `a,E,M,X,Y,Ri,Si` coefficients that can reach grade 54;
- `kappa` through relative grade 12;
- `d6,d2,dm` through relative grade 4 after their grade-50 start;
- all seven `mu4` coefficients at grades 48--54;
- the grade-54 `mu6` target and a sentinel proving `J` first occurs at 57;
- both projective kernel charts and the raw nonreduced rows.

Hard controls are the exact affine graph at grade 42, the two mu4-only
predecessors, (2.3), the ordinary/inverse-Faber connection, (3.2), target
derivatives, omission controls for every load family, and matching
exact-Q/good-prime support.

The first diagnostic may emit grades 42--54 and the two functionals.  The
controlling producer must subsequently perform the sequential chart
reduction before any mathematical endpoint is stated.

## 5. Stop conditions and nonclaims

A localized unit on both charts excludes only this fixed normalized
boundary.  A survivor is only a deeper normalized receiver.  Timeout,
resource exhaustion, nonunique sentinel, source-hash mismatch, or omitted
correction/load is no verdict.

This design does not prove that the integer-slope descent criterion is
correct, that every slope-four source arc enters (1.1), or that the H18
cell lifts.  It does not impose terminal/global algebraization or either
finite Taylor family and does not close order two, `(8,12)`, maximum
twelve, or JC2.
