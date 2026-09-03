# The q-directions of the K=16 terminal cone: a uniform sub-chart theorem,
# and the exact reach of the sub-chart method

Continuation of the weighted-cone route of `k16-terminal-proof-opus5-20260903`.
That report reduced `(8.1)` to `tau_t in sqrt(I_(t,+))`, proved the spine
grading and Proposition SUBCHART, and killed the `b3`-direction for every
`t>=3`.  The residual it named was `(10.1)`, the `q`-directions of the `b4=0`
cone.  This lane carries out the `R = {q_(t-1,0), b3}` computation symbolically
in `t`, iterates it in `j`, and then determines exactly how much of `(10.1)`
the sub-chart method can and cannot deliver.

## Verdict

```text
(T) on the K=16 ray for all t>=1 : NOT PROVED.  Typed OPEN.
(10.1) as stated                 : NOT PROVED, and NOT REACHABLE by sub-charts
                                   (Sec. 1 and Sec. 6; the obstruction is
                                   proved, not conjectured).

PROVED-HERE-1  Lemma CHAIN.  dim I_(t,+)=0 holds iff the residual variables
               admit an ordering v_1..v_n with v_i in sqrt(I+(v_1..v_(i-1)))
               for each i.  Step i is a statement on the sub-chart where
               v_1..v_(i-1) vanish, so the method supplies the TAIL of the
               chain, never its head; the head of the natural ordering is
               exactly the producer's b4=1 top-tail unit test.

PROVED-HERE-2  Theorem Q-PLANE.  For t>=6, on S={b4=q_(2,0)=..=q_(t-2,0)=0} the
               spine collapses to five A_t-scalars in closed form, exactly
               eight (band,monomial) coefficients survive in the positive
               terminal rows -- ALL EIGHT units of A_t in closed form for
               t>=3 -- and T_(t,2t-1)|_S = alpha_t b3^2,
               T_(t,t+4)|_S = A2 q_(t-1,0)^3 with alpha_t (the banked b3-axis
               unit, re-derived here) and A2 both units.  So
               sqrt(I_(t,+)|_S) = (q_(t-1,0),b3): the chain step (C_(t-1)).
               t=3,4,5 confirmed separately on the exact records.

PROVED-HERE-3  Lemma UNIQUE-POWER: for fixed r and t >= m(1+r), q_(t-r,0)^m is
               the ONLY monomial of weight m(t-r) in the chain residual.  Hence
               the two-variable chart R_r already computes the coefficient on
               the full chain sub-chart and delivers the step (C_(t-r)) itself.
               The r=1..5 closed forms give
               V(I_(t,+)) cap {b4=q_(2,0)=..=q_(t-R-1,0)=0} = {0} for t>=3R+3,
               R=1..5 -- a coordinate subspace of dimension R+1; every further
               step reduces to one unit test HYP(r), capped at r<=(t-3)/3.

PROVED-HERE-4  The initial-form upgrade FAILS.  Sub-chart restriction is the
               in_w degeneration for w=0 on R and 1 off R, so
               dim <in_w(gens)> = 0 would certify dim I_(t,+) = 0.  It does
               not: DIM = 2,3,3,4 at t = 4,5,6,7.

RESIDUAL      The head of the chain: b4 in sqrt(I_(t,+)) (equivalently the
              b4=1 chart is the unit ideal) and then q_(2,0) on the full b4=0
              cone.  Neither is a sub-chart statement.
```

`FALLACY-v2` applies throughout.  No exit-price assertion is made, so no
`charge_basis` line is declared.  No ledger, `jc2-lean`, `ideation-*` or
in-progress lane report was read or written.

## 0. Custody

The 24 charged inputs were verified mechanically: the manifest was generated
from the lane receipt with `awk -F=` over its `charged_input_<i>_sha256=` and
`charged_input_<i>_basename=` lines and piped to `sha256sum -c`.  All 24 lines
report `OK`.  Drivers and artifacts are in
`box/k16subchart-20260903/`.  Exact records used: the charged
`box/k16spine-20260903/terminal_laurent_t{3,4,5}.json`, the charged
`chart_t7_b4_0.json`, and (as prior-lane, non-charged artifacts of the same
campaign, flagged as such wherever used) `chart_t6_b4_0.json`.

Typing of the algebra is unchanged: `A_t = Q[y]/(H_t)`, `q=2t+1`, `e=3t+1`,
and with `d = 2qy-(t+1)`, `3d^2 = t+1`, so `A_t = Q[d]/(3d^2-(t+1))`.  `H_t` is
reducible over `Q` exactly at `t = 3s^2-1`; in `2<=t<=8` only `t=2`, branched
to `y=1/5` (`d=-1`) and `y=2/5` (`d=+1`) wherever it appears.  Norm convention:
for `u = (Ad+B)/D` with `A,B,D` polynomial in `t`, the printed `N` is
`N(Du) = B^2 - A^2(t+1)/3`, so `N(u) = N(Du)/D^2` and the vanishing locus is
that of the printed polynomial.  The map to the record encoding is
`Res_y(H_t,u) = 12q^2 N(u)`, verified at `t=6,7` (Sec. 7).

## 1. Lemma CHAIN: what a sub-chart can and cannot prove

Work over an algebraically closed field `K` with a ring map `A_t -> K` (a
geometric point of `Spec A_t`).  Write `I = I_(t,+)` in `K[v_1,...,v_n]`, the
residual variables `b4, q_(2,0),...,q_(t-1,0), b3` in some order, `n = t`.

**Lemma CHAIN.** If `v_i in sqrt(I + (v_1,...,v_(i-1)))` for `i = 1,...,n`,
then `sqrt(I)` is the irrelevant maximal ideal, so `V(I) = {0}` and
`dim I = 0`.  Conversely if `dim I = 0` then every ordering works.

