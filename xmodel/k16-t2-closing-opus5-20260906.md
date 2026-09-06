# K16 UNIFORM test lane: the closing ideal is NOT inside (T_2), but it does force T_2 = 0; and the ray is not a 3:2 datum

Lane `k16-t2-closing-opus5-20260906`. Opus 5. 2026-09-06.

**VERDICT: BOTH conjectures are REFUTED as stated. CONJECTURE 1 fails in every
reading: no closing condition `Phi_k` (`2N < k <= 4N`) is divisible by `T_2` — not
even by its square root `Lpivot` — at `N = 4, 5`, and on the ray no frozen row
`E_2..E_{2t}` is divisible by `T_2` at `t = 3, 4` (with a weight proof for all `t`).
CONJECTURE 2's premise is false: the K = 16 ray's terminal datum is not a 3:2 pair
with a 16-approximate root; it has `n_1 = 3t+1`, `n_2 = 4`, `D_2 = 24t^2-1`, so
the charged Prop. 3.1 family `G^3 - F^2 + aG^2 + bFG + cF + dG + e_0` is not its
`T_2^char` at any `t`, and the leader `lambda` requested does not exist as described.
No uniform statement is obtained; (R) is not proved; theorem (T) is not promoted
for any new index.**

**What is gained.** The CONVERSE of CONJECTURE 1 is confirmed at `N = 4` and `N = 5`:
`Lpivot` — hence `T_2`, and in fact `eta` and `B*eta` themselves — lies in the radical
of the closing ideal alone, with NO leading-coefficient row, NO `d`, NO ray data and
no frozen certificate. That upgrades
the charged "Observation, not a theorem" (universal-series §4) from a remark on the
zero-dimensional `V(J_t)` to a non-vacuous statement about a positive-dimensional
variety, and it names the uniform target `(U-TAC)` in §4.

## 1. Custody

The receipt `xmodel/k16-t2-closing-opus5-20260906.run.v2` was parsed with
`awk -F=`, pairing every `charged_input_<i>_sha256=` with its `_basename=` into
`/tmp/manifest.sha256`; `sha256sum -c` returned **5/5 OK** before any input was
opened. No digest was retyped. Basis `ed41ab40`. All five charged inputs were read
from `/tmp/jc2-lane.kQOPzL/inputs`. Consumed: from the charged tacnode report,
`T_2`, `Lpivot := 4eta + 3b l_2`, Theorem 5.1(i) and the notation of §2; from the
charged universal-series report, (UF) in Euler form, `G`, `R`, the jets, the
recursion `row_k`, Props. 2.1(b,c), 2.2, 4.2, 4.3, the closed forms of `Phi_4`,
`Phi_5`, and the §5 table; from the charged Astra report, the chart (1), Theorem H,
the weights, `J_t`, `U`, `X`, the (8.1) chain and the residual (R); from the charged
char-degree report, the p.150 definitions of `d_i, n_i, q_i, Lambda_i, mu_i, D_i`,
Prop. 2.2, Theorem A, the Prop. 3.1 enumeration and the §5 cone-vertex argument.

The frozen certificates replayed are `box/k16xempty-20260905/controls_t{3,4}_raw.sing`
and `controls_t{3,4}_W.txt`, read byte-unchanged (read-only; nothing was written to
that box), imported under the **identity map on `(c_i, b)`** with `minpoly 3d^2 - N`,
exactly as in the charged `custody_bu.py`/`custody_tacnode.py`. No ledger, `jc2-lean`
or `ideation-*` file was read or written. New drivers and transcripts are confined to
`box/k16-t2-closing-20260906/` (136 KB total).

