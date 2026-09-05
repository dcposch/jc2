# K16 Γ-Galois lane: the Eagon–Northcott curve Γ_t is one Galois orbit over A_t at t = 3, 4, 5 (proved),
# the all-or-nothing lemma with its étale lift, the one-evaluation instrument through t = 8, and the
# exact residual of (V0) on the K = 16 ray

Lane `k16-gamma-galois-fable5-20260905`, basis `9aede103`, 2026-09-05.  Drivers and every transcript in
`box/k16galois-20260905/` (worker outputs mirrored under `w7/`, `w18/`, `w166/`, `w254/`, `w28/`).
Engines: Singular 4.3.3 (`std`, `finduni`, `factorize`, `quotient`; exact over `A_t = Q(yy)/(H_t)` with
`minpoly`, or `GF(p)` at a declared root of `H_t`), msolve 0.x on one worker (F4 + rational parametrization
mod p, t = 6 calibration and t = 8), python3/sympy/numpy (bookkeeping, root scan).  Foreground CAS under
`timeout` + `stdbuf -oL`; ≤ 5 desk cores; ≤ 4 processes per fleet worker (the fleet was shared with another
lane's jobs throughout).  No ledger, `jc2-lean`, `ideation-*` or in-progress lane report was read or written.
`FALLACY-v2` applies; no exit-price assertion is made, so no `charge_basis` line is due.

## 0. Verdict

```text
REQUESTED  (1) exact factorisation of the Γ_t point polynomial over A_t at t = 4 (46 points) and t = 5 (265 points),
               with Frobenius cycle types;  (2) the all-or-nothing lemma with its Hensel/étale step;  (3) the
               one-evaluation instrument at t = 3, 4, 5, 6, 8;  (4) the uniform problem (I);  (5) the liaison
               colon (G):T_top at t = 3, 4;  (6) the verdict on (V0) for all t.
VERDICT    PARTIAL — fixed-t results PROVED, the uniform statement NOT closed and relocated, not removed.
PROVED     (1) f_t is IRREDUCIBLE over A_t for t = 3, 4, 5 AND 6 (Q(√3), Q(√15), Q(√2), Q(√21)): the affine
               points of Γ_t are ONE Galois orbit, by the degree-pattern criterion (Cor. 3.6) at 49 / 48 / 24 / 8
               prime ideals with the good-reduction hypotheses verified at each (Lemmas 3.3–3.5; exact chart
               vdim 7, 46, 265 over A_t; empty boundary at t = 4, 6), and exactly (factorize over A_3) at t = 3.
               Gal(f_t/A_t) = S_7, S_46, S_265, S_1548 (Jordan: prime cycles 41, 257, 1019 of length > n/2; odd types).
           (2) Lemma 3.1 (all-or-nothing), Lemma 3.7 (étale lift of a simple F_p-point on the flat model, the
               FALLACY-v2 lift statement), Lemmas 3.3–3.5 (flatness from the EN Hilbert function; freeness from
               n' = n; good reduction of the point polynomial) — written out, §3.
           (3) the instrument certifies clause (ii)_t at t = 3, 4, 5, 6 by ONE modular evaluation each (W ≠ 0 at a
               simple F_p-point, lifted; 28, 28, 17, 5 independent witnesses); boundary orbits handled EXACTLY at
               t = 3, 5 (b_3 = 1, b_5 = 2: six conjugate points with q_3 = 0 forming one orbit over Q(√2), plus the
               rational q_3-axis point) and empty at t = 4, 6.  Cost at t = 6: three modular jobs, ≤ 3 min, no
               number-field std, no radical.
           (5) (G):T_top = (G) exactly at t = 3 and mod p at t = 3, 4, 5, with positive/negative controls.
NOT CLOSED (4) problem (I) for t ≥ 7: no uniform mechanism; the determinantal structure fixes the degree, not the
               field of definition; the measured S_n groups are the generic (uniform-position) behaviour and
               any proof of (I) is a genericity statement of the same type as (V0)-tail itself (§7).  Moreover
               Prop. 7.1 shows (I) is NOT NECESSARY: clause (ii)_t over A_t follows from the modular cone statement
               V(I_2 + (W)) = {0} plus flatness, with no orbit count.  The binding uniform gap is (II): a t-indexed
               point of Γ_t with a closed-form T_top — unchanged by this lane.
           (3) at t = 8: the CI system (7 forms, 52140 points) mod 32003 was exported and msolve's F4 (4 threads,
               shared worker) was at degree 14 (45739 × 81237) at seal; the boundary of Γ_8 mod 32003 is six points
               in the stratum q_3 = 1 with W ≠ 0 at all of them (modular); the affine one-point test is typed
               OPEN[K16-ONE-POINT-T8] with the verify job ready (validated at t = 6 against Singular).
CONSEQUENCE (V0) ⇒ (8.1) ⇒ (T) on the whole K16 ray is NOT obtained (no MAJOR claim).  What changes: the fixed-t
           certificate of (V0)-tail is now  (i)_t  ∧  [one simple point per Galois orbit with W ≠ 0]  with
           k_t = 1 proved through t = 6, and the all-t problem is (i) ∀t  ∧  (II) — problem (I) is a structural
           fact (S_n) rather than a hypothesis.
NOTIFY     not warranted (no new (V0) index; fixed-t re-proofs by a cheaper route; irreducibility is new but
           closes no ledger item beyond OPEN[K16-GAMMA-IRREDUCIBLE] at t ≤ 6).
```

## 1. Custody

The receipt `xmodel/k16-gamma-galois-fable5-20260905.run.v2` was parsed with `awk -F=`, pairing its
`charged_input_<i>_sha256=` / `_basename=` lines into `box/k16galois-20260905/manifest.sha256`; `sha256sum -c`
→ **10/10 `OK`** (`manifest.check.log`).  No digest was retyped.  All ten charged inputs were read before any
driver ran.

**Row provenance.**  Every job in this lane is emitted by `gen.py` from the frozen rank-lane row dumps
`box/k16rank-20260903/terminal_t{t}_exact_none.out` (t = 3..8; the charged `singular_terminal_driver.py`
`--mode exact --dump-rows` outputs, byte-unchanged; each file carries `RECURRENCE_PASS` and `DRIVER_DONE`
and no error marker).  The top-tail rows `T_{t,2t−1−r}`, r = 0..t−1, are re-parsed into
`S = K[b4,q2_0,..,q{t−1}_0,b3]`, `wp(1,2,..,t−1,t+1)` with `K = Q(yy)/(H_t)` (`minpoly`) or `GF(p)` with
`yy` a declared root of `H_t` mod p; every job re-asserts, before anything else, `T = a_r b3² + b_r b3 + c_r`,
weighted homogeneity of weight 2t+2+r, `G_r = a_0 T_{2t−1−r} − a_r T_{2t−1} = B_r b3 + C_r`, and the ELIMINANT
certificate `W_r = B_r² T_{2t−1} − G_r(a_0 G_r − 2a_0 C_r + b_0 B_r)`; a `FAIL` marker aborts acceptance (none
occurred in any accepted run).  The mod-p generators are therefore the reductions of the exact generators (ring
operations, one division by 2); `.err` streams were scanned for `div. by 0` (none).  Modular primes are the
largest split primes below 2¹⁵, both primes 𝔭 | p used (`primes.txt`).

## 2. Setting (charged conventions) and the objects of this lane

```text
A_t = Q[y]/(H_t),  H_t = 12q²y² − 12q(t+1)y + (t+1)(3t+2),  q = 2t+1;   A_t ≅ Q(√(3(t+1)))
P_t = A_t[b4, q_2, .., q_{t−1}]  (weights 1, 2, .., t−1),   S_t = P_t[b3]  (weight t+1)
T_{t,2t−1−r} = a_r b3² + b_r b3 + c_r   (r = 0..t−1),   a_0 = −α_t a unit for t ≥ 3
G_r = a_0 T_{t,2t−1−r} − a_r T_{t,2t−1} = B_r b3 + C_r,   N = ((C_r, B_r))_{r=1..t−1},   Γ_t = V(I_2(N)) ⊂ Spec P_t
W_r = a_0 C_r² − b_0 B_r C_r + c_0 B_r²;   at a rank-1 point p with kernel (1:β):  W_r(p) = B_r(p)² T_{t,2t−1}(p, β)
clause (i):  V(B, C) = {0};   clause (ii):  T_{t,2t−1}(p, β(p)) ≠ 0 at every point p ≠ 0 of Γ_t   (FITT, 17(rrrrr))
(V0)-tail_t  ⟺  (i) ∧ (ii)   ⟹  (V0)_t  ⟹  (8.1)_t  ⟹  (T)_t
```

`Γ_t` is a cone over a zero-dimensional weighted-projective scheme; its affine chart `{b4 = 1}` is the
zero-dimensional scheme `Y_t := Spec P_t/(I_2(N) + (b4 − 1))` in the coordinates `q_2, .., q_{t−1}`, and its
boundary `{b4 = 0}` is stratified by the first nonzero coordinate.  The **point polynomial** `f_t ∈ A_t[x]` is
the minimal polynomial of the coordinate `q_2` on `Y_t ⊗ Ā_t`; when `q_2` separates the geometric points and
`Y_t` is reduced, `deg f_t = #Y_t(Ā_t)` and `A_t[x]/(f_t) ≅ O(Y_t)`, so the `Gal(Ā_t/A_t)`-orbits of the affine
points of `Γ_t` are exactly the irreducible factors of `f_t` over `A_t`.

**Charged as measured (17(tttttt))**: `Y_t` reduced with 7, 46, 265 points at t = 3, 4, 5 (mod p), `f_3`
irreducible over `A_3` (exact), Frobenius (2,5) at p = 32003.

### 2.1 Summary table (all entries measured in this lane unless marked charged)

```text
 t  A_t          n_t = #Y_t  boundary of Γ_t (b4=0)                   f_t irreducible over A_t?      Gal(f_t/A_t)      one-point test (ii)   colon (G):T_top = (G)
 3  Q(√3)        7           q_2-axis point (rational)               YES exact + 49 primes          S_7  (proved)      YES (28 primes; bdry exact)   YES exact, YES mod p
 4  Q(√15)       46          none (exact: slice b4=0 has dim 0)      YES (48 primes; 46-cycle)      S_46 (proved)      YES (28 primes)               YES mod 32029; exact: see §6
 5  Q(√2)        265         6 pts (b4=0,q2=1,q3=0) + q_3-axis pt    YES (24 primes)                S_265 (proved)     YES (17 primes; bdry exact)   YES mod 32009
 6  Q(√21)       1548        none (mod p ⇒ none over A_6)              YES (8 primes; 3.6)            S_1548 (proved)    YES (5 primes)                not run
 8  Q(√3)        (52140)     6 pts in stratum q_3 = 1 (mod 32003)     not attempted                  —                  §5.3 (msolve at seal)         not run
```

## 3. The all-or-nothing lemma, its étale lift, and the auxiliary lemmas the instrument stands on

Throughout, `K = A_t`, `R = O_{K,𝔭}` for a prime 𝔭 of `O_K`, `k = O_K/𝔭` (= `F_p`: only split primes are used),
`K̂, R̂` the completions.  `A := R[b4,q]/I_2(N)` is the R-model of the cone (the exact minors are 𝔭-integral),
`M := A/(b4−1)A` the R-model of the chart, `M_K = O(Y_t)`, `M_k = O(Y_t ⊗ k)` (the mod-p chart scheme: the mod-p
generators are the reductions of the exact ones, §1).

**Lemma 3.1 (all-or-nothing).**  Let `f ∈ P_t[b3]` have coefficients in K and let `Z ⊂ Γ_t(K̄)` be one
`Gal(K̄/K)`-orbit.  Then `f(P, β(P)) = 0` for every `P ∈ Z` or for none, where `β(P) = −C_r(P)/B_r(P)` for any r
with `B_r(P) ≠ 0` (Gal-equivariant: `B_r, C_r` are K-rational and `−C_r/B_r` is r-independent on a rank-1 point).
*Proof.*  `σ(f(P, β(P))) = f(σP, β(σP))` and Gal is transitive on Z.  ∎  For `f = T_{t,2t−1}` (equivalently the
K-rational vector `(W_1..W_{t−1})`, which vanishes at P iff `T_{t,2t−1}(P, β(P)) = 0` when some `B_r(P) ≠ 0`, while
`W_r(P) = a_0 C_r(P)² ≠ 0` if all `B_r(P) = 0` — FITT):

> **Corollary 3.2.**  Clause (ii)_t holds on an orbit iff it holds at one of its points.  With `k_t` affine and
> `b_t` boundary orbits, clause (ii)_t is `k_t + b_t` non-vanishings, one point each.  For `k_t = 1` (proved here,
> t = 3..6) and the boundary done exactly (§5.3), clause (ii)_t is ONE non-vanishing at ONE affine point.

**Lemma 3.3 (flat model from the Hilbert function).**  If `dim P_k/I_2(N)_k = 1` (printed `CONE dim = 1`), then
(a) `dim P_K/I_2(N) = 1`; (b) A is R-torsion-free; (c) M is R-torsion-free.  *Proof.*  (a) `Proj A → Spec R` is
proper, so the special-fibre dimension is ≥ the generic one (EGA IV 13.1.5); the generic fibre is nonempty
since `ht I_2 ≤ t−2 < t−1`.  (b) In the CM rings `P_K, P_k` the height of `I_2(N)` is then the generic t−2, so
the Eagon–Northcott complex resolves over both fields (EN-CURVE, 17(rrrrr)) and `HF_K = HF_k` in every weight.
Each `A_d` is a f.g. R-module, `A_d ≅ R^{r_d} ⊕ T_d`, `r_d = HF_K(d)`, `HF_k(d) = r_d + dim T_d/𝔭T_d`, so `T_d = 0`.
(c) `b4` has weight 1, so `A/(b4−1) ≅ (A_{b4})_0`, torsion-free as a piece of a localisation of A.  ∎

**Lemma 3.4 (freeness).**  Let M be torsion-free over the DVR R with `n' = dim_K M_K < ∞`, `n = dim_k M/𝔭M`.
Then `n' ≥ n`, and `n' = n` ⇒ M is free of rank n.  *Proof.*  Lifts `m_i` of a k-basis of `M/𝔭M` are
K-independent (scale a relation to integral coefficients not all in 𝔭 and reduce), so `n' ≥ n`.  If `n' = n`,
write `m = Σ c_i m_i`, `c_i ∈ K`; if `v = min val(c_i) < 0` then `π^{−v}m ∈ 𝔭M` maps to 0 in `M/𝔭M` while its
coefficients are integral with a unit among them — contradiction with the independence of the `m̄_i`.  ∎
(Torsion-freeness is essential: `K ⊕ k` has `n' = n = 1`.)

**Lemma 3.5 (good reduction of the point polynomial).**  Assume `CONE dim = 1`, `n' = n`, and let `m̄ ∈ k[x]` be the
minimal polynomial of `q̄_2` on `M_k` with `deg m̄ = n`.  Then the exact point polynomial `f_t` (minimal polynomial
of `q_2` on `M_K`) is in `R[x]`, has degree n, and `f_t mod 𝔭 = m̄`.  *Proof.*  M is R-free of rank n (3.3, 3.4)
and `q_2`-stable; the minimal polynomial of an integral endomorphism over the integrally closed R lies in `R[x]`.
Reducing `f_t(q_2) = 0` gives `m̄ | f̄_t`, and `deg f̄_t ≤ n = deg m̄` forces equality.  ∎

**Corollary 3.6 (degree-pattern criterion).**  Under 3.5, if `m̄` is squarefree with irreducible factors of
degrees `d_1..d_s`, the Frobenius at 𝔭 acts on the n points with cycle type `(d_1..d_s)` (Dedekind), and every
monic factor of `f_t` over K is 𝔭-integral (Gauss) with degree a subset sum of `{d_j}`.  If the intersection over
several good primes of the proper subset sums is empty — e.g. if `m̄` is irreducible at ONE prime — `f_t` is
irreducible over `A_t`: the affine points of `Γ_t` are one Galois orbit.  ∎

**Lemma 3.7 (étale lift — the FALLACY-v2 statement).**  Assume `CONE dim = 1` (M flat, 3.3c) and let
`P̄ ∈ Y_t(k)` be a simple point (`vdim` of the fibre `J_1 + (q − P̄)` equal to 1; Jacobian rank t−2 printed).
Then `Spec M → Spec R` is étale at `P̄`, so `P̄` lifts uniquely to `P ∈ Y_t(R̂) ⊂ Γ_t(K̂)` (EGA IV 18.5.17), and
`g(P, β(P)) ≡ g(P̄, β̄) (mod 𝔭̂)` for every `g ∈ R[q, b3]`.  Hence `W_r(P̄) ≠ 0 ⇒ W_r(P) ≠ 0`: the non-vanishing is
at a genuine characteristic-0 point of `Γ_t`, the Hensel lift of `P̄`.  The lift needs flatness and simplicity;
it does NOT need `n' = n`.  ∎

**Lemma 3.8 (boundary bookkeeping).**  `d_Γ(t) = n' + Σ_{L ⊂ {b4=0}} e_L/g_L` (`e_L` multiplicity of the boundary
line L, `g_L` the gcd of the weights of its nonzero coordinates).  For the stratum chart `Y_{t,j} = Spec P/(I_2 +
(b4, q_{<j}, q_j − 1))`, `vdim Y_{t,j} = Σ_{L ⊂ stratum} (j/g_L) ℓ_L` with `ℓ_L = length(A_L/b4A_L) ≤ e_L` (the cone
`V(I_2, b4)` has no embedded component off the origin, by G_m-equivariance).  Hence the stratum contributes
`≥ vdim(Y_{t,j})/j` to `d_Γ − n'`.  ∎  (With 3.4's `n' ≥ n` this gives `n' = n` from the boundary alone, §5.3.)

## 4. Task (1): exact factorisation of the point polynomials — Γ_t ∩ {b4 ≠ 0} is ONE Galois orbit at t = 3, 4, 5, 6

### 4.1 What was computed, per t

Per prime ideal 𝔭 (`pattern_t{t}_mod_p{p}_b{b}.out`): mod-𝔭 rows, split and identities (§1); `CONE dim` of
`P_k/I_2(N)` (t ≤ 6); `SLICE dim` of `V(I_2, b4)`; the chart `J_1 = I_2 + (b4 − 1)`: `std`, `vdim`, `dim`; `finduni`,
the ordinary degree of every chart variable's minimal polynomial, squarefreeness of `m̄(q_2)`; `factorize(m̄)` and
its degree pattern (the Frobenius cycle type, 3.6); and, whenever `m̄` has a linear factor, the instrument of §5 at
the first rational point.  The exact chart `std` over `A_t` gave `vdim = 7, 46, 265` at t = 3, 4 (< 1 s) and 5
(426 s), equal to every modular count, so `n' = n` and 3.4–3.6 apply wherever the printed hypotheses hold.  Exact
`finduni` + `factorize` over `A_t` completed at t = 3 (`7^1`: irreducible over `Q(√3)`, reproducing my round's
`gammax_t3`); at t = 4, 5 the exact `finduni` did not finish inside the caps (§9) and irreducibility is proved by
3.6, which needs no exact point polynomial.

### 4.2 The verdict per t, with the hypotheses of 3.5 checked at every prime used

```text
 t  n_t   primes 𝔭 used (all split, both 𝔭|p)   hypotheses at every 𝔭            proper-subset-sum intersection   f_t over A_t
 3    7   49 (24 p × 2, + 32003)                cone dim 1, vdim 7, deg m̄ 7, sqf   ∅  (also: m̄ irreducible at 9 𝔭)   IRREDUCIBLE (exact + 3.6)
 4   46   48 (24 p × 2)                          cone dim 1, vdim 46, deg 46, sqf   ∅  (m̄ irreducible at 32323,32443,32579,32749)   IRREDUCIBLE (3.6)
 5  265   24 (12 p × 2)                          cone dim 1, vdim 265, deg 265, sqf ∅                                IRREDUCIBLE (3.6)
 6 1548    8 (8 p, branch 0)                     chart dim 0 + slice dim 0 (⇒ cone dim 1), vdim 1548, deg 1548, sqf   ∅ (was {292, 1256} after 4 𝔭)   IRREDUCIBLE (3.6)
```

At t = 6 the exact chart `vdim` was not computed; `n' = n = 1548` follows from Lemma 3.8 with an EMPTY boundary:
the slice `V(I_2, b4)` has dimension 0 mod p, hence (properness: a nonempty generic fibre would specialise to a
nonempty special fibre) the boundary of `Γ_6` over `A_6` is empty and `n' = d_Γ(6) = 1548`.  The same argument
gives `n' = 46 = d_Γ(4)` at t = 4 independently of the exact `std` (slice dim 0 at every prime).

So `k_3 = k_4 = k_5 = k_6 = 1`: **the affine points of Γ_t form a single Galois orbit over A_t for t = 3, 4, 5, 6**.
This closes `OPEN[K16-GAMMA-IRREDUCIBLE]` for t ≤ 6 and answers the charged "is it irreducible?" with YES.

### 4.3 Frobenius cycle types and the Galois groups (proved, not conjectured)

The cycle types are the printed degree patterns (full lists: `pattern_*.out`, tabulated in `frobenius_tables.txt`).
Excerpts:

```text
 t=3 (n=7):   7 (×9), 1+2+4 (×7), 2+2+3 (×7), 1+1+2+3 (×5), 1+1+5 (×4), 1+6 (×4), 2+5 (×3), 1+3+3 (×3), 3+4 (×2), ...
 t=4 (n=46):  46 (×4), 1+45 (×4), 1+1+3+10+31 (×2), 13+33, 18+28, 5+41, 15+31, 21+25, 22+24, 1+4+41, 1+1+44, ...
 t=5 (n=265): 1+3+261, 2+3+3+257, 1+2+2+12+248, 1+4+7+9+244, 4+14+42+205, 9+14+18+21+203, ...
 t=6 (n=1548): 1+2+4+7+108+180+308+336+602, 1+2+2+47+107+120+137+1132, 1+1+1+2+524+1019, 9+26+35+114+292+1072, ...
```

*Consequences (Jordan).*  `G_t := Gal(f_t/A_t)` is transitive (4.2).  A Frobenius power is a pure c-cycle whenever
c occurs once in a cycle type and divides no other part; a transitive group containing a prime cycle of length
c > n/2 is primitive, and a primitive group containing a prime cycle of length c ≤ n − 3 contains `A_n` (Jordan);
an odd cycle type then gives `S_n`.
- t = 3: degree 7 is prime, so `G_3` is primitive; `(2,5)^5` is a transposition ⇒ **`G_3 = S_7`**.
- t = 4: prime cycles 29, 31, 41 (23 < c ≤ 43) ⇒ `G_4 ⊇ A_46`; `46` is an odd cycle ⇒ **`G_4 = S_46`**.
- t = 5: prime cycles 137, 139, 149, 181, 257 (132 < c ≤ 262) ⇒ `G_5 ⊇ A_265`; the type `1+3+261` is odd ⇒ **`G_5 = S_265`**.
- t = 6: the prime cycle 1019 (774 < 1019 ≤ 1545, from the type `1+1+1+2+524+1019` at p = 32633) ⇒ `G_6 ⊇ A_1548`; odd types present ⇒ **`G_6 = S_1548`**.

The Galois groups are FULL SYMMETRIC: the points of `Γ_t` have no hidden symmetry over `A_t` — the generic
(uniform-position) behaviour of a 0-dimensional determinantal scheme, and the datum any uniform argument for (I)
would have to reproduce (§7).

## 5. Tasks (2)–(3): the one-evaluation instrument, run at t = 3, 4, 5, 6 (and t = 8, §5.3), and the boundary

### 5.1 The instrument (what one modular evaluation proves, by 3.1 + 3.7)

At a split prime 𝔭 with `CONE dim = 1` (flatness, 3.3) take a root `v` of a linear factor of `m̄(q_2)`; the
fibre `J_1 + (q_2 − v)` has `vdim = 1` (printed), so it is one simple `F_p`-point `P̄ = (1, v, q̄_3, ..)` (the
Jacobian of the minors in the chart variables has rank t−2 at `P̄`, printed as `JACRANK_FREE`); all minors
vanish at `P̄` (`MINORS_ZERO=1`); `β̄ = −C_r(P̄)/B_r(P̄)` is computed from the first r with `B_r(P̄) ≠ 0` and
checked against every other r (`KERNEL_CONSISTENT=1`); `T_{t,2t−1}(P̄, β̄) = a_0 β̄² + b_0(P̄) β̄ + c_0(P̄)` and
all `W_r(P̄)` are printed, together with the FITT identity `W_r(P̄) = B_r(P̄)² T_{t,2t−1}(P̄, β̄)` (`FITTcheck=1`).
By 3.7, `P̄` lifts to `P ∈ Γ_t(K̂)` with `W_r(P) ≡ W_r(P̄) (mod 𝔭̂)`; by 3.1, `W(P) ≠ 0` propagates to the whole
`Gal(K̄/K)`-orbit of `P`; by §4 that orbit is all of `Γ_t ∩ {b4 ≠ 0}` for t ≤ 6.  **The lift is stated, not
assumed (FALLACY-v2): the char-0 point is the Hensel lift of a simple point on the flat model; no modular
non-vanishing is promoted without it.**

### 5.2 Results

```text
 t  #𝔭 with a rational point / #𝔭 tried   W ≠ 0 at the lift (all of them?)   example (p, b): P̄ = (b4, q_2, ..), β̄, T_top(P̄,β̄)
 3  28 / 49                                 28 / 28  YES                        (32183, 0): (1, 12012), β̄ = ·, T_top = −642 ≠ 0
 4  28 / 48                                 28 / 28  YES                        (32749, 0): (1, −5944, −5832), T_top = −11 ≠ 0;  (32203,0): T_top = 86
 5  17 / 24                                 17 / 17  YES                        (32479, 0): (1, 13130, −6481, 8290), T_top = 6541 ≠ 0
 6   5 / 8                                   5 / 5   YES                        (32003, 0): (1, 4339, 9016, −15982, −6895), β̄ = 12955, T_top = 13229 ≠ 0
```

(The fraction of primes with a rational point, 0.57–0.71, is the fixed-point probability in `S_n`, consistent with
4.3.)  Every rational simple point at every prime gave `W ≠ 0`; one per t suffices.  Combined with §4:

> **Clause (ii)_t on Γ_t ∩ {b4 ≠ 0} holds for t = 3, 4, 5, 6**, each by ONE modular evaluation + the étale lift +
> one Galois orbit.  For t = 3, 4, 5 this re-proves the charged exact/promoted clause (ii) by a different route
> (no number-field `std`, no `radical`); at t = 6 it replaces the promoted `dim(F_6) = 0` by an argument that
> needs only a 3 s modular `std`, a 150 s `finduni`, and one evaluation.

### 5.3 Boundary orbits (b4 = 0), exact

The boundary of `Γ_t` is the cone `V(I_2, b4)`, stratified by the first nonzero coordinate `q_j` (chart `q_j = 1`).
Exact over `A_t` (`boundary_t{3,5}_exact.out`) and mod p (t = 4, 6, 8):

```text
 t  stratum j=2 (b4=0,q2=1)                         stratum j=3 (b4=q2=0,q3=1)    higher strata   (stratum + (W_1..W_{t−1})) vdim
 3  1 point, the q_2-axis (rational)                —                             —               0  ⇒ W ≠ 0 there (exact)
 4  ∅ (slice dim 0, mod 32029)                       ∅                             ∅               —
 5  6 points with q_3 = 0; q_4-minpoly of degree 6   1 point, the q_3-axis (q_4=0)  ∅               0 and 0  ⇒ W ≠ 0 at all 7 points (exact)
    IRREDUCIBLE over Q(√2) ⇒ ONE orbit                (rational)
 6  ∅ (slice dim 0, mod 32003 and 32713/17/19)       ∅                             ∅               —
 8  ∅ (mod 32003)                                    6 points (mod 32003)          ∅               0 (mod p) ⇒ W ≠ 0 at all 6 (modular; lift as in 3.7 needs flatness, see 5.4)
```

At t = 5 the six stratum-2 points have `q_3 = 0` (the μ_2 acting on the chart fixes them, so each is a
weighted point with `g_L = 2`), the `q_4`-minimal polynomial is irreducible of degree 6 over `A_5` (printed in
`boundary_t5_exact.out`), i.e. they are ONE Galois orbit; with the rational axis point, `b_5 = 2`.  The
bookkeeping of Lemma 3.8 then reads `265 + 6/2 + 1/3 = 805/3 = d_Γ(5)` exactly over `A_5`, a second proof of
`n' = 265` independent of the exact chart `std`.  At t = 3: `7 + 1/2 = 15/2`.  W-nonvanishing on the boundary
was tested as `vdim(stratum ideal + (W)) = 0`, i.e. at EVERY geometric boundary point at once (Nullstellensatz),
exactly over `A_t` at t = 3, 5 — so clause (ii) on the boundary needs no orbit argument at all at these t.

### 5.4 Consequence for (V0) at fixed t

For t = 3, 4, 5, 6: clause (i) is charged (exact t ≤ 5, promoted t = 6..8, B-hsop), clause (ii) on the affine
orbit is §5.2, on the boundary §5.3 (t = 6: empty).  Hence `(V0)-tail_t` holds for t = 3..6 by the new route.
No new index is added to the banked `(V0)` list (t ≤ 7 was banked); what is new is the COST: at t = 6 the
whole certificate is three modular jobs of ≤ 3 min and no number-field or radical computation.

## 6. Task (5): the liaison cross-check — `(G_1..G_{t−1}) : T_{t,2t−1} = (G)`

`S_t/(G)` is the complete-intersection curve `V(G) = (b3-axis, multiplicity C(2t,t−1)) ∪ (lift of Γ_t)`
(17(rrrrr) §5.3); it is Cohen–Macaulay of dimension 1, so its associated primes are its minimal primes and
`T_{t,2t−1}` is a nonzerodivisor on it iff it vanishes identically on no component, i.e. iff clause (ii) holds
at every point of Γ_t (affine AND boundary) and `a_0 ≠ 0` on the axis.  So `(G) : T_top = (G)` is exactly
clause (ii) in its ideal-theoretic form, tested on the whole curve at once and independently of §4–5.

```text
 t  field               (G): dim, mult      (G):T_top  ==  (G)?    control (G):G_1 = (1)?   control (G):b4 == (G)?  (expected NO: the axis lies in b4=0)
 3  exact A_3           1, 45               YES (10 gens, all reduce to 0)   YES                      NO   ✓
 3  GF(32003)           1, 45               YES                    YES                      NO   ✓
 4  GF(32029)           1, 286              YES (53 gens)          YES                      NO   ✓
 4  exact A_4           1, 286 (std 55 s)   see §9 (quotient running at seal)
 5  GF(32009)           1, 1820             YES (262 gens, 4 s)    YES                      NO   ✓
```

`mult(G) = 45, 286, 1820 = C(3t+1,t−1)` is the CI degree (LENGTH-SPLIT), as it must be.  The colon equality at
t = 3 (exact), 4, 5 (mod p) is the arithmetically-CM cross-check the card asked for and agrees with §5 at every
index.  A modular colon equality is evidence only: a nonzero element of `((G):T_top)/(G)` over K has nonzero
reduction at all but finitely many 𝔭, which could include the one tested; the exact t = 3 run and §5 carry the
char-0 weight.

## 7. Task (4): the uniform problem (I) — is Γ_t ∩ {b4 ≠ 0} one orbit over A_t for ALL t?  Typed OPEN, with the structure

**What is proved.**  `k_t = 1` for t = 3, 4, 5, 6 with `Gal(f_t/A_t) = S_{n_t}` (t ≤ 5; t = 6: `⊇ A_1548`, and
`S_1548` since odd cycle types occur).  The boundary orbits are `b_3 = 1`, `b_4 = 0`, `b_5 = 2`, `b_6 = 0`.

**What the determinantal structure gives, and what it does not.**  `Γ_t` is the rank-≤1 locus of a `(t−1)×2`
matrix of weighted forms, cut out by the `C(t−1,2)` minors; the EN complex makes `P_t/I_2(N)` CM of dimension 1 with
Hilbert series determined by the weights alone, hence `d_Γ(t)` and `n_t = d_Γ(t) − (boundary)` are uniform.
Irreducibility, however, is NOT a consequence of the resolution: `I_2(N)` is generically reduced with `d_Γ(t)`
distinct points, and which field of definition those points have is a property of the specific entries `B_r,
C_r`, not of the format.  Three uniform routes were examined:

1. *Bertini/monodromy in a family.*  If `(B_r, C_r)` were a general member of the linear system of pairs of forms
   of weights `(t+1+r, 2t+2+r)`, the monodromy of the `d_Γ` points would be the full symmetric group (uniform-position
   for a general 0-dimensional determinantal scheme: the incidence variety over the parameter space is irreducible
   and the discriminant has codimension one), which is exactly what §4.3 measures.  But K16 is ONE point of that
   parameter space for each t, and Bertini says nothing about a specific member.  The measured `S_n` shows that
   K16's forms are "generic enough" at t ≤ 6; there is no theorem that they stay off the (codimension-one)
   locus of imprimitive/reducible monodromy for all t.  This is the same discriminant-avoidance typing as
   (V0)-tail itself (my card §1.2): (I) RELOCATES the genericity, it does not remove it.
2. *A resultant/elimination argument in t.*  At t = 3, `f_3` is the weight-14 part of the single minor
   `B_1 C_2 − B_2 C_1`, a binary form; irreducibility over `Q(√3)` was decided by factoring.  For t ≥ 4 the point
   polynomial is an eliminant of `C(t−1,2)` minors whose coefficients are the spine scalars (no closed form in t,
   17(rrrrr) §7, brcr CORRECTION), so no uniform Eisenstein/Newton-polygon criterion can even be written down;
   the natural candidate prime `p = 4t+1` (K16 p-adic regularity, banked) is only prime for some t.
3. *Chebotarev.*  The cycle-type statistics at t = 3..6 are those of `S_n` and determine the group — one t at a time;
   there is no t-uniform Frobenius.

**What a proof of (I) for all t would need**: a uniform *transitivity witness*, e.g. a t-indexed prime `𝔭_t` at
which `m̄` is a full `n_t`-cycle (at t = 4: 32323, 32443, 32579, 32749; at t = 3: nine of 49); one such prime is a
complete proof by 3.6, but full cycles have frequency `1/n` in `S_n` and nothing suggests a structural prime.
Typed `OPEN[K16-GAMMA-IRREDUCIBLE]` for t ≥ 7 with this quantity.

**Is (I) even necessary?**  No — and this is the useful observation.  Corollary 3.2 needs only `k_t + b_t`
evaluations, one per orbit; the instrument does not need to KNOW the orbits: it needs, for each orbit, one simple
point mod some prime.  Equivalently, the fixed-t certificate of clause (ii) is: a set of simple `F_p`-points of
`Γ_t` (over one or several primes) whose Hensel lifts meet every Galois orbit — which is exactly what
`vdim(J_1 + (W)) = 0` mod p certifies in one shot when combined with flatness (every geometric point of the
mod-p chart has `W ≠ 0`; every K̄-point specialises to one of them; by 3.7 applied in reverse — a K̄-point of the
flat proper model specialises to a k̄-point of the special fibre, and `W(P) = 0` would force `W(P̄) = 0`).  So

> **Proposition 7.1 (modular clause (ii) without irreducibility).**  If `CONE dim = 1` mod 𝔭 (flat model) and
> `V(I_2 + (W_1..W_{t−1})) = {0}` in `P_k` (a positive-weight cone statement, promotable by the banked properness
> lemma), then clause (ii)_t holds over `A_t`.  *Proof.*  By 3.3 the model `A` is flat; `Proj A → Spec R` is proper,
> so every `K̄`-point `P` of `Γ_t` extends to an `R̄`-point and specialises to a `k̄`-point `P̄` of `Γ_t ⊗ k`;
> `W_r(P̄) = W_r(P) mod 𝔭̄`; if all `W_r(P) = 0` then all `W_r(P̄) = 0`, contradicting the hypothesis.  ∎

This is the charged/banked promotion route (rank lane §8) re-derived; it needs no orbit count.  What the Galois
mechanism adds is not logical strength but COST and STRUCTURE: it turns `d_Γ(t)` non-vanishings into `k_t + b_t`
non-vanishings and tells one that the `d_Γ(t)` points are a single algebraic object (an `S_n`-extension of `A_t`).
The honest all-t statement is therefore: `(V0)-tail_t ⟸ (i)_t ∧ [one simple point per orbit with W ≠ 0]`, and
uniformity fails at the same place it always did — there is no t-indexed point of `Γ_t` with a closed-form
`T_top(P_t, β_t)`.  Problem (II) is thus the binding one, and it is unchanged by this lane.

## 8. FALLACY-v2 check

No exit-price assertion is made; no `charge_basis` line is due.  **Modular → char 0 (the v2 item named in the
card):** every characteristic-0 statement in §4–5 passes through Lemmas 3.3–3.7: the flat model (`CONE dim = 1`
printed at the prime used), the freeness/good-reduction step (`n' = n` from the exact chart `std` at t = 3, 4, 5
and from the empty boundary + EN degree at t = 4, 6; `deg m̄ = n` and squarefreeness printed), and the étale lift
of a simple point (`vdim` of the fibre = 1, Jacobian rank printed).  A modular non-vanishing is never promoted
without the lift; the t = 8 evaluation (§5.3/§9) is typed by which of these hypotheses were verified.
**Floor/attainment:** `d_Γ(t)`, `C(2t,t−1)`, `C(3t+1,t−1)` are used only as EN/CI values of quotients whose
dimension was measured or proved (3.3a); Lemma 3.8 is a lower bound closed by `n' ≥ n` (3.4).  **`sat()`, raw
remainder degree:** none; memberships are `reduce` against a reduced `std`; the colon is `quotient` + `reduce`
with positive and negative controls (§6).
**Variable/ring map:** declared in §1–2; generator order `b4, q2_0, .., q{t−1}_0(, b3)`, weights, coefficient
field `(0,yy)` with `minpoly = H_t` or `GF(p)` with `yy` a root; image checks are the split identities, the
weights, the ELIMINANT certificate, `A0VALUE ≠ 0`, `MINORS_ZERO`, `FITTcheck`, `KERNEL_CONSISTENT` at every point.
msolve's parametrization was validated against the Singular point at t = 6 (same `F_p`-point, coordinates and
β) before being used at t = 8.  **Prime label/derivative:** primes are field characteristics (𝔭 | p in `A_t`);
no derivative notation.  **Galois statements:** cycle types are Dedekind's theorem under 3.5 (squarefree
reduction, integral point polynomial), Jordan's theorem is quoted with its hypotheses (prime cycle of length
≤ n−3 in a primitive group; primitivity from a prime cycle of length > n/2 in a transitive group), transitivity
is the proved irreducibility, parity from the printed types.  Nothing beyond t = 6 is claimed for (I); the t ≥ 7
statement is typed OPEN with a quantity (§7, §11).