*Proof.* `v_i in sqrt(J)` gives `sqrt(J) = sqrt(J+(v_i))`; applying this with
`J = I + (v_1..v_(i-1))` for `i=1..n` in turn gives
`sqrt(I) = sqrt(I+(v_1,..,v_n)) = (v_1,..,v_n)`.  Converse immediate. `[]`

Step `i` is *exactly* a sub-chart statement: `I + (v_1..v_(i-1))` is generated
by the restrictions of the `T_(t,k)` to `S = {v_1=..=v_(i-1)=0}`, with residual
variables `v_i,...,v_n`.  A sub-chart collapses (Prop. SUBCHART) only when few
variables survive, i.e. only for *large* `i`: the method supplies the tail of a
chain and never its head, since the first step is posed on the full chart.
With the ordering `b4, q_(2,0), ..., q_(t-1,0), b3` the last step is B3-AXIS
(one residual variable), the last-but-one is Sec. 3 (two), and the first is
`b4 in sqrt(I)`, equivalent by homogeneity to `I|_(b4=1) = (1)`, the producer's
`TOP-TAIL-UNIT`.

So `(10.1)` as posed -- `q_(j,0) in sqrt(I_(t,+) + (b4))` -- is not what a
sub-chart delivers: at `j = t-1` it would need the *whole* `b4=0` cone with
`q_(2,0)..q_(t-2,0)` free, whereas the sub-chart proves
`q_(t-1,0) in sqrt(I + (b4,q_(2,0),..,q_(t-2,0)))`.  Nor can a different chart
be chosen: on `{b4=0}` the residual weights are `2,3,...,t-1,t+1`, and for
`t >= 5` the pair `2,3` already generates every integer `>= 2`, so no
eliminated variable is killed by weight and Proposition SUBCHART yields
nothing there.  The correct all-`t` target replacing `(10.1)` is the chain

```text
(C0)  b4      in sqrt(I)                                        [= TOP-TAIL-UNIT]
(Cj)  q_(j,0) in sqrt(I + (b4, q_(2,0),...,q_(j-1,0))),  2<=j<=t-1
(Cb)  b3      in sqrt(I + (b4, q_(2,0),...,q_(t-1,0)))           [= B3-AXIS]
```

of which this lane proves `(Cb)` (re-derived) and `(C_(t-r))` for `r = 1,...,5`
in the ranges `t >= 3r+3` (Sec. 3 and Sec. 5).

## 2. The sub-chart `R = {q_(t-1,0), b3}`: the ansatz and the five scalars

Write `x = q_(t-1,0)` (weight `t-1`), `b3` (weight `t+1`), `S_r` for the
sub-chart `{b4 = 0, q_(i,0) = 0 for i != t-r}` and, for the moment, `r = 1`.
`Sem = <t-1, t+1>`; writing `w = n t + m` with `n = a+b`, `m = b-a`, an element
of `Sem` is exactly one with `|m| <= n` and `n = m mod 2`.

**Which eliminated variables survive.** By Proposition SUBCHART a variable of
weight `w` restricts to `0` unless `w in Sem`, and to one `A_t`-scalar times
the unique monomial of that weight when there is one.

```text
C_j        wt j in [1,t-1] :  only j = t-1  ->  C_(t-1) = c1 x
q_(j,0)    wt j in [t,2t]  :  j = t+1, 2t-2, 2t
                              q_(t+1,0)=c2 b3, q_(2t-2,0)=c3 x^2, q_(2t,0)=c4 x b3
b2         wt 2t+1         :  2t+1 in Sem only at t = 2, 4     ->  0 for t>=5
T(0)       wt t            :  t in Sem only at t = 2           ->  0 for t>=3
b1         wt 3t+1         :  unique monomial x b3^2 except at t = 2,3,5
                                                               ->  b1 = c5 x b3^2
```

The exceptional indices are exactly the three collisions named in the charged
Sec. 10: `2t-2 = t+1` at `t=3`, `2t+1 = 3(t-1)` at `t=4`, `3t+1 = 4(t-1)` at
`t=5`.  The ansatz is therefore valid for every `t >= 6`; `t = 3,4,5` are
branched in Sec. 4.

**The collapsed spine.** With `b4=0` (so `s = h`) and the ansatz substituted,
the recursion of the charged `terminal_laurent_model.py` becomes, uniformly in
`t` (`sq_engine.py`, `s1_subchart_r1.py`, in `Q(t)[d]/(3d^2-(t+1))`):

```text
C = h^(t-1) + c1 x,  A = hC,  B = g2 h^t + (5c1 g/2y) x h,  B0 = b2 = 0
U = h^(2t+1) + x h^(t+2) + c2 b3 h^t + c3 x^2 h^3 + c4 x b3 h
D = Euler^(-1)( 3gU' + AB - hAB' + 2hA'B + g b3 (C + (5/2)A') )
V = hA - y b3,  Y = hD - b3 B,  Z = hB - g b3,  b1 = c5 x b3^2
X' = (y g b1 - VY' + V'Y + 2U'Z)/(2yh),  Phi = VX' - U'Y + c,
T_(t,k) = [h^k] Phi                                                    (2.1)
```

(2.1) is carried out with the `h`-exponents kept as formal symbols `a t + b`.
Every operation used -- product, `d/dh`, integration, the Euler inverse, the
single division by `h` -- commutes with specialising `t`, and none of the
divisors (`t`, `r`, `2(at+b)+1`, `at+b+1`) vanishes at a positive integer, so
each symbolic exponent carries its own correct coefficient; where two symbolic
exponents coincide at a particular `t` (`collisions()` lists them) the actual
band is their sum, which is precisely the merging discussed in Sec. 4.  `Phi`
has exactly thirteen symbolic bands, whose weights `4t+1-k` are exactly the
elements of `Sem` in `[0,4t+1]`:

```text
high (k >= 2t):   k = 3t+2, 3t, 2t+3, 2t+1        weights t-1, t+1, 2t-2, 2t
terminal:         k = 2t-1, t+4, t+2, t, t-2, 5, 3, 1   weights 2t+2, 3t-3,
                                                   3t-1, 3t+1, 3t+3, 4t-4,
                                                   4t-2, 4t
band zero:        k = 0                                       weight 4t+1
```

Four high bands and one divisibility condition, five unknowns: the count of the
charged Sec. 10 is confirmed, and the solve is triangular -- band `4t+1-w` is
affine in the weight-`w` variable and free of every variable not yet solved.

**The five scalars.** Solving in that order.  Each pivot's norm is displayed;
the driver also multiplies it by the square of the monomial carried by the
pivot coefficient (`x^2`, `b3^2`, `x^4`, `b3^2 x^2` respectively), which is
dropped here since it does not affect unit-ness in `A_t`:

```text
Q4(t) = 27t^4+206t^3+527t^2+540t+300
band 3t+2 -> c1 : N(pivot) = -3t^2(3t+1)^2(3t+2)^3 Q4(t)
  c1 = (t+2)(-9dt^3-12dt^2-9dt+30d+27t^4+153t^3+283t^2+247t+90)/((2t+1)Q4)
band 3t   -> c2 : N(pivot) = -9 t^4 (3t-1)(3t+1)^2(3t+2)^2
  c2 = -(6dt-3d+9t^2+2t-1) / (6t(3t-1))                                (2.2)
band 2t+3 -> c3 : N = -108 t^2(t+1)(2t+1)^2(3t+1)^2(3t+2)^6(t^2+3t+6)
  c3 = 5(t+2)^2 P9(t,d) / ( 6(2t+1)(t^2+3t+6) Q4^2 )
band 2t+1 -> c4 : N = -12 t^2(t+1)(2t+1)^2(3t+1)^2(3t+2)^6(t^2+t+1)
  c4 = -(t+2) P7(t,d) / ( 12(2t+1)(3t-1)(t^2+t+1) Q4 )
b1 divisibility -> c5 = -(c1+c4)/y
     = (t+2) P5(t,d) / ( 2(3t-1)(t^2+t+1) Q4 )
```

`P9, P7, P5` are the explicit integral polynomials printed in `s1_r1.log`.

Two checks that are not free.  `c2` is *identical* to the scalar `lam` of the
banked b3-axis theorem (4.4) -- forced, since band `3t` sees neither `c1` nor
`r` -- the first independent reproduction of (4.4) from a two-variable chart;
and `c5 = -(c1+c4)/y` is the hand form of the `b1` divisibility condition.
After substitution all four high bands vanish identically (asserted in the
driver): the mechanical confirmation of Proposition SUBCHART here.

## 3. The eight restricted rows, and Theorem Q-PLANE

Substituting (2.2) into the terminal bands gives, for every `t >= 6`, exactly
eight nonzero (band, monomial) coefficients -- for `t >= 8` in eight distinct
bands, at `t = 7` with the last two sharing band `5` (Sec. 4):

```text
 band k   weight    monomial      scalar
 2t-1     2t+2      b3^2          A1 = alpha_t
 t+4      3t-3      x^3           A2
 t+2      3t-1      x^2 b3        A3
 t        3t+1      x b3^2        A4
 t-2      3t+3      b3^3          A5 = phi_t
 5        4t-4      x^4           A6
 3        4t-2      x^3 b3        A7
 1        4t        x^2 b3^2      A8                                   (3.1)
```

The two that certify the radical are in closed form:

```text
A1 = t(3t+1) [ (27t^3-30t^2+t-2) d + (6t^3+13t^2-3t+2) ]
     / ( 12 (2t+1)^2 (3t-1)^2 (3t+2) )                                 (3.2)

N(12(2t+1)^2(3t-1)^2(3t+2) A1)
   = -t^2 (t-2) (3t-1)^2 (3t+1)^2 (3t+2) (27t^3+17t^2+t+2) / 3         (3.3)

A2 = 3 t (t-1)^3 (t+2)^3 (3t+1) * P8(t,d)
     / ( (2t+1)^3 (t^2+3t+6) Q4(t)^3 )                                 (3.4)

P8(t,d) : the explicit d-linear integral polynomial of degrees (8,9),
          printed in s1_r1.log

N((2t+1)^3 (t^2+3t+6) Q4(t)^3 A2)
   = 3 t^2 (t-1)^6 (t+1) (t+2)^6 (3t+1)^2 (4t+1) (t^2+3t+6)
     (25t^2+12t-12) Q4(t)^3                                            (3.5)
```

(3.2)-(3.3) are *identical* to `alpha_t` and its norm in the banked (4.5),
(4.8): setting `x = 0` in the two-variable chart returns the one-variable
b3-axis chart, and it does so on the nose.  That is the strongest available
control on the derivation, and it was not built in.

**Integer roots.** `(3.3)` vanishes at `t=2` only (`27t^3+17t^2+t+2 > 0` for
`t>=1`; `3t-1, 3t+1, 3t+2` have no positive integer root).  `(3.5)` vanishes at
`t=1` only: `(t-1)^6` is the sole factor with a positive integer root --
`25t^2+12t-12` has real roots `(-6 +- 4 sqrt 21)/25`, both non-integral, and
`Q4`, `t^2+3t+6` have all coefficients positive, hence no positive root.

**Theorem Q-PLANE.** For every `t >= 6`, on
`S = {b4 = q_(2,0) = ... = q_(t-2,0) = 0}` the eight coefficients (3.1) hold
with `A1` and `A2` units of `A_t`, and therefore

