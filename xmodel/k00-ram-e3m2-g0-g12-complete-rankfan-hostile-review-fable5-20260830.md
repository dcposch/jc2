# Hostile review: generic K00 `e=3,m=2` complete fan through G12

Date: 2026-08-30
Reviewer: Fable 5 (different-model hostile review; Grok mandate executed per
substitution — the prior Grok attempt failed pre-research on exhausted paid
balance and none of its output was consumed)
Frozen campaign basis: `0d7544ebd5cb12def6bac892646010301098be3c`
Producer under review: `xmodel/k00-ram-e3m2-g0-g12-complete-rankfan-sol56-20260830.md`
Verdict: **CONFIRMED** (itemized below; observations listed, none material)

## 1. Custody, seal, replay, ordinary/-O behavior

- Git HEAD equals the frozen basis. Working tree clean apart from `jc2-lean`
  and `pilot-local.log` (neither charged, neither touched by this review).
- Producer report full-file SHA-256 `3a4565b8…88ae` matches the mandate; body
  seal re-derived independently: bytes through the unique standalone
  `<!-- BODY-END -->` line inclusive = 14,872 bytes, SHA-256
  `06ccbd8b…1eb7`, both exact. The second marker occurrence is inside the
  seal's own definition sentence, not standalone; the body definition is
  unambiguous.
- Replay SHA-256 `7cbc45a1…6a33` matches. All nine charged source hashes
  verified byte-exact AND all nine files verified tracked at the frozen
  basis (none is an untracked producer-authored stand-in).
- `python3 -B` and `python3 -B -O` runs: exit 0, byte-identical stdout
  matching the report's block, ≈10.5 s each. Neither the replay nor the
  imported engine contains a single bare `assert` statement (all checks go
  through explicit `fail()`/`assert_zero`/`assert_equal`), so `-O` strips
  nothing; the identical `-O` output is honest, not vacuous.
- The replay writes no files (no write calls present); the 5,968-byte
  certificate is rebuilt in memory and its SHA-256 `6ae3c1d9…7c70` is
  hard-pinned (not `PENDING`), so certificate drift fails closed (verified
  by live mutation, item 7).
- Custody architecture observation: the replay hashes `tails.json` itself
  but never parses it; the parse happens inside the imported engine through
  the engine's own module-level `TAILS` constant. In canonical repo layout
  both constants resolve to the same frozen file, so the linkage is sound in
  situ; it would silently decouple only if the engine were relocated, which
  custody prevents.

## 2. Literal source calendar, reconstructed from the frozen 569 tails

I reconstructed rows and loads directly from `tails.json` with my own
parser and my own exact arithmetic (no producer/engine code imported),
using the coordinate map pinned in the frozen compiler
(`C0=(1+d0)/256, C1=d1, C2=(1+d2)/16, C3=d3, C4=(3+d4)/8, C5=d5, C6=1`)
and the compiler's Λ-shift table (K10=2, K6=6, K2=10, mu2=14, mu4=16,
mu6=18, Jdet=19; `Q[Lambda]/(Lambda^20)`), giving τ-shifts 6/18/30/42/48/54/57
for `Lambda=tau^3`. Results:

- census 569, all weights `12+ell`, loads linear, at most one load flag;
  C6-padding present in 371 monomials and harmless (image is 1).
- Raw minimal d-degrees: R rows `[2,2,2,2,2,3,2]` (rows 1–5,7 first at G4;
  row 6 has no quadratic part at all — `Q6 ≡ 0` — and first arrives G6);
  A10 rows all 2 (nominal K10 at G10); A6 `[1,1,1,2,1,2,1]` (K6 at G21,
  rows 4,6 at G23); A2 all 1 (K2 at G33); targets at G43/G49/G55/G57 under
  the cell constraints. Everything at or beyond G13 is out of the window;
  even a hypothetical degree-0 K6 term could only reach G19 > G12.
- Nominal vs actual K10: `A10^[2](plane) ≡ 0` (all rows) and the A10^[2]
  polarization between the plane and the full cone `C` vanishes
  identically (all rows) — re-proved from scratch. On the exact surface
  with `S=s·τ²+α·τ³+γ·τ⁴`, `T=t·τ²+β·τ³+η·τ⁴` (I retained γ,η beyond the
  producer's α,β), all K10 τ-grades 0–5 vanish identically and grade 6
  equals exactly `W1=(5/4096)t(3s²−64t²)`, `W2=(5/65536)s(s²−192t²)`,
  free of α,β,γ,η; row 6's grade-6 value is 0 (its surface restriction has
  minimum degree 4, so surface K10 row 6 first arrives G14), and row 4's
  A10 restriction is identically zero. Surface-restriction minima
  `[3,3,3,None,3,4,3]` confirmed. The asserted exact G10/G11 cancellation
  is therefore real, and the retained odd surface coefficients cannot
  restore a G10/G11 K10 arrival.

