# Hostile review: AS D7 exact Q9 source-state gate

**Reviewer: hostile different-model session (Claude), 2026-08-25.  All
producer bytes treated as immutable; nothing written except this file.**

## 0. Session constraints and evidence basis

This review session had no shell: no Bash, no local execution, no SHA-256
recomputation, and no run of `verify_frozen_results.sh` (read line-by-line
but not executed).  Every hash statement below is a textual
cross-consistency check across the frozen files, and the AWS outputs are
trusted as transported bytes under their manifests.  All mathematics below
was re-derived by hand from the frozen sources, independently of the
producer; every count audit below is a hand summation over the frozen
per-shard outputs, not a replay of PASS lines.

Read in full: the charged report
`xmodel/as-fonly-d7-vertical-q9-source-state-gate-20260825.md`; every file
of `cases/as_fonly_d7_vertical_q9_state_gate_20260825/` including all 27
`shard_*.out`, representative `.rc/.time/.err`, `aggregate.out/.err`,
`launch.meta`, the `aws_*` deployment tree, both manifests, both freezes,
`PREREGISTRATION.md`, `README.md`, `RESULT_README.md`, `compile_shard.py`,
`aggregate_shards.py`, `launch_all.sh`, `verify_frozen_results.sh`; the
divided-Frobenius erratum (report and `replay_source.py`); the corrected
Q11/Q10 parents' compilers and the corrected-Q10 result freeze; and the
entire pinned source closure down to `generate_degree10_gate.py`
(`generate_corrected.py`, `audit_full_e1_degree7.py` path,
`audit_full_c5_source.py`, `compile_full_c5_gate.py`,
`audit_next_cartier_source.py`, `compile_next_cartier.py`,
`compile_next_top_carry.py`, and the three shard compilers in between).

Charged hashes, tie-out: report `6fb2ce4b…`, result manifest `06b7c540…`,
source freeze `1aa89a7b…`, aggregate `ab38fefa…`, and Merkle `31b77bef…`
appear verbatim and mutually consistently in `FREEZE_RESULT.txt`,
`RESULT_MANIFEST.sha256`, `REMOTE_RESULTS_MANIFEST.sha256`,
`aggregate.out`, and the report.  The result-freeze hash `97755c63…`
(the hash of `FREEZE_RESULT.txt` itself) cannot be recomputed here; it is
corroborated textually by the downstream
`cases/as_fonly_d7_q9_kuranishi_q8_20260825/FREEZE_SOURCE.txt`, which pins
it as `q9_result_freeze_sha256`.  The corrected-Q10 predecessor freeze
`e73b854b…` — left "terminal and uncorroborated" by the previous hostile
review — is now cited by both Q9 freezes, closing that loop.  All 27
shard-output hashes listed in `aggregate.out` equal the transported hashes
in `REMOTE_RESULTS_MANIFEST.sha256` entry-by-entry, and `smoke26.out`
carries the same hash as `shard_26.out` (pre-launch determinism check).

## 1. The degree-nine integer residual, T, and the divided-term sweep

From the frozen master identity (erratum §1), re-derived here by direct
hand expansion of `P_xQ_y−P_yQ_x−1` with `P=x−x^3+3U+9C+27W`,
`Q=y+3V+9D+27Z`:

```text
det J−1 = 3L + 9(K+C_x+D_y) + 27(M+W_x+Z_y) + 81(N+T) + 243S + 729{W,Z},
L=A+V_y, A=U_x−x^2, K=AV_y−U_yV_x,
M=AD_y+C_xV_y−U_yD_x−C_yV_x, N={C,D},
T=AZ_y+W_xV_y−U_yZ_x−W_yV_x.
```

The `−x^2` in `A` comes from `−x^3` in `P`; the sign and placement of every
term were checked term-by-term.  `T` is exactly `M` with `(C,D)↦(W,Z)`, and
this is forced: substituting `C↦C+3W`, `D↦D+3Z` in the accepted tower gives
`E(C+3W,D+3Z)=E+3(W_x+Z_y)` and `M(C+3W,D+3Z)=M+3T`, so
`G=F/3+N+T` with `F=E/3+M+W_x+Z_y`, matching `RESULT_README`'s frozen
filtration and equation (1) of the report exactly.  The `3({C,Z}+{W,D})`
and `9{W,Z}` parts of `{C+3W,D+3Z}` die mod 3 (and are degree ≥ 10
anyway), so `N` is correctly the bracket of `C,D` alone.

