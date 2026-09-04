# The terminal tail on the K=16 ray: complete-intersection length, the rank-two
# splitting, and two structural impossibility theorems for the all-`t` route

Lane `k16-hsop-length-allt-opus5-20260903`, basis `158179af`, 2026-09-04.
Drivers and transcripts in `box/k16hsop-20260903/`.  Desk CAS only (sympy /
generating functions), single core, no engine beyond sympy.  Every job is under
the 10-minute cap; all but one are under a minute (Sec. 8 records the times, and
which jobs were launched detached rather than blocking the shell).  No ledger,
`jc2-lean`, `ideation-*` or in-progress lane report was read or written.

## 0. Verdict

```text
REQUESTED  (V0) for all t>=3, Groebner-free, via "the terminal tail
           T_{t,t..2t-1} is an hsop of S_t for every t".
VERDICT    PARTIAL.  The hsop statement is NOT proved for all t.  What is
           proved is the length side in full, the structural half of the
           dimension side, and -- new -- that TWO of the three routes named in
           the card are impossible, not merely unfinished.

PROVED-HERE-1  Theorem CI-SERIES.  For every t>=2 the complete-intersection
               numerator/denominator cancellation is exact and gives
                 P_t(s) = prod_{d=2t+2}^{3t+1}(1-s^d) / D_t(s)
                        = (1 + s^{t+1}) * [3t+1 choose t-1]_s,
               a palindromic polynomial of degree (2t-1)(t+1) with NONNEGATIVE
               coefficients, and
                 L_t = P_t(1) = 2*binom(3t+1,t-1)
                     = 2 * #{monomials of TOTAL degree <= 2t+2 in t-1 variables}.
               This is the requested combinatorial derivation of L_t: both
               factors have a structural meaning (PROVED-HERE-2), and the
               nonnegativity is a Gaussian-binomial identity, not a check.

PROVED-HERE-2  Theorem TAIL-SPLIT (uniform in t>=3, on both factors at split
               indices).  alpha_t is a unit of A_t, so
                 T_{t,2t-1} = a_0 b3^2 + b_0 b3 + c_0,  a_0 = -alpha_t a UNIT,
               hence  M_t := S_t/(T_{t,2t-1})  is a FREE graded P_t-module of
               rank 2 on {1,b3}, P_t = A_t[b4,q_{2,0},..,q_{t-1,0}], and
                 J_t^tail = (T_{t,2t-1}, G_1, .., G_{t-1}),
                 G_r := a_0 T_{t,2t-1-r} - a_r T_{t,2t-1} = B_r b3 + C_r,
               b3-LINEAR of weighted degree 2t+2+r.  Consequently
                 J_t^tail hsop  <=>  (G_1..G_{t-1}) hsop in the (t-1)-dimensional
                 Cohen-Macaulay ring M_t,
               and the two factors of P_t(s) are exactly rank(M_t/P_t)=2 and the
               CI series of t-1 forms of degrees 2t+3..3t+1 in weights 1..t-1.
               The "2" in L_t is the b3-degree of the top tail row.

PROVED-HERE-3  Theorem NO-COPRIME-LEADERS.  For every integer t>=3 with
               t not in {3,5}, NO monomial order and NO choice of generators
               makes the t tail rows have pairwise coprime leading monomials.
               Reason: t pairwise coprime monomials in t variables are forced to
               be pure powers of distinct variables, a generating regular
               sequence is a minimal generating set so its degrees are forced to
               be 2t+2..3t+1, and the weight/degree divisibility bipartite graph
               then has no system of distinct representatives.  A
               prime degree in [2t+3,3t+1] admits only the weight 1; two of them
               break Hall's condition; Nagura's theorem supplies two primes for
               all t>=16 and the range t<=15 is a finite table.  This REFUTES
               the "triangular change of generators making the leading terms
               coprime powers" half of card item (2).

PROVED-HERE-4  Theorem DEGREE-BLIND.  No argument that uses only the weighted
               degrees -- Bezout, Froberg, the CI Hilbert numerator -- can prove
               dim = 0 for this family.  Exact witness: the two geometric fibres
               of A_2 carry tail systems with IDENTICAL degree data (rows of
               weight 6,7; variables of weight 1,3) and opposite answers:
               y=1/5 gives dim 1 (the b3-axis), y=2/5 gives dim 0 of length
               14 = L_2.  This REFUTES card item (3) as posed; the minimal extra
               input is a unit statement, and a_0 = -alpha_t is the unique
               weight-0 coefficient anywhere in the tail.

PROVED-HERE-5  Lemma ELIMINANT.  W_r := a_0 C_r^2 - b_0 B_r C_r + c_0 B_r^2 has
               the explicit certificate
                 W_r = B_r^2 T_{t,2t-1} - G_r (a_0 G_r - 2 a_0 C_r + b_0 B_r),
               so W_r lies in J_t^tail, is b3-free of weight 4t+4+2r, and
               V(W_1..W_{t-1}) = {0} implies the tail hsop.  The square eliminant
               system has Bezout number 2^{t-2} L_t: the b3-elimination costs a
               factor 2^{t-2} in length, measured 180 = 2*90 at t=3.

PROVED-HERE-6  Criterion RANK (exact, not merely sufficient).  With N the
               (t-1)x2 matrix of rows (C_r, B_r),
                 V(J_t^tail) = {0}   <=>   (i) V(B_1..B_{t-1},C_1..C_{t-1}) = {0}
                 and (ii) every p != 0 with rank N(p) = 1 whose kernel is spanned
                 by a vector with nonzero first coordinate has W_r(p) != 0 for
                 some r.
               The rank-<=1 locus of a (t-1)x2 matrix in a (t-1)-dimensional
               space has expected dimension 1, so the residual content is one
               non-vanishing statement along a CURVE.

EXACT          t=2, y=2/5: tail dim 0, length 14 = L_2 (new; the charged reports
               record only the full-cone length 12 there).  t=2, y=1/5: b4^3
               divides both tail rows, dim 1, V contains the b3-axis.
MEASURED-MODULAR  t=3 and t=4, both roots of H_t mod 1009, on rows regenerated
               independently in this lane: dim 0, vdim 90 and 572 = L_3, L_4.
               These agree with the banked exact characteristic-zero values.  At
               t=3 the FULL graded series was checked, not only the length, and
               equals P_3(s) on both roots.  The TAIL-SPLIT structure itself
               (a_0 = -alpha_t a unit, a_r support/weight, G_r b3-linear with the
               predicted weights, all mu_{t,k} units, all 2x2 minors nonzero) is
               verified exactly, over A_t, at t=2,3,4,5.
OPEN           the hsop / dim-0 statement itself for all t>=3; equivalently
               criterion RANK; equivalently a closed form in t for the b_r,c_r.
```