```text
sqrt( I_(t,+)|_S ) = ( q_(t-1,0), b3 ),   i.e.
V(I_(t,+)) cap {b4=q_(2,0)=..=q_(t-2,0)=0} = {0}                       (3.6)
```

on both geometric points of `Spec A_t`.  The certificate is two rows: band
`t+4` gives `q_(t-1,0)^3`, band `2t-1` gives `b3^2`; the other six rows are not
needed.  Equivalently, in the chain of Sec. 1,

```text
q_(t-1,0) in sqrt( I_(t,+) + (b4, q_(2,0),...,q_(t-2,0)) )   for all t>=6.
```

*Proof.* Sec. 2 gives the collapse and the unique solution of the high-band
system, so the restrictions are (3.1); `A1, A2` are units by (3.3),(3.5); so
`b3^2` and `x^3` lie in `I_(t,+)|_S`, and both variables lie in its radical.
Every generator of `I_(t,+)|_S` is weighted homogeneous of positive weight, so
`I_(t,+)|_S` is contained in `(x,b3)` and is proper; its radical is therefore
exactly `(x,b3)`. `[]`

`(3.6)` is strictly stronger than B3-AXIS, which is its restriction to
`q_(t-1,0)=0`, and needs no separate appeal to it: `A1 = alpha_t` is produced
by this computation.

**The remaining scalars.**  `A5 = phi_t = -t(t-2)(3t+1)(6dt-t-1)/(72(2t+1)^3(3t-1))`,
*identical* to the banked (4.6), with `N = -t^2(t-2)^2(t+1)(3t-1)(3t+1)^2(4t+1)`
matching (4.8) -- reproduced independently by the `r=1` and the `r=2` chart.
`A3, A4, A6, A7, A8` are in closed form as well; their norms are banked in
`box/k16subchart-20260903/NORMS.txt`, and the only positive integer root of any
of them is `t=1` (`A3, A6, A7`), `t=2` (`A4`) or none (`A8`).  So **all eight
scalars of (3.1) are units of `A_t` for every `t >= 3`**, in closed form; only
`A1` and `A2` enter the proof of (3.6).  The independent fixed-`t` run of the
identical construction (`s3_fixed.py`) agrees at `t = 6,...,14`.

## 4. The exceptional and merging indices `t = 3,4,5` and `t = 6,7`

Two different things happen at small `t`, and they must be kept apart.

**(a) Merging of band indices, `t = 6,7`.**  The eight weights of (3.1) are
pairwise distinct for `t = 6` and for every `t >= 8`; the sole coincidence in
`t >= 6` is `3(t+1) = 4(t-1)` at `t = 7`, merging the `b3^3` and `x^4` rows
into the single band `k = 5 = t-2`.  At `t = 6` the extra semigroup element
`5(t-1) = 4t+1` lands in band zero, outside `I_(t,+)`.  Neither affects (3.6):
the certifying bands `2t-1` and `t+4` stay separate for all `t >= 6`.  Both are
visible on the records:

On the charged `chart_t7_b4_0.json` the rows are `k=13 b3^2, 11 x^3, 9 x^2b3,
7 xb3^2, 5 x^4 AND b3^3, 3 x^3b3, 1 x^2b3^2` -- seven rows, the predicted
merge; on the prior-lane `chart_t6_b4_0.json` the same eight monomials sit in
the eight separate bands `k = 11,10,8,6,5,4,3,1`.

**(b) Genuine ansatz failure, `t = 3,4,5`.**  Here the collapse itself is
different; the three collisions predicted by the semigroup are all realised on
the charged exact records (`s4_records_subchart.py`):

```text
t=5  five rows: k=9 = b3^2 AND x^3 (2t+2 = 3(t-1)); k=5 = xb3^2 AND x^4
     (3t+1 = 4(t-1), b1 gains x^4); k=3 = b3^3 AND x^3b3 (3t+3 = 4t-2);
     k=7 = x^2b3; k=1 = x^2b3^2.  k=7 forces x=0 or b3=0, then k=9 forces
     the other: DIM 0.
t=4  no x^3 row: weight 3(t-1) = 2t+1 = 9 is the b2 slot, so band 2t is HIGH
     and b2 = c x^3 survives; x is certified by k=5 (x^4) or k=2 (x^5), and
     k=7 gives b3^2.  DIM 0.
t=3  2t-2 = t+1, so the rows are not single monomials: k=5 is a binary
     quadratic in (x^2,b3), k=3 is x times a quadratic, k=1 a cubic.  DIM 0.
```

So `(3.6)` extends to `t = 3,4,5` on the records but not by the closed forms;
it is typed there `EXACT-BY-RECORD`, not `PROVED-UNIFORMLY`.

## 5. Iteration in `j`: the charts `R_r = {q_(t-r,0), b3}`

Put `j = t-r`.  `Sem_r = <t-r, t+1>` grows with `r`, but the *count* of
survivors does not: solving `a(t-r)+b(t+1) = w` identically in `t` fixes `a+b`
and `b-ar`, so each weight admits at most one monomial, and

```text
C_j    (<=t-1)   only j = t-r
q_(j,0) (t..2t)  j = t+1, 2t-2r, 2t-r+1
b2 (2t+1), T(0) (t)  need a(1+r) = 1   -> never for r>=1
b1 (3t+1)            needs a(1+r) = 2  -> only r = 1                  (5.1)
```