**One uncharged consumption, declared.** The K = 16 ray's source 4-tuple
`(n, m; M_2; V_2) = (12t+4, 8t+4; 12t+1; 3)` is in NO charged input of this lane. It
is taken from the banked `xmodel/k16-middle-spine-opus5-20260903.md:51,284,330-337`
and `xmodel/bridge-chart-gate-gpt55-20260903.md:38-40` (`n=4e`, `m=4q`, `e=3t+1`,
`q=2t+1`, `h` the monic **quartic** approximate root), labelled `CONSUMED-UNCHARGED`
throughout §5; every numerical consequence is recomputed here from the CHARGED p.150
formulas with the charged `(99,66)`/`(108,72)` tables as exact controls. Corroboration
inside the charged Astra report: its normalizer scalars carry exactly `(3t+1)`,
`(2t+1)`, `(4t+1)` (`N(g) = t^2(t+1)(3t+1)^2(4t+1)/(36 q^6)`).

## 2. Setup: in free jets `T_2` is exactly minus a quarter of a perfect square

Charged notation: `N = t+1`, `theta = x d/dx`, `L = -b + sum_{j>=2} l_j x^j`,
`G = (3/2)L(L+b) - Bx`, `R = (3/16)L^2(L(L+2b) - 4Bx) - eta x^2(bL/2 + Bx)`,
(UF) `(theta-3)(P^2) + GP = R`, jets `P_0 = -b^2/4`, `P_1 = -B`, `P_2 = eta`,
`P_3 = w_2`, `P_4 = w_3`. Row `x^k` has pivot `-(k-3)b^2/2`, so `P_k = Phi_k` for
`k >= 4`; the degree-`N` closing conditions are `Phi_{2N+1} = ... = Phi_{4N} = 0`.

The charged Theorem 5.1(i) reads `Lpivot^2 = -4T_2 - 24E_2` with
`E_2 = -(b^2/2)(P_4 - Phi_4)`. **In free jets `P_4` IS `Phi_4` (that is what row 4
says), so `E_2 = 0` identically and**

```text
(F)      T_2  =  -(1/4) * Lpivot^2  =  -(1/4)*(4 eta + 3 b l_2)^2       (free jets)
```

Everything about `(T_2)` in free jets is therefore a statement about `(Lpivot^2)`.
Two immediate consequences used below: `(T_2) = (u^2)` where `u := Lpivot`; and a
free-jet quantity is divisible by `T_2` iff its `u`-order is `>= 2`.

**Normalization `b = 1` is legitimate and lossless.** All objects are
weighted-homogeneous (`wt c_j = j`, `wt b = t+1`, `wt B = 2t+1`, `wt eta = 2t`,
`wt Phi_k = 2N-k`, `wt T_2 = 4t`) and `b != 0` throughout the charged charts, so the
weighted `G_m` acts with `wt b = N != 0` and `b = 1` fixes it; every `b`-power is
recovered from the weight. Divisibility by `T_2` in `Q[jets][1/b]` is therefore
divisibility by `u^2` at `b = 1`. Every driver substitutes `eta = (u - 3 l_2)/4`, so
`u` is a coordinate, not a derived quantity.

## 3. CONJECTURE 1 — REFUTED in all three readings

### 3.1 Free jets (the literal reading): `I_close = (Phi_{2N+1},...,Phi_{4N}) ⊄ (T_2)`

Driver `closing_freejets.sing`: build `L` of degree `N` with free `l_2..l_N`, free
`B, w_2` and `u`, run the charged recursion `P_k = 2*bracket_k/((k-3)b^2)` to
`k = 4N`, then read off the `u`-order of each `Phi_k`. `Phi_k in (T_2)` iff
`uord >= 2`.

```text
N=4 (t=3), KMAX=16   uord(Phi_k) = 0 for EVERY k = 4..16   (closing rows k = 9..16)
N=5 (t=4), KMAX=20   uord(Phi_k) = 0 for EVERY k = 4..20   (closing rows k = 11..20)
```

Not one closing row is divisible by `u`, let alone by `u^2 = -4T_2`. The exact
nonzero remainder of the first closing row at `N = 4` is the 26-term polynomial

