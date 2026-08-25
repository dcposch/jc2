# Hostile review: AS D7 exhaustive Q7/Q6 exclusion below one Q8 survivor

**Reviewer: hostile different-model session (Claude), 2026-08-25.  All
repository bytes treated as immutable; nothing written except this file.**

## 0. Session constraints and evidence basis

This session had no shell: no Bash, no execution, no SHA-256 recomputation
of any file, stream, or archive.  Every hash statement below is a textual
cross-consistency check over frozen bytes, and the AWS stdout/JSON/meta are
trusted as transported under their manifests.  All mathematics was
re-derived by hand from the frozen sources; no PASS string, rank, or
emitted row was accepted without that reconstruction.  The census map
itself — all four high rows on the whole kernel — is re-proven in closed
form in §2, so the verdict rests on hand algebra plus the transported
attestations, not on the producer's arithmetic.

Read in full: the charged report
`xmodel/as-fonly-d7-q7kernel-next-high-carry-exclusion-20260825.md`; every
file of `cases/as_fonly_d7_q7kernel_next_high_20260825/` (compiler,
aggregator, preregistration, README, RESULT_README, run_remote.sh, both
freezes, all four custody manifests, verify_result.sh, and the result tree:
all 27 shard stdout/stderr/json, aggregate.json/stdout/stderr,
launcher.stderr, run.meta, OUTPUTS.sha256, with shard 00/01 records
extracted raw); the parent pointwise report
`as-fonly-d7-q6-zero-next-divided-high-carry-20260825.md` and upstream
fibre report `as-fonly-d7-q9-fibre-q8-kuranishi-survivor-20260825.md`; and
the entire pinned source chain:
`compile_q7_transition.py`, `compile_witness.py` (Q9→Q8),
`vertical_q9_state_gate/compile_shard.py`, the corrected Q10 and Q11
shards, the pre-erratum top shard, `compile_next_top_carry.py`,
`compile_next_cartier.py`, `compile_full_c5_gate.py`, plus the two prior
confirmed hostile reviews of this lineage (corrected top carry;
Q9-witness/Q8 V3), whose hand-certified predecessor facts are reused and
independently re-checked here where load-bearing.

Custody tie-out, textual only: report `cc2cf641…`, result manifest
`a1eafec7…`, aggregate JSON `87f63bdd…`, aggregate stdout `c9b36bd7…`,
ordered high stream `6e4df883…`, compiler `7842ba69…`, aggregate source
`8ff06ec8…`, source freeze `ad30a493…`, git head `2e6104a…` appear verbatim
and mutually consistently across the charge, both freezes, both manifests,
OUTPUTS.sha256, the stdouts, and the report.  The charged result-freeze
self-hash `30754347…` appears nowhere in the repository except the review
charge (standard terminal-hash situation; see finding 5).

## 1. Typed cumulative state, prefix chain, and the exact fibre (charge 1)

**Conventions are inherited, not re-typed.**  The shard compiler exec's the
hash-asserted definition prefix of `compile_q7_transition.py`
(`5e181b09…`), which exec's `compile_witness.py` (`fbf327fb…`), which
exec's the Q9 state gate (`54d05ebf…`), and so on through `3837508e…`,
`349ea509…`, `64bbd0e1…`, `1fc18eeb…`; each split marker is asserted
unique.  Every polynomial primitive (`homogeneous_numeric`, `row`,
`divide_exact`, `nbracket`, `degree_part`) is therefore the deepest layer's
single definition: monomial keys are `(x-exp, y-exp)`,
`homogeneous_numeric(d, v)` maps `v[i]` to `x^i y^{d-i}`, `row(P, d)[i]` is
the `x^i y^{d-i}` coefficient mod 3, and `divide_exact` hard-asserts
integer divisibility.  This settles the labeling question below (§4): the
constant coordinate really is `x^10`, not `y^10`.

