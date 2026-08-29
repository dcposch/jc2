# K00 V20R2 valuation four: the `R4-00` entry solved, and its rank-zero cell excluded

Author: Claude Opus 5 (independent exact primary lane)
Date: 2026-08-29 UTC
Frozen campaign basis: `459ecb8051c11dcde55f51d178ea1b925f868a72`
Lifecycle: `PROVISIONAL_EXACT_DESK_THEOREM / DIFFERENT-MODEL REVIEW REQUIRED`

## 0. Result

On the exact normalized V20R2 source over a characteristic-zero field, on the
`R4-00` packet

```text
d = Lambda^4*x + Lambda^5*y + Lambda^6*z + ...,
x = ell(s,t), (s,t) != (0,0),      y = ell(s1,t1),
C6=1, k10[0]=kappa != 0, Jdet[0] != 0,
k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0,
```

with all literal rows `G_i,n = 0` (`1<=i<=7`, `8<=n<=19`) imposed:

1. **The grade-12 entry system is solved exactly.** The complete field-valued
   solution set of the six live rows of `Q(z)+kappa*polar_M2(x,z)=0` is
   precisely the reduced cone `A(z)=B(z)=0` — a four-dimensional linear space,
   independent of `(s,t,s1,t1,kappa)`. It is neither the single point `z=0`
   nor the full six-space, and it is *not* obtained by radicalizing: the
   defining ideal is a proper subideal of `(A,B)` and the equality is proved
   set-theoretically over every field of characteristic `!= 2`.
2. **The next linearization is the leading matrix at a shifted argument.**
   With `z = cone(a_z,b_z,u_z,v_z)`, the exact operator on the newest jet is
   `T[q] = DQ(z)[q] + kappa*polar_M2(x,q)`, and `T` equals the `DQ` matrix of
   Section 2 with `(u,v)` replaced by
   `(U,V) = (u_z + 5*kappa*s/6, v_z - 5*kappa*t/6)`. Its complete reduced rank
   fan is `rank 0: U=V=0`, `rank 1: Delta_T=U^2+64V^2=0, (U,V)!=(0,0)`,
   `rank 2: Delta_T != 0`.
3. **Grades 13, 14, 15 impose no new universal cokernel condition.** Grade 13
   is exactly `T[w]` with zero inhomogeneity; the five universal projections
   at grade 14 force `A(w)=B(w)=0` by the same two-line cone argument, in
   every cell; all five vanish identically at grade 15.
4. **One master law governs grade 14 in all three cells.** In the
   characteristic coordinates `sigma=s+8i*t`, `sigmabar=s-8i*t`,
   `tau=U+8i*V`, `taubar=U-8i*V` the grade-14 obstruction decouples into the
   conjugate pair `Omega(tau,sigmabar)`, `Omega(taubar,sigma)` of a single
   polynomial, with `Omega(0,x) = 5*kappa*Psi(x)/864` and
   `Psi(x) = x^2*(9x+50*kappa^2)`.
5. **The rank-zero cell of that fan is exactly empty.** Grade 14 pins the base
   to three explicit branches, grade 16 pins `(A(d[8]),B(d[8]))` to zero on
   each of them, and row 6 at grade 18 is then the raw nonzero unit
   `(5/6)^9*kappa^9/2^10` (first branch) or `(5/6)^9*kappa^9/2^11` (the two
   conjugate branches). No jet, load, target, cone coordinate or localizer
   enters that value.
6. **Grade 16 obeys a uniform closed law** `2592*Chat^2 + Xtilde(tau,sigmabar) = 0`
   and its conjugate, which on `tau,taubar != 0` becomes `K(tau,sigmabar)=0`,
   `K(taubar,sigma)=0` for one explicit nine-term polynomial `K`. That law
   does **not** exclude the rank-one or rank-two cells: for every `kappa!=0`
   and every `tau!=0` there are six nonzero roots `sigmabar` of `K(tau,-)`
   over an algebraic closure, all opens intact.

Hence the valuation-four `R4-00` packet is **not** closed. Its exact residual
through grade 19 is the disjoint union of two typed cells

```text
R4-00-1:  Delta_T = 0, (U,V) != (0,0)   [next-rank one]
R4-00-2:  Delta_T != 0                  [next-rank two]
```

serialized in Section 9. Neither is asserted nonempty or attained. This is a
strict narrowing plus one exact exclusion, not a valuation-four result.

## 1. Custody and independent reconstruction

All pinned inputs were re-hashed at this basis and are byte-identical to the
pins carried in the consumed pair:

```text
be37360e22524c0f5e7a739753c237c3c94f71f0b5d44bfd9dcd89dddade134a
  xmodel/k00-r4-jetfan-provisional-sol56-20260829.md
2ce2e4bfd9c23564a8e2be66437772d1cb9855ece4ebaf8ee37b005436c4ff43
  xmodel/k00-r4-jetfan-hostile-review-fable5-20260829-r1.md
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/compile_contracted_source_v20r2.py
196b693a24914469a70feb4349b2c60465a45c1f98ed677e93a3698b6d03e6ee
  xmodel/k00-r4-jetfan-replay-sol56-20260829.py
2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4
  xmodel/k00-r2-full-rank-fan-replay-sol56-20260829.py
```

The producer replay and the reviewer replay were **not executed and not used
as oracles**. Everything below was rebuilt clean-room in scratch outside the
repository (`/tmp/k00r400op5/`, stdlib-only, exact `Fraction` and
`Q[I]/(I^2+1)` arithmetic, no import of any producer or reviewer code): the
569 tail terms are parsed directly, the weight law
`sum(monomial * [8,7,6,5,4,3,2,2,6,10]) = 12+ell` and load linearity are
re-checked, and the seven rows are rebuilt from the frozen compiler's own
coordinate map. Total measured compute for every computation in this report
is under 20 CPU-seconds and well under 1 GiB. No Singular process, AWS job,
web request, external model, or `jc2-lean` access was used.

Independently reproduced against the reviewed pair (not assumed):

- constant-term cancellation `R_i(0)=M_i(0)=N_i(0)=P_i(0)=0`, all seven rows;
- degree censuses `R:{2,3,4},{2,3,4},{2,3,4,5},{2,3,4,5},{2,3,4,5},{3,4,5,6},
  {2,3,4,5,6}`; `N:{1,2},{1,2},{1,2,3},{2,3},{1,2,3},{2,3,4},{1,2,3,4}`;
- `Q_1+8Q_3 = (3/2048)*A*B`, `Q_4 = (3/524288)*B^2 - (3/8192)*A^2`,
  `Q_6 = 0` identically, and the whole `alpha_i/beta_i` table;
- the reviewed `R4-02` identity `G_6,15 = u_y*(192*v_y^2-u_y^2)/65536`
  (Section 10, control 1).

## 2. Literal source, calendar, and the binding calendar

Rows are `R_i(d) + Lambda^2*k10*M_i(d) + Lambda^6*k6*N_i(d)
+ Lambda^10*k2*P_i(d) - target_i`, truncated at `Lambda^20`, under
`C0=(1+d0)/256, C1=d1, C2=(1+d2)/16, C3=d3, C4=(3+d4)/8, C5=d5, C6=1`.
Write `Q=R^(2)`, `C3=R^(3)`, `C4=R^(4)`, `M2=M^(2)`, `N1=N^(1)`, `P1=P^(1)`,
and

```text
A(q) = 16q1 - 4q3 + q5,          B(q) = q0 - 4q2 + 2q4,
cone(a,b,u,v) = (2b+2u, a, b, 8a+v, b-u, 16a+4v),
ell(s,t)      = (2s, t/8, s, t, s, 2t) = cone(t/8, s, 0, 0),
adapted(a,b,u,v,A,B) = cone(a,b,u,v) + (B,0,0,0,0,A).
```

`adapted` is a `Q`-linear bijection with `A(adapted)=A`, `B(adapted)=B`.
On the old plane every functional that could carry `x` or `y` into the window
vanishes: for `x=ell(s,t)`,

```text
Q_i(x) = 0,  polar_Q_i(x, -) = 0,  M2_i(x) = 0,  N1_i(x) = 0,  C3_i(x) = 0,
polar_M2_i(ell(s,t), ell(s1,t1)) = 0,
C4_i(ell) != 0 for i != 6,  C4_6(ell) = 0,
P1_i(ell) != 0 for i in {1,2,3,5,7}.
```

Only `d[4..13]` occur anywhere in grades `8..19` on `R4-00`; the `d[14]` and
`d[15]` columns multiply only vanished functionals (verified, not assumed).

**Binding calendar.** Each target coefficient occurs in exactly one row at
exactly one grade with coefficient `-1` (or `-1/4`), so it converts that row
into a determination rather than an equation from its arrival grade on:
`mu2[j]` in row 2 at grade `14+j` (`j=1..5`), `mu4[j]` in row 4 at `16+j`
(`j=1..3`), `mu6[1]` in row 6 at 19, `Jdet[0]/4` in row 7 at 19. The five
universal cokernel projections (those annihilating both columns of the
leading matrix for every `(u,v)`) are

```text
G4,   G6,   c31 = G_3 + G_1/8,   c51 = G_5 + G_1/128,   c71 = G_7 + G_1/1024,
```