## 3. Graph recentering and rank strata, n=2,3,4,5 (independent)

Foundations re-proved independently: `R_r(D(S,T)) ≡ 0` for all 7 rows and
all 42 first partials vanish identically on the surface (the exact-surface
identity carrying the whole branch bookkeeping); `Q_r(cone) ≡ 0`; each
`Q_r` lies in the ideal `(A,B)` (so field-valued points of `V(Q)` lie in
`C={A=B=0}`, the set-theoretic step is legitimate and only set-theoretic);
`Q4=(3/524288)(B²−64A²)` identically; the 42-entry DQ factorization
`∂Q_r/∂d_j(cone)=avec_j·α_r+bvec_j·β_r` with the exact α/β table; minor
(rows 1,2) `=(9/2^24)·Δ`, so the rank stratification is exactly rank 2 on
`D(Δ)`, rank 1 on `Δ=0,(p,q)≠0`, rank 0 at `p=q=0`, independent of the
plane part. Each rank-zero recentering was checked as a genuine
reparametrization: the plane component moves into the free next surface
coefficients (`∂D/∂S, ∂D/∂T` reduce to the plane basis at leading order),
producing the identical d-series; nothing is deleted. The n4→n5
recentering was verified as the exact identity `G10|_{p=q=0} = Q_r(N5)`
with a fully general six-parameter `N5`.

Strengthenings beyond the producer replay, all passing:

- n=2 with **fully general** `d3` and `d4` (twelve extra coordinates, k10
  retained): grades 0–4 vanish, `G5_r = α_r A(d3)+β_r B(d3)` exactly, and
  G6 row 6 equals `p(192q²−p²)/65536` with everything retained.
- n=2 rank-2 kill re-derived: row 6 forces `p=0` or `p²=192q²`; the four
  cokernel combos are provably free of `d4` and all kernel coordinates;
  `p=0` gives row4 `=(3/512)sq²` then `t=−8q/3` vs `t=−4q` (incompatible,
  `q≠0`); on `p²=192q²` my own quotient arithmetic in `Q[r]/(r²−192)`
  confirms row 4 is linear in `s` with unit coefficient, forces
  `s=−r(t+2)` at `q=1`, and the two reduced combos are the nonzero
  constants `1/8` and `−1/64`. Rank-1 row 6 is `ε·i·q³/32` on both
  Gaussian charts.
- n=3: G8 rank-2 compatibility `det([α,β,N]₁₂₃)=(27/2^35)ΔC`,
  row4 `=(3/2^15)E`, and `det_(s,t)(C,E)=−Δ²` (forcing `s=t=0`,
  impossible on the recentered open); rank-1 F3/F4 combos exact (they
  force `X=0`, `s=8εit` over a field on `D(q)` — linear-algebra
  re-derived); the reduced branch (with γ,η retained beyond the producer)
  vanishes G0–G8 and has G9 row 6 `= ε·i·q³/32`.
- Fresh-cone extraction at n=4 and n=5 with fully general residual and
  tangent plus `k10[0..2]`: grades below `2n` vanish and
  `G(2n)=Q(N_n)`, `G(2n+1)=DQ(N_n)[N_{n+1}]` exactly — this is the check
  that rules out any early K10 arrival through a hypothetical low-degree
  A10 part on the branches.

## 4. G8/G9/G10 chronology, the n=4 survivor, and the unloaded G12 kill

- n=4: raw K10 grades 4 and 5 vanish identically on the branch (nominal
  G10/G11 never arrives); rank-2 dead at G10 by the (2.8) pair; on either
  rank-1 chart, after the forced `X=0`, `s=8εit`, all seven G10 rows equal
  `factor_r·q·H` with `H=B(N6)−8εi·A(N6)+128tq` and factors
  `(−3/1024, 3εi/2048, 3/8192, 0, 3/131072, 0, 3/1048576)` — a genuine
  rank-one G10 survivor at `H=0`.
