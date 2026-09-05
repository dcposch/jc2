# K16 at t = 8: the affine half of Proposition 7.1 is empty — orbit-free clause
# (ii)_8, and (T) at t = 8.  The FGLM landed too, and rules the one-point route
# out at this prime: Y_8 (x) F_32003 has no F_p-rational point.

```text
lane      k16-t8-fglm-harvest-opus5-20260905
basis     4e9fd0969be986d844958eb7977d3d8bdfdcb904
charged   k16-t8-onepoint-grok46-20260905.md, k16-gamma-galois-fable5-20260905.md,
          ops/fleet/fleet.sh, ops/fleet/dispatch.sh, FALLACY-v2.md   (5/5 sha256 OK)
```

## 0. Verdict

```text
REQUESTED  harvest the t=8 FGLM, extract an affine F_p-point of Gamma_8, verify it,
           and decide (T) at t = 8 (charged report Sec.10 steps (1)-(4)).
VERDICT    PROVED-HERE.  Theorem (T) holds at t = 8.
           Route: Proposition 7.1 (orbit-free), NOT the one-point instrument.
PROVED     (1) msolve F4 of I_2 + (W_1..W_7) + (b4-1) over F_32003, 30 threads,
               8520.47 s elapsed / 142866.24 s cpu, deepest degree 19:  reduced
               Groebner basis = [1], "No solution".  So V(I_2+(W)) cap {b4=1} is
               EMPTY -- the affine half of Prop 7.1, the one item the charged
               lane could not finish (Sec.4, Sec.8).
           (2) With the charged boundary half (stratum j=3 + (W): vdim=0 dim=-1;
               j=2 and j=4..7 empty) and G_m-homogeneity:  V(I_2+(W)) = {0} in P_k.
               With CONE dim = 1 (charged Sec.5, from the CI quotient dim 52138),
               Prop. 7.1 gives clause (ii)_8 over A_8 = Q(sqrt 3).
               With the banked clause (i)_8 (B-hsop, 17(rrrrr)):
                  (i)_8 ^ (ii)_8 => (V0)-tail_8 => (V0)_8 => (8.1)_8 => (T)_8.
           (3) The charged FGLM FINISHED at 15:56Z (7739.98 s elapsed / 104020.95 s
               cpu): eliminating polynomial of b3, degree 52138 = n, squarefree
               (so the mod-p chart is REDUCED, 52138 distinct points).
NEGATIVE   (4) w has NO root in F_32003 (brute force AND gcd(x^p-x,w) = 1), so
               Y_8 (x) F_32003 has no F_p-rational point at all: charged steps
               (2)-(3) are not slow, they are EMPTY at this prime.
           (5) Frobenius cycle type at p=32003 contains 7, 17, 20 (each factor
               verified irreducible and dividing w; RABIN_FULL False), so w is
               reducible and Cor. 3.6 CANNOT give k_8 = 1 here.  A second good
               prime would be needed.  k_8 = 1 stays OPEN for t >= 7.
CAVEATS    single prime p = 32003, branch yy = 11288 (good reduction charged);
           clause (i)_8 is cited and carries the rank lane's DETECTOR-ONLY
           p-integrality caveat at t = 8, which (T)_8 inherits;  and the (H2b)
           computation is ONE engine -- the Singular replication timed out at
           11000 s without printing (Sec.8).  Controls: Sec.5.
CONSEQUENCE the proved range of the K = 16 ray extends from t <= 7 to t <= 8; the
           all-t residual is unchanged (problem (II), not (I)).
NOTIFY     warranted: (V0)_8 is a new index on the banked (V0) list.
```

## 1. Custody

The receipt `…-harvest-opus5-20260905.run.v2` was parsed with `awk -F=`, pairing
`charged_input_<i>_sha256=` with `_basename=` into `/tmp/manifest.sha256`;
`sha256sum -c` printed **5/5 `OK`**.  No digest was retyped; all five inputs were
read before any driver ran.  New drivers and data live only in
`box/k16t8-20260905/`; no ledger file was edited, no `jc2-lean`, no `ideation-*`.