Degreewise at total degree nine, in the typed support (first digit `U0,V0`
of degree ≤ 4 plus degree-six Frobenius `UF,VF`; current digits
`C5,C6,C7,D5,D6,D7`; restored `C2,D2,C4,D4,W7,Z7`):

- `E_9=0` identically: `K`'s factor degrees are `{2,3,5}×{2,3,5}`, whose
  sums omit 9; `L/3` has degree ≤ 5; `C_x,D_y` have degree ≤ 6.  Asserted
  per state by the compiler as well.
- `(W_x+Z_y)_9=0` by degree (the only W/Z layer is degree 7).
- Hence `F_9=M_9` and the typed row is `G_9=M_9/3+{C,D}_9+T_9`, exactly as
  imposed by `source_rows` (`F1_9 + N9 + degree_part(T,9)`).

Exhaustive sweep for a further single- or double-Frobenius quotient term
analogous to the Q11/Q10 erratum, over the pair degrees:

- `M_9` decomposes exactly as `[A_3(D7)_y+(C7)_xv_{y,3}−u_{y,3}(D7)_x−
  (C7)_yv_{x,3}]` (non-Frobenius) plus `[A_5(D5)_y+(C5)_xv_{y,5}−
  u_{y,5}(D5)_x−(C5)_yv_{x,5}] = {UF,D5}+{C5,VF}` (single-Frobenius, every
  coefficient carrying the factor 3 of a Frobenius derivative).  The pairs
  `(a,b)∈{2,3,5}×{4,5,6}` summing to 9 are only `(3,6)` and `(5,4)`; there
  is no other contribution.  The degree-nine analogue of the erratum's
  missing terms is therefore `({UF,D5}+{C5,VF})/3`, and the producer
  includes it automatically because it computes `M` over Z with `UF,VF`
  inside `U,V` and divides once; the erratum class of error (hand-derived
  symbolic rows omitting a divided summand) is structurally precluded here.
- Double Frobenius: `{UF,VF}` is pure degree 10; `K` has no degree-9 part
  at all; nothing at 9.
- `T_9` uses only degree-3 parts of `A,u_y,v_x,v_y` (`{2,3,5}+6=9` forces
  `a=3`), so `T_9` contains no Frobenius quotient; `T`'s Frobenius part
  `T_{11}` and the C/D-cross of the new layers never reach degree 9.
- New-layer contributions to `M` cap at degree 8 (`5+3`), so full
  `M_9 =` base `M_9`; the compiler asserts exactly this
  (`degree_part(M,9)==3·F1_9`).

Every division used, with its guarantee:

- `L/3`: identically exact over the canonical representatives — verified
  coefficientwise by hand (e.g. `x^3`: `4·((2t)%3)+t ∈ {0,9,6}`;
  `xy`: `2h+2·((2h)%3) ∈ {0,6,6}`; `x^2y`: `3q`; `x^5`: `6fb`).
- `E_6/3`: `E_6=K_6+(C7)_x+(D7)_y`; its mod-3 class vanishes because the
  degree-6 accepted rows are baked into the frozen `sub` elimination of
  `c7_1,c7_2,c7_4,c7_5,c7_7,d7_2,d7_5` in `generate_degree10_gate.py`;
  additionally asserted per state.  The integer/symbolic difference is a
  3-multiple (e.g. `3q x^2y` inside `u_x`, `3c7_3x^2y^4` inside `(C7)_x`),
  which is precisely the carry content that survives in the quotient.
- `M_9/3`: the non-Frobenius bracket above is, mod 3, exactly the imposed
  D98-gate degree-nine rows (labels `M_i_{9−i}` in
  `generate_corrected.py`): `KFdiv` has no degree-9 part
  (`5+{2,3}` and `{2,3}+5` give only 7, 8, 10), so the imposed `R_9` equals
  `M_9` mod 3, and every visible state — hence every corrected-Q10 state —
  satisfies it.  The Frobenius part is identically divisible.  Asserted per
  state; all 27 shards exited 0.
