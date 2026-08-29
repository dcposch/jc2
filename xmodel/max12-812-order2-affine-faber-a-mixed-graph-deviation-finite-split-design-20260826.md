# Affine-Faber `A`: mixed graph-deviation finite successor split

Date: 2026-08-26

Status: **PRODUCER-TIER VALUATIVE DESIGN; FIXED `H=16,q=6` FIRST FACE
DUAL-AWS PASS, EQUALITY WALL UNRESOLVED.**

## 1. Scope and frozen input

Work on the literal delayed-load ray

```text
Lambda=sigma^3,
k10=Lambda^12*K10,  k6=Lambda^8*K6,  k2=Lambda^4*K2,
```

in the repeated-`A` coefficient chart on `D(E*M*K10)`.  Let

```text
H=ord_sigma(lambda),
q=min(ord_sigma(X),ord_sigma(Y))>0,
alpha=ord_sigma(a)>0.
```

All leading loads and `mu2` have grade `42`; `mu4,mu6,J` have grades
`48,54,57`.  The first square-normal block is at `2H`, its transverse
kernel correction is at `2H+2q`, and the intrinsic cubic is at `3H`.

The controlling fixed representative is

```text
H=16, q=6, complements=12,
affine graph=42, transverse graph deviations=44,
alpha>=4, intrinsic cubic=48.
```

Its dual-AWS custody is

```text
RESULT   f5d92c3856ef5e3684b2879d6b6b4d46894fb9a78f4715e750f896cbb918b71d
EVIDENCE fd9133fa7fb9f17f21c0151583df8201ac871761d812cca5a0ba7b3f0feba620
FREEZE   8ee2fb6e2cd87a5457e2b0ba0edaffe014407feb946cde11ba1ebc35f6d83773
```

The exact-Q lane is evidence; characteristic `65521` is a software
control only.

## 2. First finite split in `15<H<21`

The first normal block at `2H<42` puts the normal in the repeated-factor
null line.  Compare the first transverse quadratic grade

```text
g=2H+2q
```

with the affine load graph at grade `42`.  This gives the exhaustive
valuation split

```text
q < 21-H:  the complete unloaded two-chart quadratic block occurs first;
q = 21-H:  quadratic and leading affine load graph tie;
q > 21-H:  the affine graph occurs first and the first transverse
            deviations can tie the quadratic at grade g>42.
```

The first line is the registered low-kernel receiver.  The second line
requires the complete graph/predecessor equality face.  This note concerns
the third line after the exact affine graph

```text
K6=(15*E^2/32)*K10,
K2=(15*E^4/256)*K10,
mu2=-(5*E^6/4096)*K10
```

has been imposed through grades `<g`.  Use the two-sided transverse
coordinates

```text
d6=K6-(15*E^2/32)*K10,
d2=K2-(15*E^4/256)*K10,
dm=mu2+(5*E^6/4096)*K10,
d4=mu4.
```

At the fixed `H=16,q=6` representative, `g=44` and the complete source
rows are

```text
C1=-3*r1*m^2/8+3*s0*m/4,
C2= 3*d6*p^4/128-3*r0*m^2/8-d2*p^2/8+3*y^2/8-dm,
C3=-3*r1*m^2*p/32-3*x*y*m/8+3*s0*m*p/16,
C4= 3*x^2*m^2/32-3*r0*m^2*p/16-3*y^2*p/16,
C5=-3*r1*m^2*p^2/256+3*x*y*m*p/32+3*s0*m*p^2/128,
C6=-d6*p^6/512-3*r0*m^2*p^2/64+d2*p^4/128
   +3*y^2*p^2/64,
C7= 3*r1*m^2*p^3/1024-3*x*y*m*p^2/256
   -3*s0*m*p^3/512.
```

Both projective residue charts survive.  Representatives are

```text
D(x): y=0, r0=x^2/(2*p),  s0=r1*m/2;
D(y): x=0, r0=-y^2/m^2,  s0=r1*m/2,
```

with `C6,C2` solving `d2,dm`.  Therefore it is false to reapply the empty
homogeneous quadratic block after the affine graph.

## 3. Second finite split after the mixed face

Modulo the grade-`g` mixed predecessor, the first center-bearing part of
the exact row functional `K=E*H3+H5` is

```text
a*lambda^2*(-3*M^2*X^2/8+3*E*Y^2/2),
```

and the intrinsic term is

```text
-E*lambda^3*M^3/16.
```

The former has grade `g+alpha`; the latter has grade `3H`.  Hence only
one further rational wall remains:

```text
alpha < H-2q:  center functional first;
alpha = H-2q:  center, mixed-deviation, and intrinsic terms tie;
alpha > H-2q:  intrinsic cubic first.
```

On either displayed survivor chart the center coefficient is a unit on
`D(E*M*x*y)` chartwise: it specializes to `-3*M^2*x^2/8` on `D(x)` and
`3*E*y^2/2` on `D(y)`.  Thus the strict `<` cone is expected empty.  In
the strict `>` cone the intrinsic coefficient is a unit.  Only equality
needs a new source computation.

At equality, before reducing by the mixed predecessor, the exact support
sentinel is

```text
-E*lambda^3*M^3/16
-3*a*lambda^2*M^2*X^2/8
+3*a*lambda^2*E*Y^2/2
+a*(-9*E^5*d6/128+E^3*d2/8-E*dm).
```

This polynomial is not itself a verdict: `d6,d2,dm`, kernel/complement
jets, and the seven source rows at all intervening grades must be reduced
together.  The first integral representative is

```text
(H,q,alpha)=(16,6,4),  g=44, equality grade=48.
```

It must retain both `D(x)` and `D(y)`, arbitrary moving `a,E,M,K10`, all
kernel and complement jets capable of contributing through grade `48`,
all transverse-deviation jets through grade `48`, all seven complete
ordinary-Faber rows, and the independently typed `mu4` target at grade
`48`.

## 4. Iterated raising rule

If a leading kernel pair is absorbed by complementary or transverse graph
variables and its order rises, recompute `q`, `g=2H+2q`, and the threshold
`H-2q` from the new leading pair.  An old complement known only to have
order `>=2q_old` can lie below `2q_new`; it cannot be silently discarded.
The recursion either reaches a strict center unit, reaches the intrinsic
cubic unit, lands on a new equality wall, or converges to `X=Y=0`, where
the intrinsic cubic remains.  This is the intended valuation algorithm,
not yet a proved noetherian or total-Rees termination theorem.

## 5. Stop conditions and nonclaims

Stop on any omitted target/load coefficient, graph-deviation jet, moving
center/tangent jet, complement that can fall below the raised threshold,
ordinary/Faber connection mismatch, lost coefficient-factor stratum, or
projective chart tested only after an unlicensed localization.  Preserve
raw nonreduced ideals before every saturation.

This design does not yet prove rational-regrading invariance of the mixed
rows, the equality wall, iterative graph absorption, literal source/Rees
coverage, factor-degenerate opens (`E*M*K10=0`), the `H=21` receiver, the
load-first region `H>21`, terminal/Taylor closure, order two, maximum
twelve, or JC2.