so the binding subsets are

```text
grade 13,14 : {G4, G6, c31, c51, c71}  + both W-directions
grade 15,16 : {G4, G6, c31, c51, c71}  + the e-direction only
grade 17,18 : {     G6, c31, c51, c71} + the e-direction only
grade 19    : {         c31, c51     } + the e-direction only,
              plus the inequation Jdet[0] != 0 after c71 determines it.
```

Here `W = span(e,f)` is the fixed two-plane containing both columns, with
`e = (3/1024, 0, -3/8192, 0, -3/131072, 0, -3/1048576)` and
`f = (0, 3/256, 0,0,0,0,0)`; the `f` (row-2) direction stops binding once
`mu2[1]` arrives at grade 15.

## 3. The grade-12 `R4-00` entry system, solved

With `x=ell(s,t)`, `y=ell(s1,t1)` and every later jet, load and target
symbolic, grades 8 through 11 vanish identically and

```text
G_i,12 = Q_i(z) + kappa*polar_M2_i(x,z),        i = 1..7,
```

verified as a raw identity for all seven rows, with `G_6,12 = 0` identically
and with no dependence on `s1`, `t1`, on `d[7]` or later, or on any load
beyond `kappa`. In `z = adapted(a_z,b_z,u_z,v_z,A_z,B_z)` the system loses
`a_z,b_z` entirely and reads, with

```text
E = A_z*u_z - B_z*v_z,   F = A_z*B_z,   K = kappa*(A_z*s + B_z*t),
```

```text
G_1,12 = ( 3/1024   )E - ( 3/2048   )F + ( 5/2048   )K
G_3,12 = (-3/8192   )E + ( 3/8192   )F - ( 5/16384  )K
G_5,12 = (-3/131072 )E - ( 3/262144 )F - ( 5/262144 )K
G_7,12 = (-3/1048576)E                 - ( 5/2097152)K
G_4,12 = (3/524288)*(B_z^2 - 64*A_z^2)
G_2,12 = (3/256)A_z*v_z + (3/16384)B_z*u_z + (15/2048)A_z^2
         + (5/32768)*kappa*(B_z*s - 64*A_z*t)
G_6,12 = 0.
```

The `4x3` matrix of rows `{1,3,5,7}` in the basis `(E,F,K)` has rank two with
reduced row echelon form `{F = 0, 6E + 5K = 0}` — a verified exact linear
algebra fact, not a Groebner step. So

```text
rows {1,3,5,7}  <=>  A_z*B_z = 0  and  6*(A_z*u_z - B_z*v_z) + 5*kappa*(A_z*s + B_z*t) = 0,
row 4           <=>  B_z^2 = 64*A_z^2.
```

**Two-line solve.** `A_z*B_z = 0` gives `A_z=0` or `B_z=0`; either one fed
into `B_z^2 = 64*A_z^2` gives the other. Over every field of characteristic
`!= 2`, `A_z = B_z = 0`. Conversely all seven rows vanish identically on
`A(z)=B(z)=0` (verified). Therefore

```text
V(G_*,12)  =  { z : A(z) = B(z) = 0 }  =  cone(a_z,b_z,u_z,v_z),  four free parameters,
```

with no condition on `(s,t,s1,t1,kappa)` and no localizer used. The zero
solution `z=0` is one point of this space, not the answer. Scheme-theoretic
caution: every listed generator lies in `(A,B)*(u,v,A,B,kappa*s,kappa*t)`, so
the grade-12 ideal is a proper, non-radical subideal of `(A,B)`; the equality
above is a statement about field-valued points only, which is the type of the
`R4-00` packet.

## 4. The next linearization and its complete reduced rank fan

At every grade `n` in `13..19` the newest jet is `d[n-6]`; it enters exactly
once, through

```text
T_i[q] := DQ_i(z)[q] + kappa*polar_M2_i(x,q).
```

`T` factors through `(A(q),B(q))` only, and with

```text
U := u_z + 5*kappa*s/6,        V := v_z - 5*kappa*t/6
```

the seven-row matrix of `T` is, coefficient-exactly, the leading `DQ` matrix
with `(u,v)` replaced by `(U,V)`:

```text
row1: ( 3/1024   )U*A + (-3/1024   )V*B     row2: (3/256)V*A + (3/16384)U*B
row3: (-3/8192   )U*A + ( 3/8192   )V*B     row4: 0
row5: (-3/131072 )U*A + ( 3/131072 )V*B     row6: 0
row7: (-3/1048576)U*A + ( 3/1048576)V*B
```

