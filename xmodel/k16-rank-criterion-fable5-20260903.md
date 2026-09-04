# Criterion RANK on the K=16 ray: the split tail B_r, C_r at t=3..8, the rank-one
# curve as an Eagon-Northcott scheme with weighted degree [C(3t+1,t-1)-C(2t,t-1)]/(t+1),
# and the exact residual

Lane `k16-rank-criterion-fable5-20260903`, basis `15b2778f`, 2026-09-04.
Drivers and every transcript in `box/k16rank-20260903/`.  Engines: the charged
`singular_terminal_driver.py` (rows), Singular 4.3.2 (ideals; exact over
`A_t = Q(yy)/(H_t)` with `minpoly`, or `GF(p)` at a declared root), sympy 1.12
(series identities).  No ledger, `jc2-lean`, `ideation-*` or in-progress lane
report was read or written.  `FALLACY-v2` applies; no exit-price assertion is
made, so no `charge_basis` line is due.

## 0. Verdict

```text
REQUESTED  criterion RANK -- (i) V(B_1..B_{t-1},C_1..C_{t-1}) = {0} in Spec P_t and
           (ii) W_r != 0 at every rank-1 point with kernel (1:beta) -- PROVED for
           all t >= 3, hence (V0), (8.1), (T) on the whole K=16 ray.
VERDICT    PARTIAL.  Criterion RANK is NOT proved uniformly in t.  Neither clause
           has a uniform proof, and the report says exactly why (Sec. 5.4, 7).
           What is new is (a) the exact shape of the residual curve for every t,
           (b) exact/promoted verifications of both clauses through t=6, of
           clause (i) through t=8, and (c) two structural facts that sharpen the
           criterion: the b3-linear parts B_r ALONE are an hsop at every tested
           index, and the tail length L_t splits as an axis part 2*C(2t,t-1)
           plus a curve part (2t+2)*d_Gamma(t).

PROVED-HERE-1  Theorem FITT.  For t>=3, V(J_t^tail)={0}  <=>  V(F_t)={0} in Spec P_t,
               F_t = I_2(N) + (W_1..W_{t-1}) + (X_rs)_{r<s},  X_rs = a0 C_r C_s
               - b0 B_s C_r + c0 B_r B_s,  the 0-th Fitting ideal of M_t/(G)M_t;
               and  V(F_t) = V(I_2(N) + (W_1..W_{t-1})).  On a rank-1 point p with
               kernel (1:beta):  W_r(p) = B_r(p)^2 T_{t,2t-1}(p,beta)  and
               X_rs(p) = B_r B_s T_{t,2t-1}(p,beta).  So clause (ii) is exactly
               "the top row does not vanish at the unique b3-lift of any rank-1
               point", i.e. T_{t,2t-1} is a nonzerodivisor on S_t/(G_1..G_{t-1}).
PROVED-HERE-2  Theorem EN-CURVE.  If V(J_t^tail)={0} then grade I_2(N) = t-2 is
               maximal, P_t/I_2(N) is Cohen-Macaulay of dimension 1 (Eagon-
               Northcott), the rank-1 curve Gamma has no embedded components, and
                 Hilb(P_t/I_2(N); s)
                   = [ prod_{r=1}^{t-1}(1-s^{2t+2+r}) - s^{t+1} prod_{r=1}^{t-1}(1-s^{t+1+r}) ]
                     / [ (1-s^{t+1}) prod_{i=1}^{t-1}(1-s^i) ]
                   = Hilb(S_t/(G)) - s^{t+1} Hilb(P_t/(B)) / (1-s^{t+1})        (EN)
               (closed form of the Eagon-Northcott numerator, proved by a
               generating-function identity, checked symbolically t=3..15 and
               against Singular's numerators at t=3,4,5).  Its weighted degree is
                 d_Gamma(t) = [ C(3t+1,t-1) - C(2t,t-1) ] / (t+1)
                            = 15/2, 46, 805/3, 1548, 35805/4, 52140  (t=3..8),
               the number of weighted-projective points of Gamma counted with
               multiplicity (orbifold convention), and
                 L_t = 2 C(3t+1,t-1) = 2 C(2t,t-1) + (2t+2) d_Gamma(t)   (LENGTH-SPLIT)
               is an identity: the tail length is the b3-axis contribution (the
               axis has multiplicity C(2t,t-1) in the CI curve V(G_1..G_{t-1})
               when (B) is an hsop, times ord_{b3}(a0 b3^2)=2) plus the rank-1
               curve contribution.  Clause (ii) is therefore a non-vanishing of
               ONE scalar per weighted point of Gamma, d_Gamma(t) scalars in all.
PROVED-HERE-3  Theorem DOMINANT-LEADER.  For every monomial order on P_t there is a
               dominant variable x_* such that every full-support form of weight
               divisible by wt(x_*) has leading monomial a pure power of x_*.
               Every B_r, C_r has full support (measured t=2..8), and in every
               order with b4 dominant -- including the prompt order wp(1,..,t-1)
               -- all 2(t-1) leaders are powers of b4.  So card item (2), "a
               closed form of leading terms making a subset an sop", cannot be
               executed in the prompt order at any t, and in any order the
               coprime-leader set can contain at most one form of weight
               divisible by wt(x_*).  Together with the banked NO-COPRIME-
               LEADERS this closes the leading-term route to clause (i).
EXACT          (char 0, number field, both clauses): t=3 and t=4: (i) holds
               (vdim P/(B,C) = 15, 49), the rank-1 curve has dim 1, V(F_t)={0}
               (vdim 105, 670), V(I_2+(W))={0} (vdim 114, 775); the CI curve
               V(G) decomposes as the b3-axis (multiplicity 15 = C(6,2), 56 =
               C(8,3)) plus 3 resp. 5 further weighted lines, and the top row
               vanishes on none of them.  t=2, y=2/5: (i),(ii) hold with
               (W_1) = (b4^14), length 14; t=2, y=1/5: a0=a1=0, G_1 = 0, N = 0,
               every ideal has dim 1 -- the discriminating control.
PROMOTED       (modular dim 0 of positive-weight cones in P_t, promoted to
               characteristic zero by the banked properness lemma; hypotheses
               in Sec. 8): clause (i) at t=5,6,7,8; (i)/\(ii) at t=5,6; "(B)
               alone is an hsop" at t=5,6,7,8 with vdim = C(2t,t-1) exactly;
               "(C) alone is an hsop" at t=5,6,7 with vdim = C(3t+1,t-1) = L_t/2.
               Clause (i) at t=8 is new (the t=8 tail itself is untested).
MEASURED       the (t-1)-subsets of {B_r,C_r} that are sops: at t=3,4 exactly
               those passing the coordinate-axis divisibility test (Sec. 4.3).
OPEN           criterion RANK for all t (both clauses); closed forms in t of
               b_r, c_r (the banked obstruction stands: they are spine-complete);
               conjecture B-HSOP (Sec. 4.2).  Any all-t proof must produce a
               non-vanishing at d_Gamma(t) ~ 3^{3t}-growth many weighted points
               whose coordinates are t-indexed algebraic numbers.
```