Polynomial provenance is unchanged: every driver here is the *charged* `gen.py`
prefix, cut verbatim at the `evalpoint` terminator `  return(wnz);\n}` and given a
new payload.  Every run reprints `RING S: b4,q2_0,…,q7_0,b3 wp 1,2,3,4,5,6,7,9`,
`A0VALUE: 7970`, `PREFIX_S_OK`, `PREFIX_P_OK ngens(I2)=21` and the b3-split /
weight / G-identity / ELIMINANT self-checks, and aborts on `FAIL`.  None occurred;
`.err` streams were empty.

## 2. Why the certificate does not go through the FGLM

The charged report §10 lists four steps.  Steps (1)–(3) (FGLM → parametrisation →
one affine point) buy clause (ii)_8 only on **one Galois orbit**, because `k_8 = 1`
is `OPEN[K16-GAMMA-IRREDUCIBLE]` for t ≥ 7 (FALLACY-v2: `k_8` must not be inferred
from t ≤ 6).  Step (4) has a second, orbit-free branch, and that branch is
*cheaper* than the FGLM:

> **Proposition 7.1** (Galois report §7, charged).  If `CONE dim = 1` mod 𝔭 and
> `V(I_2 + (W_1,…,W_{t−1})) = {0}` in `P_k`, then clause (ii)_t holds over `A_t`.

Its two hypotheses at t = 8, p = 32003, branch 0 (`yy = 11288`):

```text
(H1) CONE dim = 1          BANKED  (charged §5: the CI chart subst(G,b4=1) has
                                    quotient dimension 52138, finite and nonzero,
                                    I_2 homogeneous of positive weights ⇒ the cone
                                    V(I_2) is a curve; Lemma 3.3)
(H2) V(I_2+(W)) = {0}      splits G_m-equivariantly (all weights positive, w(b4)=1):
     (H2a) boundary half  V(I_2+(W)) ∩ {b4 = 0} = {0}          — CHARGED, see §3
     (H2b) affine half    V(I_2+(W)) ∩ {b4 = 1} = ∅            — THIS LANE, §4
```

`(H2a) ∧ (H2b) ⇒ (H2)`: `I_2` and every `W_r` is weighted-homogeneous
(`w(minor_{rs}) = 27+r+s ∈ [30,40]`, `w(W_r) = 36+2r ∈ [38,50]`, printed by the
exporter, §4), so `V(I_2+(W))` is `G_m`-stable and a `k̄`-point with `b4 = c ≠ 0`
scales by `λ = c^{-1}` to the `{b4 = 1}` slice.  No generator has a constant term,
so `0 ∈ V`; hence `V = {0}` exactly.

## 3. The boundary half (H2a), charged, re-read

`V(I_2, b4)` is stratified by the first nonzero coordinate `q_j`, `j = 2..7`
(chart `q_j = 1`; over `k̄` the normalising `j`-th root exists).  At t = 8,
p = 32003 the charged boundary job (worker .18, 179 s) printed `j = 2: ∅`,
`j = 3: vdim = 6, dim = 0` (six geometric points), `j = 4..7: ∅`; this box's
`listboundary_t8_mod_p32003_b0.out` (wall 1 s) re-ran the j = 3 stratum:

```text
LISTBOUNDARY stratum j=3: vdim=6 dim=0 gbsize=7
LISTBOUNDARY stratum j=3 + (W): vdim=0 dim=-1        <-- unit ideal: EMPTY
```

`dim = −1` is the Nullstellensatz statement at all six geometric points at once —
not one point, not one orbit.  So `V(I_2+(W)) ∩ {b4=0} = {0}` mod 32003.  (The
single `F_p`-point `P̄_bd = (0,0,1,0,0,7416,0)` with `W_3 = −6850`, `W_6 = 12365`,
`JACRANK_FREE = 4`, `KERNEL_CONSISTENT = 1`, `T_top = 4235 ≠ 0` is a *witness*
inside that stratum, not the certificate; the certificate is `dim = −1`.)

## 4. The affine half (H2b): what was built and why the charged attempt died

The charged `affinew` job did **not** crash: its `halt 1` was a watchdog SIGTERM at
exactly 5400 s (created 13:50:37, `halt 1` 15:20:37, empty `.err`), and `conew` on
.28 died identically at exactly 7200 s.  Both were single-threaded Singular `std`.
The diagnosis is *budget*, not a bug — so the ideal was handed to a parallel F4.

