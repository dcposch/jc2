# Gate T: contact-independent three-row unique-`AC` certificate

Date: 2026-08-27

Status: **THE CORE ALGEBRAIC LEMMA IS PROVED BELOW.  THE LOW-BAND CHAMBER
CLASSIFICATION IS MECHANICALLY DERIVED FROM THE PINNED POLAR INVENTORY.
A FROZEN ROW-LEVEL LINKER AND DIFFERENT-MODEL HOSTILE REVIEW ARE STILL
REQUIRED BEFORE THIS REPLACES ANY PROMOTED D1 ENDPOINT.**

This is an additive refinement of the provisional uniform contact-shift
interface

```text
1cfa10b45d83ba4ecd98861c1f82e9bd41056d1cef7eaa43ad2802aa73aada5d
  xmodel/max12-812-order2-gate-t-uniform-contact-shift-naturality-interface-sol-20260827.md
```

and consumes the direct-coordinate simplification in the independent Opus5
review

```text
23007a2bb15e866f87a05bdff9f7a0ea0f1b05588d721d4b03bd377f0b89ce12
  xmodel/max12-812-order2-gate-t-drho-unique-ac-ledger-a2d2-composition-hostile-review-opus5-20260827.md
```

It does not alter either file.

## 1. Algebraic lemma

Let the coefficient field have characteristic zero, let `rho` be nonzero,
and put

```text
L = z^2-rho^2,
A0 = A1*z+A0c,
C0 = (C1*z+C0c)/2.
```

Define the two coefficients of `A0*C0 mod L` and the symmetric `C0^2`
coefficient, with the actual row normalizations, by

```text
g1 = (3/8)*(A0c*C1 + A1*C0c),
g2 = (3/8)*(A0c*C0c + rho^2*A1*C1),
g4 = (3/32)*(C0c^2 + rho^2*C1^2).                 (1.1)
```

Set `D=rho^2*C1^2-C0c^2`.  Direct expansion gives

```text
C1*g2 - C0c*g1             =  (3/8)*A1*D,
C0c*g2 - rho^2*C1*g1       = -(3/8)*A0c*D,
(32/3)*g4 + D              = 2*rho^2*C1^2,
(32/3)*g4 - D              = 2*C0c^2.              (1.2)
```

Consequently, for `I=(g1,g2,g4)`, both `C0c^2` and `rho^2*C1^2`
belong to `I` after localizing at either `A0c` or `A1`.  Therefore

```text
C0c,C1 in radical(I[rho^-1,A0c^-1])
and
C0c,C1 in radical(I[rho^-1,A1^-1]).                (1.3)
```

Equivalently, on

```text
D(rho) intersect (D(A0c) union D(A1)),
```

the three equations `g1=g2=g4=0` force `C0c=C1=0`.  Thus they contradict
exact nonzero leading `C`, given exact nonzero leading `A`.  This is a
set-theoretic/radical statement; it does not assert a scheme-theoretic
unit ideal before localization or radical.

The proof uses no root allocation, Hensel series, deck case split, leading
`k10` unit, `J` unit, or inversion of a leading `C` coefficient.  Only
`rho != 0` and `(A0c,A1) != (0,0)` are load-bearing.

## 2. When literal Faber rows have exactly these forms

For a strict unique-`AC` contact `(a,c=a+d,r)`, write

```text
G = 10+a+c,      T_C2 = 10+2c.
```

At grade `G`, the unique primitive `(3/4) AC/L` contributes (1.1)'s
`g1,g2` to `Phi1,Phi2`.  At grade `T_C2`, the primitive
`(3/8) C^2/L^2` contributes (1.1)'s `g4` to `Phi4`.  Every pole-one
primitive contributes identically zero to

```text
Phi4 = h4 + (P/2)*h2
```

by the exact moving-`P` simple-pole recurrence.  Hence the three rows are
literally (1.1), without allocating a root, whenever a fail-closed inventory
check proves all of the following:

1. `AC/L` is the only polar primitive at or before `G`;
2. every other primitive at or before `T_C2`, except `C^2/L^2`, has pole
   one;
3. the row-2 target has not reached `G` (`G<28`) and the row-4 target has
   not reached `T_C2` (`T_C2<32`); and
4. a reviewed literal-row bridge identifies `Phi1,Phi2,Phi4` with the
   total seven-tail emitter after the contact shift.

Condition 2 allows arbitrary pole-one loads and moving connection jets;
they cancel from `Phi4` rather than being set to zero.  It forbids silently
discarding a second- or higher-pole term.

The pinned low-`a` support miner

```text
0e94e5408b8a3b5db06c8eff5c759df1c75a2e8bb4563aa4964f42c39952fe9a
  cases/max12_812_order2_square_owner_d1_unique_ac_d23_small_a_support_miner_20260826/mine_support.py
```

