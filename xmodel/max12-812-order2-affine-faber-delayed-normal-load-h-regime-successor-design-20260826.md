# Delayed affine-Faber source: normal/load `H`-regime successor

Date: 2026-08-26

Status: **CORRECTION-AWARE NEWTON SKELETON; PROVISIONAL NAVIGATION.**

## 1. Fixed source timings

Retain the literal delayed ray

```text
Lambda=sigma^3,
k10=Lambda^12*K10,  k6=Lambda^8*K6,  k2=Lambda^4*K2.
```

All three effective loads and `mu2` occur at sigma grade 42.  The remaining
targets occur at

```text
mu4:48,       mu6:54,       J:57.                 (1.1)
```

After exact monic square division `C=Q^2+Delta`, put
`H=ord_sigma(Delta)`.  The nominal unloaded quadratic, intrinsic cubic,
and first loaded-normal grades are

```text
2H,             3H,             42+H.             (1.2)
```

Polynomial null directions can erase a nominal face but do not change
these support walls; every leaf must retain its predecessor ideal.

## 2. Confirmed region `0<H<=15` and its center boundary

On a repeated-`A` special fibre `Q0=z^2(z^2+p)`, `p` a unit, the first
block at `2H<42` forces

```text
Delta_H=m*z*(z^2+p),       m a unit.              (2.1)
```

The exact coefficient chart then has `q=min(v(U),v(V))>0`.  The homogeneous
predecessor/direct-unit theorem

```text
c4926d0476f4df7d910b09645bf387f06292f3faaa25f2e7793b81ba2001bf71
  xmodel/max12-812-order2-affine-faber-a-homogeneous-direct-unit-cone-theorem-20260826.md
```

excludes every

```text
0<H<=15,       v(a)>=H/3,                          (2.2)
```

including `K10=0`, because `42>=14H/5`.  The theorem and its hostile review
are frozen at

```text
c4926d0476f4df7d910b09645bf387f06292f3faaa25f2e7793b81ba2001bf71
  xmodel/max12-812-order2-affine-faber-a-homogeneous-direct-unit-cone-theorem-20260826.md
9c537ad4e1d422c21e4845c0ac3b60a45057b838c859613e14d08f8fe6bc586e
  xmodel/max12-812-order2-affine-faber-a-homogeneous-direct-unit-cone-hostile-review-grok-20260826.md
```

The complement `v(a)<H/3` is an earlier center fan.  At the boundary
`H=15`, the exact graph-relative support calculation refines the raw
center/load wall as follows:

```text
v(a)>3, q>=6:  intrinsic direct unit;
v(a)=3, q>6:  intrinsic direct unit;
v(a)=3, q=6:  unresolved grade-42 predecessor face.       (2.3)
```

At the last equality the raw grade-45 functional contains, besides the
intrinsic term, the two exact nondeviation ties

```text
-(3/8)*X^2*a*lambda^2*M^2,
+(3/2)*E*Y^2*a*lambda^2.                                (2.4)
```

Graph deviations are strict ties.  Thus the exact affine-graph
cancellation and the complete grade-42 predecessor must be applied before
taking a hull; neither the whole `v(a)=3` cell nor the equality face is
closed by the raw direct-unit support alone.  The dual-AWS equality client
owned by the root lane is controlling for this one wall.

## 3. The mixed open band `15<H<21`

The pure first block still occurs before the loads, so (2.1) remains valid.
For the first kernel order `q`, the correction face is

```text
2H+2q.                                            (3.1)
```

Hence the complete unloaded two-chart block kills

```text
0<q<21-H.                                         (3.2)
```

At `q=21-H` it ties the affine load/`mu2` face at grade 42; for larger `q`
the affine face comes first.  This is the genuine new mixed region.  It
must be expressed in transverse graph coordinates

```text
d6=K6-(15*E^2/32)*K10,
d2=K2-(15*E^4/256)*K10,
dm=mu2+(5*E^6/4096)*K10,
d4=mu4,                                            (3.3)
```

only on the exceptional affine-`A` predecessor.  The exact functional has

```text
[normal]K=normal*M*E*(-3*E^2*d6/64+d2/8),
[a]K=a*(-9*E^5*d6/128+E^3*d2/8-E*dm+4*d4).        (3.4)
```

Thus a raw load monomial is not a legitimate lower-hull generator until
the graph ideal is imposed.  The next client must group the complete 371
terms after (3.3), with symbolic weights `(H,v(a),q,v(d*))`, and reduce each
face by the grade-42 predecessor ideal.  The already known low-q interval
(3.2) is a mandatory positive control.

## 4. The boundary `H=21`

Here the first square-normal quadratic, all three loads, and `mu2` tie at
grade 42.  Divisibility may not be imposed before forcing.  The literal
mixed receiver is the complete ordinary-Faber block of

```text
[(3/8)*N0^2/Q0
 +K10*Q0^(5/2)+K6*Q0^(3/2)+K2*Q0^(1/2)]_-,        (4.1)
```

with the row-two target `mu2`.  The first-block theorem classifies only the
unloaded summand in (4.1).  A minimal exact-Q/F65521 client must retain all
four coefficients of `N0`, all three loads, `mu2`, and the full ordinary
connection; it must not pre-project onto `N0=m*A*D` or the affine graph.

The first successor after (4.1) is the grade-63 block, where the intrinsic
normal cubic and load-normal terms tie.  It should use an exact
row-functional mined from the complete predecessor quotient rather than a
preselected `K` specialization.

## 5. Load-first region `H>21`

The grade-42 exact-square affine receiver precedes the square-normal
quadratic.  Its corrected reduced support supplies the first routing:

```text
square/Pell component;
affine-Faber component on D(discriminant), including its exceptional A face.
```

Normals must then be pulled back separately to each component.  The raw
target walls refine the region at

```text
H=24   (2H=48),
H=27   (2H=54),
H=57/2 (2H=57).                                  (5.1)
```

Thus the finite coarse bands are

```text
(21,24), {24}, (24,27), {27}, (27,57/2), {57/2}, (57/2,infinity).
```

At every equality retain the tying target.  A leading normal in a
first-block null module starts a correction recursion rather than raising
`H` automatically.

## 6. Minimal execution order and stop rules

1. Finish the graph-relative `H=15,v(a)=3,q=6` grade-42 predecessor client.
   The surrounding `v(a)>3,q>=6` and `v(a)=3,q>6` cells already have the
   exact direct unit, so this equality is the unique unresolved wall of
   that local fan and the smallest negative/positive control for imposing
   (3.3) before a hull.
2. Extract the symbolic relative cones in `15<H<21`, seeding the exact
   empty interval (3.2); launch only faces surviving the graph predecessor.
3. Compile the correction-complete mixed receiver (4.1) at `H=21`.
4. For `H>21`, pull the first normal to the two reviewed affine support
   components, starting with the generic component where the two-row
   `(beta,gamma)` pivot is a unit.

Stop on any omitted load/target, coefficient-factor localization, moving
center/tangent jet, nonunique graph coordinate, connection mismatch,
ramified valuation not represented by the cone, or predecessor reduction
performed after saturation.  Exact Q is evidence; good primes are software
controls only.

## 7. Factor and scope firewall

Squarefree `Q0`, square `[2,2]`, triple-root `[3,1]`, quadruple-root `[4]`,
`p=0`, and `M=0` are separate factor-type receivers.  This design does not
prove total-Rees or saturation/base-change compatibility, terminal/Taylor,
order two, `(8,12)`, maximum twelve, or JC2.