**The ring map, declared.**  Ring `P = (ZZ/32003)[b4,q2_0,…,q7_0]`, order
`wp(1,2,3,4,5,6,7)` (printed by the driver).  `I_2` = the 21 two-by-two minors of
the 7×2 matrix `N = (C_r, B_r)_{r=1..7}`; `Ws = (W_1,…,W_7)`,
`W_r = a_0 C_r² − b_0 B_r C_r + c_0 B_r²` (the charged FITT eliminant, verified in
the prefix by the `ELIMINANT` identity).  The map is

```text
  φ : P ⟶ F_32003[q2,…,q7],   b4 ↦ 1,  q_j_0 ↦ q_j   (j = 2..7)
```

i.e. `P/(b4−1) ≅ F_32003[q2..q7]`, the affine chart.  Implemented as
`subst(I2+Ws, b4, 1)` in Singular, then a pure textual rename `q{j}_0 → q{j}`
in python.  Image checks printed / asserted:

```text
AFFINEWMS2 ngens=28 (21 minors + 7 W_r);  B4_ELIMINATED=1  ZERO_GENS=0  CONSTANT_GENS=0
gen weighted degrees 30..40 (minors = 27+r+s) and 38..50 (W_r = 36+2r); terms 1816..18106
IMAGE_CHECK residual '_' / 'b4' / 'b3' in generators: []   (python)
IMAGE_CHECK variable names present: ['q2','q3','q4','q5','q6','q7']
```

Drivers: `affinewms2_t8_mod_p32003_b0.sing` (raw export; a first attempt renaming
inside Singular was abandoned — the `find`/substring loop is quadratic), and the
resulting msolve system

```text
box/k16t8-20260905/msolve_t8_affinew_p32003_b0.ms   3111128 bytes
sha256 d6401d43c62af47b17b67a1fd91221e31b9bbfbb775f092bda1d839057749e6c
first line  q2,q3,q4,q5,q6,q7      second line  32003      28 polynomials
```

The verdict instrument is msolve `-g 2` (reduced grevlex GB, no FGLM): the GB is
`[1]` iff the ideal is the unit ideal iff the variety is empty over `k̄` — Singular's
`vdim = 0`, `dim = −1`, exactly the quantity charged §10 step (4) asks for.
Emptiness is order-independent, so exporting to plain grevlex loses nothing.

## 5. Controls (positive and negative, same pipeline, t = 6)

The identical emitter → rename → `msolve -g 2` pipeline was run at t = 6 from the
charged `verifypoint_t6_mod_p32003_b0.sing` prefix (`RING S: b4,q2_0..q5_0,b3
wp 1,2,3,4,5,7`, `A0VALUE: -2571`, `ngens(I2)=10`), on this host:

```text
NEGATIVE  Y_6 = V(I_2) ∩ {b4=1}, 10 gens, 4 vars   — must NOT be empty
          msolve -g 2 ⇒ "length of basis: 455 elements"      NOT [1]   ✓
POSITIVE  V(I_2+(W)) ∩ {b4=1} at t = 6, 15 gens    — must be empty, since
          clause (ii)_6 is charged   ⇒ "length of basis: 1 element"  [1]:  ✓
```

The negative control shows the pipeline does not manufacture `[1]`; the positive
control is the t = 6 instance of the very statement (H2b), and it agrees with the
charged clause (ii)_6.

The t = 8 negative control — *is `I_2 + (b4−1)` itself already the unit ideal, which
would make §8 vacuous?* — needs no new computation.  If `(q, b3) ∈ V(G) ∩ {b4=1}`
then `B_r b3 = −C_r` for every r, hence
`C_r B_s − C_s B_r = (−B_r b3)B_s − (−B_s b3)B_r = 0`: the CI chart projects into
`V(I_2) ∩ {b4=1}`.  The CI chart has 52138 points (charged §5, §6), so
`I_2 + (b4−1) ≠ (1)` at t = 8, and the `[1]` of §8 is produced by the `W_r`, not by
the minors.

## 6. The FGLM landed — and it closes the one-point route *negatively*

`msolve` pid 64330 on 172.30.0.7 finished at 15:56Z (started 13:47Z):