**The state.**  The predecessor hard-coded in `compile_witness.py` is the
30-vector with 2 at index 23 of `structural(7)+frob(6)+unknowns(17)`, i.e.
`c5_5=2`, everything else zero — identical to the state-gate's frozen first
witness and to what the prior reviews hand-certified: `U=0`, `V=x²y`,
`A=−x²`, `u_y=0`, `v_x=2xy`, `v_y=x²`, `L=0`, `L1=0`, `K=−x⁴`,
`Cbase=2x⁵`, `Dbase=0`.  Under `new_names`
(`c2,d2,c4,d4,w7_0..7,z7_0..7`), index 23 is `w7_7` and index 30 is
`z7_6`, so the charged canonical Q9 survivor `x23=x30=1` is exactly
`W7=x⁷`, `Z7=x⁶y` — the fibre point the Q9-witness review predicted
unobstructed (`10+7+1≡0` on `F₆`'s `x⁶` row; `T₈=6x⁸≡0`).  The Q8 vector
is the zero 32-vector in `y_names` order, so `C3=D3=W4=Z4=W6=Z6=0`.  Every
shard re-executes, inside the exec'd prefix, both
`source_rows(source_data, q9_survivor)==[0]*23` and
`transition_rows(q9_survivor, q8_survivor)==[0]*22`, so the cumulative
state is re-verified on the box in the source conventions, not assumed.

**Homogeneous, rank nine, and the whole fibre.**  `q7_rows` returns blocks
`row(F5,5), row(F4,4), row(G7,7)` — 6+5+8 = 19 rows on the 18 restored
values (`c6_0,c6_3,c6_6,d6_0,d6_3,d6_6` on the Frobenius support
`{y⁶,x³y³,x⁶}`, plus full `w5_*,z5_*`).  Each shard asserts `q7_b==[0]*19`
(homogeneity: the zero 18-vector is the parent's accepted point) and
`q7_rank==9`.  Affinity of the 19 rows over `F₃` is a *theorem* at this
state, proven here, not only sampled by the all-ones control: every
variable channel is Z-linear (`E`, `M`, `T`, divergences), the only
bilinear candidate `{C6,D6}` has degree 10 and cannot reach rows 4/5/7,
and every division taken inside the rows (`E_4/3`, `E_5/3`, `F_7/3`) has
identically-3-divisible variable part because the `C6/D6` support is
Frobenius (`∂x(x³y³)=3x²y³`, `∂x(x⁶)=6x⁵`, …), so division is Z-linear on
the affine family.  Hence the finite-difference matrix is exact, the RREF
kernel is the exact solution set, and the injective parameterization
(`RREF` basis has the identity on the nine free columns) makes the
enumeration all `3⁹=19,683` distinct points of the *whole* fibre — a
census, not samples.

I additionally solved the system by hand.  With the state above:
`E = 9x⁴ + ∂xC6 + ∂yD6`, `M = 10x⁶ + x²∂xC6 − x²∂yD6 − 2xy∂yC6`, so

- `F5 = E_5/3 = c6_3·x²y³ + 2c6_6·x⁵ + 2d6_0·y⁵ + d6_3·x³y²` — rank 4,
- `F4 = 3x⁴/3 + ∂xW5 + ∂yZ5`: rows `(a+1)w5_{a+1} + (5−a)z5_a` for
  `a=0,1,3,4` (the `x²y²` Cartier row is `3w5_3+3z5_2≡0` identically) —
  rank 4,
- `G7 = M_7/3 = 2c6_6·x⁷ + 2d6_3·x⁵y² + 2c6_3·x⁴y³ + d6_0·x²y⁵ +
  2c6_0·xy⁶` — one new pivot (`c6_0`) — rank 1 more.

Total rank 4+4+1 = 9, kernel `= {c6=0, D6=d6_6·x⁶ free, div(W5,Z5)≡0 on
the four non-Cartier rows}`, dimension 1+8 = 9.  This reproduces the
frozen rank and kernel dimension exactly and identifies the kernel
explicitly: five of the six erstwhile Q9 Frobenius spectators are forced
back to zero at Q7; `d6_6` and eight `W5/Z5` directions remain.

## 2. Carry derivation, rederived from the literal determinant (charge 2)

**Master identity.**  Direct expansion of `P_xQ_y−P_yQ_x−1` with
`P=x−x³+3U+9C+27W+81H`, `Q=y+3V+9D+27Z+81J`, checking every sign and
factor:

```text
det J−1 = 3·D1 + 9·D2 + 27·D3 + 81·D4 + 243·D5 + 729·X,
D1 = U_x+V_y−x²,                    D2 = A·V_y−U_yV_x + C_x+D_y,
D3 = M + W_x+Z_y,                   D4 = {C,D} + T + H_x+J_y,
D5 = Rmix + S,                      A  = U_x−x²,
M  = A·D_y+C_xV_y−U_yD_x−C_yV_x,    T  = A·Z_y+W_xV_y−U_yZ_x−W_yV_x,
Rmix = C_xZ_y+W_xD_y−C_yZ_x−W_yD_x, S  = A·J_y+H_xV_y−U_yJ_x−H_yV_x,
X  = {W,Z} + (C,D)×(H,J) cross + higher.
```

The `−x²`-absorptions are exact: `−9x²V_y` into `K=A·V_y−U_yV_x`,
`−27x²D_y` into `M`, `−81x²Z_y` into `T`, `−243x²J_y` into `S`.  With
`L1=D1/3`, `E=L1+D2`, `F=E/3+D3`, `G4=F/3+D4`, one gets
`(det−1)/243 = G4/3 + D5 + 3X`, i.e. exactly the charged
`R = G4/3 + S(U,V;H,J) + Rmix(C,D;W,Z)` with `3X≡0 (mod 3)`.  The
compiler's recursion (`E1d=E_d/3`, `F1d=F_d/3`, `G1d=G_d/3`,
`R_d=G1d+Rmix_d`, degrees 7…12) and its literal side
(`(det−1)_d/243`) are precisely the two ends of this identity at `H=J=0`,
each `divide_exact` asserting the integrality that the digit tower
requires; `assert recursive == direct` runs inside the per-index loop, so
the literal comparison charges every one of the 19,683 representatives,
and the degree-7 division re-verifies each point's own `G7` acceptance row
on the box.

**Closed form on the kernel (the whole result, by hand).**  On the kernel
of §1: `C=2x⁵`, `D=d·x⁶` (`d:=d6_6`), `W=W5+x⁷`, `Z=Z5+x⁶y`, `U=0`,
`V=x²y`.  Then, exactly over Z:

```text
E = 9x⁴,          M = 10x⁶,        N = {2x⁵, d·x⁶} = 0,
T = x²∂xW5 − x²∂yZ5 − 2xy∂yW5 + 6x⁸,
Rmix = 10x⁴·∂yZ5 + 10x¹⁰ − 6d·x⁵·∂yW5 .
```

Hence for every kernel point: `E_d=F_d=0` for `d∈7..12`; `G_8=6x⁸`,
`G_d=0` for `d∈{7,9..12}`; and

```text
R12 = 0,   R11 = 0,   R10 = 10x¹⁰ ≡ x¹⁰,   R9 = −6d·x⁵∂yW5 ≡ 0,
R8  = 2x⁸ + x⁴∂yZ5 (state-dependent),      R7 = 0.
```

This reproduces the frozen census identically: the constant coefficient
`1 = 10 mod 3` on `x¹⁰` is the cross-carry `C_x·Z_y = ∂x(2x⁵)·∂y(x⁶y)`,
i.e. the accepted degree-four row `div(C5,D5)≡x⁴` times the survivor's
`x⁶`.  I checked it against the raw transported records: shard 00 index 0
has `high` = 46 zeros with a single 1 at position 35 (degree-10 block
offset 25, `x`-exponent 10) and `r8=[0,…,0,2]=2x⁸` (the parent pointwise
values), and shard 01 index 757 has the identical `high` with a different
`r8` — exactly the hand formula `2x⁸+x⁴∂yZ5`.  The direct side is also
integral by hand: e.g. `(det−1)_10 = 243·10x¹⁰ + 729·{W,Z}_10` and
`(det−1)_12 = 729·7x¹²`, so `R12 = 21x¹² ≡ 0` — the two byte streams agree
only after the mod-3 `row` reduction, which both sides apply.

**Erratum-class sweep.**  The prior Q11/Q10 defect was an omitted divided
single/double-Frobenius summand (`{UF,·}/3`, `{UF,VF}/9`).  Here all six
`frob` values are zero, so every erratum-class term vanishes identically —
but they are structurally present anyway (`U=U0+UF`, `V=V0+VF` inside
`canonical_source`, `L1=L/3` and `K` carry them), and the corrected Q10
prefix that this chain consumes attaches `MF6q` and `Kdoubleq` explicitly.
The only divided-Frobenius channels alive at this branch are `∂xC6/3,
∂yD6/3` in `E_5/3` and `M_7/3` in `G7` — both carried, both re-derived in
§1.  The per-state literal-determinant equality in degrees 12…7 makes an
omitted summand in those degrees impossible without a crash.  No omission
found.

## 3. Q6 elimination and fibre-independence of degrees 12..9 (charge 3)

**Rank seven, termwise.**  The divergence of `(H,J)` homogeneous of degree
7 has degree-6 rows `(a+1)h_{a+1} + (7−a)j_a`, `a=0..6`.  Every row has a
unit coefficient (`a=0: h₁+j₀`; `a=1: 2h₂`; `a=2: 2j₂`; `a=3: h₄+j₃`;
`a=4: 2h₅`; `a=5: 2j₅`; `a=6: h₇+j₆`), and each row owns a variable no
other row touches, so the rank is exactly 7 on all seven rows — hand-
confirmed, matching the per-shard `q6_rank==7`, kernel dimension
`16−7=9`.  Full row rank means *every* right-hand side is hit, so every
Q7 kernel point has a nonempty 9-dimensional Q6 fibre; the RHS itself is
well-posed because `F_6 = 10x⁶+8x⁶ = 18x⁶ ≡ 0`, so `G_6` is integral on
the whole kernel.

**Degrees 12..9 are H,J-independent, at integer level.**  From §2's master
identity, the complete `H,J` dependence of `(det−1)/243` is:
`81·(H_x+J_y)/243` (pure degree 6), `243·S/243 = S` with, at this branch,
the *exact integer* identity `S = −x²J_y + x²H_x − 2xyH_y` (degree ≤ 8,
attained: `H=x⁷ ↦ 7x⁸`), and `729`-level `(C,D)×(H,J)` crosses that are
`3·(…) ≡ 0` after the division.  So in degrees 9–12 the residual rows and
the exactness of every division are unchanged by any integer digit choice
of `H,J` — representative changes inside the fibre can move `R6` (through
`(G_6+div)/3`) and `R7/R8` (through `S`), never `R12..R9`.  Two remarks
of precision: (i) the frozen 16-direction support certificate
(`q6_high_max_degree 8`, identical in all 27 shards and the aggregate)
covers the `S` channel and, by Z-linearity of `S`, extends from the basis
to all integer combinations; (ii) the second channel — `div(H,J)` confined
to the single degree-6 row of `G4` — is a structural degree fact not
separately certified in source; it is supplied here (finding 2).  Together
they close the charge.

## 4. Enumeration, aggregation, and the constant quadratic map (charge 4)

Ternary indexing (`index = Σ t_i 3^i`, asserted exhausted), residue-class
shards `range(i, 3⁹, 27)` — disjoint by residue, each of the 27 shards
carrying exactly 729 states; the aggregate asserts no duplicate index and
`set(records) == set(range(3⁹))`, coverage of exactly `0..3⁹−1`.  Shard
agreement asserts (identical kernel SHA `2052da9d…`, identical support
lists, ranks) all passed — verified 27/27 by grep on the transported
stdouts.  Width `46 = 13+12+11+10`; the ordered stream is by global index
and hashes to the frozen `6e4df883…` (report = freeze = aggregate.json,
textual).  The quadratic model is built from the 1+18+36 evaluations at
`0, e_i, 2e_i, e_i+e_j` (correct `F₃` finite differences) and then
*checked against every one of the 19,683 records*, so `quadratic_exact` is
an exhaustive identity, not an interpolation; the emitted term list —
degree 10, `x`-exponent 10, constant 1, nothing else — plus the check
forces every record to be the same 46-vector, which I confirmed on raw
records in two shards.  The labeling is right: `row()` orders coefficients
by ascending `x`-exponent (deepest-layer definition, §1), the degree-10
block starts at offset 25, and the nonzero coordinate 35 is `x¹⁰y⁰` — so
`R10=x^10` is literally correct, `high_zero_count 0`, histogram
`{10: 19683}`, and "every state first obstructs in degree ten" is exact
for the high window 12..9.  No quadratic term can have been lost: the
exhaustive equality check would have failed on any mismatch, constant or
not.

## 5. Cap obstruction and every wider inference (charge 5)

A fifth-level cap-seven correction pair `(A5,B5)` enters `(det−1)/243` as
`div(A5,B5) + 3(…)`: a divergence of a degree-≤7 pair has degree ≤ 6, so
no next-digit choice can touch the degree-10 row, and `R10=x¹⁰≠0` is
terminal for every enumerated state.  Stronger, and closing the one
hypothesis the report's single-sentence justification leaves implicit: at
this branch the mixed-carry coefficients are *exactly* `A=−x², u_y=0,
v_x=2xy, v_y=x²` (degree ≤ 2), so even hypothetical later restorations of
lower-degree level-4 or level-3 digit slots reach the fifth residual only
in degree ≤ 8 (`S`-type: `2+(k−1) ≤ 8`; `Rmix`-type with `C_x` capped at
degree 6 against degree-≤3 layers: ≤ 8; brackets at level ≥ 6 die mod 3).
Degrees 12..9 of the fifth residual are therefore immune to the *entire*
unexplored remainder of the digit system below this state, not only to the
fifth-level divergence — the branch is dead outright (finding 3, in the
producer's favor).

Scope attack, all directions: (i) the 13 other free directions of the Q8
affine zero locus — untouched, correctly disclaimed; the upstream chart
classification (3) is unreduced there and this census fixes its first
point only.  (ii) The six Q9 Frobenius spectators — *below this Q8 state*
they are in fact fully covered (they are six of the 18 restored variables;
the kernel forces five to zero and frees `d6_6`), so the report's
disclaimer is conservative rather than necessary in that direction; what
genuinely remains open is their interaction with the other Q8-chart
directions, where the chart was computed at pinned spectators (finding 1).
(iii) Other Q9 predecessors, the full cap-seven system, all-depth
lift/no-lift, counterexamples, JC2 — none claimed, none supported; the
report, freezes, README, and preregistration all carry the disclaimer.
The preregistered discriminator (exhaust, compare both constructions,
prove Q6 independence, test the quadratic presentation) is exactly what
was run and reported; a zero-free census was preregistered as the branch
kill, and that is the outcome obtained.  No overreach found anywhere in
the charged text.

## 6. Custody (charge 6)

Verified textually: FREEZE_SOURCE (preregistered, no result yet, git head
`2e6104a…`, compiler `7842ba69…`, aggregate `8ff06ec8…`, closure stream
`70c0710b…`, runner stream `0a8e03fd…`, package list `7ca55b9b…`);
RUNNER_MANIFEST's five entries repeat the compiler/aggregate/preregistration
hashes; SOURCE_CLOSURE's 20 entries agree with every in-code pin
(`5e181b09…`, `fbf327fb…`, `54d05ebf…`, `3837508e…`, `349ea509…`,
`64bbd0e1…`, `1fc18eeb…`) and cover the runpy-loaded bottom layer;
FREEZE_RESULT repeats the report/README/verifier/manifests/aggregate/
stream hashes and the execution window (Box02 `ip-172-30-0-186`, tag
`…T030036Z`, 03:01:09–03:01:24Z, rc 0), all consistent with `run.meta` and
the report; every one of the 29 stderr entries in OUTPUTS.sha256 is the
canonical empty-input SHA `e3b0c442…`; shard 00's stdout-printed
`output_sha256` equals its OUTPUTS entry; RESULT_MANIFEST covers the shard
tree via the OUTPUTS indirection, whose own hash it pins.

`OUTPUTS.sha256` records remote absolute paths
(`/home/ubuntu/jobs/<tag>/…`) because `run_remote.sh` hashes with an
absolute `find`.  The portable verifier strips exactly the
`…/results_<tag>/` prefix with an anchored `sed` before `sha256sum -c`
from inside the result directory; since every listed file lives flat in
that directory and the pattern is tag-specific, the normalization is
adequate for full integrity re-checking, not merely custody decoration —
but only a shell can run it (disclosed).  Residuals, none re-checkable
here: (a) every SHA-256 recomputation; (b) the run itself (rc, bytes)
trusted as transported; (c) the bottom three runpy links
(`compile_next_cartier.py`, `compile_full_c5_gate.py`,
`generate_corrected.py` + audits) carry no in-code SHA assert, and unlike
the corrected-shard runs this result tree transports no on-box
source-closure check log, so their on-box byte identity rests on the
frozen source archive hash (`d26cdd11…`) and the pinned upper chain
(finding 4).

## 7. Findings

No false identity, omitted term, missing hypothesis, or counting error was
found.  The smallest findings, none affecting the verdict:

1. (Wording) The scope sentence "does not cover … the six Q9 Frobenius
   spectators pinned to zero there" reads as if the census left them
   unexplored; below this fixed Q9/Q8 state they are in fact exhausted
   (five forced to zero by `F5/G7`, `d6_6` free in the kernel).  The
   disclaimer is only needed for their interaction with the thirteen
   other Q8-chart directions.  Conservative, not false.
2. (Wording/precision) "Q6 digits enter the following carry only in
   degrees at most eight" is attributed to the 16-direction termwise
   certificate; that certificate covers the `S` channel only.  The second
   channel — `div(H,J)`, confined to the degree-6 row of `G4` — is a
   structural degree fact used silently; it is proven here (§3), so the
   claim is true but its stated evidence was incomplete by one line.
3. (Favorable) The report justifies terminality only through the
   fifth-level divergence bound; at this branch the stronger statement
   holds (all unrestored digit channels cap at degree 8 because
   `A,u_y,v_x,v_y` have degree ≤ 2), so `R10=x¹⁰` kills every completion
   of the branch, not merely the next digit.  Worth recording at the next
   promotion.
4. (Custody) The three bottom runpy links are unpinned in code and this
   run transports no source-closure check log; on-box source identity
   below `compile_next_top_carry.py` rests on the frozen archive hash and
   the closure manifest.  Suggest the next producer either add SHA asserts
   at those links or transport the check log, as the corrected-shard runs
   did.
5. (Custody, disclosed) The result-freeze self-hash `30754347…` is
   corroborated only by the review charge until a successor pins it; and
   only the `G7` row of the 19 is re-asserted per enumerated point (via
   the degree-7 exact division) — `F4/F5` membership rides on linearity
   plus RREF, a gap closed by the hand linearity theorem of §1.
6. (Display, trivial) The report's display lists `R = G4/3 + S + Rmix`
   while both computed constructions set `H=J=0` (so `S=0` there); the
   `S` term belongs to the general identity whose `H,J` content is then
   bounded separately.  Harmless given the next paragraph, but a reader
   could think `S` was evaluated in the census.

## Promotable sentence

For the AS F-only `D=7` vertical branch at the frozen predecessor
`c5_5=2` (all other 29 coordinates zero), canonical Q9 survivor
`w7_7=z7_6=1` (i.e. `W7=x⁷`, `Z7=x⁶y`), and zero Q8 vector, the 19-row Q7
transition in the 18 restored digits (`C6,D6` Frobenius, `W5,Z5`) is
homogeneous of rank nine, its full `3⁹=19,683`-point kernel
(`c6=0`, `d6_6` free, `div(W5,Z5)≡0`) was exhausted in 27 disjoint
residue-class shards, on every point the recursively derived and literal
`(det J−1)/243` rows agree and equal `R12=R11=R9=0`, `R10=x¹⁰`
(hand-identity: `R10 = C_x·Z_y = ∂x(2x⁵)·∂y(x⁶y) = 10x¹⁰ ≡ x¹⁰`), every
Q7 state has a nonempty nine-dimensional Q6 fibre (divergence rank 7 on 7
rows) whose digits reach the fifth residual only in degrees ≤ 8
(`S=−x²J_y+x²H_x−2xyH_y` exactly, plus the degree-6 divergence row), and a
fifth cap-seven correction has divergence degree ≤ 6 — so every Q7/Q6
choice beneath this fixed Q9/Q8 state is terminal at the fifth carry, and
this licenses nothing about the thirteen other Q8-chart directions,
spectator-interaction with those directions, other Q9 predecessors, the
full cap-seven system, all-depth lifting, counterexamples, or JC2.

Next decisive discriminator: run this same next-high pipeline across the
remaining Q8 chart — the `3¹³` Kuranishi zero locus (and its canonical
digit-lift classification, tested only on 36 points so far) with the six
spectators unpinned at the Q8 stage — to decide whether the `x¹⁰`
obstruction is a branch accident or persists across the whole Q8 stratum
(the already-staged `as_fonly_d7_q8state_next_high_samples_20260825` case
is the natural vehicle).

CONFIRMED