```text
Phi_9|_{u=0} = 12012*B^6*w2 - (81081/20)*B^5*l2^2 - 10395*B^4*w2*l2 + ...
             + 8*w2^3 - 5*w2^2*l3 + (1/4)*l3^3 + (47/8)*w2*l2*l4 + (2/5)*B*l4^2
```

(full string in `freejets_N4.out`; `Phi_11|_{u=0}` at `N = 5`, 63 terms, in
`freejets_N5.out`). At `l_4 = l_3 = l_2 = B = 0` it is `8 w_2^3 != 0`, so the
remainder is nonzero on a dense set, not only generically. **REFUTED.**

**Controls (all four pass).** (i) `Phi_4`, `Phi_5` agree with the charged closed forms
of Prop. 2.1(c) exactly. (ii) the (UF) residual has every row `x^0..x^{4N}` zero at
`N = 4`. (iii) POSITIVE CONTROL on the only known closed-form family (Prop. 4.3,
`t = 2, d = -1`): at `N = 3` with `B = eta = l_2 = 0`, `w_2 = l_3/2` the recursion
returns `Phi_4 = Phi_5 = 0`, `Phi_6 = -l_3^2/4`, `Phi_7..Phi_12 = 0` and
`P + L^2/4 = 0` exactly. (iv) §3.2.

### 3.2 On the ray (the frozen-basis reading): `J_t ⊄ (T_2)`, and no row is divisible

Driver `onray_T2.sing`: `controls_t{t}_W.txt` read into `(0,d),(x,c1..c_{t-1},b)`,
`minpoly 3d^2-N`, giving `B = -[x^0]W`, `eta = [x^1]W`, `w_2 = [x^2]W`, `w_3 = [x^3]W`,
`l_2 = c_{t-1}/y`, `y = (d+t+1)/(2(2t+1))`; `controls_t{t}_raw.sing` imported into
`(0,d),(c1..c_{t-1},b),wp(1,..,t-1,t+1)` under the identity map on `(c_i,b)`.

```text
t   CUSTODY B/eta/B*eta   Lp^2+4T_2+24E_2   wt T_2 / Lpivot / B*eta   dim,vdim   T_2,T_2^2,Beta,(Beta)^2 in J
3   0 / 0 / 0             0                 12 / 6 / 13  (=4t,2t,4t+1) 0, 66      no, yes, no, yes
4   0 / 0 / 0             0                 16 / 8 / 17  (=4t,2t,4t+1) 0, 338     no, yes, no, yes
```

Every line reproduces the charged tables (universal-series §5; tacnode §6) exactly,
including Theorem 5.1(i) as an identity on the frozen data. Then:

```text
t=3   E_2..E_6  weights 12,11,10,9,8      divisible by T_2:  no,no,no,no,no
t=4   E_2..E_8  weights 16,15,14,13,12,11,10   divisible by T_2:  no (all seven)
```

**Proof for every `t` (not just `3, 4`).** `S_t = k[c_1..c_{t-1}, b]` is graded by
strictly positive weights, so a nonzero element of `(T_2)` has weight `>= wt T_2 = 4t`.
But `wt E_k = 4t+2-k`, which is `< 4t` for every `k >= 3`. Hence
`E_3, ..., E_{2t} in (T_2)` would force `E_3 = ... = E_{2t} = 0`, which is false at
`t = 3, 4` (row term counts 12,12,9,9 and 47,40,34,29,24,20 above). Only `E_2` has
the matching weight `4t`, and `E_2 in (T_2)` would mean `E_2 = lambda T_2` for a
scalar `lambda`; the computation says no at `t = 3, 4`. So `J_t ⊄ (T_2)` for all
`t >= 3`, with the single row `E_2` needing the finite check. **REFUTED, uniformly.**

### 3.3 The dual reading `l_{N+1} == 0 mod T_2` is VACUOUS as stated