verified slot by slot for all seven rows. The `2x2` minors are rational
multiples of `Delta_T = U^2 + 64V^2`, so the complete reduced rank fan of the
next linearization is

```text
R4-00-0 : U = V = 0                          (rank T = 0)
R4-00-1 : Delta_T = 0, (U,V) != (0,0)        (rank T = 1; empty unless i is in the field)
R4-00-2 : Delta_T != 0                       (rank T = 2)
```

The shift is genuinely nonzero: `kappa != 0` and `(s,t) != (0,0)` force
`(5*kappa*s/6, -5*kappa*t/6) != (0,0)`. This is a literal identity at one
grade; **no periodicity, shift-ladder or self-similarity is inferred from it**,
and none is used below.

## 5. Grades 13, 14 and 15

- **Grade 13** is exactly `G_i,13 = T_i[w]`, all seven rows, with zero
  inhomogeneity (verified with the matching `z`).
- **Grade 14.** The five universal projections of the grade-14 rows are
  exactly the corresponding `Q`-combinations of `w`, i.e. in adapted
  coordinates `A(w)*B(w)` (from `c31`, `c51`, `c71`) and
  `B(w)^2 - 64*A(w)^2` (from `G4`), with `G6 = 0`. By the same two-line
  argument, `A(w) = B(w) = 0` in **every** cell, independently of
  `rank T`, of `(U,V)`, and of `kappa,s,t`. With `w` on the cone the grade-14
  rows become `T[d[8]] + I_14` with `I_14` lying in the fixed two-plane `W`
  (all five universal projections of `I_14` vanish identically).
- **Grade 15.** All five universal projections vanish identically.

So no cell is separated before grade 16 by a universal cokernel row.

## 6. The grade-14 obstruction: one master law

Write `I_14 = P_14*e + Q_14*f`, i.e. `P_14 = (1024/3)*I_14[1]`,
`Q_14 = (256/3)*I_14[2]`. In the characteristic coordinates

```text
sigma = s + 8i*t,   sigmabar = s - 8i*t,   tau = U + 8i*V,   taubar = U - 8i*V,
Delta_T = tau*taubar,   s = (sigma+sigmabar)/2,   t = (sigma-sigmabar)/(16i),
```

the obstruction decouples completely:

```text
P_14 + 8i*Q_14 =  i*Omega(tau,    sigmabar),
P_14 - 8i*Q_14 = -i*Omega(taubar, sigma),

Psi(x)   = x^2*(9x + 50*kappa^2),
Omega(y,x) = [ 360*kappa*y^2 - 12*x*(9x+50*kappa^2)*y + 5*kappa*Psi(x) ] / 864,
Omega(0,x) = 5*kappa*Psi(x)/864.
```

Grade 14 is therefore, in every cell,

```text
tau   * ( A(d[8]) + (i/8)*B(d[8]) ) = -i*Omega(tau,    sigmabar),
taubar* ( A(d[8]) - (i/8)*B(d[8]) ) = +i*Omega(taubar, sigma).
```

**Cell law at grade 14.**

```text
R4-00-2 (tau,taubar != 0) : no base condition; (A,B)(d[8]) uniquely determined.
R4-00-1 (taubar = 0)      : Psi(sigma) = 0;    A - (i/8)B free, A + (i/8)B determined.
R4-00-1 (tau    = 0)      : Psi(sigmabar) = 0; conjugate statement.
R4-00-0 (tau=taubar=0)    : Psi(sigma) = Psi(sigmabar) = 0; (A,B)(d[8]) free.
```

In the real coordinates the rank-zero law is `E1 = E2 = 0` with

```text
E1 = t*(27*s^2 - 576*t^2 + 100*kappa^2*s),
E2 = 9*s^3 + 50*kappa^2*s^2 - 1728*s*t^2 - 3200*kappa^2*t^2,
16*E1 = -i*Psi(sigma) + i*Psi(sigmabar),      2*E2 = Psi(sigma) + Psi(sigmabar),
```

and the rank-one law is `8*E1 -+ i*E2 = 0`, i.e. exactly
`Psi(sigma) = 0` resp. `Psi(sigmabar) = 0`. Every identity in this section is
verified as a polynomial identity with all jets, loads and targets symbolic.

## 7. Cell `R4-00-0` (rank `T = 0`): exact emptiness at grade 18

**Step 1 (grade 14).** `Psi(sigma) = Psi(sigmabar) = 0` with `(s,t)!=(0,0)`
means `sigma, sigmabar` each lie in `{0, -50*kappa^2/9}`, not both zero:

```text
(a)  sigma = sigmabar = -50*kappa^2/9  :  t = 0,  s = -50*kappa^2/9;
(b+) sigma = -50*kappa^2/9, sigmabar=0 :  s = -25*kappa^2/9, t = +(25/72)*i*kappa^2;
(b-) sigma = 0, sigmabar=-50*kappa^2/9 :  s = -25*kappa^2/9, t = -(25/72)*i*kappa^2.
```

Branch (a) exists over every characteristic-zero field; (b±) need `i`.
Equivalently, in real form: `t=0` forces `s^2*(9s+50*kappa^2)=0` hence
`s = -50*kappa^2/9`; and for `t != 0`, eliminating `t^2` from `E1` in `E2`
gives exactly `-(8/9)*s*(9s+25*kappa^2)^2`, so `s = -25*kappa^2/9` and
`t^2 = -625*kappa^4/5184`.

**Step 2 (grade 16).** At `U=V=0` the two independent grade-16 projections are
exactly

```text
c31@16 = (3/16384)*Ahat*Bhat        - (25*kappa^2/442368 )*E1,
G4 @16 = (3/524288)*(Bhat^2-64*Ahat^2) - (25*kappa^2/7077888)*E2,
```

with `Ahat = A(d[8]) + alpha_0`, `Bhat = B(d[8]) + beta_0`,
`alpha_0 = -2*s*t - (50/9)*kappa^2*t`,
`beta_0 = -s^2 + 64*t^2 - (50/9)*kappa^2*s`
(and `c51@16 = -c31@16/8`, `c71@16 = -c31@16/128`, `G6@16 = 0`). Since
`E1 = E2 = 0` from Step 1, grade 16 is again `Ahat*Bhat = 0` and
`Bhat^2 = 64*Ahat^2`, hence `Ahat = Bhat = 0`. On each of the three branches
`alpha_0 = beta_0 = 0`, so

```text
A(d[8]) = B(d[8]) = 0,   i.e. d[8] lies on the reduced cone.
```

**Step 3 (grade 18, the kill).** Row 6 at grade 18 is target-free (`mu6[0]` is
a fixed zero and `mu6[1]` first arrives at grade 19). With `x,y` on the old
plane, `z` at `U=V=0`, `w` on the cone, `d[8]` on the cone, and
`d[9]..d[13]` in adapted coordinates fully free, all load columns
`k10[1..9], k6[1..9], k2[1..5]` symbolic, all targets symbolic, and
`a_z,b_z,s1,t1` free, the raw row-6 grade-19-window coefficient is the
constant

```text
branch (a) :  G_6,18 = 5^9 * kappa^9 / (2^19 * 3^9) = (5/6)^9 * kappa^9 / 2^10,
branch (b+):  G_6,18 = 5^9 * kappa^9 / (2^20 * 3^9) = (5/6)^9 * kappa^9 / 2^11,
branch (b-):  G_6,18 = 5^9 * kappa^9 / (2^20 * 3^9) = (5/6)^9 * kappa^9 / 2^11.
```

Since `kappa != 0` is an open of the packet, this is a unit and
`G_6,18 = 0` is unsatisfiable. Because the constant carries no jet, load,
target, cone-coordinate or localizer, no later grade, no deeper rank fan and
no choice at grades 15 or 17 can rescue it. **Cell `R4-00-0` is empty over
every characteristic-zero field.**

The kill is genuinely sequential: with `A(d[8]),B(d[8])` left free the same
row-6 grade-18 expression is `-5*kappa*A(d[8])^2/32768 +
5*kappa*B(d[8])^2/2097152 + (12500/169869312)*kappa^5*B(d[8]) + (5/6)^9*kappa^9/2^10`
on branch (a), which is not a unit; Step 2 is load-bearing and is reported as
such rather than folded into a single identity.

## 8. Grade 16: one uniform closed law

With `Chat = Ahat + (i/8)*Bhat`, `Cbar = Ahat - (i/8)*Bhat` (the same
`alpha,beta` shifts, now at general `(U,V)`:
`alpha = -(20/3)*V*kappa - 2*s*t - (50/9)*kappa^2*t`,
`beta = (20/3)*U*kappa - s^2 + 64*t^2 - (50/9)*kappa^2*s`), the two
independent grade-16 constraints decouple exactly:

```text
c31@16 + 2i*G4@16 = -(3i/4096)*Chat^2 - i*X(tau,    sigmabar),
c31@16 - 2i*G4@16 = +(3i/4096)*Cbar^2 + i*X(taubar, sigma),

Xtilde(y,x) = 72*y^2*(9x+25*kappa^2) - 30*kappa*x*y*(27x+100*kappa^2) + 25*kappa^2*Psi(x),
X = Xtilde/3538944,      Xtilde(0,x) = 25*kappa^2*Psi(x).
```