## 1. Custody

The receipt `xmodel/k16-hsop-length-allt-opus5-20260903.run.v2` was parsed
mechanically with `awk -F=`, pairing its `charged_input_<i>_basename=` and
`charged_input_<i>_sha256=` lines into `/tmp/manifest.sha256`, which was then
passed to `sha256sum -c`: **8/8 `OK`**.  No digest was retyped.  All eight
charged inputs were read before any driver ran.

## 2. Setting, conventions, and the independent row generator

As charged: `q=2t+1`, `e=3t+1`,
`H_t = 12q^2 y^2 - 12q(t+1)y + (t+1)(3t+2)`, `A_t = Q[y]/(H_t) = Q[d]/(3d^2-(t+1))`
with `d = 2qy-(t+1)`; `A_t` is a separable rank-two algebra, a field except at
the split indices `t=3s^2-1`, where every statement below is read on both
factors separately and no zero divisor is inverted.  Residual ring and grading:

```text
S_t = A_t[b4, q_{2,0}, .., q_{t-1,0}, b3],
wt(b4)=1, wt(q_{j,0})=j (2<=j<=t-1), wt(b3)=t+1,
deg_wp T_{t,k} = 4t+1-k,   I_{t,+} = <T_{t,1..2t-1}>,
J_t^tail = <T_{t,t}, .., T_{t,2t-1}>,  degrees 3t+1, 3t, .., 2t+2.
```