Driver `dual_lNplus1.sing` (charged Prop. 4.2). With `P_3, P_5, P_6, P_7` free and
`P_4 = Phi_4`, rows 5, 6, 7 eliminate `l_3, l_4, l_5` with the k-independent pivot
`-u/4` — confirming Prop. 2.2 numerically. But Prop. 4.2 is valid only on
`{Lpivot != 0}`: on the dual chart `u` is a **unit**, hence `T_2 = -u^2/4` is a unit
and `(T_2)` is the whole ring, so `l_{N+1} == 0 mod T_2` holds for every jet vector
and carries no information. FALLACY-v2 (sat()/localization; floor/attainment).

The non-vacuous measurement is the `u`-order after clearing denominators. At `N = 4`,

```text
l_5  in  Q[u,1/u][B,l2,w2,Q5,Q6,Q7],  u-support = [-5, +2],  88 terms,
     leading pole  -288*u^{-5}*Q5^3 - ... ,  and  l_5 contains -8*u^{-1}*Q_7.
```

`ord_u(l_5) = -5`, not `>= +2`. So even the numerator reading — `u^{5+2} | u^5 l_5` —
fails at the first coefficient. **REFUTED.**

The type `K16-CLOSING-NOT-IN-T2` offered by the lane prompt is therefore not opened:
the question is closed here in the negative. The typed residual that replaces it is
`(U-TAC)` in §4.

## 4. The CONVERSE — the useful direction — holds, and is the right uniform target

CONJECTURE 1 asked for `I_close ⊆ (T_2)`: every degenerate-tacnode jet vector solves
every closing condition. The useful containment is the other one,
`T_2 ∈ rad I_close` (every polynomial solution has a degenerate tacnode). That one is
confirmed here in a strictly cleaner chart: **no `(UL)` row, no `d`, `y`, `omega` or
`t`, no frozen certificate** — only the closing ideal over `Q`.

Driver `power_membership.sing`. `S = k[u, B, w_2, l_2..l_N]` (`b = 1`), one
`std(I_close)`, then minimal-exponent membership.

```text
                   |GB|   dim   minimal e with target^e in I_close
                                u=Lpivot  l_2  eta  B*eta   B         w_2
N=4 (t=3),  8 gens  1296    1      19      15   19    19    none<=40  none<=40
N=5 (t=4), 10 gens 10017    1      27      20   27   (27)   none<=45  none<=45
```

`N = 4` at both primes, every entry identical; `N = 5` at `p = 1000003` only, where
the `B*eta` run hit its budget — but `eta ∈ rad` gives `B*eta ∈ rad` at once. So at
both indices `V(I_close) ⊆ {eta = 0} ⊆ {T_2 = 0} ∩ {B*eta = 0}`, non-vacuously: the
variety is a curve, not a point, and `B, w_2` are demonstrably NOT in the radical, so
the machinery is not returning "everything".

**Independent saturation controls** (`p = 1000003`, a plain prime field — the
`p = 31991` saturation was run over `F_p[d]/(3d^2-4)`, which SPLITS, and is not
counted). `(I_close, 1-z u)` is the unit ideal; the wrong saturators `u+1`, `B`, `w_2`
do NOT give it on the same ideal with the same machinery; truncating to the first
1, 2, 3 closing rows gives non-unit ideals of dimension 5, 4, 3 (+1 for the dummy
`z`) — the unit at 8 rows comes from the closing rows, not from the localizer.

**Label.** `MEASURED-MODULAR`. NOT a characteristic-zero proof: an ideal can be the
unit ideal mod `p` and not over `Q` (`(px-1)`). Exact-`Q` attempts are in §8. The
charged `bottom_up.py` is fast at `t = 3, 4` because it also imposes the two `(UL)`
rows `l_N = 1/y`, `P_{2N} = omega`, which cut the dimension to 0; the `(UL)`-free
ideal used here is the harder, stronger object.