So grade 16 is exactly

```text
2592*Chat^2 + Xtilde(tau, sigmabar) = 0,     2592*Cbar^2 + Xtilde(taubar, sigma) = 0.
```

Grade 14 supplies the closed forms (valid identically, no division):

```text
tau    * Chat = +(5i*kappa/864)*(72*tau^2    - Psi(sigmabar)),
taubar * Cbar = -(5i*kappa/864)*(72*taubar^2 - Psi(sigma)).
```

Multiplying the grade-16 equations by `tau^2`, `taubar^2` gives the single
nine-term polynomial law

```text
K(y,x) = 25*kappa^2*(72*y^2 - Psi(x))^2 - 288*y^2*Xtilde(y,x)
       = -15552*(12x+25*kappa^2)*y^4 + 8640*kappa*x*(27x+100*kappa^2)*y^3
         - 10800*kappa^2*Psi(x)*y^2 + 25*kappa^2*Psi(x)^2,

grade 16  ==>  K(tau, sigmabar) = 0   and   K(taubar, sigma) = 0,
```

an equivalence whenever `tau`, `taubar != 0`. This was cross-checked against
the independent route that first solves grade 14 for `(A,B)(d[8])` as rational
functions with denominator `Delta_T` and then clears denominators:
`Delta_T^2*(c31 + 2i*G4)@16 = i*taubar^2*K(tau,sigmabar)/1019215872` exactly,
and the conjugate.

Consistency across the fan: `K(0,x) = 25*kappa^2*Psi(x)^2`, so at rank zero
the law is implied by grade 14 and the content of grade 16 there is the
determination `Chat = Cbar = 0` used in Section 7; at rank one
(`taubar = 0`, `Psi(sigma) = 0`) it is the determination `Cbar = 0` together
with `K(tau,sigmabar) = 0`.

**Grade 16 does not exclude `R4-00-1` or `R4-00-2`.** As a polynomial in `x`,
`K(y,x)` has degree six with leading coefficient `2025*kappa^2 != 0`, and
`K(y,0) = -388800*kappa^2*y^4 != 0` for `kappa,y != 0`. Hence for any
`kappa != 0` and any `tau != 0` there are six roots `sigmabar`, all nonzero,
over an algebraic closure; likewise for `taubar`. Every open survives:
`Delta_T = tau*taubar != 0`, and `(sigma,sigmabar) != (0,0)` gives
`(s,t) != (0,0)`. This is a statement about the grade-16 constraint alone; it
asserts nothing about grades 17 to 19 and nothing about `R4-00`.

## 9. Serialized residual for `R4-00-1` and `R4-00-2`

Variable order (canonical, used for the digest):

```text
kappa . x . y . sg . sgb . ta . tab . I . A8 . B8 . U . V . s . t
[ + az . bz . uz . vz . Az . Bz for the grade-12 records ]
```

Source map (frozen compiler, restated for the packet):

```text
C0=(1+d0)/256; C1=d1; C2=(1+d2)/16; C3=d3; C4=(3+d4)/8; C5=d5; C6=1;
k10 << 2; k6 << 6; k2 << 10; mu2 << 14; mu4 << 16; mu6 << 18; Jdet << 19 (coefficient -1/4);
truncation Lambda^20;  boundary zeros k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0.
```

Characteristic map:

```text
sigma = s+8i*t; sigmabar = s-8i*t; tau = U+8i*V; taubar = U-8i*V;
U = u_z + 5*kappa*s/6;  V = v_z - 5*kappa*t/6;  Delta_T = tau*taubar = U^2+64V^2.
```

Equalities imposed (complete, grades 8 to 19):

```text
g08..g11  identically satisfied
g12       A(z) = B(z) = 0                                       [Section 3]
g13       A(w) = B(w) = 0 (via g14 universal projections)        [Section 5]
g14       tau*Chat    = +(5i*kappa/864)*(72*tau^2 - Psi(sigmabar))
          taubar*Cbar = -(5i*kappa/864)*(72*taubar^2 - Psi(sigma))
          plus, on R4-00-1 only, Psi(sigma) = 0 (taubar=0) or Psi(sigmabar)=0 (tau=0)
g15       no universal constraint; e-direction determines (A,B)(d[9]) on R4-00-2
g16       2592*Chat^2 + Xtilde(tau,sigmabar) = 0
          2592*Cbar^2 + Xtilde(taubar,sigma) = 0
          equivalently K(tau,sigmabar) = K(taubar,sigma) = 0 on tau,taubar != 0
g17       c31@17 = 0  (c51@17 = -c31@17/8, c71@17 = -c31@17/128; G4 absorbed by mu4[1])
g18       G6@18 = 0 and c31@18, c51@18, c71@18 = 0
g19       c31@19 = 0 and c51@19 = 0
```