```text
sequence generation 2434.12 sec (30.90 Gops/sec); eliminating polynomial 0.50 sec
Elimination polynomial has degree 52138.
msolve overall time 7739.98 sec (elapsed) / 104020.95 sec (cpu)
```

`w7/msolve_t8_param_t16.txt`, 2427727 bytes, sha256
`f978d249e4b65f09ea664a900561703291c0b30a54f835fa18ec1d78de50d427`; header
`char 32003, nvars 7, deg 52138, vars ['q2'..'q7','b3'], linform [0,0,0,0,0,0,1]`
— **the separating element is the last variable `b3` itself**, no random linear
form, and the denominator slot is the constant `1`.  So `w` is the minimal
polynomial of `b3` on the mod-p CI chart algebra with `deg w = 52138 = n`: `b3`
generates.

`python3 msolve_point.py w7/msolve_t8_param_t16.txt` (validated at t = 6) printed
`rational roots of w: 0 []` and **no** `ROOT` line.  Independently, on .7 with
python-flint 0.9.0, `gcd(x^p − x, w)` has degree `0`:

```text
DEG 52138
SQFREE True gcd_deg 0
DDF 1 deg 0   (no linear factors)     <-- no F_p-point, by an exact gcd
DDF 2 deg 0   DDF 3 deg 0
```

Two consequences, both new:

1. **`Y_8 ⊗ F_32003` has no `F_32003`-rational point.**  Charged §10 steps (2)–(3)
   — extract a point, run `verifypoint` — therefore **cannot be executed at this
   prime**: they are not "still pending", they are *empty at p = 32003*.  This
   explains the charged §4 affine hunt (all coordinate lines, 2-planes, 3-spaces
   and eight 4-spaces in `{b4=1}` empty).