## 9. Computation record (`box/k16galois-20260905/`)

```text
manifest.sha256, manifest.check.log         custody (awk-generated; sha256sum -c: 10/10 OK)
gen.py                                      the emitter (prefix from the frozen rows; jobs pattern | exactchart | boundary | colon | msolve | verifypoint)
run.sh, deploy.sh                           foreground runner (stdbuf -oL, timeout, .time), worker deployment
primes.txt, sweep_t{3,4}.sh, w18_jobs.txt, w166_jobs{,2}.txt, misc_desk.sh    prime lists and batch drivers
pattern_t{3,4}_mod_p*_b*.{sing,out,err,time}         desk sweeps (49 + 48 prime ideals; < 1 s each)
w18/pattern_t5_mod_p*_b*.*                   t = 5 sweep, 24 prime ideals (0–3 s each)
w166/pattern_t6_mod_p*_b0.*, pattern_t6_mod_p32003_b0.*   t = 6, 8 completed primes (≈ 150 s each: std 3 s, finduni ≈ 145 s, factorize ≈ 1 s)
minpoly_pattern_*_q2_0.txt                   the modular point polynomials m̄ (written by every pattern job)
exactchart_t3_exact.*                        exact chart std, finduni, factorize over A_3 (< 1 s): 7^1
exactchart_t4_exact.*                        exact chart std over A_4 (< 1 s, vdim 46); finduni not finished (see below)
w7/exactchart_t5_exact.*                     exact chart std over A_5: vdim 265 in 426 s; finduni not finished (see below)
boundary_t{3,5}_exact.*, boundary_t{4,6}_mod_*.*, w18/boundary_t8_mod_p32003_b0.*   boundary strata (exact at t = 3, 5; t = 8 re-run on W18, 179 s), with (stratum + (W)) vdim
colon_t3_exact.*, colon_t{3,4,5}_mod_*.*     (G):T_top = (G) with controls (t = 3 exact < 1 s; t = 5 mod p 5 s)
colon_t4_exact.* (W166, lost; rerun on W18)   exact t = 4 colon: std(G) 55 s, quotient not finished when W166 went down
msolve_t6_mod_p32003_b0_ci.{sing,ms}, w254/msolve_t6_param.txt, msolve_point.py    msolve calibration at t = 6 (1.5 s), parser validated
msolve_t8_mod_p32003_b0_ci.{sing,ms} (79 MB), w28/msolve_t8.log   t = 8 CI system mod 32003, msolve F4 (see §5.3 / OPEN)
verifypoint_t6_mod_p32003_b0.*               the verify job on the t = 6 point (local vdim 1, all checks 1)
analyze_patterns.py, frobenius_tables.txt    subset-sum intersection, Galois bookkeeping, the full cycle-type / instrument tables
sections/                                    the report sections as written (append-only), assembled into the report
```