Opens: `kappa != 0`; `Jdet[0] != 0` (determined by `c71@19`, hence an
inequation on the remaining data); `(s,t) != (0,0)`, equivalently
`(sigma,sigmabar) != (0,0)`; `Delta_T != 0` on `R4-00-2`,
`Delta_T = 0 != (U,V)` on `R4-00-1`.

Inert affine factors (occur in no binding constraint through grade 19, hence
free after every equation is imposed): the ten target columns
`mu2[1..5], mu4[1..3], mu6[1], Jdet[0]` — each determined by exactly one row
at exactly one grade. The jet columns `d[14]`, `d[15]` do not occur in any
row at any grade `<= 19` on `R4-00` and are unconstrained. Every other listed
variable occurs in some binding constraint and is *not* inert.

Canonical serialization rule (pinned, so the digest is reproducible):
each record is `name|dotted-variable-order|body`; the body is
`;`-joined `exponent-vector:numerator/denominator` items with the exponent
vector comma-joined in the declared order, coefficients in lowest terms with
positive denominator, items sorted by `(total degree, exponent vector)`;
records joined by `\n` with a trailing `\n`; digest is SHA-256 of the UTF-8
bytes. Records, in order: `SRCMAP`, `CHARMAP`, `CALENDAR`, `Psi`, `Omega`,
`Xtilde`, `K`, `G1_12` .. `G7_12`.

```text
RESIDUAL_SERIALIZATION_BYTES = 3060
RESIDUAL_DIGEST_SHA256 = edd47ee14d921e720ac4b214afa0e7c28ec914d26a8b64279aea0080b4995ec8
```

## 10. Controls

Positive:

1. From this reconstruction alone, with `x=ell(s,t)`, `y` on the cone, `z` on
   the cone and `d[7]` onward fully free with all loads and targets symbolic,
   `G_6,15 = (3/1024)*u_y*v_y^2 - u_y^3/65536 = u_y*(192*v_y^2-u_y^2)/65536`,
   reproducing the promoted `R4-02` identity exactly.
2. On the leading cone, `G_6,12 - u*(192*v^2-u^2)/65536 = kappa*M2_6(d[5])`,
   which vanishes once `d[5]` is on the cone. This reproduces the producer's
   Section 4 identity *and* independently confirms the reviewer's Repair 4:
   the identity is true in the sequential reading (grade 9 first) and false in
   the free-`d[5]` reading.
3. A consolidated harness of seventeen assertions covering Sections 3, 4, 5,
   6, 7 and 8: sixteen passed on the first run (4.5 s) and the seventeenth
   failed because I had built that assertion with a mismatched `z` (plain
   `cone(a,b,u,v)` compared against rows generated at `z(U,V)`); rebuilt with
   the matching `z` it passes. The identity it tests had already been
   verified separately in Section 5.

Negative (mutation) controls, all detected:

1. `+1` on the row-6 unloaded tail monomial `C4*C5^2*C6^4`: `Q_6` is no longer
   identically zero, and the rank-zero grade-18 row-6 value stops being a unit
   — it becomes a 40-term expression in `A9..A13, a8..a13, aw, az, t1, s1,
   kappa`. So Section 7 is a property of the frozen source, not a formality.
2. `+1` on the first row-6 tail coefficient (`C6^4*k2`): detected by the
   constant-census gate, which fires with `P_6(0) = 1`. Recorded honestly: this
   mutation is *invisible* to my row builder itself, because that builder keeps
   only the homogeneous degrees that can arrive in the `Lambda^20` window
   (`R^(2..4)`, `M^(2..4)`, `N^(1..3)`, `P^(1..2)`) and therefore silently drops
   a degree-zero part. The constant cancellations
   `R_i(0)=M_i(0)=N_i(0)=P_i(0)=0` are consequently a precondition of every
   computation in this report, not a corollary of one; they are verified
   directly on the frozen tails (Section 1) and are exactly the load-bearing
   fact the reviewer of the parent flagged as unreplayed.

## 11. Maximum exact result and cheapest successor

Safe to promote, over any characteristic-zero field, on the `R4-00` packet:

1. the grade-12 entry system has complete field-valued solution set exactly
   `{A(z)=B(z)=0}`, with the two-line certificate of Section 3 in the original
   seven-row presentation;
2. the next linearization is the leading matrix at `(U,V) = (u_z+5*kappa*s/6,
   v_z-5*kappa*t/6)`, with the complete reduced rank fan of Section 4;