**The uniform target this names.** FALLACY-v2: two indices are not a theorem. The
identity a uniform proof must supply is

```text
(U-TAC)   For every N >= 3, in Q[u, B, w_2, l_2, ..., l_N] with b = 1 and
          u = 4 eta + 3 l_2 :        u  in  rad( Phi_{2N+1}, ..., Phi_{4N} ).
```

Equivalently: every polynomial `P` of degree `<= 2N` and `L` of degree `<= N` with
the charged jets `(UJ)` solving (UF) with `b != 0` has `4 eta + 3 b l_2 = 0`.
`(U-TAC)` is `OPEN[K16-UF-DEGENERATE-TACNODE]` with the ray data stripped off, and is
strictly weaker than `(R)` (charged Prop. 4.3 remark; the `t = 2, d = -1` family of
§3.1 control (iii) realizes `u = 0` with a genuine polynomial solution). The
measurement adds that `eta` itself — not merely `B*eta` — is in the radical, exponent
19/27 against 15/20 for `l_2`, while `B ∉ rad I_close`: the vanishing sits on the
`eta` side, so a uniform argument must be about `L`'s second coefficient and `P`'s
second jet, not about `B`.

**Why this is not `(R)`.** `(R)` is `(B*eta)^n ∈ J_t` for every `t`. At `N = 4, 5` the
free-jet chart already gives `B*eta ∈ rad I_close` without the `(UL)` rows; whether
that survives all `N` is exactly `(U-TAC)`, and nothing here proves it.

## 5. CONJECTURE 2 — the premise is false; the exact discrepancy

### 5.1 The K = 16 ray is not a 3:2 datum and has no 16-approximate root

The request presupposes a 3:2-type pair `F = h^3 + ...`, `G = h^2 + ...`, `deg h = 16`,
so that the charged Prop. 3.1 enumeration `{1,G,G^2,F,FG,F^2}` applies and
`Q = G^3 - F^2 + aG^2 + bFG + cF + dG + e_0` is the second characteristic polynomial.
That enumeration is derived in the charged report under the explicit hypothesis
`n_1 = 3` ("Here `n_1 = 3` and `T_1^psi = G + constant`").

With the banked (CONSUMED-UNCHARGED, §1) ray 4-tuple
`(n, m; M_2; V_2) = (12t+4, 8t+4; 12t+1; 3)`, the CHARGED p.150 formulas give,
recomputed here in `char_arith.py` (exact integers) with the charged `(99,66)` and
`(108,72)` tables as controls (`CONTROL_..._MATCHES_CHARGED_TABLE = True` for both,
reproducing `d = (99,33,11,1)`, `Lambda = (-6534,-1815,-1595)`, `D = (66,55,145)`
and `d = (108,36,9,1)`, `Lambda = (-7776,-2268,-2043)`, `D = (72,63,227)`):

```text
d_1 = 12t+4,  d_2 = gcd(12t+4, 8t+4) = 4,  d_3 = gcd(4, 12t+1) = 1
n_1 = d_1/d_2 = 3t+1,     n_2 = d_2/d_3 = 4
q_1 = -4(2t+1),           q_2 = M_2 - M_1 = 5(4t+1)
Lambda_1 = -16(2t+1)(3t+1),   Lambda_2 = -4(24t^2-1)
mu_1 = -4(2t+1),              mu_2 = 1-24t^2
D_1 = m = 8t+4,               D_2 = 24t^2 - 1
ambient bound L = n_1*m = 4(3t+1)(2t+1),   leader depth L - D_2 = 5(4t+1) = q_2
```

verified at `t = 2..8` (`char_arith.json`). Hence five discrepancies:

```text
(D1) n_1 = 3t+1, never 3  (3t+1 = 3 has no integer solution). The unique
     equality-weight monomial is F^{2t+1}, not F^2: solving a*m + b*n = n_1*m with
     0 <= a < n_1 gives (a,b) = (0, 2t+1) uniquely, since gcd(2t+1, 3t+1) = 1.
     The ray's family is  Q = G^{3t+1} - F^{2t+1} + (lower),  not  G^3 - F^2 + ... .
(D2) the level-2 approximate root is the monic QUARTIC h (n_2 = d_2 = 4), uniformly
     in t; there is no 16-approximate root on the ray, and gcd(n,m) = 4, not 16.
(D3) D_2 = 24t^2-1 = 215, 383, 599, 863 at t = 3..6; the leader sits at depth
     5(4t+1) = 65, 85, 105, 125 inside a degree-4(3t+1)(2t+1) object (280..988).
(D4) the free lower target coefficients #{(a,b) : a*m+b*n < n_1*m, 0 <= a < n_1}
     number 43, 69, 101, 139 at t = 3..6 — against exactly 5 ({1,G,G^2,F,FG}) in the
     charged 3:2 case, recomputed here as a control.
(D5) (n,m) = (48,32) is not on the ray: 12t+4 = 48 has no integer solution.
```