## 1. Custody

The receipt `xmodel/k16-rank-criterion-fable5-20260903.run.v2` was parsed with
`awk -F=` pairing `charged_input_<i>_sha256=` and `charged_input_<i>_basename=`
into `box/k16rank-20260903/manifest.sha256`; `sha256sum -c` printed **14/14 OK**
(`manifest.check.log`).  No digit was retyped.  All fourteen charged inputs were
read before any driver ran.  The charged `singular_terminal_driver.py` was copied
byte-for-byte into the box and run unmodified; `tail_structure.py` (charged)
was rerun at t=3 as the independent cross-check of the row generator.

## 2. Setting, ring map, and the row generator

As charged: `q=2t+1`, `H_t = 12q^2 y^2 - 12q(t+1)y + (t+1)(3t+2)`,
`A_t = Q[y]/(H_t)`, `S_t = A_t[b4,q_{2,0},..,q_{t-1,0},b3]` with weights
`1,2,..,t-1,t+1`, `P_t = A_t[b4,q_{2,0},..,q_{t-1,0}]`, `r = 2t-1-k`,

```text
T_{t,2t-1-r} = a_r b3^2 + b_r b3 + c_r,   wt(a_r,b_r,c_r) = (r, t+1+r, 2t+2+r),
a_0 = -alpha_t (unit, t>=3),  G_r = a_0 T_{t,2t-1-r} - a_r T_{t,2t-1} = B_r b3 + C_r,
B_r = a_0 b_r - a_r b_0,  C_r = a_0 c_r - a_r c_0,   wt(B_r,C_r) = (t+1+r, 2t+2+r),
W_r = a_0 C_r^2 - b_0 B_r C_r + c_0 B_r^2,  wt 4t+4+2r,   N = ((C_r, B_r))_{r=1..t-1}.
```

**Declared ring map.**  Rows come from the charged driver in `--mode exact
--dump-rows` (`terminal_t{t}_exact_none.out`, `t=3..8`; `--mode split-exact
--branch 0|1` at `t=2`, i.e. `y=1/5`, `y=2/5`), whose ring is
`(0,yy),(h,s,b1,b2,b3,b4,B0,C_j,q_{j,0}),dp` with `minpoly = H_t(yy)`; the
tail rows involve only `b3,b4,q_{2,0..t-1,0}` and `yy`.  `rank_driver.py`
re-parses the printed rows into `S = (0,yy),(b4,q_{2,0},..,q_{t-1,0},b3),
wp(1,2,..,t-1,t+1)`, `minpoly = H_t`, and `P = (0,yy),(b4,..,q_{t-1,0}),
wp(1,..,t-1)`, `minpoly = H_t`; `imap` is by name between rings sharing the
parameter and minpoly.  Modular runs use `ring (p),(...),wp(...)` with
`number yy = r`, `r` a root of `H_t` mod `p` computed in the driver (`t=3`:
`32003`, roots `7608,10680`; `t=4`: `32029`, `25378,31563`; `t=5`: `32009`,
`1821,15639`; `t=6`: `32003`, `27617,31466`; `t=7`: `32059`, `4425`; `t=8`:
`32003`, `11288`), the big rational coefficients being reduced by Singular's
parser (a `p`-divisible denominator prints `? div. by 0`; every `.out` was
scanned for `div. by 0`, `error`, `FAIL`, and only runs free of all three
carry status `PASS`).  The coefficient extraction is
`c_r = T|_{b3=0}`, `b_r = (dT/db3)|_{b3=0}`, `a_r = (d^2T/db3^2)|_{b3=0}/2`, and
each run asserts `T = a_r b3^2 + b_r b3 + c_r`, `G_r = a_0 T_{2t-1-r} - a_r T_{2t-1}`,
and the ELIMINANT certificate `W_r = B_r^2 T_{2t-1} - G_r(a_0 G_r - 2a_0 C_r + b_0 B_r)`
(all three print `FAIL` otherwise; none did in any accepted run).  Sign: the
driver's rows are the negatives of the frozen JSON records; `B_r, C_r, G_r`
are sign-invariant, `W_r` and `T` flip together, so nothing below depends on it.