Throughout, `P_t := A_t[b4,q_{2,0},..,q_{t-1,0}]` is the b3-free subring
(`t-1` variables of weights `1,2,..,t-1`), and I index the tail by
`r = 2t-1-k`, so `T_{t,2t-1-r}` has weighted degree `2t+2+r`, `r=0..t-1`
(the card's `j`).  `J_t^tail subset I_{t,+}` gives the only implication used:
`dim S_t/J_t^tail = 0  =>  dim S_t/I_{t,+} = 0`, i.e. `(V0)`
(`k16-square-tail-stdhilb-gpt55-20260903.md` Sec. 9).  A prime mark denotes
differentiation in the banked Laurent formulas; the finite field is always
written `p` or `mod 1009`.

**Independent generator.**  I re-implemented the closed coefficient-array
recurrence of the charged Sol report (`k16-terminal-proof-sol56-20260903.md`
equations (2.1)-(2.13): the arrays `U,C`, then `B,S,V,Y,Z,N,P0',R`, the
triangular high solve `z_j = -rho_j/p_j` for the `2t+1` spine weights, then
`T_{t,k} = -[X^k]R`) from the equations only, in `tail_structure.py`.  Its
outputs were checked against the charged records before use:

| check | this lane | charged source | agree |
|---|---|---|---|
| `deg_wp T_{t,k}` | `4t+1-k` for every `k`, `t=2,3,4`, single weighted degree per row | sol56 (2.14) | yes |
| `T_{2,0}(0)` | `7y/25 - 28/625` | `= yg` reduced mod `H_2` | yes |
| `[b3^2]T_{2,3}` | `-28(5y-1)/625` | sol56 Sec. 6.2 band-three row at `b4=0` | yes |
| `[b3^2 b4]T_{2,2}` | `-252(5y-1)/3625`, i.e. `-252/3625` at `y=2/5` and `0` at `y=1/5` | fable5 Sec. 3(b) `a_1` (`a_0=a_1=0` at `y=1/5`) | yes |
| `Res_y(H_3, mu_t)` | `159028943/148574272` | fable5 Sec. 3(b) table | yes |
| `Res_y(H_3, mu'_t)` | `-4250137195970063/4803319854964400` | same | yes |
| `Res_y(H_3, mu''_t)` | `-11399375/34603212` | same | yes |
| tail vdim `t=3,4` (mod 1009) | `90`, `572` | sol56 Sec. 4 exact char-0 | yes |
| roots of `H_t` mod 1009 | `632,810` (`t=3`), `468,990` (`t=4`) | sol56 Sec. 2 table | yes |

Transcripts: `tail_structure_t{2,3,4}.out` (per-band weighted degrees and the
constant `T_{t,0}(0)`), `tail_audit_t{2,3,4}.out`, `crosscheck_norms.out`,
`t2_boundary.out`, `tail_ideal_t3.out`, `graded_series_t3.out`, `t4_ideal.out`,
`tail_audit_t5.out`.  The three
`Res_y(H_3, .)` values were computed by fable5 from a different driver and a
different sign convention; reproducing them digit-for-digit from an
independently written recurrence is the strongest available image check on the
variable/ring map (declared: `A_t = Q[y]/(H_t)`, generator order
`b4, q_{2,0}, .., q_{t-1,0}, b3`, coefficient field `A_t` or `GF(1009)` at a
declared root).

## 3. Theorem CI-SERIES: the length, derived combinatorially

Let `D_t(s) = (1-s) prod_{j=2}^{t-1}(1-s^j) (1-s^{t+1})` be the weighted
denominator of `S_t`, and let the tail degrees be `2t+2, .., 3t+1`.

**Theorem CI-SERIES.**  For every `t>=2`,

```text
P_t(s) := prod_{d=2t+2}^{3t+1}(1-s^d) / D_t(s) = (1+s^{t+1}) * [3t+1 choose t-1]_s .
```

*Proof.*  Split off the first numerator factor and use the Gaussian binomial in
the form `[n choose k]_s = prod_{d=n-k+1}^{n}(1-s^d) / prod_{i=1}^{k}(1-s^i)`
with `n = 3t+1`, `k = t-1`:

```text
prod_{d=2t+3}^{3t+1}(1-s^d) = [3t+1 choose t-1]_s * prod_{i=1}^{t-1}(1-s^i),
D_t(s) = prod_{i=1}^{t-1}(1-s^i) * (1-s^{t+1}),
```

so `P_t(s) = [3t+1 choose t-1]_s * (1-s^{2t+2})/(1-s^{t+1})
= (1+s^{t+1}) [3t+1 choose t-1]_s`, because `2t+2 = 2(t+1)`.  QED

Three consequences, all immediate and all requested by card item (2):

* **Exactness and nonnegativity.**  `P_t` is a polynomial with nonnegative
  coefficients, since Gaussian binomials are.  No cancellation argument is
  needed; the "numerator-denominator cancellation" is the single identity
  `(1-s^{2t+2})/(1-s^{t+1}) = 1+s^{t+1}`.
* **Degree and symmetry.**  `deg P_t = (t-1)(2t+2) + (t+1) = (2t-1)(t+1)`, and
  `P_t` is palindromic (Gorenstein, as a CI must be).
* **The length, combinatorially.**  Conjugating partitions in the
  `(t-1) x (2t+2)` box turns `[3t+1 choose t-1]_s` into the weight-generating
  function of the monomials in `t-1` variables of weights `1,..,t-1` whose
  TOTAL (unweighted) degree is at most `2t+2`.  Hence

```text
[s^n] P_t = #{ (eps,m) : eps in {0,1}, m in Z_{>=0}^{t-1}, |m|_1 <= 2t+2,
                          eps(t+1) + sum_i i*m_i = n },
L_t = P_t(1) = 2 * binom((2t+2)+(t-1), t-1) = 2 * binom(3t+1, t-1)
            = prod_{d=2t+2}^{3t+1} d / ((t-1)! (t+1)) = (t/(t+1)) binom(3t+1,t).
```

`ci_series_identity.py` verifies exactness of the division, the Gaussian
identity, nonnegativity, the degree, the binomial form of `L_t` and the
combinatorial model (I6) for `t=2..16` in exact integer arithmetic; all pass
(`ALL_IDENTITY_CHECKS_PASS = True`).  The equality of `2 binom(3t+1,t-1)` with
the product form `prod_{d=2t+2}^{3t+1} d / ((t-1)!(t+1))` is the elementary
rewrite `binom(3t+1,t-1) = (3t+1)!/((t-1)!(2t+2)!)` and `2t+2 = 2(t+1)`; it is
confirmed numerically against every banked measurement below.

| `t` | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `L_t` | 14 | 90 | 572 | 3640 | 23256 | 149226 | 961400 | 6216210 | 40320150 |
| measured | exact, new here (`y=2/5`) | exact (banked); mod `p` both fibres here | exact (banked); mod `p` both fibres here | mod `p`, both fibres (banked) | mod `p`, both fibres (banked) | mod `p`, one fibre (banked) | -- | -- | -- |

`P_3 = [1,1,2,2,4,4,6,6,8,7,8,7,8,6,6,4,4,2,2,1,1]` (degree 20, sum 90).

**What this does and does not do.**  It closes the length half of the card
completely and it fixes the target series.  It does *not* bear on dimension:
`P_t` is the series the quotient *has if* the tail is an hsop.  The logical
direction is `dim = 0  =>  length = L_t`, never the converse; Theorem
DEGREE-BLIND (Sec. 6) shows that this direction cannot be reversed by any
degree-only reasoning.

## 4. Theorem TAIL-SPLIT: what the closed indexed forms actually give

### 4.1 The b3-degree of the tail is at most two, uniformly

`wt(b3) = t+1` and `deg_wp T_{t,2t-1-r} = 2t+2+r <= 3t+1 < 3(t+1)`, so no
monomial of a tail row can carry `b3^3`.  Writing the rows as polynomials in
`b3` over `P_t`,

```text
T_{t,2t-1-r} = a_r b3^2 + b_r b3 + c_r,
wt(a_r) = r,  wt(b_r) = t+1+r,  wt(c_r) = 2t+2+r,   all in P_t.        (4.1)
```

Since `wt(a_r) = r`, the form `a_r` can only involve `b4, q_{2,0}, .., q_{r,0}`;
in particular `a_0` has weight 0, i.e. `a_0 in A_t`.  These are the charged
fable5 statements (3.1)-(3.2), re-derived from the weights alone.  Verified on
regenerated rows at `t=2,3,4,5`: the support of `a_r` is exactly
`{b4, q_{2,0}, .., q_{r,0}}`, its weight is exactly `r`, and its term count is
the number of partitions of `r` into parts `<= t-1` (`1,1,2,3,5` at `t=5`), so
every allowed monomial occurs (`tail_audit_t{2,3,4,5}.out`).

### 4.2 The unit

The banked symbolic-`t` b3-axis extraction
(`k16-terminal-proof-sol56-20260903.md` (6.1)-(6.2)) gives, as an identity in
`Q(t)[d]/(3d^2-t-1)`,

```text
a_0 = -alpha_t,
alpha_t = t(3t+1)(A_b d + B_b) / (12 q^2 (3t-1)^2 (3t+2)),
A_b = 27t^3-30t^2+t-2,   B_b = 6t^3+13t^2-3t+2.                        (4.2)
```

I re-derived its norm from scratch in `alpha_norm_audit.py`:

```text
Res_y(H_t, A_b d + B_b) = 4q^2 (3B_b^2 - A_b^2(t+1))
   = -4 (t-2) (2t+1)^2 (3t-1)^2 (3t+2) (27t^3+17t^2+t+2).              (4.3)
```

The factorisation is exact (difference from the charged (3.6) is identically
zero).  Its only integer root is `t=2`: `(3t-1)^2` and `(3t+2)` have no integer
root, and `27t^3+17t^2+t+2` has the single real root `-0.720814492060...`.
Hence

```text
alpha_t is a UNIT of A_t for every integer t>=3 (and t=1), on BOTH factors at
every split index; at t=2 it is a zero divisor.                        (4.4)
```

(4.2) was independently confirmed here at `t=2,3,4,5`: `a_0 + alpha_t = 0`
exactly in `A_t` in each case, with `a_0 = -28(5y-1)/625`, `-5(115y-28)/1232`,
`-26(5625y-1417)/205821`, `-30(3212y-817)/100793`.  The same audit, run unchanged
at each index, prints `Res_y(H_t,a_0) = 0` at `t=2` and `-22175/34496`,
`-1356056/617463`, `-507600/100793` at `t=3,4,5`
(`tail_audit_t{2,3,4,5}.out`), so the unit
hypothesis is seen to fail and to hold by one and the same measurement.  The
uniform statement in `t` rests on the banked (6.1)-(6.2); this lane verifies its
norm, its factorisation and three of its values, not its symbolic derivation.

### 4.3 The splitting

**Theorem TAIL-SPLIT.**  Let `t>=3`.  Then:

1. `T_{t,2t-1} = a_0 b3^2 + b_0 b3 + c_0` with `a_0 in A_t^x`.  Hence
   `T_{t,2t-1}` is a monic-up-to-unit quadratic in `b3` over `P_t`, is a
   nonzerodivisor of `S_t`, and

   ```text
   M_t := S_t/(T_{t,2t-1}) is a FREE graded P_t-module with basis {1, b3},
   Hilb(M_t; s) = (1+s^{t+1}) / prod_{i=1}^{t-1}(1-s^i),
   dim M_t = t-1,  M_t Cohen-Macaulay.                                 (4.5)
   ```

2. Put `G_r := a_0 T_{t,2t-1-r} - a_r T_{t,2t-1}` for `r=1..t-1`.  Since `a_0` is
   a unit, `J_t^tail = (T_{t,2t-1}, G_1, .., G_{t-1})`, and by construction the
   `b3^2` terms cancel:

   ```text
   G_r = B_r b3 + C_r,  B_r = a_0 b_r - a_r b_0,  C_r = a_0 c_r - a_r c_0,
   wt(B_r) = t+1+r,  wt(C_r) = 2t+2+r,  wt(G_r) = 2t+2+r.              (4.6)
   ```

3. Consequently

   ```text
   J_t^tail is an hsop of S_t
     <=> (G_1,..,G_{t-1}) is an hsop of the (t-1)-dimensional CM ring M_t
     <=> dim M_t/(G_1,..,G_{t-1}) = 0,
   ```

   and in that case, `M_t` being CM, the `G_r` are an `M_t`-regular sequence and

   ```text
   Hilb(S_t/J_t^tail; s) = (1+s^{t+1}) * prod_{r=1}^{t-1}(1-s^{2t+2+r})
                                       / prod_{i=1}^{t-1}(1-s^i)
                         = (1+s^{t+1}) [3t+1 choose t-1]_s = P_t(s).    (4.7)
   ```

*Proof.*  (1) is (4.1) plus (4.4).  In `S_t = P_t[b3]`, division with remainder
by `T_{t,2t-1}` is possible and unique because its leading coefficient `a_0` is
invertible; so every class in `M_t` has a unique representative of `b3`-degree
`<= 1`, i.e. `{1,b3}` is a `P_t`-basis of `M_t`.  A free module is torsion-free,
so `T_{t,2t-1}` is a nonzerodivisor; `M_t` is finite free over the regular ring
`P_t`, hence Cohen-Macaulay of dimension `t-1`; and the graded basis degrees `0`
and `t+1` give the stated series.  (2) is the definition; the
`b3^2` coefficient of `G_r` is `a_0 a_r - a_r a_0 = 0`, and the substitution
`T_{t,2t-1-r} = a_0^{-1}(G_r + a_r T_{t,2t-1})` shows the two generating sets
agree.  (3): an ideal generated by `t-1` elements in a `(t-1)`-dimensional CM
ring is an hsop iff the quotient is `0`-dimensional, and an hsop in a CM ring is
a regular sequence; the Hilbert series of a quotient by a regular sequence is
the stated product, and the last equality is Theorem CI-SERIES.  QED

This is where the two factors of `P_t(s)` come from: `(1+s^{t+1})` is
`rank_{P_t} M_t = deg_{b3} T_{t,2t-1} = 2` with the b3 shift, and
`[3t+1 choose t-1]_s` is the CI series of `t-1` forms of the *consecutive*
degrees `2t+3, .., 3t+1` in `t-1` variables of weights `1,..,t-1`.  So `L_t`'s
factor `2` is not a fibre artefact: it is the generic degree of the finite flat
projection `Spec M_t -> Spec P_t`, i.e. the b3-degree of the top tail row.

**Verification.**  At `t=2,3,4,5`, on regenerated rows: every `G_r` has
`deg_{b3} = 1` with `wt(B_r) = t+1+r` and `wt(C_r) = 2t+2+r` exactly as
predicted (at `t=5`: `B_r` of weights `7,8,9,10`, `C_r` of weights `13,14,15,16`).
At `t=3` and `t=4` the two generating sets have the same reduced Groebner basis:
`GB(J_t^tail) = GB(T_{t,2t-1}, G_1, .., G_{t-1})` mod 1009, checked on the first
root of `H_t` at each of `t=3` and `t=4` (`tail_ideal_t3.out`, `t4_ideal.out`).
The measured lengths are `90` and `572` on BOTH roots, `= L_3, L_4`.

At `t=3` the whole GRADED prediction was checked, not only its total: counting
the standard monomials of the Groebner basis by weighted degree gives, on both
roots of `H_3` mod 1009,

```text
Hilb(S_3/J_3^tail) = [1,1,2,2,4,4,6,6,8,7,8,7,8,6,6,4,4,2,2,1,1]
                   = (1+s^4)[10 choose 2]_s = P_3(s),   sum 90, degree 20
```

(`graded_series_t3.out`).  The charged reports measure only the tail length; this
is the first check of the full series (4.7) for the tail.

**Uniform corollaries proved by TAIL-SPLIT alone (all `t>=3`):**

* the projection `V(J_t^tail) -> Spec P_t` is FINITE (degree 2 generically), so
  `dim S_t/J_t^tail = dim P_t/(J_t^tail cap P_t)`: the hard variable `b3` is
  eliminated uniformly and rigorously;
* `V(J_t^tail) cap {b4 = q_{2,0} = .. = q_{t-1,0} = 0} = {0}`, because the top
  row restricts there to `a_0 b3^2` with `a_0` a unit -- this is the `r=0` case
  and it recovers the charged b3-axis statement (sol56 Sec. 6.1) as a corollary;
* `dim S_t/J_t^tail <= t-1`, with equality impossible unless every `G_r`
  vanishes on a `(t-1)`-dimensional component.

## 5. Leading forms (card item (1)), and Theorem NO-COPRIME-LEADERS

### 5.1 What the prompt order gives

Every `T_{t,k}` is weighted homogeneous, so the *weight* initial form is the
whole row and only Singular's `wp` reverse-lex tie-break selects a monomial.
Since `b4` is the first variable, the greatest monomial of the fixed weighted
degree `4t+1-k` is `b4^{4t+1-k}`, and

```text
mu_{t,k} := [b4^{4t+1-k}] T_{t,k} != 0   =>   LM_wp(T_{t,k}) = b4^{4t+1-k}.
```

This is sol56 (6.1).  I recomputed `mu_{t,k}` for every positive band at
`t=2,3,4,5`; all `2t-1` of them are nonzero with nonzero norm, i.e. units
(`tail_audit_t{2,3,4,5}.out` Sec. E), so at those indices
every row's leader is a pure power **of the same variable** `b4`, the leading
monomial ideal of the tail is `(b4^{2t+2})`, of dimension `t-1`, and the
tail is not a coprime-leading-monomial CI in this order.  The card's premise --
that Opus V4 and Fable E2 found the naive leading-form ideal not zero-dimensional
-- is confirmed and explained: the leading monomials are pure powers, but all of
the same variable.  No uniform certificate that `mu_{t,k} != 0` for all `t` is
available (its recursion depth grows with `t`; sol56 Sec. 6), so (6.1) is
conditional uniformly and unconditional only at checked indices.

### 5.2 The right order does not exist

**Theorem NO-COPRIME-LEADERS.**  Let `t>=3`, `t not in {3,5}`.  Then there is no
monomial order on `S_t` and no generating set of `J_t^tail` by `t` elements
forming a regular sequence whose leading monomials are pairwise coprime.

*Proof.*  Suppose `f_0,..,f_{t-1}` is such a regular sequence.  `t` pairwise
coprime monomials of positive degree in `t` variables have pairwise disjoint
supports, so each support is a single variable and each leading monomial is a
pure power `x_{sigma(r)}^{e_r}` with `sigma` injective.  Next, the degrees are
forced.  A regular sequence of length `t` generates an ideal of height `t`; such
an ideal cannot be generated by fewer than `t` elements (Krull), so it has
exactly `t` minimal generators.  The `t` tail rows generate `J_t^tail`, hence
are a minimal generating set, hence the graded minimal-generator degrees are
`2t+2, .., 3t+1`; and any two minimal generating sets of a graded ideal have the
same degree multiset, so `deg f_r = 2t+2+r` after reindexing.  Hence
`wt(x_{sigma(r)})` divides `2t+2+r` for each `r`, with `sigma` injective: a
system of distinct representatives for the bipartite graph
`{degrees 2t+2..3t+1} x {weights 1,..,t-1,t+1}` with edges given by
divisibility.  Now:

* `2t+2 = 2(t+1)` is the only multiple of `t+1` in `[2t+2,3t+1]` (the next is
  `3t+3 > 3t+1`), so the weight `t+1` -- the variable `b3` -- is forced onto the
  top row `T_{t,2t-1}`, with exponent exactly `2`.  That is consistent: it is
  precisely the row whose `b3^2` coefficient is the unit `alpha_t`.
* The remaining weights `1,..,t-1` must be matched injectively into
  `[2t+3, 3t+1]`.  If `D` in that interval is PRIME then, since
  `D >= 2t+3 > t+1`, its only divisor among the available weights is `1`.  Two
  primes in `[2t+3,3t+1]` therefore both require weight `1`: Hall's condition
  fails and no SDR exists.
* Two primes are present for every `t>=16`.  By Nagura's theorem (for `x>=25`
  there is a prime in `(x, 1.2x]`), applying it at `x=2t+2` and again at
  `x = floor(1.2(2t+2))` produces two distinct primes in `(2t+2, 2.88t+2.88]`,
  and `2.88t+2.88 <= 3t+1` as soon as `t>=16`.  For `3<=t<=15` the bipartite
  matching is decided directly.  QED