For `r >= 2` the `b1` row is doubly absent: `x b3^2` is no longer of weight
`3t+1`, and the divisibility condition itself restricts to `y g b1 = 0`
(`U'`, `Y'` have lowest `h`-exponent `r-1 >= 1` and `V'` lowest exponent `r`,
so only `y g b1` survives at `h=0`), forcing `b1|_S = 0` for *every* `t` --
including the sporadic `t` at which `3t+1` does acquire a monomial.  The driver
prints that constant as identically zero.  So for `r >= 2` the collapse is to
four scalars and four high bands.  `s11_ansatz_range.py` enumerates the
remaining failures of (5.1):

```text
r=1 : t = 3,4,5      r=2 : t = 4,6,7      r=3 : t = 5,6,8,9,10
```

(the `b1`-only flags it also prints at `r>=2`, `t = 9` and `t = 13`, are
spurious by the divisibility argument just given), so the ansatz holds for
`t >= 6`, `t >= 8`, `t >= 11` respectively -- in each case at most the bound
`t >= 3r+3 = 6, 9, 12` that Corollary CHAIN-STEP needs anyway.

The terminal weights are `Sem_r cap (2t+1, 4t+1]`, again eight once `t` is
large enough relative to `r` for all eight bands to lie in `[1, 2t-1]`:

```text
k = 2t-1, t+3r+1, t+2r, t+r-1, t-2, 4r+1, 3r, 2r-1
  r=1 : k = 2t-1, t+4, t+2, t,   t-2, 5, 3, 1
  r=2 : k = 2t-1, t+7, t+4, t+1, t-2, 9, 6, 3                        (5.2)
```

and the two certifying rows are always `b3^2` at band `2t-1` and `x^3` at band
`t+3r+1`.  Band `2t-1` has weight `2(t+1)`, whose only monomial is `b3^2` for
every `r`, so **its coefficient is `alpha_t` for every `r`**: the b3-axis unit
is shared by the whole family and only the `x^3` coefficient is new.  In closed
form:

```text
r=1 : N( den * A2^(1) ) = 3 t^2 (t-1)^6 (t+1) (t+2)^6 (3t+1)^2 (4t+1)
                          (t^2+3t+6) (25t^2+12t-12) Q4^(1)(t)^3
      Q4^(1) = 27t^4+206t^3+527t^2+540t+300 ;  root t=1 only
r=2 : N( den * A2^(2) ) = 3 t^2 (t-2)^6 (t+1)^2 (t+3)^6 (3t+1)^2 (4t+1)
                          (25t-23) (t^2+5t+13) Q4^(2)(t)^3
      Q4^(2) = 27t^4+278t^3+963t^2+1380t+1100 ; root t=2 only
r=3 : N( den * A2^(3) ) = 3 t^2 (t-3)^6 (t+1) (t+4)^6 (3t+1)^2 (4t+1)
                          (25t^2-8t-32) (t^2+7t+22) Q4^(3)(t)^3
      Q4^(3) = 27t^4+350t^3+1531t^2+2800t+2792 ; root t=3 only
r=4 : N( den * A2^(4) ) = 3 t^2 (t-4)^6 (t+1) (t+5)^6 (3t+1)^2 (4t+1)
                          (25t^2-18t-39) (t^2+9t+33) Q4^(4)(t)^3
      Q4^(4) = 27t^4+422t^3+2231t^2+4944t+5808 ; root t=4 only
r=5 : N( den * A2^(5) ) = 3 t^2 (t-5)^6 (t+1) (t+6)^6 (3t+1)^2 (4t+1)
                          (25t^2-28t-44) (t^2+11t+46) Q4^(5)(t)^3
      Q4^(5) = 27t^4+494t^3+3063t^2+7956t+10652 ; roots t=2, t=5 only
      (here 25t^2-28t-44 = (t-2)(25t+22) splits, so t=2 joins t=r;
       both are far below the bound t >= 3r+3 = 18)                    (5.3)
```

The `r=2` chart was likewise carried through completely: all eight scalars of
its analogue of (3.1) are in closed form and *every one of their norms has
`t = 2` as its only positive integer root*; among them `A1 = alpha_t` and
`A5 = phi_t` reappear with the banked formulas, from a chart two steps removed
from the `b3`-axis.

**Lemma UNIQUE-POWER.**  Fix `r >= 1` and `m >= 1`.  In the residual variables
of the *chain* sub-chart `S_r' = {b4 = q_(2,0) = .. = q_(t-r-1,0) = 0}`, namely
`q_(t-r,0),...,q_(t-1,0), b3` of weights `t-r,...,t-1,t+1`, the only monomial
of weight `m(t-r)` -- as an identity in `t` -- is `q_(t-r,0)^m`.

*Proof.*  Write the monomial as `prod_(i=1..r) q_(t-i,0)^(e_i) * b3^f`, put
`E = sum e_i` and `M = sum i e_i`.  Matching the coefficient of `t` gives
`E + f = m`; matching the constant gives `-M + f = -mr`.  Hence
`E + M = m(1+r)`.  Since `i <= r` we have `M <= rE`, so `m(1+r) <= E(1+r)`,
i.e. `E >= m`; and `E <= m` because `f >= 0`.  So `E = m`, `f = 0`, `M = mr`,
which with `sum e_i = m` and `i <= r` forces `e_r = m`. `[]`

Non-uniformly, a second monomial can appear at particular `t`, but only below
an explicit bound.  With `E+f = m+k`, `k != 0`, the weight equation forces
`t = (M-f-mr)/k`; for `k > 0`, `M <= rE` gives `t <= r`, and for `k < 0`,
`M >= E` gives `t <= m(1+r)-1`.  Hence

```text
for t >= m(1+r)  the monomial q_(t-r,0)^m of weight m(t-r) is unique;
m=3 : t >= 3r+3    m=4 : t >= 4r+4                                    (5.3a)
```