**Image checks.**  `a_0 = -575/1232*yy + 5/44 = -5(115y-28)/1232` at `t=3`
(banked value, 17(ppppp) Sec. 4.2); the charged sympy generator
`tail_structure.py 3` (rerun here, 9.5 s) gives the same `a_0`, `a_1 =
-b4(9978031y-1065166)/37143568`, `a_2`; term counts of `a_r` are
`1,1,2,3,5,7,11` at `t=7` (partitions of `r`); `JTAIL` reproduces `90`, `572`
(`t=3` exact and mod `p`, `t=4` mod `p`, both roots); `(W_1..W_{t-1})` has
`vdim = 2^{t-2} L_t = 180, 2288, 29120` at `t=3,4,5` (the charged `2^{t-2}` cost,
measured only at `t=3` before).  `alpha_t`-unit: `A0VALUE` nonzero at every
`t>=3` and `0` at `t=2, y=1/5`.

## 3. The split tail at t=3..8: weights, supports, leaders, axis values

All entries verified in every run (`STRUCT`/`SPLIT` lines): `deg_b3 T = 2` on
every top-tail row for `t>=3` (`=1` at `t=2, y=1/5`), `homog = 1` and the
predicted weights for every `a_r, b_r, c_r, B_r, C_r, W_r`.

| `t` | `#B_r` (r=1..t-1) | `#C_r` | `#W_r` |
|---:|---|---|---|
| 3 | 3, 4 | 5, 6 | 9, 11 |
| 4 | 7, 8, 10 | 16, 19, 21 | 52, 61, 69 |
| 5 | 11, 15, 18, 23 | 39, 47, 54, 64 | 198, 247, 289, 350 |
| 7 | 26, 35, 44, 58, 71, 90 | 163, 199, 235, 282, 331, 391 | 1903, 2429, 2950, 3692, 4439, 5402 |
| 8 | 38, 49, 65, 82, 105, 131, 164 | 300, 364, 436, 522, 618, 733, 860 | 5073, 6398, 8029, 9918, 12202, 14940, 18106 |

Each count equals the number of monomials of the given weight in variables of
weights `1..t-1` (e.g. `#B_3 = 44` at `t=7`: partitions of 11 with parts
`<=6`; `#B_3 = 65` at `t=8`: partitions of 12 with parts `<=7`): **every `B_r`,
`C_r` has full support**, exactly as the charged TOPTAIL report found for
`b_r, c_r`.  There is no sparsity.  In the prompt order every leader is the pure
power `b4^{wt}` (`lead=` column of every `SPLIT` line, `t=2..8`): the b4-axis
coefficients are all units at the tested indices, and the leading monomial
ideal of any subset is `(b4^m)`, of dimension `t-2`.

Exact `t=3` values (`A_t = Q(yy)/(588yy^2-336yy+44)`, `rank_t3_exact.out`):

```text
B_1 = (2278007000913733232200497/7001018435389567388254000 yy - 2365467889291185441299247/19602851619090788687111200) b4^5
    + (11315049086235562929/112627702494057964304 yy - 28901637095985431289/788393917458405750128) b4^3 q2
    + (96325440598125/12410131200818624 yy - 228572228373375/86870918405730368) b4 q2^2
B_2 = (..) b4^6 + (..) b4^4 q2 + (..) b4^2 q2^2 + (1472343328125/6055953854497456 yy - 3149652046875/42391676981482192) q2^3
C_1 = (..) b4^9 + .. + (179207764706387446875/62651349789671944266784 yy - 63130602825027121875/62651349789671944266784) b4 q2^4
C_2 = (..) b4^10 + .. + (1609844176353828125/91718695904650342834488 yy - 994155653781640625/214010290444184133280472) q2^5
```

(full expressions in the `DUMP` lines).  On the coordinate axes (`AXIS` lines)
a weight-`w` form restricts to `(scalar) x_j^{w/j}` when `j | w` and to `0`
otherwise; every such scalar is nonzero at `t=3,4`.  At `t=3` this is the
parity structure: `B_1, C_1` (odd weight) vanish on the `q2`-axis, `B_2, C_2`
do not.  The b4-axis scalars carry the pivot norms of the whole spine
(denominators grow with `t`, cf. the charged terminal-proof Sec. 4) and admit no
closed form in `t`; this is unchanged.

## 4. Clause (i): V(B,C) = {0}

### 4.1 Results

`PARTI` lines, ring `P_t`, `dim` and `vdim` of `std`:

| `t` | field | `(B,C)`: dim, vdim | `(B)` alone: dim, vdim | `C(2t,t-1)` | `(C)` alone: dim, vdim | `C(3t+1,t-1)` | pure powers in `lead(B,C)` |
|---:|---|---|---|---:|---|---:|---|
| 2 (y=2/5) | `Q` exact | 0, 4 | 0, 4 | 4 | 0, 7 | 7 | `b4^4` |
| 2 (y=1/5) | `Q` exact | **1** (N=0) | 1 | -- | 1 | -- | none |
| 3 | `Q(yy)` exact; mod 32003 both roots | 0, 15 | 0, 15 | 15 | 0, 45 | 45 | `b4^9, q2^5` |
| 4 | `Q(yy)` exact; mod 32029 both roots | 0, 49 | 0, 56 | 56 | 0, 286 | 286 | `b4^13, q2^7, q3^5` |
| 5 | `Q(yy)` exact for `(B,C)`,`(B)`; mod 32009 both roots for all | 0, 159 | 0, 210 | 210 | 0, 1820 (mod) | 1820 | `b4^17, q2^9, q3^6, q4^5` |
| 6 | mod 32003 root 27617 | 0, 512 | 0, 792 | 792 | 0, 11628 | 11628 | `b4^23, q2^12, q3^8, q4^6, q5^5` |
| 7 | mod 32059 root 4425 | 0, 1641 | 0, 3003 | 3003 | 0, 74613 | 74613 | `b4^28, q2^14, q3^10, q4^7, q5^6, q6^5` |
| 8 | mod 32003 root 11288 | 0, 5224 | 0, 11440 | 11440 | not finished (killed at 1470 s) | 480700 | not finished |