2. **`w` is squarefree**, so the mod-p chart is *reduced*: 52138 distinct geometric
   points.  Charged §5 explicitly declined to claim this ("the 52138 is a length,
   not yet a reduced geometric count").  It is now a count.

Item 1 is why this lane pivoted to Prop. 7.1 instead of waiting: the one-point
instrument has no input at this prime, while Prop. 7.1 needs no point at all.

## 7. Step (iv)(a): exactly what would prove `k_8 = 1`, and what this prime says

### 7.1 The instrument, stated

Charged Cor. 3.6 is written for `m̄` = minimal polynomial of `q̄_2`; msolve's
separating element here is `b3`, so the corollary must be transported.  The missing
step is supplied here (it is *not* charged):

**Lemma 7.A (β lies in the R-model).**  Let `M = A/(b4−1)A`, `A = R[b4,q]/I_2(N)`.
Clause (i)_8 says `(B_1..B_7)` is an hsop, i.e. `(B_1,…,B_7)M + 𝔭M = M`; `M` is a
finite module over the local `R`, so Nakayama gives `u_r ∈ M` with `Σ u_r B_r = 1`.
Put `β := −Σ_r u_r C_r ∈ M`.  The minors `C_r B_s = C_s B_r` (that *is* `I_2`) give
`β B_s = −C_s` for every s, so `β` is the canonical `−C_s/B_s`, lies in `M` (not
merely `M_K`), and reduces to the `b3`-coordinate of the CI chart.  ∎

With 7.A the proof of charged Lemma 3.5 applies verbatim to `β`: `M` is `R`-free of
rank `n = n' = 52138` (charged 3.3 + 3.4 + the EN bookkeeping `d_Γ(8) = 52140` with
boundary contribution exactly 2), and `β` is an integral endomorphism of a free
module, so its minimal polynomial `f^β` over `K = A_8` lies in `R[x]`, has degree
`n`, and `f^β mod 𝔭 = w`.  Charged Cor. 3.6 then reads: `w` squarefree with
irreducible factor degrees `d_1..d_s` ⇒ Frobenius at `𝔭` has cycle type `(d_j)` on
the `n` geometric points of `Y_8 ⊗ k`, and every monic factor of `f^β` over `A_8`
is `𝔭`-integral of degree a subset sum of `{d_j}`; if the proper subset sums have
empty intersection over the primes used — in particular if `w` is irreducible at ONE
prime — then `f^β` is irreducible, `M_K = A_8[β]` is a field, and `Y_8(K̄)` is ONE
orbit: `k_8 = 1`.

So **`k_8 = 1` would be proved by `w` being irreducible over `F_p` at one good
prime**, and the mechanical test is Rabin's: `x^(p^n) ≡ x (mod w)` and
`gcd(x^(p^(n/ℓ)) − x, w) = 1` for each prime `ℓ | n = 52138 = 2·131·199`.
Everything needed is already in the msolve `-P 1` output.

### 7.2 What p = 32003 actually says: `w` is REDUCIBLE

Run on 172.30.0.7, python-flint 0.9.0, `k8_degree_pattern.py` / `ddf_sweep.py`
(`w_t8_b3_p32003.txt`, sha256 `6c163cef5c398ba8bddf77a45117c2d0f60084d7d70a3080f59399f23c4f9794`;
the extractor asserts `len(coeffs) = deg + 1 = 52139` and reads the leading
coefficient 1.  It also *tested* the second slot against `w'` and got False — that
slot is the constant `1`, as §6 says, which is why the test is reported and not
asserted).

```text
DEG      52138           = n            (Lemma 3.5 degree condition holds for β)
SQFREE   True                           (Cor. 3.6 hypothesis holds)
DDF k    deg gcd(x^(p^k) − x, w) = Σ{deg f : f | w irreducible, deg f | k},
         swept k = 1..40 (ddf_sweep.log); the only k with a nonzero value are
         k  =  7  14  17  20  21  28  34  35  40
         d  =  7   7  17  20   7   7  17   7  20
RABIN_PROPER l=2   n/l=26069  gcd_deg=0     RABIN_PROPER l=199 n/l=262 gcd_deg=0
RABIN_PROPER l=131 n/l=398    gcd_deg=0     RABIN_FULL x^(p^n)==x : False
```

Unfolding the divisor lattice (k = 1..6, 8..13, 15, 16, 18, 19 all give 0, and
k = 14, 21, 28, 34, 35, 40 add nothing over their proper divisors), the low part of
the Frobenius cycle type at 𝔭 is *exactly*

```text
        {7, 17, 20}   and no further factor of degree ≤ 40   (sum 44 of 52138)
```

so **`w` is reducible**: it has one irreducible factor of each of the degrees
7, 17, 20.  `RABIN_FULL` is `False`, independently and as predicted (`7 ∤ n`).
`verify_factors.py` re-checks the three: each divides `w` exactly, each is
irreducible, they are pairwise coprime, and the cofactor has degree 52094.

Consequence, exactly: **`k_8 = 1` is NOT provable from `p = 32003`.**  Cor. 3.6
here only says every factor degree of `f^β` is a subset sum of the (7-containing)
multiset `{d_j}`, and `7` is itself an allowed proper subset sum.  Closing `k_8 = 1`
by this route now needs a *second* good prime whose proper subset sums avoid every
one available here — a new computation the size of the one just finished (≈ 2 h 10 m
on 16 threads), outside this lane's budget.  FALLACY-v2: `k_8` is not inferred from
t ≤ 6, and the t = 8 answer at this prime is negative, not pending.

The degree-7 factor is a positive by-product: a Frobenius orbit of exactly 7 points
of `Y_8` over `F_{32003^7}`, and since the sweep finds no smaller factor, that is
*the smallest field over which this chart has a point at all*.  With Lemmas 3.1+3.7
(unramified base change to `W(F_{p^7})`) one `W ≠ 0` evaluation there would certify
clause (ii)_8 on that one orbit — not needed below, recorded as the cheapest
fallback if the Prop. 7.1 route is ever contested.

## 8. (H2b) PROVED: the affine W-locus at t = 8 is empty

`msolve 0.10.1`, 30 threads, worker 172.30.0.18, on
`msolve_t8_affinew_p32003_b0.ms` (§4), `-g 2` (reduced GB, no FGLM), started
15:47:39Z, finished 18:09:4xZ.  Output file `w18/affinew_gb_t8.txt`, 206 bytes:

```text
#Reduced Groebner basis data
#field characteristic: 32003
#variable order:       q2, q3, q4, q5, q6, q7
#monomial order:       graded reverse lexicographical
#length of basis:      1 element
#---
[1]:
```

and the transcript `w18/affinew_msolve.log` ends

```text
size of basis 1   #terms in basis 1   #pairs reduced 244165   #rows reduced 490019
max. matrix data  63303 x 104538 (38.036%)
overall(elapsed) 8520.47 sec / (cpu) 142866.24 sec   (80.9% linear algebra)
Grobner basis has a single element
No solution
```

The deepest F4 degree was 19 (the CI chart of §6 needed only 15).  So

```text
   I_2 + (W_1,…,W_7) + (b4 − 1)  =  (1)   in  F_32003[q2,…,q7]
⟺  V(I_2 + (W)) ∩ {b4 = 1}  =  ∅   over  F̄_32003          (H2b)  ✓
```

With (H2a) from §3 and the `G_m`-scaling of §2,

```text
   V(I_2 + (W_1,…,W_7))  =  {0}   in  P_k ,  k = F_32003 ,  t = 8
```

which is the second hypothesis of Proposition 7.1; the first, `CONE dim = 1` at
`(p, yy) = (32003, 11288)`, is charged (§5 of the charged report, from the CI
quotient dimension 52138).  Proposition 7.1 therefore applies and gives

```text
   clause (ii)_8 over A_8 = Q(√3) :  T_{8,15}(P, β(P)) ≠ 0 at every P ≠ 0 of Γ_8
```

with **no orbit count, no affine F_p-point, and no use of `k_8`** — which is
essential here, since §6 shows no affine `F_p`-point exists at this prime and §7
shows `k_8 = 1` is false-at-this-prime as a Cor. 3.6 conclusion.

Chaining the charged implications with the banked clause (i)_8 (rank lane
`PARTI (B): dim=0, vdim=11440 = C(16,7)`, B-hsop, 17(rrrrr) — carrying its
DETECTOR-ONLY `p`-integrality caveat, restated in §11):

```text
   (i)_8 ∧ (ii)_8  ⇒  (V0)-tail_8  ⇒  (V0)_8  ⇒  (8.1)_8  ⇒  (T) at t = 8.
```

**Independent replication attempted, and it did NOT finish.**  The same 29
generators were given to Singular `std` on .28 at 15:54:45Z
(`affinew_t8_mod_p32003_b0.sing`, sha256
`65fc8f6da451e3491c435e6a89c90d785da9a9d6312dd8ceebdb2c2277ccbd5f`, pid 52704,
`timeout 11000`).  It was SIGTERMed at 18:58Z: `exit=124 wall=11000s timeout=11000`,
`halt 1`, having printed only `AFFINEW ngens=29`.  That is the third watchdog kill of
this ideal under single-threaded Singular (5400 s, 7200 s, 11000 s).  **So §8 rests
on one engine, msolve 0.10.1, not two.**  What stands behind it instead is the §5
control pair on the identical pipeline and the t = 8 non-triviality argument, plus
the fact that a `[1]` verdict is the cheapest possible thing for an F4 to reach and
the hardest to reach spuriously: msolve spent 8520 s and 490019 row reductions
before it did.

## 9. Computation record (`box/k16t8-20260905/`, this lane)

```text
file                               bytes   sha256(16)        what
affinewms2_t8_mod_p32003_b0.sing 1779448  4c8684cda0e18f0f  export driver
msolve_t8_affinew_p32003_b0.ms   3111128  d6401d43c62af47b  I2+(W)+(b4-1), 28 gens
w18/affinew_gb_t8.txt                206  (quoted in §8)    THE CERTIFICATE: [1]:
w18/affinew_msolve.log                 -  30-thread msolve transcript, 8520 s
ctrl_t6_{y6,wlocus}.ms + _gb.txt       -  the two §5 controls (455 elements; [1])
w7/msolve_t8_param_t16.txt       2427727  f978d249e4b65f09  FGLM param, deg 52138
w7/msolve_t8_t16.log                7942  995c13413b7326d8  full F4+FGLM transcript
w_t8_b3_p32003.txt                294490  6c163cef5c398ba8  w = minpoly(b3)
k8_degree_pattern.py, ddf_sweep.py, verify_factors.py, w7/ddf_factor_k{7,17,20}.txt
   + w7/{k8_pattern,ddf_sweep}.log      -  the §7 instrument and its transcripts
msolve_point_t8.out                    0  empty: no F_p-point at this prime
```

**This lane launched no instance and terminated none** — the planned
`fleet.sh launch 1 c7i.4xlarge` was unnecessary (worker .18 was already running and
idle) and would have been too small anyway: the affine F4 peaked above 36 GiB.

## 10. FALLACY-v2

- **Floor/attainment.** The certificate is an equality of ideals (`GB = [1]`;
  `dim = −1` on the boundary), never a bound promoted to attainment.
- **`sat()` wrapping.** No saturation.  `{b4 ≠ 0} → {b4 = 1}` is the explicit ring
  map `P/(b4−1) ≅ F_32003[q2..q7]`, justified by `G_m`-homogeneity with all weights
  positive (§2, §4), not by inverting `b4`.
- **Variable/ring map.** Declared with generator order, coefficient field and three
  image checks (`B4_ELIMINATED=1`, `ZERO_GENS=0 CONSTANT_GENS=0`, python re-scan
  showing only `q2..q7`); matching names alone were not trusted.  Controls: §5.
- **Prime label/derivative.** msolve's second parametrisation slot is here the
  constant `1`, not `w'`; §6 says so instead of assuming the t = 6 shape.
  `𝔭 ⊂ A_8` and `p = 32003` are kept distinct.
- **No inference from t ≤ 6.** `k_8` is computed at t = 8 and is negative at this
  prime (§7); the certificate does not use `k_8` at all.  Lemma 7.A (`β ∈ M`) is
  derived here and labelled so; everything else cited is charged.
- Flag/place/series, per-ray charge, carrier/attainment, pole/interior, raw
  remainder degree, merge-free/M-descent, target index: not engaged.

## 11. OPEN, caveats, and the state of every job at seal

```text
CLOSED here  OPEN[K16-ONE-POINT-T8] as posed is superseded, not solved: the
             quantity it tracked (verified simple affine F_p-points with W ≠ 0)
             is PROVABLY 0 at p = 32003 (§6), and clause (ii)_8 is obtained
             without it (§8).  Re-typing it is a ledger action, not taken here.
STILL OPEN   OPEN[K16-GAMMA-IRREDUCIBLE]: k_t = 1 for t ≥ 7.  At t = 8 this lane
             adds a hard negative — the Frobenius cycle type at p = 32003
             contains 7, 17, 20, so Cor. 3.6 cannot conclude here and a second
             good prime is needed (§7).  Prop. 7.1 makes this logically
             unnecessary for (V0), as the Galois report already argued.
STILL OPEN   problem (II), the uniform-in-t statement.  Nothing here is
             t-uniform: the certificate is one 8521-second F4 at one prime;
             (T) at t = 9 needs the same jobs again, at ≈ d_Γ(9).
CAVEAT       clause (i)_8 is cited, not re-run, and carries the charged
             DETECTOR-ONLY p-integrality caveat at t = 8 (no PINT PASS, only
             the absence of `div. by 0`).  (T)_8 inherits it.
CAVEAT       one prime only, p = 32003, yy = 11288 (branch 0 of H_8); good
             reduction of A_8 there is charged (disc H_8 = 124848 ≢ 0,
             (3/p) = 1, A0VALUE = 7970 ≠ 0).  Prop. 7.1 needs one good prime,
             so this is sufficient, not a gap.
JOBS AT SEAL .7   msolve pid 64330 FINISHED 15:56Z (param harvested); flint
                  instruments all finished.  Worker now idle.
             .18  msolve pid 71425 FINISHED 18:09Z, "No solution".  Idle.
             .28  Singular pid 52704 TIMED OUT 18:58Z, exit=124 wall=11000s,
                  no verdict printed: the second-engine replication of §8 is
                  NOT in hand and is the main thing a follow-up should get
                  (Singular will not do it single-threaded; use a second
                  msolve at a different prime, or `-c 1`).  Also on .28, the
                  leftover redundant 4-thread msolve pid 32489 of the CI
                  system, left running.  No worker was launched or terminated
                  by this lane.
```

No `charge_basis=` line: this lane asserts no new exit price.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `24207`.
- Body SHA-256:
  `4bd7f800e807af81db775ae239f58685ea501e93a80c79f29fe49066be91c5a3`.
- Frozen basis: `4e9fd0969be986d844958eb7977d3d8bdfdcb904`.
