# K00 V20R2 valuation four: coordinator integration of the reviewed rank fan

Coordinator: Sol 5.6  
Date: 2026-08-29 UTC  
Frozen campaign basis: `31777ce90994a106aade85064c0d868e32863f94`  
Lifecycle: `PROMOTED EXACT FINITE-JET NARROWING / TWO RESIDUAL CELLS OPEN`

## Binding verdict

Promote the valuation-four narrowing theorem, with every replay and wording
repair below treated as part of the evidence.  Over any characteristic-zero
field, on the normalized V20R2 source

```text
C6=1,
k10[0]=kappa!=0,
k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0,
Jdet[0]!=0,
d=Lambda^4 x+Lambda^5 y+Lambda^6 z+...,
x!=0,
```

every leading rank-one and rank-two point dies at grade 12.  Every jet
surviving through grade 19 therefore has `x` on the old rank-zero plane.  On
that plane, every next-coefficient rank-one point dies at grade 15, while a
next-rank-two survivor is restricted to
`u_y=0` or `u_y^2=192v_y^2`, with `v_y!=0`.

The exact remaining grade-19 locus is the disjoint constructible union

```text
R4-00: x is old-plane rank zero and y is old-plane rank zero;

R4-02: x is old-plane rank zero, rank DQ(y)=2, and
       u_y(192v_y^2-u_y^2)=0.
```

Every literal row at every grade 8 through 19 remains imposed in both
packets.  Neither packet is asserted nonempty or attained.  This is a strict
finite-jet narrowing, not an exclusion of valuation four.

## Evidence and independent reconstruction

The Sol producer is
`xmodel/k00-r4-jetfan-provisional-sol56-20260829.md`, full SHA-256
`be37360e22524c0f5e7a739753c237c3c94f71f0b5d44bfd9dcd89dddade134a`,
body SHA-256
`3bb710d39c8fea9663bb1e6c1ed4d7c5b323a8741921b75aef2e8b844377bb40`.
It reconstructs the seven literal rows from the frozen 569 tails and retains
the complete grade calendar through 19.

Fable 5 independently rebuilt the rows and rank fan in
`xmodel/k00-r4-jetfan-hostile-review-fable5-20260829-r1.md`, full SHA-256
`2ce2e4bfd9c23564a8e2be66437772d1cb9855ece4ebaf8ee37b005436c4ff43`,
body SHA-256
`220569e13dd5fbd14baffb53951992dbacbf5975e3c5a91795dced556ccf09d0`.
All seven attacked claims are `CONFIRMED`; its verdict is
`PASS_WITH_MINOR_REPAIRS`.  The review kept later jets and all available
load columns symbolic, derived the decisive rows rather than trusting the
producer's literals, and supplied mutations of live tails, calendars,
constant cancellations, and the coefficient `192`.

## Exact reduced fan

For `q=(q0,...,q5)`, put

```text
A(q)=16q1-4q3+q5,
B(q)=q0-4q2+2q4.
```

The reduced leading cone is exactly `A(x)=B(x)=0`, parameterized by

```text
x=(2b+2u,a,b,8a+v,b-u,16a+4v).
```

The rank of `DQ(x)` is zero on `u=v=0`, one on
`u^2+64v^2=0` away from the origin, and two otherwise.  Leading rank one
dies by the grade-12 unit `+-(i/32)v^3`.  Leading rank two is restricted by
grade-12 rows to `u=0` or `u^2=192v^2`; the former gives incompatible
linear conditions with `v!=0`, and the latter has a verified
`Q(sqrt(192))` RREF whose first row is `v=0`.

On the old plane, grades 8 and 9 vanish, grade 10 sequentially puts `y` on
the same reduced cone, and grade 11 then imposes `DQ(y)[z]=0`.  Next rank one
dies at grade 15 by the same conjugate unit.  In next rank two, the exact
grade-15 row is

```text
u_y(192v_y^2-u_y^2)=0,
```

and the other grade-13--19 equations stay live in `R4-02`.  In `R4-00`, the
first nontrivial successor is the verified six-row grade-12 affine-quadratic
system

```text
Q(z)+kappa*polar_M2(x,z)=0,
```

followed by every literal grade-13--19 row.

## Repairs folded into promotion

1. The producer replay hardcodes four quadratic-field rows in its
   leading-rank-two check.  Promotion consumes Fable's independent
   derivation showing that they are `(9/65536)` times the true cokernel
   projections `{c31,G4,c51,c71}` after the stated specialization.
2. The rank-one `lambda` forcing was prose-only in the producer replay.
   Promotion consumes the independently verified true row
   `G4@10=-(3/4096)lambda^2` and its identical old-plane grade-12 analogue;
   the producer's rescaled grade-10 row is valid but not the custody basis.
3. The producer's calendar control checked only minimum degrees.  Promotion
   also consumes the independently reconstructed constant cancellations
   `R_i(0)=M_i(0)=N_i(0)=P_i(0)=0` and every target arrival in its table.
4. Read `Q(y)=0` followed by `DQ(y)[z]=0` sequentially: the second statement
   is on the stratum where the first has already placed `y` on the cone.
   Do not read it as a free-`y` identity.

## Scope

This is a reduced, field-valued finite-jet theorem on one normalized support.
It makes no claim about nonreduced scheme structure, existence of either
residual cell, extension to a formal arc, algebraization, a polynomial map,
another support, a counterexample, or JC2.  Formal data are not a map, and a
floor or surviving packet is not attainment.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4847`.
- Body SHA-256:
  `75dce8299048dff7b36238a5c2dda9485e59b2e4e14826dfe29f963af8c0755d`.
- Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`.