Clause (i) holds at every index `t=3..8` (exactly at `t=3,4,5`; promoted at
`t=6,7,8`, Sec. 8).  At `t=3` the `C_r` lie in `(B_1,B_2)` (`vdim(B,C) =
vdim(B) = 15`); from `t=4` on `(B,C)` is strictly larger than `(B)`.

### 4.2 The b3-linear parts alone are an hsop (conjecture B-HSOP)

At every tested index `(B_1,..,B_{t-1})` is an hsop of `P_t` with length
**exactly** the complete-intersection value

```text
vdim P_t/(B_1..B_{t-1}) = prod_{r=1}^{t-1}(t+1+r) / (t-1)! = C(2t, t-1)
                        = 4, 15, 56, 210, 792, 3003, 11440   (t=2..8),
```

and `(C_1,..,C_{t-1})` is an hsop with `vdim = C(3t+1,t-1) = L_t/2` (`t<=7`).
Both are cone statements in `P_t` and are promoted to characteristic zero at
the modular indices.  Consequences, all elementary:

* **(B) hsop `=>` clause (i)**, and no rank-1 point has kernel `(0:1)`; so
  criterion RANK reads: `V(J_t^tail)={0} <=> (B) hsop-or-(i) and (ii)`.
* **(C) hsop `<=>` `b3` is a nonzerodivisor on `S_t/(G_1..G_{t-1})`** (since
  `C_r = G_r|_{b3=0}`), i.e. `(G_1..G_{t-1}, b3)` is an hsop of `S_t` of CI
  length `prod(2t+2+r)(t+1)/((t-1)!(t+1)) = C(3t+1,t-1) = L_t/2`.
* **Clause (ii) `<=>` `T_{t,2t-1}` is a nonzerodivisor on `S_t/(G_1..G_{t-1})`**
  (Theorem FITT).  So `(C)`-hsop and clause (ii) are the SAME kind of statement
  -- a form (`b3` of weight `t+1`, resp. the top row of weight `2t+2`)
  avoiding the finitely many weighted lines of `V(G)`; measured, both hold.

Conjecture B-HSOP is a cleaner target than (i): `t-1` forms of weights
`t+2..2t` in `t-1` variables, involving only the `b3`-linear parts of the
spine.  It is typed OPEN; nothing here proves it beyond `t=8`.

### 4.3 Which subsets are sops, and the axis test

`SUBSETS` (mod `p`, both roots agree where both ran): at `t=3`, `5` of the `6`
pairs are sops, the exception `{B_1,C_1}`; at `t=4`, `16` of the `20` triples,
the exceptions `{B_2,B_3,C_1}, {B_2,B_3,C_3}, {B_2,C_1,C_3}, {B_3,C_1,C_3}`.
In both cases the non-sops are **exactly** the subsets failing the coordinate-
axis test: a subset all of whose weights are prime to `j` vanishes on the
`q_j`-axis (at `t=4`: `B_1` (wt 6) and `C_2` (wt 12) are the only forms with
weight `0 mod 3`, and the four exceptions are the triples avoiding both).
`subset_pattern.py` confirms `20/20` and `6/6` agreement.  At `t=5` the subset block had not
flushed when the runs were killed at 1470 s (Singular block-buffers stdout when redirected;
the kill discarded the buffer): not obtained, typed INCONCLUSIVE_TIMEOUT.
The axis test is a proved necessary condition for every `t` (a form of weight
`w` restricts to `q_j`-axis as `(scalar) q_j^{w/j}` if `j|w` and `0` otherwise);
it is not claimed sufficient beyond the measured indices.

### 4.4 Theorem DOMINANT-LEADER and the deep-strata chain

**Theorem DOMINANT-LEADER.**  Let `<` be any monomial order on
`K[x_1..x_n]`, `wt x_i = w_i > 0`.  Write `x_i >> x_j` if `x_i^{w_j} > x_j^{w_i}`
(both of weight `w_i w_j`).  This is a total order on the variables (if
`x_i^{w_j} > x_j^{w_i}` and `x_j^{w_k} > x_k^{w_j}`, raising to the powers
`w_k`, `w_i` and multiplying gives `x_i^{w_j w_k} > x_k^{w_i w_j}`, hence
`x_i^{w_k} > x_k^{w_i}`), so it has a maximum `x_*`.  For any monomial `x^m` of
weight `w` with some `m_i > 0`, `i != *`: `(x^m)^{w_*} = prod x_i^{m_i w_*}
< prod x_*^{m_i w_i} = x_*^{w}`, hence `x^m < x_*^{w/w_*}` whenever `w_* | w`.
Therefore a form with full support and `w_* | wt` has `LM = x_*^{wt/w_*}`.  QED

Consequences.  (a) In the prompt order `wp(1,2,..,t-1)` with `b4` first, and in
every order with `b4` dominant, every `B_r, C_r` has leader `b4^{wt}` (this is
the measured `lead=` column); no two are coprime, and the leading-monomial
ideal of any subset is a single `b4`-power, of dimension `t-2`.  (b) In any
order a set with pairwise coprime leaders contains at most one form whose
weight is divisible by `w_*`.  So the "closed form in `t` for the leading terms
of `B_r, C_r` that makes a subset an sop" (card item (2)) does not exist in the
prompt order, and a Groebner-type proof of (i) has to pass through
S-polynomial leaders (the pure powers `q_j^{e_j(t)}` of the table in 4.1 all
arise that way, none from a generator).  The exponents `e_j(t)` are recorded
as MEASURED: `b4`: `9,13,17,23,28`; `q2`: `5,7,9,12,14`; `q_{t-1}`: `5,5,5,5,5`
(`t=3..7`); no formula is claimed.