Wall clock (single core unless stated): modular jobs at t ≤ 5 are seconds; t = 6 pattern 143–163 s; exact chart
`std` 0 s (t = 3, 4), 426 s (t = 5); t = 8 prefix + export 59 s, t = 8 boundary strata 190 s.  Not finished:
exact `finduni` over `A_4` (desk) and `A_5` (W7) — number-field linear algebra, > 40 min at seal although the
exact std before it took 0 s / 426 s; `nfmodStd` was killed twice (it ignores `--cpus` and forked 17–30
processes, over the core budget); the exact t = 4 `quotient` and the Singular t = 8 chart `std` were lost when
workers .166 and .254 became unreachable at ≈ 13:16Z and were re-launched on W18 (status at seal: §5.3, §6).  No
unfinished item carries a claim.

## 10. What this changes (for the synthesis), in three lines

1. **17(tttttt) is confirmed and strengthened**: `Γ_t ∩ {b4 ≠ 0}` is one orbit with full symmetric Galois group
   at t = 3..6; the "one scalar per simple point" of the rank lane is "one scalar per t" at these indices.
2. **The instrument is real**: clause (ii) at fixed t costs one modular `std` + one `finduni` + one evaluation
   (t = 6: 3 min).  At t = 8 the wall is the 52140-point elimination (msolve F4/FGLM), not a number-field std; a
   fleet-hour with ≥ 16 threads should land it — the CI formulation (7 forms in q_2..q_7, b3) is the right one.