and `s10_unique.py` confirms that both bounds are attained (`t = 3r+2` and
`t = 4r+3` respectively) for `r = 1..6`.  At `t = 3r+2` one has
`3(t-r) = 2(t+1)`, so the `x^3` row merges with the `b3^2` row; the `t=5` merge
of Sec. 4 is the case `r=1`.

**Corollary CHAIN-STEP.**  Let `r >= 1` and `t >= 3r+3`.  Then band
`k = t+3r+1` lies in `[1,2t-1]`, and its restriction to `S_r'` is
`A2^(r) q_(t-r,0)^3` with `A2^(r)` the *same* scalar computed on the
two-variable chart `R_r` (setting the intermediate `q`'s to zero cannot change
a monomial in which they do not occur).  If `A2^(r)` is a unit then

```text
q_(t-r,0) in sqrt( I_(t,+) + (b4, q_(2,0),...,q_(t-r-1,0)) ),           (5.4)
```

which is exactly the chain step `(C_(t-r))` of Sec. 1 -- not a coordinate-plane
statement.  This is the point at which the two-variable computation becomes a
link of the chain.

**Theorem Q-SPACE.**  Composing `(C_(t-R)), ..., (C_(t-1))` (from (5.3)) and
`(Cb)` (B3-AXIS) in that order gives, for `R = 1,2,3,4,5`,

```text
V(I_(t,+)) cap {b4 = q_(2,0) = ... = q_(t-R-1,0) = 0} = {0}  for t >= 3R+3,
i.e. a coordinate subspace of dimension R+1: t >= 6, 9, 12, 15, 18.    (5.5)
```

**Induction hypothesis for general `r`** (proved at `r = 1,...,5`):

```text
HYP(r):  for every t >= 3r+3 the sub-chart S_r collapses to the four scalars
         of (5.1) (five when r=1), and the coefficient A2^(r) of x^3 in band
         t+3r+1 is a unit of A_t, its norm having (t-r)^6 as its only factor
         with a positive integer root.
```

`HYP(1)` to `HYP(5)` are theorems here; `HYP(r)` remains a hypothesis for
`r >= 6`.  The five computed norms share `(t-r)^6`, `(t+r+1)^6`, `(3t+1)^2`,
`(4t+1)`, a quartic with all coefficients positive, and two quadratics; the
only positive integer roots are `t = r` (and, at `r = 5` only, `t = 2`), all
strictly below the bound `t >= 3r+3` that Corollary CHAIN-STEP requires.  The
two quadratics were fitted at `r = 1,2,3` as

```text
t^2 + (2r+1) t + (r^2+4r+1)     and     25 t^2 + (22-10r) t + (r^2-14r+1)
```

and the `r = 4` and `r = 5` runs, computed afterwards, returned exactly
`t^2+9t+33`, `25t^2-18t-39` and `t^2+11t+46`, `25t^2-28t-44` -- the prediction
confirmed at two independent points; the same holds for the `t^3` and `t^2`
coefficients of `Q4^(r)` (`72r+134` and `66r^2+238r+223`).  That is evidence
for a general-`r` closed form, not a proof of one: nothing above or below uses
the fitted forms, and each `HYP(r)` used is an exact computation.

**Where this route stops.**  Even granting `HYP(r)` for all `r`, `t >= 3r+3`
caps the reach at `r <= (t-3)/3`, i.e. `j = t-r >= (2t+3)/3`: the chain is
proved from the top down through about a third of the `q`-range and no
further, because for larger `r` the band `t+3r+1` exceeds `2t-1` and the `x^3`
row is one of the HIGH bands already consumed by the elimination.  The obvious
substitute, `x^4` at band `4r+1`, does not help: its uniqueness exceptions run
up to `t = 4r+3` (`s10_unique.py`), so it needs `t >= 4r+4`, a *worse* cap --
and this although its scalar is in closed form at `r = 1, 2` (`NORMS.txt`),
with only `t = r` as a positive integer root.  No variant of this route reaches
`j = 2`, and none touches `(C0)`.

## 6. Assembly, and the `b4`-direction

**What closes and what does not.**  Lemma CONE reduces `(8.1)` to
`tau_t in sqrt(I_(t,+))`, with `dim I_(t,+) = 0` sufficient; Lemma CHAIN says
`dim I_(t,+) = 0` is exactly the chain of Sec. 1.  Of that chain the campaign
now holds

`(Cb)` for `t>=3` (B3-AXIS, re-derived as `A1`) and `(C_(t-r))` for `r=1..5`
at `t >= 3r+3`; `(C_j)` for `j<=t-6` and `(C0)` remain open, the former
reducing to `HYP(r)` with `r <= (t-3)/3`.  So what is proved unconditionally is
(5.5), and with it: for `t >= 18`, a point of `V(I_(t,+))` other than the
origin must have `b4` or one of `q_(2,0),...,q_(t-6,0)` nonzero.  Separately,
at `t = 3..7` **every coordinate axis meets `V(I_(t,+))` only at the origin**
(`s6_axes.py`, all norms nonzero,
including the `b4`-axis, on which band `k` restricts to `mu_k b4^(4t+1-k)` with
every `mu_k` a unit) -- but that check is record-based, not uniform in `t`,
except for the `b3`- and `q_(t-1,0)`-axes, which follow from B3-AXIS and (3.6).
These are genuine constraints and they are not `dim = 0`.

**Does the `b4`-direction need its own axis theorem?  Yes -- and it is not a
cone statement at all.**  `b4` has weight `1`, so `Sem({b4}) = Z_(>=0)` and the
`b4`-axis sub-chart kills no eliminated variable by weight; the collapse is to
one scalar per variable, not to a linear system.  More importantly `b4` sits at
the head of the chain, and by weighted homogeneity

```text
b4 in sqrt(I_(t,+))   <=>   V(I_(t,+)) cap {b4 != 0} = empty
                      <=>   I_(t,+)|_(b4=1) = (1)   (the b4=1 chart)      (6.1)
```