**Deep strata.**  On `S_rho = {b4 = q_2 = .. = q_{t-1-rho} = 0}` a monomial of
`B_r` (weight `t+1+r`) has two factors of weight `>= t-rho`, three only if
`3(t-rho) <= 2t`, i.e. `t <= 3 rho`.  For `t > 3 rho` the square `q_{t-j}^2`
(weight `2t-2j = t+1+r` at `r = t-1-2j`, `j=1..rho`) is the only monomial of its
weight in `q_{t-j},..,q_{t-1}` that does not involve a heavier stratum variable,
so `B_{t-1-2j}|_{S_rho} = beta_j q_{t-j}^2 + (terms divisible by q_{t-j+1},..,q_{t-1})`
and, if the `rho` scalars `beta_j` are units, `V(B) cap S_rho = {0}` by the
triangular chain `q_{t-1}^2, q_{t-2}^2, .., q_{t-rho}^2`.  This is the
`B`-version of the banked UNIQUE-POWER chain, with the same cap `rho < t/3`;
it adds nothing beyond the banked strata results and is recorded only to show
that clause (i) has the same "dense middle" as the original chain: for
`rho >= t/3` the restricted forms have three-factor monomials and are no longer
triangular.

## 5. Clause (ii): the rank-one curve

### 5.1 Theorem FITT (exact reformulation, all t>=3)

`M_t = S_t/(T_{t,2t-1})` is `P_t`-free on `{1,b3}` (TAIL-SPLIT).  Multiplication
by `G_r = C_r + B_r b3` has matrix `[[C_r, -c_0 B_r/a_0],[B_r, C_r - b_0 B_r/a_0]]`
(columns = images of `1`, `b3`; `b3^2 = -(b_0 b3 + c_0)/a_0`).  Hence
`S_t/J_t^tail = coker( P^{2(t-1)} --[G_1|..|G_{t-1}]--> P^2 )`, whose support is
`V(Fitt_0) = V(I_2[G_1|..|G_{t-1}])`.  The `2x2` minors are: within a block
`det G_r = W_r/a_0`; across blocks `-(B_r C_s - B_s C_r)`, `(c_0/a_0)(B_r C_s - B_s C_r)`,
`X_rs/a_0`, `-X_sr/a_0`, with `X_rs - X_sr = b_0 (B_r C_s - B_s C_r)`.  So

```text
F_t = I_2(N) + (W_1..W_{t-1}) + (X_rs)_{r<s},  and  V(J_t^tail) = {0} <=> V(F_t) = {0},
```

because `Spec S_t/J_t^tail -> Spec P_t` is finite (`b3` integral over `P_t` mod
the top row) with image `V(F_t)`.  At a point `p` with `rank N(p) = 1` and kernel
`(1:beta)` one has `C_r = -beta B_r`, hence
`W_r = B_r^2 (a_0 beta^2 + b_0 beta + c_0) = B_r^2 T_{t,2t-1}(p,beta)` and
`X_rs = B_r B_s T_{t,2t-1}(p,beta)`; with kernel `(0:1)` (all `B_r = 0`, some
`C_r != 0`) `W_r = a_0 C_r^2 != 0`.  Therefore `V(F_t) = V(I_2(N) + (W))` and
clause (ii) is precisely: **the top row does not vanish at the unique lift
`(p, beta(p))` of any rank-1 point `p != 0`**, equivalently `T_{t,2t-1}` is a
nonzerodivisor on `S_t/(G_1..G_{t-1})`.  (Verified numerically: `dim(I_2+(W)) =
dim(F_t) = 0` at every tested index; `vdim(P/F_t) = 14, 105, 670, 4126, 25395`
and `vdim(P/(I_2+(W))) = 14, 114, 775, 4910, 30288` for `t=2..6`.)

### 5.2 Theorem EN-CURVE

Suppose `V(J_t^tail) = {0}`.  Every component of `V(G_1..G_{t-1})` has
dimension `>= 1` and is cut to `{0}` by the single form `T_{t,2t-1}`, so
`dim V(G) = 1`: `G_1..G_{t-1}` is a regular sequence in `S_t`.  If some `p != 0`
had `rank N(p) = 0`, the cone over `{p} x A^1` (dimension 2) would lie in
`V(G)`; so clause (i) follows, and `V(I_2(N)) = Gamma cup {0}` with
`Gamma = {rank N = 1}` of dimension `1`.  For a `(t-1) x 2` matrix the height of
`I_2` is at most `t-2`; here it equals `t-2`, so `I_2(N)` is perfect and the
Eagon-Northcott complex of `phi: (+)_{r} P(-(2t+2+r)) -> P (+) P(-(t+1))`
(rows `(C_r, B_r)`; the column shift `t+1` is forced by `wt C_r - wt B_r = t+1`)
is a minimal graded free resolution: `P_t/I_2(N)` is Cohen-Macaulay of
dimension 1, `Gamma cup {0}` has no embedded component, and `Gamma` is a finite
union of weighted lines through `0`.  The `k`-th EN term `wedge^{k+2}F (x)
S_k(G)^* (x) wedge^2 G^*` has generators in degrees
`sum_{r in R}(2t+2+r) - (j+1)(t+1)`, `|R| = k+2`, `0 <= j <= k`, so the numerator
of `Hilb(P_t/I_2(N); s) = HN_t(s)/prod_{i=1}^{t-1}(1-s^i)` is

```text
HN_t(s) = 1 + sum_{k=0}^{t-3} (-1)^{k+1} sum_{|R|=k+2} s^{sum_R (2t+2+r) - (t+1)} [k+1]_{s^{-(t+1)}} .
```

