# Affine-Faber `A`: center-independent first kernel face

Date: 2026-08-26

Status: **EXACT LAURENT-LEVEL LEMMA; ORDINARY-ROW COMPOSITION SCOPED TO A
COMPLETE FIRST FACE.**

## 1. Statement

In the exact moving-`A` coordinates

```text
A=z-a,                 D=A^2+4*a*A+E,
Q=A^2*D+U*A+R0,
N=lambda*(M*A*D+V*A+M*U/2+W0),                   (1.1)
```

assume `E,M,lambda` are units after their registered radial factors are
removed, `v(a)>0`, and

```text
q=min(v(U),v(V))>0.                               (1.2)
```

At a grade where every load, target, cubic normal, and genuine complement
precedes neither nor ties the quadratic kernel face, the first nonzero
kernel initial ideal is independent of the positive value `v(a)`.  It is
the same two-chart ideal used in the reviewed `a>=5` composition and is
empty on `D(E*M)`.

## 2. Exact polar calculation

Put

```text
Qp=A^2*D,            Np=M*A*D,
dQ=U*A+R0,           dN=V*A+M*U/2+W0.             (2.1)
```

The linear polar part of `N^2/Q` is

```text
2*Np*dN/Qp-Np^2*dQ/Qp^2
 =2*M*V+(2*M*W0)/A-(M^2*R0)/A^2.                 (2.2)
```

Thus `U` cancels identically at first order for every `a,E,M`.  Either the
`A^-2,A^-1` coefficients in (2.2) give a unit pivot, or genuine complements
start at least at twice the first kernel order.  On the kernel itself
`R0=W0=0`, the exact quadratic term is

```text
dN^2/Qp-2*Np*dN*dQ/Qp^2+Np^2*dQ^2/Qp^3
 =(V*A-M*U/2)^2/(A^2*D).                          (2.3)
```

Since

```text
1/D=1/E-(4*a/E^2)*A+O(A^2),                      (2.4)
```

every center-dependent polar coefficient in (2.3) contains a positive
factor of `a`.  It therefore occurs strictly after the first valuation
`2q`.  Tangent jets of `E,M` behave the same way.  The residue of the first
face is obtained by setting `a=0`, not by assuming `v(a)>=5`.

## 3. Complete first ordinary rows

Multiplication by the unit normal square and by `3/8` gives, after the
linear complement split, the first ordinary rows

```text
G1=-3*r1*M^2/8+3*s0*M/4,
G3=-3*E*r1*M^2/32-3*M*x*y/8+3*E*s0*M/16,
G4= 3*M^2*x^2/32-3*E*M^2*r0/16-3*E*y^2/16,
G6=-3*E^2*M^2*r0/64+3*E^2*y^2/64.                (3.1)
```

The Laurent-to-ordinary connection is lower unitriangular.  At a complete
first face its positive-center corrections multiply earlier zero rows, so
(3.1) is unchanged.  The exact eliminations are

```text
G3-(E/4)*G1=-(3/8)*M*x*y,
G6=0 => r0*M^2=y^2.                               (3.2)
```

On `D(x)`, (3.2) gives `y=r0=0` and
`G4=3*M^2*x^2/32`.  On `D(y)`, it gives `x=0`,
`r0=y^2/M^2`, and `G4=-3*E*y^2/8`.  Both are units on their named charts.
Unequal kernel orders specialize to one of the same axes.

## 4. Consequence for the delayed `a=3` successor

With normal order 15, the quadratic kernel face is at grade `30+2q` and
the fixed delayed loads/`mu2` start at grade 42.  Hence every

```text
0<q<6                                             (4.1)
```

is excluded for **any** positive center order, including `v(a)=3`.  A
graph-relative support unit for `q>=6` may therefore compose with this
lemma to close the full `a=3` kernel fan, provided its source predecessor
really imposes the affine graph.

## 5. Firewall

This lemma requires a complete first face: at `q=6` the loads tie and must
be retained.  It does not cover `v(a)=0`, a factor-degenerate closed point,
an earlier complement, another normal/load schedule, graph accessibility,
total-Rees/saturation, terminal/Taylor, order two, maximum twelve, or JC2.