3. **The all-t residual is problem (II), not (I)**: Prop. 7.1 makes irreducibility logically unnecessary for
   clause (ii); no uniform point of `Γ_t` is known, and the `S_n` Galois data say it cannot come from a symmetry —
   it must come from the Abel/formal-solution side (Astra's non-truncating (F3) solutions).  Disposition: STOP
   fixed-t (V0) work below t = 8; finish the t = 8 one-point test as a fleet job; route the uniform effort to (II).

## 11. OPENs

OPENS RAISED

- `OPEN[K16-GAMMA-IRREDUCIBLE]` (re-scoped) — for t ≥ 7, is `Γ_t ∩ {b4 ≠ 0}` one Galois orbit over `A_t`?
  QUANTITY: `k_t = 1` is PROVED for t = 3, 4, 5, 6 (this lane; `Gal = S_{n_t}` for t ≤ 6); the first undecided
  index is t = 7 (`n_7 = 35805/4 − boundary`), decidable by the subset-sum criterion 3.6 from ≤ 20 modular `finduni` jobs of the t = 7 chart
  (`finduni` is cubic in the point count: 150 s at n = 1548 extrapolates to ≈ 8 h per prime at n ≈ 8950, a
  fleet-day, not a desk job); a uniform proof needs a t-indexed prime with an
  irreducible reduction and none is in sight (§7).
- `OPEN[K16-ONE-POINT-T8]` — clause (ii)_8 by the instrument.  QUANTITY: the number of verified simple
  `F_p`-points of `Γ_8 ∩ {b4 ≠ 0}` with `W ≠ 0` is `= 0` today and `≥ 1` closes the affine part (52140 points;
  the msolve F4 run at 4 threads on a shared worker was at degree 14 of the CI system, 45739 × 81237, at seal);
  with the point the check is a 1 s `verifypoint` job; the flat-model hypothesis at t = 8 (`CONE dim = 1`,
  i.e. chart dim 0 + slice dim 1) is the other printed item still owed.
- `OPEN[K16-UNIFORM-POINT]` (= problem (II), unchanged) — a t-indexed point `P_t ∈ Γ_t` with a closed-form
  `T_{t,2t−1}(P_t, β_t)`; QUANTITY: `#{t : a formal/closed-form point of Γ_t is known} = 0`.  This is the binding
  uniform gap; Proposition 7.1 shows problem (I) is not logically necessary for it.

OPENS ANSWERED HERE

- `OPEN[K16-GAMMA-IRREDUCIBLE]` for t = 4, 5, 6: YES (§4); `OPEN[K16-ONE-POINT-CERTIFICATE]` for t = 3..6: the
  instrument runs and certifies clause (ii) at each (§5); `OPEN[K16-GAMMA-REDUCED-T6]`: YES, `Y_6` is reduced with
  1548 simple points (`deg m̄ = vdim = 1548`, squarefree, at 8 primes).

## 12. Collision scan (`ops/open_collision.py --root .`, filtered of this lane's own files and the same-round ideation files)

Output: `box/k16galois-20260905/collision_scan.filtered.txt` (status CANDIDATES).  Dispositions:
- `OPEN[K16-GAMMA-IRREDUCIBLE]`: one hit, 17(tttttt) — the synthesis that charged this lane (KNOWN; it states
  the question, this lane answers it for t ≤ 6 and re-scopes it to t ≥ 7).
- `OPEN[K16-ONE-POINT-T8]`: NONE.
- `OPEN[K16-UNIFORM-POINT]`: lexical hits on the K16 deltas 17(xx), (ooo), (iiii)–(llll), (qqqqq) FITT/EN-CURVE,
  (uuuuu)–(aaaaaa), (nnnnnn)–(pppppp), (tttttt), the `k16-nzd-gamma-gpt55` event and several ideation files — all
  KNOWN context on the uniform (V0)/(8.1) problem; none exhibits a t-indexed point of Γ_t or a closed-form
  `T_top` value, none closes the OPEN.

<!-- BODY-END -->