**Closed form.**  Put `x_r = s^{2t+2+r}`, `y = s^{t+1}`; then
`sum_{j=0}^{k} y^{-j} = (1 - y^{-(k+1)})/(1 - y^{-1})` and, with `e_m` the
elementary symmetric functions and `sum_m (-1)^m e_m(x) = prod(1-x_r)`,
`sum_m (-1)^m e_m(x) y^{-(m-1)} = y prod(1 - x_r/y)`,

```text
HN_t(s) = [ prod_{r=1}^{t-1}(1 - s^{2t+2+r}) - s^{t+1} prod_{r=1}^{t-1}(1 - s^{t+1+r}) ] / (1 - s^{t+1}) .   (EN)
```

`en_degree.py` checks `(EN)` against the term-by-term EN sum for `t=3..15`
(zero difference) and `hilb_compare.py` checks it against Singular's
`hilb(std(I_2),1,wv)` numerators at `t=3` (exact), `t=4`, `t=5` (mod `p`):
identical.  Consequently

```text
Hilb(P_t/I_2(N)) = Hilb(S_t/(G_1..G_{t-1})) - s^{t+1} Hilb(P_t/(B_1..B_{t-1}))_CI / (1 - s^{t+1}),
```

where the first term is the CI series `prod(1-s^{2t+2+r})/((1-s^{t+1})prod(1-s^i))`
of the `G_r` in `S_t` and the second is the CI series of forms of weights
`t+2..2t` in `P_t`, tensored with `K[b3]` and shifted by `t+1`.  Multiplying by
`(1-s)` and letting `s -> 1`:

```text
d_Gamma(t) := lim_{s->1} (1-s) Hilb(P_t/I_2(N))
            = C(3t+1,t-1)/(t+1) - C(2t,t-1)/(t+1) = [C(3t+1,t-1) - C(2t,t-1)]/(t+1).
```

`d_Gamma` is the weighted degree of `Gamma`: a weighted line through a point
with nonzero coordinates of weights `w_i` has coordinate ring `K[lambda^g]`,
`g = gcd(w_i)`, hence contributes `mult/g` (orbifold points count fractionally).
Values: `15/2, 46, 805/3, 1548, 35805/4, 52140, 3064347/10, 1817465`
(`t=3..10`).  At `t=3` the single minor (weight 15 in `b4, q2`) factors mod
`32003` as `b4 * (quartic) * (weight-10 form)` on one root and
`b4 * (quadratic)^2-type * (weight-10 form)` on the other, i.e. `1/2 + 2 + 5 = 15/2`
weighted points; at `t=4` the three minors give `5` prime components on one
root (`mult 3,9,21,33,72`, sum `138 = mult(I_2)`) and `3` on the other
(`18,39,81`), the geometric point count being `46` in both cases.

### 5.3 LENGTH-SPLIT and the axis multiplicity

`L_t = (2t+2) * deg_w V(G) = (2t+2) C(3t+1,t-1)/(t+1) = 2 C(3t+1,t-1)` is the CI
length of the tail (top row of weight `2t+2` cutting the CI curve `V(G)`).
By `(EN)`, `deg_w V(G) = d_Gamma(t) + C(2t,t-1)/(t+1)`, so

```text
L_t = 2 C(2t,t-1) + (2t+2) d_Gamma(t)        (identity, all t).
```

Interpretation (proved when `(B)` is an hsop): `V(G)` always contains the
`b3`-axis (over `p=0` every `G_r` vanishes).  In the chart `b3 = 1` the axis
point is the origin of `P_t`-space and `G_r|_{b3=1} = B_r + C_r` has lowest
weighted part `B_r`; if `(B)` is an hsop the initial forms are a regular
sequence, the initial ideal of `(B_r + C_r)` in the weighted local order is
`(B)`, and the local multiplicity of the axis point is `vdim P_t/(B) = C(2t,t-1)`.
Measured (`GCURVE` lines, weighted local order `ws`): `15` at `t=3`, `56` at
`t=4` (= `C(6,2)`, `C(8,3)`), and `primdecGTZ` of `(G)` in `S_t` returns the
axis prime `(b4,q_{2,0},..)` with primary multiplicity `15`, resp. `56`.  The
axis meets the top row with `ord_{b3}(a_0 b3^2) = 2`, contributing
`2 C(2t,t-1)`; the residual curve `Gamma~' = V(G) minus axis` projects
isomorphically onto `Gamma` (over a rank-1 point the lift is unique) and
contributes `(2t+2) d_Gamma(t)`.  This is the exact meaning of the two factors
of `L_t`: `2 = ord_{b3}` of the top row on the axis (charged TAIL-SPLIT), and
`d_Gamma(t)` is the number of points at which clause (ii) must be checked.

### 5.4 The curve at t=3,4 and the residual one-variable statement

`GCURVE` (mod `p`, `primdecGTZ((G_1..G_{t-1}))` in `S_t`, then `dim(prime +
(T_{t,2t-1}))` for every prime): `t=3`: `4` components -- the axis (mult 15) and
three lines of multiplicities `2, 8, 20`; `t=4`: `6` components -- the axis
(mult 56) and five lines (`5, 15, 35, 55, 120`).  On every non-axis component
`dim(prime + (T_top)) = 0`: the top row vanishes on none of them.  This IS clause
(ii) at `t=3,4`, seen on the curve rather than through `W_r`.  At `t=5` the run
printed `dim V(G) = 1`, `mult 1820` and was killed inside `primdecGTZ` at 1420 s
(INCONCLUSIVE_TIMEOUT); clause (ii) at `t=5,6` rests on the flushed `dim(F_t) = 0`
and `dim(I_2+(W)) = 0` lines of the modular runs (Sec. 5.1).