`pure_power_sdr.py` runs the matching for `t=3..400`: an SDR exists **only** at
`t=3` (`8->b3^2, 9->b4^9, 10->q_2^5`) and `t=5`
(`12->b3^2, 13->b4^13, 14->q_2^7, 15->q_3^5, 16->q_4^4`), and no `t` with two or
more primes in `[2t+3,3t+1]` has one.  (The prime criterion is sufficient, not
necessary: `t=9` has one prime and still no SDR.)

So card item (2)'s alternative -- "exhibiting a regular sequence explicitly (a
triangular change of generators making the leading terms coprime powers)" -- is
impossible for all `t>=6` and for `t=4`, and the pattern is a number-theoretic
accident of the degree window, not a failure of search.  What survives of item
(1) is TAIL-SPLIT: the right change of generators is not one that separates the
variables but one that separates the *b3-degrees*, `(T_{t,2t-1}, G_1..G_{t-1})`
with `G_r` b3-linear, and the right ambient is the rank-2 module `M_t`, not a
monomial degeneration of `S_t`.

## 6. Theorem DEGREE-BLIND: card item (3) is impossible as posed

Card item (3) asks for a Bezout-type or resultant bound on the weighted degrees,
uniform in `t`, that forces `dim = 0`.

**Theorem DEGREE-BLIND.**  The weighted degree data do not determine the
dimension: there are two weighted-homogeneous systems with identical row degrees
and identical variable weights, both occurring as the terminal tail of this
family, one of dimension `0` and one of dimension `1`.  Hence no invariant
computed from the degrees alone -- a Bezout product, a Froberg positive prefix,
the CI Hilbert numerator -- can certify `dim = 0` here.