So `lambda` "the leader of the second characteristic polynomial of a 3:2 pair with
a 16-approximate root" does not exist on this ray at any `t`, and the identification
asked for ("is `lambda` a unit multiple of `B*eta`; is `T_2` a factor of the leading
attainment row") cannot be tested as posed. **CONJECTURE 2: NO, premise refuted.**

### 5.2 What Theorem A does give the ray, uniformly — and why it does not advance (R)

The one uniform consequence that survives the correction is the charged §5
cone-vertex mechanism, now with a `t`-free proof:

**Proposition 5.1 (PROVED-HERE, uniform in `t`).** On the K = 16 ray no point at
which the source pair lies in `k[h]` (`h` the monic quartic approximate root) attains
the second characteristic degree. *Proof.* Every constant-coefficient target polynomial
in `(F,G)` with `F,G in k[h]` lies in `k[h]`, and a nonconstant element of `k[h]` has
degree divisible by `deg h = n_2 = 4`; but `D_2 = 24t^2-1` is odd. ∎ (The charged
"`55` is not divisible by `33`" argument, here as a congruence `D_2 ≡ 3 (mod 4)`
holding for all `t` at once — which the two char-degree clients did not have.)

**But this is not progress on (R).** If `F, G in k[h]` then `J(F,G) ≡ 0`, so the
charged identity `tau = -(g y/3) B eta` mod `I_+` already puts that stratum inside
`{B*eta = 0}`. Prop. 5.1 excludes a locus the target concedes — FALLACY-v2
(carrier/attainment): a necessary condition killing only where the conclusion already
holds supplies no floor for `(R)`.

### 5.3 The attainment rows at `t = 3..6`: cannot be written, and would be vacuous

Two independent obstructions, both reported rather than worked around.

**(a) Not writable from the charged inputs.** Theorem A's rows are coefficient
equations of `Q(G,F)` in the SOURCE coordinates. The intrinsic chart
`S_t = k[c_1..c_{t-1}, b]` is reached from the source ray system through "banked
constant spine, normalizer, second affine spine" (charged Astra §8); that transport is
in none of this lane's five charged inputs, so `lambda` cannot be written in the jets
`(b, B, eta, l_j, w_j)`. Declaring the map by name — `F` to `P`, `G` to `Q` — would be
the FALLACY-v2 variable/ring-map error. Typed `OPEN[K16-ATTAINMENT-TRANSPORT]`.

**(b) Vacuous at every index the lane asks for.** Even with the transport, the
requested test "do the attainment rows cut the terminal cone to `{B*eta = 0}`?" is
empty at `t = 3..6`: the charged inputs already give `dim std(J_t) = 0` with
`V(J_t) = {0}` and `(B*eta)^2 in J_t` at `t = 3, 4, 5` (reproduced here in §3.2 at
`t = 3, 4`: `dim 0`, `vdim 66/338`, `(B eta)^2 in J`), and the charged Astra report
banks the characteristic-zero range through `t = 7`, leaving `t >= 8` as its frontier;
the ledger has since promoted `(T)` at `t = 8` (`AUDIT.md:17892`, 2026-09-05T21:22Z),
so the live frontier is `t >= 9`. Adding any further necessary equation to `I_{t,+}`
at `t <= 8` cuts an already empty cone. The first index at which an attainment row
could be non-vacuous is therefore `t = 9`. This is a socle/vacuity check in
the sense of the charged tacnode §5 caveat, applied to the instrument rather than to
a membership.

## 6. FALLACY-v2 check

**Floor/attainment.** The lane premise "(R) is equivalent (tacnode report) to the
vanishing of `T_2`" is not what the charged sources say. The charged tacnode
Theorem 5.1 states `OPEN[K16-UF-DEGENERATE-TACNODE] <=> T_2 ∈ rad J_t for every t`,
and the charged universal-series Prop. 4.3 remark says that "every polynomial solution
of (UF) has a degenerate tacnode" is **strictly weaker** than (V0). `T_2 ∈ rad J_t` is a weight-`4t` statement; `(R)` is the weight-`4t+1`
statement `B*eta ∈ rad J_t`. Proving `T_2 = 0` on the cone is a floor, not `(R)`.
Everything above is stated against the weaker target and labelled as such.

**sat()/localization.** Every localization is an explicit inverse equation `1 - z*g`
in a declared ring, or `sat(I,g)[1]` with the component extracted and the ring
asserted; positive (`g = u`) and negative (`g = u+1, B, w_2`) saturators were run on
the same ideal with the same machinery (§4).

**Variable/ring map.** Every import from `box/k16xempty-20260905/` names the ring,
generator order, coefficient field `Q(d)` with `minpoly 3d^2-N`, and the identity map
on `(c_i, b)`; images were checked against the frozen `Bsol`, `eta`, `target` (all
differences 0, §3.2). `b = 1` is justified by the weighted `G_m`, not asserted.

**Raw remainder degree.** §3.1 is a remainder after division by `u^2` in a declared
global order, with an explicit point where it is nonzero — not generic vanishing.

**Uncharged consumption.** The ray 4-tuple is declared `CONSUMED-UNCHARGED` with
path:line in §1; the charged p.150 formulas are re-run on it here with the two
charged client tables as exact controls.

No exit-price assertion is made, so no `charge_basis=` line applies.

## 7. OPENs

OPENS RAISED

- `OPEN[K16-ATTAINMENT-TRANSPORT]` - Theorem A's attainment rows for the K = 16 ray
  are coefficient equations of `Q(G,F)` in the SOURCE coordinates; no charged input
  of this lane carries the transport from those coordinates to the intrinsic chart
  `S_t = k[c_1..c_{t-1}, b]`, so `lambda` cannot be written in the jets
  `(b, B, eta, l_j, w_j)`. QUANTITY: number of charged inputs carrying the
  source-to-chart transport = 0; first index at which an attainment row could be
  non-vacuous = 9 (the cone is already empty for t <= 8, AUDIT.md:17892).

OPENS RETAINED

- `OPEN[K16-UF-DEGENERATE-TACNODE]` (charged): retained and RESTATED as `(U-TAC)`
  in §4 - `u = 4 eta + 3 b l_2 ∈ rad(Phi_{2N+1},...,Phi_{4N})` for every `N >= 3`, a
  statement over `Q` with no `(UL)` row, no `d` and no frozen certificate.
  QUANTITY: number of indices at which `(U-TAC)` is measured = 2 (N = 4, 5); minimal
  exponent `e` with `u^e ∈ I_close` = 19, 27; for `l_2` = 15, 20; number of indices
  with a characteristic-zero certificate for `(U-TAC)` = 0.
- `OPEN[K16-INTRINSIC-SLICE-UNIT]` (charged): unchanged in kind. QUANTITY: first
  index without an exact certificate = 9 (charged inputs say 8; `(T)_8` was promoted
  after they were sealed, `AUDIT.md:17892`).
- `OPEN[K16-UF-CONTACT-ORDER-BOUND]` (charged): unchanged. QUANTITY: solutions with
  known `j0` = 1.
- `OPEN[K16-UF-SECOND-KIND-FAMILY]` (charged): unchanged. QUANTITY: known theorems
  bounding polynomial roots of a power-series quadratic of shape `F_0` = 0.
- `OPEN[K16-UNIFORM-POINT]` (charged Galois lane): untouched. QUANTITY:
  #{t : a closed-form point of Gamma_t is known} = 0.

The type `K16-CLOSING-NOT-IN-T2` is deliberately not raised: §3 settles it in the
negative rather than leaving it open.

## 8. Computation record, collision scan, completion

`box/k16-t2-closing-20260906/`, 136 KB, no CAS dumps and no artifact tree; `df -h /`
was checked before work (2.8 GB free) and at sealing (13 GB); nothing was written
outside the box, the report and `results.json` (3.4 KB).

```text
closing_freejets.sing / freejets_N{4,5}.out      Phi_k, u-orders, controls  (§3.1)
onray_T2.sing / onray_t4.out                     frozen-basis on-ray test   (§3.2)
dual_lNplus1.sing                                ord_u l_{N+1}              (§3.3)
power_membership.sing / power_N{4,5}_*.out       minimal exponents          (§4)
closing_radical{,_Q}.sing, radical_graded.sing   saturations, controls      (§4)
ray_ul.sing / rayUL_N{4,5}_*.out                 ray system with (UL) rows
char_arith.py / char_arith.json                  p.150 invariants+controls  (§5)
```

**Ray-system control** (`ray_ul.sing`, over `F_{p^2}` with `3d^2-N` IRREDUCIBLE mod
`p = 100049` (N=4), `100043` (N=5), so no product algebra). `I_close + (l_N - 1/y,
P_{2N} - omega)` at `b = 1` is the UNIT ideal, `dim = -1`, at BOTH `N = 4` and
`N = 5` — reproducing the banked `V(J_3) = V(J_4) = {0}` from the free-jet chart; at
`N = 4` the control dropping the two `(UL)` rows is non-unit (`dim = 1`), and a third
control (wrong leading coefficient) is also empty, so does not discriminate.

**Exact-`Q` budget.** `std`, `slimgb` and `sat` over `Q`/`Q(d)` on the 1-dimensional
8-generator `I_close` at `N = 4` and on the `(UL)`-augmented ray system at `N = 4, 5`
all exceeded 1800–2700 s (host at load 20–32; a second lane held most cores). They
returned nothing and none is reported as a result. Every characteristic-zero
statement here comes from §3, which is exact.

Collision scan (`ops/open_collision.py`, same-round files filtered):
`OPEN[K16-ATTAINMENT-TRANSPORT]` collides only with the `AUDIT.md` deltas recording
the charged char-degree lane itself (source, not duplication); the four retained
OPENs match their charged sources. Status `CANDIDATES`, no duplicate type.

No task was left running at sealing. `PROVED-HERE` marks a derivation checked here
(§2 (F), §3.1, §3.2 with its all-`t` weight argument, §3.3, Prop. 5.1, §5.1);
`MEASURED-MODULAR` marks §4 and the ray-system control; the rest is charged, or
declared uncharged in §1.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `24490`.
- Body SHA-256:
  `73dbaeb3e9aa350ee8537b2af9181eb0391db47d7696a7ae664815bc82440184`.
- Frozen basis: `ed41ab403503f96ca603ab5711a0783d734b2180`.