On a component `Z = closure of {lambda . (p,beta)}` the top row restricts to
`lambda^{2t+2} T_{t,2t-1}(p,beta)`; the "one-variable residual" of card item (3)
is therefore not a polynomial in one variable but **one scalar per component**,
`T_{t,2t-1}(p_i, beta_i) != 0`, `i = 1..#components`, with `sum_i mult_i/g_i =
d_Gamma(t)`.  The scalars are values of the top row at points whose
coordinates are algebraic over `A_t` of degree up to `mult_i` (at `t=4` mod `p`,
degrees `3..72`); no closed form is available for them because none is
available for `b_r, c_r` (charged; unchanged).  This is the sharpest form of
the residual the lane can give: after (i), clause (ii) is a finite set of
`d_Gamma(t)` weighted non-vanishings, `d_Gamma(t) ~ (27/4)^t`-growth, with
`t`-indexed algebraic inputs.

## 6. The t=2 boundary (exact, both fibres, no zero divisor inverted)

```text
y = 1/5:  a_0 = a_1 = 0 (both tail rows b3-LINEAR),  b_0 = -77/80 b4^3,  c_0 = 413/128 b4^6,
          G_1 = a_0 T_{2,2} - a_1 T_{2,3} = 0,  N = 0,  I_2 = (0),  F_2 = (0):
          every ideal of Sec. 5 has dim 1; the split hypothesis (a_0 unit) fails and
          V(J_2^tail) contains the b3-axis (JTAIL dim 1).
y = 2/5:  a_0 = -28/625,  B_1 = -12047616/11051265625 b4^4,  C_1 = 232682357376/53905863465625 b4^7,
          (B,C) = (b4^4), vdim 4 = C(4,1); (C) = (b4^7), vdim 7 = C(7,1);
          rank N(p) = 1 for every p != 0, kernel (1 : -C_1/B_1 = (scalar) b4^3);
          W_1 = (scalar) b4^14 != 0:  (ii) holds;  F_2 = (W_1), vdim 14 = L_2;  JTAIL vdim 14.
```

So the criterion discriminates the two fibres exactly as required: on `y=1/5`
the failure is the unit hypothesis (the criterion is not even defined), on
`y=2/5` both clauses hold with the `t=2` instances of every formula above
(`d_Gamma(2) = [C(7,1) - C(4,1)]/3 = 1`, the single line `{b4 != 0}` with
`g = 1`; `L_2 = 2*4 + 6*1 = 14`).

## 7. Closed forms: what the lane could and could not derive

* `a_r` (weight `r`): truncated-spine closed forms exist in principle (charged
  (3.2)); the lane used only their exact values.
* `b_r, c_r` (weights `t+1+r`, `2t+2+r`): the lane confirms the charged
  obstruction rather than lifting it.  Their supports are full (Sec. 3), their
  `b4`-axis scalars carry the spine pivot norms, and every attempt to express
  them through a bounded number of spine scalars fails by the weight count of
  TOPTAIL (3.2): a monomial of `(b4,q)`-weight `t+1+r` in `b_r` receives
  contributions from every spine variable of weight `<= t+1+r`, i.e. from the
  whole `b3`-free spine up to weight `2t`.  No closed form in `t` was obtained,
  none is claimed, and the lane's structural results deliberately use only the
  WEIGHTS of `B_r, C_r` (Theorem EN-CURVE) or their existence (Theorem FITT).
* What IS uniform: the degree data `(t+1+r, 2t+2+r)` alone determine the
  Hilbert series `(EN)` and `d_Gamma(t)` once `dim V(J_t^tail) = 0` is known.
  Theorem DEGREE-BLIND (charged) says degree data cannot prove that dimension
  statement; consistently, `(EN)` is stated under the hypothesis, and the
  `t=2, y=1/5` fibre has the same degree data with `I_2 = (0)`.

**Exact residual statement.**  For every `t >= 3`: `(V0)` on the tail
`<=>` `(B_1..B_{t-1}, C_1..C_{t-1})` is `m`-primary in `P_t` `and` the top row
`T_{t,2t-1}` avoids the `b3`-lift of each of the `d_Gamma(t) = [C(3t+1,t-1) -
C(2t,t-1)]/(t+1)` weighted points of `Gamma = V(I_2(N))`.  A proof for all `t`
needs a uniform non-vanishing at `t`-indexed algebraic points; neither the
leading-term route (DOMINANT-LEADER, NO-COPRIME-LEADERS) nor the degree route
(DEGREE-BLIND) nor the deep-strata chain (cap `rho < t/3`) can supply it.

## 8. Verdict, dependency chain, and FALLACY-v2 audit

```text
Criterion RANK for all t >= 3:  NOT PROVED.  PARTIAL.
Uniform, proved here:   FITT (Sec. 5.1);  EN-CURVE with (EN) and d_Gamma(t) (5.2);
                        LENGTH-SPLIT identity (5.3);  DOMINANT-LEADER (4.4);
                        axis test as a necessary condition for sop subsets (4.3).
Fixed t, char 0:        (i) and (ii): t=3,4 exact; t=5,6 promoted;  (i) alone: t=7,8 promoted.
                        (B) hsop with vdim C(2t,t-1): t=2(y=2/5),3,4,5 exact, t=6,7,8 promoted.
                        (C) hsop with vdim C(3t+1,t-1): t<=5 exact, t=6,7 promoted.
Control:                t=2 both fibres exact (Sec. 6).
Open:                   both clauses for all t; B-HSOP; closed forms of b_r, c_r.
```

At an index where `(i)/\(ii)` is established, the chain is the banked one:
`V(J_t^tail) = {0} => dim S_t/I_{t,+} = 0 (containment) => (V0) => tau_t
vanishes on the cone and yg is a unit => (8.1) => constant spine / normalizer
lemma / second affine spine => (T)`.  This lane adds no new index to `(V0)`:
`t=5,6` were banked; `(i)` at `t=8` is a statement about `P_8` only and does
not give `(V0)_8`.