precisely the producer's `TOP-TAIL-UNIT`.  So the answer to the question posed
for this lane is definite: `dim I_(t,+) = 0` does **not** follow from cone
statements on `{b4=0}`; the `b4=1` top tail is a separate step, and it is the
*first*, not the last.  The two-chart split of the Sol report Sec. 7 is thereby
explained rather than replaced -- it is the first link of the chain -- and the
reason it cannot be absorbed is that `b4 = 0` is closed while `b4 != 0` is
open.

**The cheapest tempting upgrade, and why it fails.**  With `w = 0` on `R` and
`1` off `R`, and `in_w` the terms of minimal `w`-degree, `f|_(S_R) = in_w(f)`
whenever that minimum is `0`.  For homogeneous `I` and any generating set `G`,

```text
dim < in_w(g) : g in G >  >=  dim in_w(I)  =  dim I,                    (6.2)
```

so `dim <in_w(G)> = 0` would certify `dim I_(t,+) = 0` outright, from a much
sparser ideal.  It does not hold here: with `R = {q_(t-1,0), b3}`
(`s7_initial.py`, exact, `A_t` encoded by adjoining `y` with `H_t`),
`DIM = 2, 3, 3, 4` at `t = 4, 5, 6, 7`.  The generators are far from a
`w`-Groebner basis, the degeneration is too coarse, and the route is closed off
exactly rather than left as a hope.

## 7. Fixed-`t` confirmation

All tests below are the homogeneous ones licensed by Lemma CONE; ring,
generator order, weight vector and coefficient field are declared in every
emitted `.sing`.  Two encodings of `A_t` are used and agree: the Singular
algebraic extension (`minpoly = H_t/lc`), and `y` adjoined as a variable with
`H_t` added to the ideal (legitimate because `H_t = 0` cuts a finite fibre over
each point, so the dimension is unchanged).

```text
(A) FULL CONE  dim I_(t,+) = 0  =>  (8.1) by Cor. C1              EXACT, char 0
  t=2 y=1/5 : DIM=1, 3 gens   <- mandatory negative control, reproduced
  t=2 y=2/5 : DIM=0, 4 gens   => (8.1)
  t=3       : DIM=0, 34 gens  => (8.1)   [y-adjoined encoding]
  t=4       : DIM=0, 81 gens  => (8.1)   [minpoly encoding]
  t=5       : status at seal in RUN_STATUS.txt; if incomplete, typed
              INCONCLUSIVE_TIMEOUT, never read as NONUNIT
  t=6,7     : NO CLAIM -- the b4-free chart records do not exist; a rebuild at
              t=6 was started here and stopped to stay inside the core budget.

(B) THE 2-PLANE (3.6), restricted ideal in A_t[q_(t-1,0), b3]     EXACT, char 0
  t=3 DIM=0 (5 gens, lead has b3^3, q2_0^4)   t=4 DIM=0 (4, b3^2, q3_0^4)
  t=5 DIM=0 (5, b3^3, q4_0^3)   t=6 DIM=0 (4, b3^2, q5_0^3)
  t=7 DIM=0 (4, b3^2, q6_0^3)
  All five confirm (3.6) independently of the closed forms, and t=3,4,5 are
  exactly the indices where the closed forms do not apply.  The r=2 plane
  A_t[q_(t-2,0),b3] is likewise DIM=0 at t=4,5,6,7; there the lead ideal
  contains q^4 rather than q^3 at t=6,7, as it must, since band t+7 is not yet
  terminal below t=8 and the x^4 row at band 9 takes over.

(C) ENGINE_RECORD_CONTROL_r1 = PASS on chart_t6_b4_0.json and the charged
  chart_t7_b4_0.json: all 9 (band,monomial) pairs at each t agree coefficient
  by coefficient after the declared map d = 2(2t+1)y-(t+1), the two norm
  conventions differing by the measured 12q^2 (2028, 2700).  A1 = alpha_t and
  A5 = phi_t reproduce the banked (4.5),(4.6),(4.8) symbolically.

(D) All eight scalars of (3.1) have nonzero norm at t = 6..14 (fixed-t engine,
  independent of the closed forms of Sec. 3).

(E) SYMBOLIC_VS_FIXED_T_r1 = PASS (all 9 coefficients, t = 6,7,9,...,14) and
  SYMBOLIC_VS_FIXED_T_r2 = PASS (all 9, t = 10,11,12): the closed forms of
  Sec. 2-3 and Sec. 5 agree with the fixed-t engine in A_t.  With (C) this
  closes the loop symbolic -> fixed-t -> charged exact record.
```

`(8.1)` is therefore certified outright here at `t = 2` (both fibres), `t = 3`
and `t = 4`.  Those are `PROVED-HERE` by Corollary C1 with an exact
characteristic-zero certificate; `t = 5` inherits whatever the seal-time status
line records and is not promoted in advance.

## 8. Denominators, split indices, and the FALLACY-v2 audit

Every division performed in Sec. 2, 3, 5 is displayed:

```text
2y, y(2m+1) for m in {0,2,t-1,t+1,2t}   Euler inversion (y inverted with
                                        Res_y(H_t,y) = (t+1)(3t+2) != 0)
t, r, q=2t+1, 3t-1, 3t+2, t+1, 6t(3t-1) integrations, pivots, the c2 solve
Q4^(1)=27t^4+206t^3+527t^2+540t+300, Q4^(2)=27t^4+278t^3+963t^2+1380t+1100
t^2+3t+6, t^2+t+1, t^2+5t+13, 4t^2+8t+13, 12(2t+1)^2(3t-1)^2(3t+2)

integer roots for t >= 1 : NONE.  The linear factors have roots 0, -1/2, 1/3,
-2/3, -1 and half-integers; both quartics have all coefficients positive; the
four quadratics have negative discriminants.
```