*Proof (exact witness, characteristic zero).*  Take `t=2`.  `A_2 = Q x Q` with
factors `y=1/5` and `y=2/5`.  On both factors the tail is two rows of weighted
degrees `6` and `7` in two variables of weights `1` and `3` -- identical degree
data, identical predicted CI numerator, identical predicted length
`L_2 = 2 binom(7,1) = 14`.  Computed exactly over `Q` on each factor separately
(`t2_boundary.out`):

```text
y = 1/5:  T_{2,2} =  7 b4^4 (16 b3 - 35 b4^3)/640
          T_{2,3} = -7 b4^3 (88 b3 - 295 b4^3)/640
          gcd = b4^3;  a_0 = 0;  lead(J) = (b4^6, b4^4 b3, b4^3 b3^2),
          no pure power of b3;  dim = 1;  V contains the b3-axis; length infinite.
y = 2/5:  a_0 = -28/625, a unit;  gcd = 1;  dim = 0;  vdim = 14 = L_2.
```

Two systems with the same degrees and opposite dimensions.  QED

Two remarks.  First, this is the sharp form of the observation already made in
`k16-hilbert-regseq-sol56-20260903.md` Sec. 7 for its own Froberg conjecture;
here it is used as a formal obstruction, and the `y=2/5` tail length `14` is new
(the charged reports record only the *full-cone* length `12` on that fibre).
Second, it identifies exactly what any all-`t` proof must consume: a unit
statement not visible in the degrees.  The weight-0 candidate is unique -- `a_0`
-- and by (4.3) its norm is nonzero precisely off `t=2`.  So the hypothesis of
TAIL-SPLIT fails exactly at the charged obstruction `t=2, y=1/5` and holds at
`t=2, y=2/5` and at every `t>=3`, which is card item (4).