**Promotion hypotheses (properness lemma, charged gate Sec. 1.3, `R` a local
domain).**  Each promoted statement is `V(J.kappa[x]) = {0}` for an ideal `J`
of `R[x]` generated by positive-weight homogeneous forms (`homog = 1` printed
for every generator), `R` the localisation of `Z[y]/(H_t)` at `(p, y-r)`,
`kappa = GF(p)`, `K = A_t` (a field: `3(t+1)` is not a square for `t=3..8`).
`(H-gen)`: the modular generators are the reductions of the exact generators,
because the driver reduces the exact rows at `yy = r` and forms `B_r, C_r,
W_r, X_rs` by ring operations (the only division is by `2`).  `(H-int)`: the
primes/roots `(4,32029,25378|31563)`, `(5,32009,1821|15639)`, `(6,32003,27617)`,
`(7,32059,4425)` carry the gate's `PINT PASS`; for `(6,32003,31466)` and
`(8,32003,11288)` `p`-integrality rests on the absence of the `? div. by 0`
marker (a detector, not a fail-stop, as the gate notes), so those two runs are
labelled DETECTOR-ONLY and the `t=8` promotion is stated with that caveat.
No inhomogeneous unit ideal is promoted; no `sat()`; no raw remainder degree;
`vdim` values in characteristic `p` are reported as modular lengths (except
where the exact run gives the same number).

* **Flag/place/series, floor/attainment.**  `L_t`, `C(2t,t-1)`, `C(3t+1,t-1)`
  and `d_Gamma(t)` are CI/EN values the quotients *have if* the corresponding
  ideal has the right dimension; every equality claim is measured at the stated
  index and never used as evidence of dimension.
* **Variable/ring map.**  Declared in Sec. 2 with image checks (`a_0`, `a_1`,
  `JTAIL` lengths, `2^{t-2}L_t`).
* **Prime label.**  No prime-mark derivatives are used; `p` is always the
  finite-field characteristic.
* **No interpolation.**  `(EN)` is proved by an identity, not fitted; the pure-
  power exponents and subset patterns are MEASURED; B-HSOP is a conjecture.

## 9. Computation record and artifacts (`box/k16rank-20260903/`)

| driver / file | content | time |
|---|---|---|
| `manifest.sha256`, `manifest.check.log` | custody, 14/14 OK | -- |
| `singular_terminal_driver.py` (charged copy), `terminal_t{2..8}_*_none.{sing,out,json}` | exact rows, `--dump-rows`; `RECURRENCE_PASS`, `DRIVER_DONE` | 0.02 s (t=3) .. 49 s (t=8) |
| `tail_structure.py` (charged copy, output path only), `tail_structure_t3.out` | independent sympy rows, `a_0,a_1,a_2` at t=3 | 9.5 s |
| `rank_driver.py` | emits/runs the Singular job (STRUCT, PARTI, CURVE, PRIMDEC, SUBSETS, GCURVE, JTAIL, DUMP) | -- |
| `rank_t2_split-exact_b{0,1}.*` | t=2 both fibres, all tests, exact | <1 s |
| `rank_t3_exact.*`, `rank_t4_exact.*`, `rank_t5_exact.*`, `rank_t6_exact.*` | exact number-field runs; t=3 complete; t=4 complete through `Fitting` (killed in `(W)` alone at 1470 s); t=5 complete through `PARTI (B)`; t=6 nothing flushed | 0.1 s / killed 1470 s / killed / killed |
| `rank_t{3..8}_mod_p*_b*.*` | modular runs, both roots at t=3,4 complete; t=5 (both roots), t=6 (both roots), t=7 curve, t=8 parti/curve killed at 1470 s with the lines cited above already flushed; `rank_t7_mod_p32059_b0_parti` complete (602 s) | seconds .. killed |
| `rank_t{3,4,5}_mod_*_gcurve.*` | CI curve V(G): decomposition, axis multiplicity | 0.3 s / 371 s / killed 1420 s |
| `en_degree.py`, `hilb_compare.py`, `subset_pattern.py` | (EN), d_Gamma, numerator comparison, axis test | seconds |
| `launch_*.log`, `launch_*.resource`, `*.json` | status, wall, RSS per job | -- |
| `artifacts.sha256` | directory manifest | -- |

Reproduction: `python3 singular_terminal_driver.py T --mode exact --dump-rows
--run`; `python3 rank_driver.py T --mode exact --tests struct,parti,curve,dump
--run`; `python3 rank_driver.py T --mode mod --prime P --branch B --tests
struct,parti,curve,subsets,primdec,jtail,gcurve --run`; `python3 en_degree.py`;
`python3 hilb_compare.py`; `python3 subset_pattern.py`.  Every Singular job ran
under a Python timeout (`INCONCLUSIVE_TIMEOUT` otherwise); a job is accepted only
with `RANKDRIVER_DONE` and no `FAIL`/`error`/`div. by 0` marker.  Eleven Singular
jobs were still running at the lane's compute cut-off (about 1470 s of wall time
each) and were killed by `killmine.py`; for those, only lines flushed to the
`.out` file before the kill are used, each labelled where cited, and every
statement that depends on an unflushed result is typed INCONCLUSIVE_TIMEOUT.
Singular block-buffers redirected stdout, so a killed job's last buffer is lost;
future drivers should run Singular under `stdbuf -oL`.  One driver bug
was found and fixed during the lane (a coefficient polynomial named `b3`
shadowed the ring variable at `r=3`; every run reported here postdates the fix
and re-asserts the `T = a b3^2 + b b3 + c` identity at every `r`).

<!-- BODY-END -->