3. grades 13 to 15 impose no new universal cokernel condition, and grade 14 is
   governed by `Omega`, i.e. by `Psi(x) = x^2*(9x+50*kappa^2)`, as in
   Section 6;
4. the rank-zero cell `R4-00-0` is **exactly empty**, killed at grade 18 by the
   raw unit `(5/6)^9*kappa^9/2^10` (or `/2^11`), by the three-step sequential
   certificate of Section 7;
5. grade 16 obeys the closed law of Section 8, which does not exclude
   `R4-00-1` or `R4-00-2`;
6. the exact residual through grade 19 is the disjoint constructible union
   `R4-00-1 (+) R4-00-2` as serialized in Section 9, typed `OPEN`.

Cheapest decisive successor, in order:

1. **`R4-00-1` closure (preferred, likely still desk-scale).** On
   `taubar = 0`, `Psi(sigma) = 0` the grade-14 and grade-16 data collapse to
   three quadratics in one unknown `A(d[8])` over `Q(i)[kappa, tau, sigmabar]`,
   and the two grade-16 rows already reduce to `Cbar = 0` plus
   `K(tau,sigmabar) = 0`. What remains is `Res` of `K(tau,sigmabar)` against
   the grade-18 row-6 equation in the two unknowns `(tau, sigmabar)` after
   `kappa = 1` (legitimate: the whole system is weighted-homogeneous with
   `wt(kappa,s,t,U,V) = (1,2,2,3,3)` and `kappa != 0`). Both sub-branches
   `sigma = 0` and `sigma = -50*kappa^2/9` must be run.
2. **`R4-00-2`.** Three weighted-homogeneous necessary conditions in
   `(U,V,kappa,s,t)` alone — `Delta_T^2*G4@16`, `Delta_T^2*c31@16` (degree 12,
   66 and 60 terms) and `Delta_T^2*G6@18` (degree 13, 109 terms) — equivalently
   `K(tau,sigmabar) = K(taubar,sigma) = 0` plus the swap-symmetric 28-term
   `G6@18` in characteristic coordinates. Then grades 17, 18 (`c31,c51,c71`)
   and 19 (`c31,c51`), which first bring `A(d[9]),B(d[9])`, the load columns
   `k10[1..3], k6[1..3], k2[1..3]`, `s1,t1`, and the cone coordinates
   `u_w,v_w,u_8,v_8,u_9,v_9,a_z,b_z,a_w,b_w`.

**Frozen AWS packet** (if either stalls): pinned tails `d72f774c...` and
compiler `2ac7653c...`; ring `Q(I)/(I^2+1)` adjoining nothing else, `dp`
order, variables in the Section 9 canonical order; generators exactly the
Section 9 equality list with `kappa` set to 1 by the stated weighted
homogeneity; saturate by `tau*taubar` on `R4-00-2` (by `tau` on the
`taubar = 0` branch of `R4-00-1`) and by `sigma^2 + sigmabar^2 + sigma*sigmabar`
to enforce `(s,t) != (0,0)`; eliminate the jet, load and target variables
grade by grade through 19; decide emptiness. No other computation.

## 12. Scope and nonclaims

This is a reduced, field-valued, finite-jet result on the exact normalized
V20R2 support. The grade-12 statement is an exact solve of a literal
polynomial system, not a radical, a normalization, a generic-chart argument,
or a treatment of a proper ideal as nonempty; its scheme structure is
explicitly non-reduced and no scheme-theoretic claim is made. The rank-zero
exclusion is emptiness of that one cell only.

Nothing here asserts that `R4-00-1` or `R4-00-2` is nonempty, that any of them
is attained, or that a point in either would be an arc, an algebraic germ, a
map, or a Keller counterexample. Formal jets are not arcs and not maps; a
finite-jet residual is not attainment; a floor is not equality. No periodicity
or shift-ladder is claimed: the recurrence of the same two-line cone identity
at grades 12, 14 and 16 is three separately verified literal facts, and each
is used only at its own grade. Nothing is claimed about `R4-02` (excluded
elsewhere), about exact valuations three or five, about another support or
normalization, or about JC2.

Only this report was created. No canonical or existing artifact was edited,
no `jc2-lean` path was entered, listed, stated or built, and no web access,
Singular process, AWS job or external model was used. Promotion requires a
different model to rebuild the seven rows from the frozen tails and to attack
Sections 3, 4, 6, 7 and 8 independently.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `28769`.
- Body SHA-256:
  `2d165377ff03ae2d8c252333e7905dbae897daf6a593278ee0409563f7d422b9`.
- Frozen basis: `9b64db896b65e100839f6d75fbeea661cd818b9c`.