The failure mode is also explicit rather than abstract: when `a_0 = 0` the top
row loses its `b3^2` term, `b4` divides every tail row (measured: `b4^3`), the
b3-axis enters `V(J)`, and `M_t` is no longer `P_t`-free of rank 2 -- the
rank-2 splitting is exactly what breaks.

## 7. The residual: eliminant, rank criterion, and its cost

### 7.1 The b3-free eliminant and its explicit certificate

For each `r=1..t-1` put

```text
W_r := a_0 C_r^2 - b_0 B_r C_r + c_0 B_r^2   in P_t,   wt(W_r) = 4t+4+2r.
```

**Lemma ELIMINANT.**  `W_r = B_r^2 T_{t,2t-1} - G_r (a_0 G_r - 2 a_0 C_r + b_0 B_r)`.
Hence `W_r in J_t^tail cap P_t`, and if `V(W_1,..,W_{t-1}) = {0}` in `Spec P_t`
then `V(J_t^tail) = {0}` (a zero of the tail projects to a common zero of the
`W_r`; over the origin of `P_t` the top row is `a_0 b3^2` with `a_0` a unit, so
`b3=0`).  The identity is verified symbolically in indeterminates
(`eliminant_certificate.out`), hence for all `t,r`, and equals sympy's
`Res_{b3}(T_{t,2t-1}, G_r)` on the nose.  At `t=3`, mod 1009 on both fibres,
`W_r` is nonzero and reduces to zero against a Groebner basis of `J_3^tail`
(`t3_eliminant_modp.out`).

This is the charged Lemma SQUARE (fable5 Sec. 5.2) in linearised form: because
`G_r` is b3-*linear*, the general two-quadratic Sylvester expression collapses to
the three-term `W_r` above, and its cofactors are explicit.

**The cost of the elimination is exactly `2^{t-2}`.**  The square system
`W_1..W_{t-1}` consists of `t-1` forms of weights `4t+6, 4t+8, .., 6t+2` in
`t-1` variables of weights `1,..,t-1`, so its Bezout number is

```text
prod_{r=1}^{t-1}(4t+4+2r) / (t-1)! = 2^{t-1} (3t+1)! / ((2t+2)!(t-1)!)
                                   = 2^{t-2} L_t .
```

Measured at `t=3`: `V(W_1,W_2) = {0}` with `vdim = 180 = 2 * 90`, on both
modular fibres (`tail_ideal_t3.out`).  This quantifies the charged observation
that the resultant route is a structural reformulation and not a computational
shortcut (fable5 Sec. 5.2): each elimination step doubles the count.

### 7.2 The exact criterion

Let `N` be the `(t-1) x 2` matrix over `P_t` with rows `(C_r, B_r)`.  A point of
`V(J_t^tail)` over `p in Spec P_t` is a `beta` with `N(p) (1, beta)^T = 0` and
`T_{t,2t-1}(p,beta) = 0`.  Hence, for `t>=3`:

```text
V(J_t^tail) = {0}
  <=>  (i)  V(B_1,..,B_{t-1},C_1,..,C_{t-1}) = {0} in Spec P_t,  and
       (ii) for every p != 0 with rank N(p) = 1 and ker N(p) spanned by a vector
            of nonzero first coordinate, W_r(p) != 0 for some r.
```