- The reduced branch was rebuilt with `S3,T3,S4,T4` **and additionally
  `S5,T5`** (beyond the producer), all four kernel coordinates of `N5`,
  the solved `N6`, full `N7`, full `N8`, and `k10[0..2]`: all rows vanish
  G0–G10, G11 row 6 vanishes, and G12 row 6 is identically
  `ε·i·q³/32` — independent of every retained lift and of K10 (raw K10
  row-6 grades 0–6 all zero). Since `q≠0` on the chart, every possible
  G11 survivor dies at G12 regardless of what G11 imposes on other rows.
- Fixture: `(4.3)` re-evaluated numerically with my own code: passes every
  row G0–G11, `G12_6=i/32`; replacing `−128` by `−127` makes G10 nonzero.
  The stop at G12 is sharp and the G10 affine lift is honest.
- Mechanism note: the G12 row-6 terminal is the residual cubic
  `R6^[3](N4)` — the same closed form as the n=2 G6 row 6 — but it was
  re-extracted, not assumed; my independent run proves every other G12
  row-6 contribution cancels.

## 5. n=5 recentering and the delayed loaded G12 closure

- With γ,η retained (beyond the producer): grades 0–9 vanish, G10 is the
  fresh cone (identically zero on the residual chart), G11 is exactly
  `α_r X+β_r Y`, and G12 is free of `alpha,beta,gamma,eta,k10[1],k10[2]` —
  the producer's un-retained `S4,T4` at n=5 are hereby proved harmless
  rather than merely argued.
- Rank 2 dead at G12 by the same (2.8) pair. Rank 1: the cokernel combo
  `G12_2+(εi/2)G12_1` kills `A(N7),B(N7)` identically on the chart and
  equals `−(5εi/16)·k10[0]·t³` — pure `k10[0]` (the K10-unit open is
  load-bearing), nonzero since `t≠0` there. I verified the identity
  `W2+(εi/2)W1|_{s=8εit} = −(5εi/16)t³` by hand as well: the terminal is
  exactly the K10 W-combination.
- Rank 0: row 4 `=(3/524288)(B²−64A²)` with no `k10` term (`W4=0`);
  on either `B=±8A` branch the combo `G12_3+G12_1/8` is `±(3/2048)A²`
  and is `k10`-clean; so `A=B=0`, all quadratic rows vanish, and the
  remaining system is `k10[0]·W_r(s,t)=0`. `W1,W2` have no common zero on
  `D(s)∪D(t)`: `t=0⇒W2=(5/65536)s³≠0`; `s=0⇒W1=−(5·64/4096)t³≠0`; on
  `D(st)` they demand `s²=64t²/3` and `s²=192t²` with `64/3≠192`. This
  kills rank 0 including `ord(N)>5` (the pure-surface family dies by the
  load alone).
- Fixture: `(5.5)` re-evaluated with my own code: `k10[0]=0` passes **all**
  of G0–G12 (so the k10-vanishing face has genuine G12 survivors and the
  unit open is necessary, not decorative); `k10[0]=1` passes G0–G11 and
  fails G12.

## 6. Scope: field points, reduced cones, Gaussian signs, opens, faces

- All chart passages are field-legitimate: `V(Q)(K)⊆C(K)` from ideal
  membership; `B²=64A²⇒B=±8A` over a field; `Δ=0,(p,q)≠0 ⇒ q≠0, p=8εiq`
  after the Gaussian extension; `p²=192q²` handled in `Q[r]/(r²−192)` with
  constant nonzero combos. The claim is over an algebraic closure, and
  emptiness there implies emptiness over every subfield. No scheme,
  multiplicity, or nilpotent statement is made or needed; the one-way
  truncation consequence for formal in-cell solutions is sound.
- `D(s)∪D(t)` is the honest post-recentering form of `∪_i D(d_i[2])`
  because the nonplane G4 ranks are killed first (verified).
- Omitted load faces (`k6[0]≠0`, `k2[0]≠0`, `mu_i[0]≠0`) are outside the
  cell by (0.1) and are not claimed; within the cell every positive or
  infinite load order stays beyond G12 by the verified calendar.
- Observation: `Jdet[0]≠0` is declared in the open but never consumed in
  the G0–G12 window (first Jdet arrival is G57); the emptiness actually
  holds without intersecting `D(Jdet[0])`. Claiming the smaller open is
  safe, just not maximal.

## 7. Mutation testing (live runs on /tmp copies; repo untouched)

Control copy passes. Each of the following fails exactly as it should:

- tails byte mutation → custody gate (`custody`);
- discriminant `64→65` in `common_forms` → math assert (`… augmented`);
- `192→191` in the n5 W2 expectation → `n5 final W2`;
- n4 G12 row-6 terminal sign flip → `n4 reduced sign … G12 row6`;
- certificate digest flip → `certificate digest` (fail-closed verified);
- K6 calendar minima expectation mutation → `K6 degree minima`;
- independent mutation 1: engine `vector_with_ab` coefficient `−16→−15`
  **with custody hash updated** → math layer fires (`n2 rank2 p=0 row4`),
  proving the math checks, not only custody, carry the load;
- independent mutation 2: one unloaded row-6 tails coefficient bumped by
  `1/65536` **with custody hash updated** → math layer fires at
  `surface row 6` with exactly the injected residual — end-to-end data
  sensitivity of the surface identity confirmed.

Observation (not a defect): the engine's `cone_vector` plane-embedding
coefficient `(16,a)` is math-invisible to this replay (every call passes
`a=b=0`; plane parts live in the surface series) — a mutation there
survives all math checks and is caught only by certificate bytes. My
independent stage-1 check verified the full cone with symbolic `a,b`, so
the mathematical content is covered; the producer's declared mutation list
does not claim that coefficient, and every mutation it does declare was
verified to fire. The `if F(64,3)==F(192)` guard is a constant,
never-firing encoding of the W-slope disjointness; the real 192-sensitivity
is carried by the `n5 final W2` assert (verified above) — same class of
banner-versus-control nick as the e3m1 review's W2 finding, and equally
immaterial here.

Additionally, 18/18 randomized exact numeric trials (six each for the n4
reduced G12 terminal, the n5 rank-1 terminal, and the n5 rank-0
`k10[0]·W` face) passed through an independent scalar-arithmetic path with
all retained parameters randomized, including my extra `S5,T5,γ,η`.

## 8. Neighbor packets as regression controls only

The e3m1 and e2m2 producer/replay/review/integration files are charged by
hash and verified tracked at the basis; the replay only hashes them and
never parses their content — regression pins, not imported source. Every
closed form in this packet was re-extracted here directly from the e=3
tails; my recomputation confirms no coefficient-blind recurrence was
assumed (the recurring `ε·i·q³/32` terminal was re-derived per transition
and is each time the residual cubic of row 6).

## 9. Itemized verdict and maximum safe statement

| item | verdict |
|---|---|
| custody/seal/replay/-O | CONFIRMED |
| source calendar from 569 tails, nominal-G10 vs actual-G12, G10/G11 cancellation | CONFIRMED |
| recentering + rank strata n=2..5 | CONFIRMED |
| n=4 rank-one G10 survivor, `−128→−127` control, raw unloaded G12 row six | CONFIRMED |
| n=4-rank0 → n=5 recentering; all n=5 closures; K10 on/off fixture | CONFIRMED |
| field-point scope, reduced cones, Gaussian signs, opens, faces | CONFIRMED |
| mutation matrix (producer-declared + two independent) | CONFIRMED (with the cone_vector/constant-guard observations above) |
| neighbor regression separation | CONFIRMED |

**Maximum exact statement safe to promote.** Over an algebraic closure of
a characteristic-zero field, in the normalized generic K00 cell
`Lambda=tau^3`, `ord_tau(d)=2`, `C6=1`, `k10[0]≠0`, `Jdet[0]≠0`,
`k6,k2,mu2,mu4,mu6 ∈ tau·K[[tau]]` or identically zero, the seven literal
source rows have no field-valued solution through grade G12:

```text
V(G0,...,G12) ∩ D(k10[0]) ∩ (∪_i D(d_i[2])) = ∅,
```

with the leading-order open becoming `D(s)∪D(t)` after the first rank-zero
recentering. The `D(Jdet[0])` factor is declared but unconsumed; the
emptiness holds on the larger open without it. This is a finite-jet
point-set statement only; a formal in-cell solution is excluded by
truncation; no arc existence, converse lifting, source reachability,
attainment, algebraization, map, scheme/ideal, all-e induction, other-cell,
or JC2 statement follows.

**Cheapest successor** (typed OPEN, no source-completeness claim): the
complementary K10 face `k10[0]=0` of the same `e=3,m=2` support, where the
verified fixture exhibits genuine G12 survivors (the pure-surface family);
its first new obstruction window opens at the `k10[1]` arrival G13 and is
bounded above by the K6 gate at G21/G23.

<!-- BODY-END -->