The factors `(t-2)` in `N(A1)`, `(t-1)^6` in `N(A2^(1))` and `(t-2)^6` in
`N(A2^(2))` are *numerator* factors and are never inverted; they are genuine
degenerations of the chart at those indices, handled in Sec. 4 and Sec. 5, not
denominator exceptions.  `r` in the denominator of `beta = (3r+2)c1 g/(2ry)`
excludes `r = 0`, which is not a chart of this family.

Split indices.  `H_t` is reducible over `Q` exactly at `t = 3s^2-1`; in the
tested range only `t = 2`, where every statement is made on the two rational
fibres separately and `A_2 = Q x Q` is never treated as a field.  No modular
run is used anywhere in this report, so no cross-characteristic promotion
arises.

Named `FALLACY-v2` items touched:

* **`sat()` wrapping.** Not used; radical membership is asserted only where an
  explicit unit times a pure power of the variable is exhibited.
* **Floor/attainment, carrier/attainment.**  Q-PLANE is an exact identity, not
  a bound; `dim I_(t,+) = 0` is kept separate from the necessary and sufficient
  `tau_t in sqrt(I_(t,+))`; and (3.6) is never used as if it were `(10.1)`.
* **Variable/ring map.**  Two rings, `Q(t)[d]/(3d^2-t-1)` and `Q[y]/(H_t)`; the
  map `d = 2(2t+1)y-(t+1)` is declared and the controls compare coefficient by
  coefficient, not by name.  Normal forms are in the declared quotient with
  `t=2` branched; `'` is `d/ds = d/dh` as in the charged Sec. 2.
* **Generic specialisation.**  The uniform statements are derived symbolically
  in `t`, never interpolated; the one pattern visible in only two samples (the
  last factor of (5.3)) is not extrapolated, and `HYP(r)` is typed as a
  hypothesis.

## 9. Verdict

The typed status is the Verdict block at the head of this report, together with

```text
A1 = alpha_t, A5 = phi_t          : reproduced from two independent charts
HYP(1)..HYP(5)                    : PROVED-HERE
HYP(r) r>=6; (C_j) j<=t-6; (C0)   : OPEN
(8.1) at t=2 (both fibres), 3, 4  : PROVED-HERE, exact, dim I_(t,+) = 0
(8.1) at t=5,6,7                  : see Sec. 7 and RUN_STATUS.txt
```

**Sharpest partial statement.**  For `R = 1,...,5` and every `t >= 3R+3` the
terminal cone meets the coordinate subspace
`{b4 = q_(2,0) = ... = q_(t-R-1,0) = 0}` -- of dimension `R+1` -- only at the
origin, by the explicit units `A2^(1..5)` and `alpha_t`; each further link
`(C_(t-r))`, `r <= (t-3)/3`, reduces to the single unit test `HYP(r)`.  No
sub-chart reaches `(C0)`.

**Cheapest next test.**  Not another `r`: the pattern of Sec. 5 makes a
uniform-in-`r` derivation the right target.  `sq_engine.py` already carries the
`h`-exponents as `a t + b r + c` and runs with `r` symbolic (`set_r(None)`);
that run was too slow inside this budget, but it would prove `HYP(r)` for all
`r` at once and complete (5.5) up to its intrinsic cap `R <= (t-3)/3`.  Even
then `(C0)` -- the `b4=1` chart -- is untouched, and it, not the
`q`-directions, is now the binding constraint on `(8.1)`; the sharpest handle
on it remains (7.1) of the charged report, that on `b4=1` the top tail is `t`
quadratics in `b3` whose topmost has the unit leading coefficient `alpha_t`.

## 10. Reproduction

From `box/k16subchart-20260903/`:

```text
python3 s1_subchart_r1.py 1        # closed forms, r=1 (s1_r1.log)
python3 s1_subchart_r1.py R  for R=2,3,4,5     # s1_r{2,3,4,5}.log
python3 s3_fixed.py 1 6 7 8 ... 14 # same construction at fixed t
python3 s5_engine_control.py 1 6:0 7:0   # ENGINE_RECORD_CONTROL = PASS
python3 s12_symbolic_check.py 1 ; python3 s12_symbolic_check.py 2
python3 s4_records_subchart.py 1 3 4 5 6:0 7:0   # records, with norms
python3 s6_axes.py 3 4 5 6:0 7:0   # every coordinate axis, with norms
python3 s10_unique.py ; python3 s11_ansatz_range.py 1 2 3  # (5.3a) and (5.1)
python3 s8_plane_dim.py 2 4 5 6:0 7:0 ; Singular -q plane_t*_r2.sing
python3 s8_plane_dim.py 1 3 4 5 6:0 7:0 ; Singular -q plane_t*_r1.sing
python3 s7_initial.py  1 4 5 6:0 7:0   ; Singular -q initial_t*.sing
python3 sq_emit_dim.py --chart=spine --mode=minpoly 4 ; Singular -q dim_*.sing
```

`sq_engine.py` is the symbolic-in-`t` engine (`h`-exponents carried as triples
`(a,b,c)` for `a t + b r + c`); `sq_chart_model.py` is the charged
`tf_chart_model.py` with only its output path changed.  Long-job status at seal
time is in `RUN_STATUS.txt`; anything incomplete there is typed
`INCONCLUSIVE_TIMEOUT` and never read as `NONUNIT`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `35709`.
- Body SHA-256:
  `3511f8a21dd49b2bf7b32a68a5e51c4f46279764010d23a8934ee6ebc189ed56`.
- Frozen basis: `1ca13938be6d9e4b9c1858eecd6da7dc293c4cb1`.