- Replay divisions `M_{11}/3`, `E_{10}/3`, `(E_{10}/3+M_{10})/3` are
  identically exact (`M_{11}=3·[{UF,D7}+{C7,VF}]`-type, `E_{10}=K_{10}=
  9·Kdouble`-type, spectator parts divisible by 9), reproducing the
  corrected Q11/Q10 rows; I recomputed `{UF,VF}/9 mod 3` by hand and it
  matches `expected_kdouble` termwise.

No missing or false source identity was found at degree nine.

## 2. Predecessor-state sufficiency and the spectator/omitted-layer theorems

The stored corrected-Q10 state is the 30-tuple: structural
`(Pp,Qq,Rr,Tt,s,w,h)` (7), Frobenius `(fua,fa,fb,fc,fd,fvb)` (6), unknowns
`(d7_1,d7_4,d7_7,d6_1,d6_4,c5_0..c5_5,d5_0..d5_5)` (17).  Sufficiency
holds because every ingredient of the 23 rows is a function of this tuple
under the frozen conventions, all re-derived rather than trusted:

- Carry map: `canonical_source`'s `r=Rr+sh`, `t=Tt+wh`, `p=Pp+Rrh+2sh^2`,
  `q=Qq+Tth+2wh^2` is identical to the frozen `coord` in
  `generate_corrected.py`.
- First digit: `U0={h x^2y, p y^4, (2r)x y^3, q x^3y, (2t)x^4}`,
  `V0={(2h)xy^2, x^2y, r y^4, s xy^3, t x^3y, w x^4}` matches the frozen
  `normal` table entry-by-entry (`u3_2=h, v3_1=2h, v3_2=1, u4_*=…,
  v4_*=…`, `u4_2=v4_2=0`, `u5=v5=0` on the vertical branch), and
  `UF=fua y^6+fa x^3y^3+fb x^6`, `VF=fc y^6+fd x^3y^3+fvb x^6` matches the
  frozen Frobenius forms.
- Recorded digits: `recorded_homogeneous` evaluates
  `transformed_coefficient` = `sub_digits∘normal∘pivot_sub∘coord`, the
  exact frozen substitution chain, at the state, with spectators set to 0.
- The exec-prefix chain is hash-pinned in code at every link
  (`3837508e… → 349ea509… → 64bbd0e1… → 1fc18eeb…`, then runpy links
  covered by the 13-file `SOURCE_CLOSURE.sha256`, all `OK` in the box's
  `source_closure_check.log` at 01:11:43Z, before launch at 01:12:19Z),
  and the shards re-derive the full predecessor chain from scratch,
  reproducing all four controls (§4) rather than consuming a stream.

**Spectator theorem (verified, and sharpened).**  The six spectators
`c6_0,c6_3,c6_6,d6_0,d6_3,d6_6` sit at Frobenius positions
`(0,6),(3,3),(6,0)`, so both integer partial derivatives of each spectator
monomial carry a factor 3.  Consequences, all checked by hand: (i) the
E-band rows contain no `C6/D6` at all (`(C6)_x` has degree 5; `E_1,E_3`
see only `C2/D2/C4/D4` divergences plus `L/3`); (ii) `F_6` contains no
`C6/D6` (`M_6` pairs `{2,3,5}×{4,3,1}`; the degree-5 partials of `C6/D6`
would need a degree-1 partner, which does not exist); (iii) `M_9` contains
no `C6/D6` (degree-5 partials would need a degree-4 partner); (iv) `T_9`
contains no `C,D` at all; (v) the only spectator entry into the 23 rows is
`{C5,D6}_9+{C6,D5}_9` inside `N_9`, where every spectator term is an
integer multiple of 3 and dies in the final mod-3 reduction — and `N_9` is
added after the single division, so no quotient is perturbed; (vi) no
division proof (`L/3, E_6/3, M_9/3`, replays) involves the spectators
except through terms divisible by 9.  Hence the 23 rows are identical for
all `3^6` spectator values and the factor is exactly `729`; the count
`5,902,243,834,439,547 = 729·8,096,356,425,843` was verified by hand.
Caveat recorded in §6: the Q9 compiler itself performs no runtime
spectator-absence check for the four new bands (the parent prefix asserts
it only for N12/Q11/Q10); the theorem is carried by the typed support and
is proven here.