mechanically gives the following complete baseline list before the first
load wall:

```text
d=1: a=2,3,4,5,6;
d=2: a=2,3,4,5,6;
d=3: a=5,6.
```

The independent desk replay

```text
xmodel/max12-812-order2-gate-t-strict-uac-three-row-syzygy-interface-replay-20260827.py
```

checks the four polynomial syzygies with an exact sparse-polynomial engine,
rehashes and imports the miner, reproduces the twelve-contact list, and runs
negative controls for `E`, the current `B23` `r=3,4` cells, and the `a=7`
`k6` tie.

Thus the pattern can potentially replace twelve contact-specific endpoint
proofs: all four finite-band `d=1,a=2..5` contacts, the `a=6,d=1` portion
of the load-transition endpoint, and seven of the eleven nonexceptional
low-`a` `d=2,3` contacts.  It does not replace the endpoint merely because
the inventory says so: a frozen row-level linker and review must first
certify conditions 1--4 for each manifest.

For exact `r` rather than the registered least closed tail, the same
inventory calculation recovers additional sub-tails:

```text
(a,d)=(1,2): r>=3;
d=3, a=2,3,4: r>=5.
```

In particular, the current `(a,c,r)=(2,5,>=3)` contact is not wholly a
three-row contact: the direct lemma covers its sub-tail `r>=5`, while
`r=3,4` still require the reviewed `B23` endpoint (or a stronger certificate
which retains the extra `RA^2` term).

## 3. Exact first walls

The low-band failures are mathematical, not documentary.

### Pole walls

The extra unloaded double-pole family

```text
RA^2/L^2 at grade 12+r+2a
```

enters by `T_C2` exactly when `r<=2d-2`.  This invalidates literal purity
for `(a,d,r)=(1,2,2)`, `(2,3,3)`, `(3,3,4)`, and `(4,3,4)` at their
registered baselines.  For the current `(2,3,>=3)` tail it occurs at grade
19 for `r=3` and grade 20 for `r=4`.

The pole-three family

```text
A^3/L^3 at grade 15+3a
```

enters by `T_C2` exactly when `a<=2d-5`; among strict contacts this first
occurs at the exceptional `E=(a,d,r)=(1,3,>=2)` and cannot be removed by
raising `r`.  At `E`, `k10*R^2*A/L^2` also reaches grade 18 at the least
tail, while `RA^2/L^2` already starts at grade 16.  This is why `E` has a
separate pole-three endpoint.

### Load walls

The pole-one load `k6*C/L` starts at grade `17+c`.  It ties `AC/L` at
`G` exactly when `a=7` and precedes it when `a>=8`; the first two remainder
rows are then coefficients of `C(A+k60)` or of a load-first expression,
not the two coefficients of `AC` alone.  Pole-one cancellation in `Phi4`
does not repair this contamination of `Phi1,Phi2`.

The later `k2*R/L` load starts at `22+r`; it ties or precedes `G` when

```text
22+r <= 10+2a+d.
```

At the least strict tails the first ties are `(a,d)=(9,3),(10,2),(11,1)`.
The pole-two `k2*A/L^2` term starts at `25+a` and reaches `T_C2` when
`15-a-2d<=0`.  These are later failures, already beyond the `k6` wall.

### Target walls

The full row `Phi2` first contains the `mu2` target at grade 28, so `g2`
is not source-pure when `G>=28`.  The full row `Phi4` first contains the
`mu4` target at grade 32, so `g4` is not source-pure when `T_C2>=32`.
A source-row identity may still be true beyond these walls, but source rows
are not equations of the target problem unless a separate reviewed target
elimination is supplied.

## 4. Minimal mechanical interface

A direct-syzygy linker needs only:

```text
contact (a,c,r), G, T_C2 and lower-jet ideal;
complete reviewed polar inventory through T_C2;
literal-row bridge and total-emitter/tail hashes;
target schedule;
the three extracted coefficients Phi1[G], Phi2[G], Phi4[T_C2];
symbolic equality to (1.1);
the four syzygies (1.2);
exact-A and exact-C predicates and the D(rho) localization.
```

It must reject a manifest if a non-`AC` primitive reaches `G`, a non-`C^2`
pole-`>=2` primitive reaches `T_C2`, either target wall is crossed, or the
rows are analytic auxiliaries without a reviewed bridge to literal
`Phi` rows.

This interface can replace the moving-root endpoint linker on the twelve
listed contacts after review.  The uniform formal-series naturality theorem
still supplies total/D1 transport for every other contact; the two
interfaces are complementary, not competing.  Neither says anything at
`rho=0`, on equality faces, on positive-order leading loads, on `V(k)`, on
the staged Rees charts or terminal receiver, or about either global `G2`
obligation, Gate T, order two, maximum twelve, JC2, or a counterexample.