(If `rank N(p) = 0` at some `p != 0` then, `a_0` being a unit,
`T_{t,2t-1}(p, .)` has a root and `V(J)` acquires a positive-dimensional
component -- this is clause (i).)  Clause (ii) is the residual content, and its
shape is the reason no Groebner-free proof has been reached: the locus
`rank N <= 1` of a `(t-1) x 2` matrix in a `(t-1)`-dimensional space has expected
codimension `t-2`, i.e. expected dimension `1`.  So the statement to be proved
for all `t` is a non-vanishing along a *curve* of candidate directions -- one
scalar per component -- and the scalars are values of `b_r, c_r`, which the
charged analysis shows carry the whole `2t+1`-step spine and admit no closed form
in `t` by this route (fable5 Sec. 3(c); sol56 Sec. 6.3, where even the next
coordinate axis `u_2` reduces only to an unfactored norm).  At `t=3,4,5` all
`binom(t-1,2)` minors `B_r C_{r'} - B_{r'} C_r` are nonzero with the predicted
weights `3t+3+r+r'` (1, 3 and 6 minors respectively;
`tail_audit_t{3,4,5}.out` Sec. F), so clause (i) is not violated at those
indices.

### 7.3 Where the deep sub-charts sit in this picture

On `S = {b4 = q_{2,0} = .. = q_{t-2,0} = 0}` with the single residual
`x = q_{t-1,0}` of weight `t-1`, a coefficient survives only if its weight is a
multiple of `t-1`.  So `a_0` survives (weight 0, the constant `-alpha_t`),
`a_r|_S = 0` for `1<=r<=t-2` while `a_{t-1}|_S` is a scalar times `x`; `b_r|_S`
vanishes except at `r=t-3` (the only multiple `2(t-1)` of `t-1` in
`[t+1,2t]`), giving `beta x^2`; and `c_r|_S` vanishes except at `r=t-5`, when
`t>=5` (the only multiple `3(t-1)` of `t-1` in `[2t+2,3t+1]`), giving
`gamma x^3`.  For `t>=6` the tail therefore collapses on `S` to
`{a_0 b3^2, (const) x b3^2, beta x^2 b3, gamma x^3}`, and dimension `0` there is
exactly `gamma != 0` -- which is the banked `Q-PLANE` / `UNIQUE-POWER` step
`T_{t,t+4}|_S = A2 x^3` (fable5 Sec. 5.2).  So the banked chain steps
`(C_{t-r})`, `r<=5`, `t>=3r+3` are the deepest strata of criterion RANK, and the
same cap `r <= (t-3)/3` applies.  Nothing in TAIL-SPLIT lifts that cap.

## 8. Computation record

Single core, sympy 1.12, python 3, no other engine.  Every job carries a
`.resource` file written by `/usr/bin/time` (`wall`, `maxrss_kb`, `exit`); all
seventeen exits are `0` and peak RSS never exceeds 132 MB.  `run_all.sh` reruns everything
except the three `t=4` jobs and the `t=5` audit, which are launched separately
because they are the only ones over a minute.  Wall times below are the recorded
ones.  One job overran the card's 10-minute guidance: `t4_ideal.py` took
608.9 s (8.9 s over), computing sympy Groebner bases in four variables on both
roots of `H_4`; it is reported as measured rather than trimmed.

| driver | what it establishes | wall (s) |
|---|---|---:|
| `ci_series_identity.py 16` | Theorem CI-SERIES, checks I1-I6 for `t=2..16`, all pass | 0.22 |
| `alpha_norm_audit.py` | re-derivation of (4.3), integer-root analysis, `alpha_2` on both fibres | 0.82 |
| `tail_structure.py 2` / `3` / `4` | independent closed-recurrence row generator (sol56 (2.1)-(2.13)); prints `deg_wp T_{t,k} = 4t+1-k` for every band | 3.6 / 17.2 / 43.4 |
| `tail_audit.py 2` | structure A-F at `t=2`: `a_0 + alpha_2 = 0`, `Res_y(H_2,a_0) = 0` | 3.7 |
| `tail_audit.py 3` | structure A-F at `t=3` | 17.8 |
| `tail_audit.py 4` | structure A-F at `t=4` | 45.9 |
| `tail_audit.py 5` | structure A-F at `t=5` (build 265 s) | 283 |
| `crosscheck_norms.py` | three fable5 `Res_y(H_3,.)` values reproduced digit-for-digit | 0.71 |
| `t2_boundary.py` | exact `t=2` both fibres: dim 1 / dim 0 length 14 | 4.1 |
| `tail_ideal_t3.py` | `t=3` dim 0 vdim 90 both roots; `J=(Q_0,G_1,G_2)`; `V(W_1,W_2)={0}` vdim 180 | 5.7 |
| `graded_series_t3.py` | full graded series of `S_3/J_3^tail` equals `P_3(s)`, both roots | 1.0 |
| `t4_ideal.py` | `t=4` dim 0 vdim 572 both roots; `J=(Q_0,G_1,G_2,G_3)` | 608.9 |
| `eliminant_certificate.py` | Lemma ELIMINANT identity in indeterminates | 0.45 |
| `t3_eliminant_modp.py` | `W_r != 0`, `NF(W_r, GB(J_3^tail)) = 0`, both roots | 2.6 |
| `pure_power_sdr.py` | Theorem NO-COPRIME-LEADERS matching, `t=3..400` | 3.0 |

Row files `tail_t3_rows.json`, `tail_t4_rows.json` hold the regenerated rows and
the `a_r, B_r, C_r` as sympy `srepr` strings.  `artifacts.sha256` is the
directory manifest.

Two accuracy notes.  (a) The exact symbolic comparison `W_r == Res_{b3}(...)` in
`tail_ideal_t3.py` printed `False`: that is `sp.simplify` failing to normalise
large rational functions in `y`, not a discrepancy -- the identity is exact in
indeterminates and holds mod `p` on both `t=3` fibres.  (b) All `t=3,4` ideal
computations here are modular (`p=1009`, both roots of `H_t`); they are labelled
MEASURED-MODULAR and are used only to confirm banked exact values, never to
promote a length.  The `t=2` computations are exact over `Q` on each factor.

## 9. Verdict and dependency chain

```text
(V0) for all t>=3, Groebner-free:  NOT PROVED.  PARTIAL.
```

Proved here, uniformly in `t>=3` and on both factors at split indices:

```text
CI-SERIES            P_t(s) = (1+s^{t+1})[3t+1 choose t-1]_s, nonnegative,
                     palindromic, degree (2t-1)(t+1), L_t = 2 binom(3t+1,t-1)
                     = 2 #{monomials of degree <= 2t+2 in t-1 variables}.
TAIL-SPLIT           a_0 = -alpha_t is a unit; S_t/(T_{t,2t-1}) is P_t-free of
                     rank 2; J_t^tail = (T_{t,2t-1}, G_1..G_{t-1}) with G_r
                     b3-linear of degree 2t+2+r; hsop <=> dim M_t/(G) = 0;
                     the two factors of P_t(s) are the rank and the CI part.
                     [uniform in t modulo the banked sol56 (6.1)-(6.2)]
ELIMINANT            explicit W_r in J_t^tail cap P_t with a 2-term cofactor
                     certificate; elimination costs exactly 2^{t-2} in length.
RANK                 exact necessary-and-sufficient criterion, residual content
                     = non-vanishing along a curve.
NO-COPRIME-LEADERS   no order / no generators give coprime leaders, t not in {3,5}.
DEGREE-BLIND         no degree-only argument can decide dim 0 (t=2 witness pair).
```

The residual statement, stated exactly, is criterion RANK; equivalently a
uniform proof of `V(W_1,..,W_{t-1}) = {0}`, `t-1` forms of weights
`4t+6,..,6t+2` in `t-1` variables of weights `1,..,t-1`; equivalently a closed
form in `t` for the pair `(b_r, c_r)` of (4.1), which is what the charged
reports identify as spine-complete and closed-form-free.  The conclusion it
would give -- the tail hsop, hence `(V0)` -- is currently verified at:
`t=2, y=2/5` (exact, new here), `t=3,4` (exact, banked; reproduced modularly on
both roots here), `t=5,6` (`p=1009`, both roots, banked), `t=7` (`p=1009`, one
root, banked).  `t>=8` is untested; `t=2, y=1/5` is a genuine failure.

At an index where the tail hsop is established, the banked chain is unchanged:

```text
tail hsop at t
  => dim S_t/J_t^tail = 0
  => dim S_t/I_{t,+} = 0 by containment            (gpt55 Sec. 9)
  => (V0) at t
  => tau_t vanishes on the cone and the band-zero constant yg is a unit
  => terminal unit statement (8.1) at t
  => banked constant spine / normalizer lemma / second affine spine
  => theorem (T) at t.
```

The properness gate (`k16-properness-gate-opus5-20260903.md`) promotes only
`modular dim = 0 => characteristic-zero dim = 0`; it is not used to promote any
length in this report, and Cohen-Macaulayness plus TAIL-SPLIT then force the
characteristic-zero series (4.7) independently.  Nothing here changes the
`t=2, y=1/5` situation: `(V0)` genuinely fails there, `alpha_2` vanishes, and
`(8.1)` still holds on that fibre by the banked weaker radical criterion.

## 10. FALLACY-v2 audit

* **Floor/attainment.**  `L_t` is the length the quotient *has if* the tail is an
  hsop.  It is never used as evidence for dimension.  Theorem DEGREE-BLIND is the
  formal statement that the implication cannot be reversed.  The measured `t<=7`
  lengths are attainment at those indices only.
* **Carrier/attainment.**  `V(W_1..W_{t-1}) = {0}` is a *sufficient* condition
  and is labelled so; criterion RANK is the exact one, and its clause (ii) is
  explicitly not discharged.
* **Flag/place/series.**  The CI *series*, the *ideal* `J_t^tail`, and the
  *fibre* of `A_t` are kept distinct throughout; every measured number carries
  its fibre and its characteristic.
* **`sat()` wrapping / raw remainder degree.**  No saturation is used.  The one
  normal-form claim (`NF(W_r, GB(J_3^tail)) = 0`) states its ring
  (`GF(1009)[b4,u2,b3]`, grevlex, declared root of `H_3`), is run on both roots,
  and is accompanied by the positive control `W_r != 0` and the independent
  indeterminate-level certificate of Lemma ELIMINANT.
* **Variable/ring map.**  Declared everywhere: `A_t = Q[y]/(H_t)`, generator
  order `b4, q_{2,0},..,q_{t-1,0}, b3`, weights `1,2,..,t-1,t+1`.  Image checks:
  nine independently reproduced charged values, Sec. 2.
* **Prime label/derivative.**  `'` is differentiation only inside the banked
  Laurent formulas; the finite field is `p = 1009` throughout.
* **Pole/interior.**  The only pole-type manipulation is
  `(1-s^{2t+2})/(1-s^{t+1}) = 1+s^{t+1}`, an exact polynomial identity, and the
  denominator `D_t` is the actual weighted denominator of `S_t`.
* **Per-ray/exit-set charge.**  No exit price, flag, or exit set is asserted in
  this report, so no `charge_basis` line is due.  Nagura's theorem is cited as a
  published number-theoretic result, not as a validator output.
* **Merge-free/M-descent, target/arrival index.**  Not touched by this lane.

## 11. Reproduction

```text
cd box/k16hsop-20260903
bash run_all.sh                    # every job except the three t=4 jobs,
                                   # each with its own .resource record
python3 tail_structure.py 4        # t=4 rows + per-band weighted degrees
python3 tail_audit.py 4            # t=4 structure A-F
python3 tail_audit.py 5            # t=5 structure A-F
python3 t4_ideal.py                # t=4 dim/vdim on both roots of H_4
sha256sum -c artifacts.sha256
```

`tail_audit.py t` regenerates the rows for any `t` from the closed recurrence
before auditing them.  The exact-row build grows steeply (3.6 s, 17.2 s, 43.4 s,
265 s at `t=2,3,4,5`), so the structural audit was carried to `t=5` and the
ideal-theoretic computations only to `t=4`; `t>=6` is out of reach for a
sympy-only desk lane and is covered by the banked Singular measurements up to
`t=7`.  Every claim above is therefore either uniform in `t` with a stated
proof, or measured here at `t<=5` (structure) / `t<=4` (dimension and length)
and cross-referenced to the banked `t<=7` record.

<!-- BODY-END -->