**Omitted layers cannot reach the 23 rows (verified).**  `C3/D3` reach
only `E_2` (divergence), `F_5`-type bands, and `G_8` (`{C3,D7}` has degree
8) — none imposed here, all in the open lower rows; `C1/D1` reach only
`E_0`; W/Z layers other than degree 7 reach `F_3`/`G_{5,6,8}`-type bands;
`u5,v5` are zero on the frozen vertical branch; and the four degree-3
first-digit Frobenius lifts `u3_0,u3_3,v3_0,v3_3` (invisible to the mod-3
predecessors) change only 3-multiples of `K,M` at degrees ≤ 8 and the
`E_2` quotient, never any of the 23 rows or any division used.  A
degree-10 W/Z layer would enter `F_9`, but it is excluded by the frozen
`D=7` typed support, and the licensed conclusion is scoped to the
displayed problem in any case.

**No retroactive contamination (verified).**  Attaching the 32 new
variables leaves every previously imposed row invariant mod 3: their
potential contributions to the accepted E-rows (degrees 4,5,6,7), the D98
core rows (`M_8,M_9`), the Cartier row `F22`, and the N12/Q11/Q10 rows are
each either degree-impossible or carry an explicit factor 3
(Frobenius-divided pairings such as `A_5(D4)_y` in `M_8`, `3q·2d2_0` in
`M_4`'s `(2,2)` slot).  So the 33,225-state predecessor set remains the
correct base after restoration, and the compiler additionally re-asserts
the 12/11/10 residuals on every state.

## 3. The 23×32 affine system, ranks, and the witness

Row inventory: `row(E,1)` (2) + `row(E,3)` (4) + `row(F6,6)` (7) +
`row(G9,9)` (10) = 23; each homogeneous coefficient appears exactly once
(`row(poly,total)` enumerates all `total+1` monomials); no equation is
counted twice and no monomial is missing from the four bands.

Affinity in the 32 variables is a theorem of the support, not just a
runtime observation: `E,M,T` are linear in the layers (`U,V` are state
data), and the only bilinear-in-new-variables term anywhere,
`{C2+C4,D2+D4}` inside `N`, has degree ≤ 6, hence cannot reach `N_9`.
`N_9` is affine (via `{C7,D4}+{C4,D7}`, with `C2/D2` absent since
`{C7,D2}` has degree 7).  The finite-difference construction of the matrix
is therefore exact; the all-ones evaluation is a genuine negative control
for cross terms.  The row reduction is a full RREF over F3 with pivots
normalized, incompatibility read off zero-row/nonzero-RHS, augmented rank
= rank+1 exactly then, fibre `3^{32−rank}`, and the emitted witness (free
variables 0, pivots from the reduced RHS) is substituted back with
`source_rows(witness)==0` asserted — all sound.  Ranks are computed
pointwise on the numeric state; no generic-rank shortcut and no illicit
specialization occurs (spectators are provably absent rather than
specialized, per §2).

**Hand verification of the emitted witness, end-to-end.**  The first
witness is the predecessor state with all 30 coordinates zero except
`c5_5=2`, restored layer all zero except `w7_7=2`, fibre `3^19`.  By hand:
`U=0`, `V=x^2y`, `A=−x^2`, `u_y=0`, `v_x=2xy`, `v_y=x^2`, `L=0`,
`K=−x^4`; all recorded digits evaluate to 0 except `C5=2x^5`; the visible
gate holds nontrivially (accepted-4 `x^4` row: `−1+5·2=9≡0`;
`F22=c5_3+d5_2+2h^2=0`; all bracket rows vanish since `c6=c7=d5=d6=d7=0`);
the N12/Q11/Q10 replays hold (everything vanishes).  Then `E=9x^4` (rows
`E_1=E_3=0`), `M=10x^6`, `F_6`'s only nonzero row is `x^6`:
`10+7·2=24≡0` — the witness is forced to `w7_7=2` — and
`G_9=0+0+0` since `M_9=0`, `N_9=0`, `T=14x^8` has no degree-9 part.  All
23 rows vanish.  The rank decomposes by hand as `2 (E_1) + 4 (E_3) +
7 (F_6) + 0 (G_9 ≡ 0=0 rows) = 13`, fibre `3^{19}` — exactly the recorded
`(13,13)` stratum.  Nonemptiness of the displayed Q9 extension problem is
therefore proven in this review by hand, independently of every AWS byte.
As a second probe, shard 3's witness (`Qq=1`, rest zero) requires
`d4_2=1`, matching my hand-derived `E_3` row `q+2d4_2≡0` at `x^2y`, and
shard 6 (`Qq=2`) has `d4_2=2` — the frozen outputs respond to the algebra
exactly as they must.

## 4. Census, partition, aggregate, Merkle, metadata

- Partition: the 27 recorded `shard_range` lines tile `[0,3^7)` in
  contiguous width-81 blocks; the aggregate asserts contiguity and the
  endpoint, plus per-shard index/count and PASS tails; the launcher is
  fail-closed (any nonzero shard rc forces `overall_rc=1` and aggregate rc
  125).  `launch.meta` records `overall_rc=0`, `aggregate_rc=0`.
- Controls, hand-summed over all 27 frozen shard outputs (not trusted from
  the aggregate): visible `1,085,103` ✓; N12 `629,115` ✓; Q11 `260,847` ✓;
  Q10 `33,225` ✓; nonzero-`M_9/3` states `5,710` ✓; compatible `11,881` ✓;
  completions `8,096,356,425,843` ✓.  These equal the corrected-Q10
  freeze's four controls exactly.
- Rank census, hand-summed across shards: `(13,13):6615, (13,14):4320,
  (15,15):2106, (16,16):3160, (16,17):5288, (17,18):11736`; compatible
  `6615+2106+3160=11,881`; incompatible `4320+5288+11736=21,344`; total
  `33,225`.  Fibre histogram `(3^{19})^{6615},(3^{17})^{2106},
  (3^{16})^{3160},0^{21344}` matches ranks 13/15/16 exactly, and
  `6615·3^{19}+2106·3^{17}+3160·3^{16}=8,096,356,425,843` was verified by
  hand — and re-verified a second, independent way from the per-base
  completion histogram (`28·3^{16}+18·3^{17}+6·3^{18}+12·3^{19}+
  4·108·3^{16}+6·3^{21}+2·405·3^{16}+2·3^{26}+2,876,597,130,825`), which
  sums to the same total, with `2,876,597,130,825=66,825·3^{16}` exact.
- Per-base histograms: zeros `70+6·81+2·68+2·76+12·80+4·76=2108`, so
  `2187−2108=79` surviving bases ✓; the compatible-per-base histogram
  `0^{2108},1^{28},3^{18},9^{6},27^{12},108^{4},243^{6},405^{2},2187^{2},
  4347^{1}` sums to 2,187 bases and 11,881 states ✓.
  `729·8,096,356,425,843=5,902,243,834,439,547` ✓;
  `729·33,225=24,221,025` in the parent freeze ✓.
- Merkle: leaf = `H("leaf"‖index_4BE‖payload-SHA)`, odd-node duplication,
  root `31b77bef…` recorded identically in `aggregate.out`, freeze, and
  report; construction deterministic; root not recomputed here (no shell).
  The bounded verify script re-checks source closure, both manifests,
  per-shard rc/err/time, and byte-diffs a regenerated aggregate; it
  intentionally does not rerun the enumeration.
- Metadata: every one of the 27 `.err` hashes in the remote manifest (and
  `aggregate.err`, `launch.log`, `smoke26.err`) is the canonical
  empty-file SHA `e3b0c442…`, confirming "all result stderr empty" at the
  byte level; `shard_00.rc` reads `rc=0`; `shard_00.time` reads
  `Exit status: 0`, elapsed `3:51.69` (the report's "longest shard"),
  ~21.7 MB peak RSS under the 8 GiB cap; tag/host/UTC window match the
  report and `deployment.meta`, whose `verified_utc` precedes
  `launch_utc`; `source_shapes 5 12 11 23 32` matches the parent row
  counts and this gate's shape.

## 5. Scope audit

The report licenses only: nonemptiness of the displayed finite affine Q9
extension problem for the canonical accepted-digit state, with the exact
census above.  `PREREGISTRATION.md` predeclared the discriminator, the
fail-closed no-verdict conditions, and the same scope.  Degree eight and
all lower rows (including the `E_2`/`E_0` divergence bands for the
still-omitted `C3/D3, C1/D1` layers and the `G_8` band where `{C3,D7}` and
`S` first bite), recurrence, all-depth lifting, characteristic-zero
algebraization, collision persistence, counterexample, and JC2 are all
explicitly left open, and nothing read overreaches.  Two scope-honest
disclosures in `RESULT_README.md` deserve emphasis: the shards are
partitions of one implementation, not independent reviews; and the
canonical integer-representative convention itself is a frozen convention
(`G_9`'s quotient genuinely depends on the lift; the license is internal
to the displayed convention, which is fine for nonemptiness of the
displayed problem).

## 6. Findings

No false source identity, no missing state coordinate, and no count gap
was found.  The smallest findings, none affecting the verdict:

1. (Wording) The report's "proves the six current degree-six Frobenius
   variables are spectators here" overstates the runtime: the Q9 compiler
   sets spectators to zero and performs no spectator-absence check for the
   four new bands (the inherited asserts cover only N12/Q11/Q10).  The
   claim is true — proven in §2 of this review from the typed support —
   but the proof lives in the support argument, not in the producer's
   assertions.
2. (Wording) `RESULT_README`'s "the corrected-Q10 predecessor makes
   `M_9/3` integral" misattributes the mechanism: integrality mod 3 is
   enforced by the D98-gate degree-nine rows carried in the visible
   system (with `KFdiv_9=0`), inherited by every visible state; the
   degree-10 row itself adds nothing at degree 9.  The content is true and
   is independently asserted per state.
3. (Custody, disclosed) No hash could be recomputed and no verify script
   run in this session; byte custody rests on the internally consistent
   hash lattice, the box-side closure check, and the smoke/shard hash
   equality.  The charged result-freeze hash `97755c63…` is corroborated
   only by the Q8 successor's source freeze and the review prompt.
4. (Inherent, disclosed) The census rests on one implementation lineage;
   the independent checks are the erratum's integer replay for the
   universal forms and this review's hand algebra, which includes a
   complete by-hand certificate of nonemptiness (§3), the strongest
   producer-independent corroboration available.

## Promotable sentence

On all 33,225 corrected-Q10 predecessor states of the AS F-only `D=7`
vertical branch, the canonical-integer Q9 source-state gate — the 23-row
affine system `E_1=0, E_3=0, F_6=0,
G_9=M_9/3+{C,D}_9+T_9≡0 (mod 3)` with
`T=AZ_y+W_xV_y−U_yZ_x−W_yV_x`, in the 32 restored coefficients
`C2,D2,C4,D4,W7,Z7`, with every integer division proven before reduction —
is compatible for exactly 11,881 states (ranks 13/15/16, fibres
`3^19/3^17/3^16`, census `6615/2106/3160`) and incompatible for exactly
21,344, over 79 of 2,187 structural bases, with relevant completion total
8,096,356,425,843 and exactly `729×` that, 5,902,243,834,439,547, after
restoring the six provably spectator degree-six Frobenius coefficients;
this licenses nonemptiness (independently certified here by the hand-checked
witness `c5_5=2, w7_7=2`) of the displayed finite affine Q9 extension
problem under the frozen canonical-representative convention only — degree
eight and all lower rows, recurrence, all-depth lifting,
characteristic-zero algebraization, collision persistence, counterexample,
and JC2 remain open.

CONFIRMED
