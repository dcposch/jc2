# K00 V20R2 valuation four jet fan: different-model hostile review (R1)

Reviewer: Fable 5 (independent adversarial lane)  
Date: 2026-08-29 UTC  
Review basis commit: `31777ce90994a106aade85064c0d868e32863f94`  
Producer basis commit: `e930fa90b8ee9d86220a2cff72fba94e04b20baa` (parent of the
review basis; every pinned input is byte-identical at both, hash-verified below)  
Lifecycle: `HOSTILE_REVIEW_COMPLETE / PASS_WITH_MINOR_REPAIRS`

## 0. Verdict

| # | Claim | Verdict |
|---|---|---|
| 1 | exact-valuation-four source/open conditions and raw grade calendar | `CONFIRMED` |
| 2 | reduced leading cone, rank-0/1/2 fan of `DQ(x)`, field-vs-closure qualifications | `CONFIRMED` |
| 3 | grade-12 exclusions of leading ranks one and two | `CONFIRMED` |
| 4 | old-plane next-rank-one grade-15 exclusion | `CONFIRMED` |
| 5 | next-rank-two grade-15 restriction `u=0` or `u^2=192v^2` | `CONFIRMED` |
| 6 | `R4-00`/`R4-02` literally, completely, reproducibly typed through grade 19 | `CONFIRMED` |
| 7 | source sensitivity and meaningful mutations | `CONFIRMED` |

All five numbered results of the producer's Section 0 are exact.  Four
repairs are required before promotion; all are provenance/replay-strength
repairs, none touches a mathematical conclusion.  The maximum safe statement
and the cheapest decisive successor are in Sections 10 and 11.

## 1. Custody and inputs

All hashes verified at review time on the review basis:

```text
be37360e22524c0f5e7a739753c237c3c94f71f0b5d44bfd9dcd89dddade134a
  xmodel/k00-r4-jetfan-provisional-sol56-20260829.md          (producer)
196b693a24914469a70feb4349b2c60465a45c1f98ed677e93a3698b6d03e6ee
  xmodel/k00-r4-jetfan-replay-sol56-20260829.py               (replay)
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/compile_contracted_source_v20r2.py
efffbe97ab962990cc2e3a4bf8077cb12cc911c43f71864427e8a4accd6081fc
  xmodel/k00-r2-full-rank-fan-coordinator-integration-sol56-20260829.md  (promoted v=2)
2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4
  xmodel/k00-r2-full-rank-fan-replay-sol56-20260829.py        (promoted v=2 replay)
```

Producer body seal re-verified: unique standalone `BODY-END`, body bytes
`10719`, body SHA-256
`3bb710d39c8fea9663bb1e6c1ed4d7c5b323a8741921b75aef2e8b844377bb40`.

The producer replay was run once (permitted, known desk-scale): it prints
exactly the Section-6 clean output, `K00_R4_JETFAN_REPLAY=PASS`,
`RUNTIME_SECONDS=3.888` on this host.  It was then set aside and **not**
used as an oracle.

## 2. Review protocol

I wrote a clean-room reconstruction in scratch outside the repository
(`/tmp/k00r4rev/`, five scripts, stdlib-only, exact `Fraction` and
Gaussian-rational arithmetic, no import of any producer code).  It parses the
frozen 569-tail JSON itself, applies the coordinate map read from the frozen
compiler (`C0=(1+d0)/256, C1=d1, C2=(1+d2)/16, C3=d3, C4=(3+d4)/8, C5=d5,
C6=1`; load shifts `Lambda^2 k10`, `Lambda^6 k6`, `Lambda^10 k2`; targets
`-Lambda^14 mu2` on row 2, `-Lambda^16 mu4` on row 4, `-Lambda^18 mu6` on
row 6, `-(Lambda^19/4) Jdet` on row 7; truncation `Lambda^20`), and rebuilds
the seven unloaded rows `R_i` and load rows `M_i` (K10), `N_i` (K6), `P_i`
(K2) from scratch.  Every branch identity below was then recomputed by full
series expansion on the stratum, with **strictly more symbolic freedom than
the producer replay**: the grade-7, grade-8, and grade-9 jet coefficients
fully free (18 extra symbols), and load columns `k10[0..5]`, `k6[1..3]`,
`k2[1..2]` symbolic.  Total review compute is a few seconds per script;
no Singular, no AWS, no network, no `jc2-lean` access, no repository write
other than this file.

## 3. Claim 1: source, opens, raw calendar — `CONFIRMED`

- The frozen compiler's column census matches the producer's source block
  exactly: `d0..d5` series indices 1–19 (so `d=Lambda^4 x+...` additionally
  types `d[1]=d[2]=d[3]=0`, which the producer's displayed expansion does),
  boundary zeros `k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0`
  (`FIXED_ZERO_BEFORE_SOLVE`), unit opens `k10[0]` and `Jdet[0]`
  (`unit_open_columns`), `C6=1`, 169 columns / 164 free.
- **Constant-term cancellation, independently verified:** `R_i(0)=M_i(0)=
  N_i(0)=P_i(0)=0` for all seven rows.  This is load-bearing and was *not*
  checked by the producer replay (its degree ledger scans degrees 1–6 only):
  pure-`C0/C2/C4/C6` tail monomials could have produced constants, which
  would have inserted `k10[j]`, `k6[j]`, `k2[j]` columns at grades `2+j`,
  `6+j`, `10+j` and destroyed the calendar.  They cancel exactly (this is the
  v=2 integration's Repair 2 re-proved at the reconstruction level).
- Exact degree censuses: `R`: {2,3,4},{2,3,4},{2,3,4,5},{2,3,4,5},{2,3,4,5},
  {3,4,5,6},{2,3,4,5,6}; `M`: min 2 all rows, cubics all rows, quartics rows
  2–7; `N`: {1,2},{1,2},{1,2,3},{2,3},{1,2,3},{2,3,4},{1,2,3,4}; `P`: linear
  all rows, quadratic rows 4–7.  Together with vanishing constants this
  reproduces the producer's first-arrival table completely and exactly:
  `Q:8, C3:12, C4:16 | M2:10, M3:14, M4:18 | N1:11, N2:15, N3:19 |
  P1:15, P2:19`, targets `mu2[j]:14+j (j=1..5)`, `mu4[j]:16+j (j=1..3)`,
  `mu6[1]:19`, `Jdet[0]/4:19`, every later load coefficient shifting by its
  series index, and nothing else arrives in the window (degree-5+ unloaded,
  degree-5 `M`, degree-4 `N`, degree-3 `P` all first arrive at grade 20+).
- Grades 0–7 of all rows vanish identically on the stratum (verified with
  free jets), so "all literal equations through grade 19" is the full
  `Lambda^20` truncation.  The producer's remark that `N1` occurs raw but
  vanishes on the reduced cone is verified: `N1_i` vanishes identically on
  the cone for all rows that have it (rows 1,2,3,5,7).

## 4. Claim 2: reduced cone and rank fan — `CONFIRMED`

With `A(q)=16q1-4q3+q5`, `B(q)=q0-4q2+2q4`, and the adapted global
coordinates `p = cone(a,b,u,v) + (B,0,0,0,0,A)`, my reconstruction gives the
exact global decomposition

```text
Q_i = alpha_i(u,v) A + beta_i(u,v) B + q_i(A,B),
```

with the producer's alpha/beta table reproduced coefficient-exactly, and

```text
Q_1+8Q_3 = (3/2048) A B          (alpha and beta parts cancel identically),
Q_4      = (3/524288) B^2 - (3/8192) A^2     (alpha_4 = beta_4 = 0),
Q_6      = 0.
```

**Independent two-line reduced-cone proof:** any common zero of the seven
quadrics satisfies `AB=0` and `B^2=64A^2`, hence `A=B=0`, over *any* field.
So the field-valued zero locus is exactly the 4-plane `{A=B=0}` — no hidden
leading component; the producer's fan is complete.  On the plane the four
nonzero 2x2 minors of `[alpha_i, beta_i]` are rational multiples of
`Delta=u^2+64v^2` (verified), giving exactly rank 0 at `u=v=0` (the old
plane `ell(s,t)=(2s,t/8,s,t,s,2t)`), rank 1 at `Delta=0, (u,v)!=0`, rank 2
at `Delta!=0`.  Field qualifications are handled correctly: over a field
without `i` the rank-one stratum is empty (`u^2=-64v^2` forces `u=v=0`), and
the rank-one computations over `Q(i)` kill every field point via the
embedding into a closure; the Section-4.2 branch exists only over fields
containing `sqrt(192)=8*sqrt(3)` and the `Q[r]/(r^2-192)` computation
transfers along `r -> either root`.  The `M2` image identity
`M2_i(x)=DQ_i(x)[A=-10v/3, B=10u/3]` is verified for all rows.  One
structural fact my reconstruction adds (used below): `M2_6` is exactly the
pure form `(5/2097152)B^2-(5/32768)A^2` (no cross or plane terms), while
`M2_4` and the row-1 combinations have nonzero `A,B`-cross terms — these
cross terms are precisely what the producer's `H4`/`kappa^2` identity
absorbs, and they vanish at old-plane arguments.

## 5. Claim 3: grade-12 exclusions of leading ranks one and two — `CONFIRMED`

**Rank one** (`u=8iv` and conjugate, `v!=0`).  Grade 9 with the next
coefficient fully free is exactly `alpha_i(x)A(y)+beta_i(x)B(y)`; at rank
one this is the single visible equation `B(y)=8iA(y)`, so `(A,B)(y) =
lambda(1,8i)` — the producer's parameterization is complete.  At grade 10 I
computed all five universal cokernel projections (rows 4, 6 and
`G_3+(1/8)G_1`, `G_5+(1/128)G_1`, `G_7+(1/1024)G_1`) with the grade-6
coefficient fully free and `k10[1],k10[2]` symbolic:

```text
G4: -(3/4096) lambda^2,   G6: 0,
c31: +-(3i/2048) lambda^2,  c51: -+(3i/16384) lambda^2,  c71: -+(3i/262144) lambda^2,
```

nothing else appears; `lambda=0` is forced (fourfold).  The producer's
displayed row `-(9i/2097152) v lambda^2` is reproducible as
`(3v/8)*[G_7+(1/1024)G_1]` at grade 10 — a position-rescaled true cokernel
row, valid since `v!=0`, but see Repair 2.  The grade-12 unit was then
re-verified **with the grade-7 and grade-8 jets fully free** and
`k10[1..2], k6[1..2], k2[1]` symbolic: `G_6,12 = +-(i/32)v^3` exactly, on
both conjugate branches.  This is the cone cubic
`C3_6|_(cone) = u(192v^2-u^2)/65536` (independently re-derived) evaluated at
`u=+-8iv`; a nonzero unit, so the cell is empty over any field containing
`i`, and it is empty for trivial reasons otherwise.

**Rank two** (`Delta!=0`).  Grade 9 forces `y` onto the cone (kernel zero);
grade 10 uniquely determines `(A,B)(z)=(10 kappa v/3, -10 kappa u/3)` (the
`M2` image identity; kernel zero, so no transverse freedom exists — the
producer's parameterization is complete); grade 11 has *identically zero*
cokernel projection in all five directions (verified with the grade-7
coefficient fully free).  At grade 12, with grade-7 and grade-8 jets fully
free, my reconstruction reproduces both displayed rows exactly:

```text
G_6,12 = u(192v^2-u^2)/65536,
G_4,12 = (3/32768)(u^3-448uv^2+64bv^2-bu^2-1024auv)
         + (25 kappa^2/131072)(64v^2-u^2),
```

including the `kappa^2` coefficient, which decomposes as pure-form part
`(25/393216)(u^2-64v^2)` plus `M2_4`-cross part `(100/393216)(64v^2-u^2)` —
an internal consistency check the producer never states but passes.

- `u=0` branch: `G_3,12+(1/8)G_1,12 = (1/4)v^2(v+3a)` and
  `G_5,12+(1/128)G_1,12 = -(3/64)v^2(v+2a)` verified exactly (`b`-free,
  jet-free); `a=-v/3` and `a=-v/2` contradict `v!=0` in any field.
- `u^2=192v^2` branch: **I derived the four projections independently**
  (the producer replay hardcodes this matrix; see Repair 1).  Substituting
  `u=rv` in `{c31, G4, c51, c71}`, each is `v^2` times an exact linear form
  in `(v,a,b,kappa^2)` over `Q[r]/(r^2-192)` — the divisions are legitimate
  (`v!=0` on the branch) and no nonlinear residual monomial exists.  Exact
  Gaussian elimination over the field `Q(8*sqrt3)` gives rank 3, pivots
  `(v,a,b)`, RREF rows `v=0`, `a=0`, `b+(25/12)kappa^2=0`.  The first row
  contradicts `v!=0`; the branch is empty.  The producer's four hardcoded
  matrix rows are exactly `(9/65536)` times my derived projections (in the
  order `c31, G4, c51, c71`) — the literals are faithful.

## 6. Claim 4: old-plane next-rank-one dies at grade 15 — `CONFIRMED`

On `x=ell(s,t)`, grades 8 and 9 vanish identically with all later
coefficients free; grade 10 is exactly `Q_i(y)` (verified), so `y` lies on
the reduced cone by the Section-4 argument; with `y` on the cone, grade 11
is exactly `DQ_i(y)[z]` for all rows (verified on-stratum; note this
identity needs `y` on the cone — with `y` free, `kappa`-polar terms
survive, so the producer's sequential phrasing is the correct one).  On
`u_y=+-8iv_y`, grade 11 gives `(A,B)(z)=lambda(1,8i)`; at grade 12 the same
five cokernel projections were recomputed with `x=ell(s,t)` present and the
grade-7/8 jets free: they equal the *same* constants times `lambda^2` as in
the leading case (all `s,t`-dependence, `kappa`-cross and load terms vanish
because the combo cross-forms `L_c, Mm_c` are multiples of `u,v`, which die
on the old plane) — so `lambda=0` is forced, i.e. "grade 12 forces the
following coefficient back onto the cone" is exact.  Then, strictly
strengthening the producer replay, I verified

```text
G_6,15 = +-(i/32) v_y^3
```

with the grade-7 coefficient **fully free** (all six components — the
replay restricts it to cone + particular + one transverse scalar), the
grade-8 and grade-9 jets fully free, and `k10[0..5], k6[1..3], k2[1..2]`
symbolic.  No displayed or omitted freedom can rescue the cell: it is empty.
The mechanism behind this robustness is structural and now verified:
`M2_6` is a pure `(A,B)`-form and `C3_6`'s trilinear polar `B3_6(x,x,·)`
vanishes identically for old-plane `x`, so row 6 at grade 15 cannot see any
jet beyond the displayed ones.

## 7. Claim 5: next-rank-two grade-15 restriction — `CONFIRMED`

On `Delta_y!=0`: grade 11 forces `z` onto the cone (kernel zero); at grade
12 all seven rows vanish identically on the particular
`(A,B)(w)=(10 kappa v_y/3, -10 kappa u_y/3)` (verified — so the particular
is exact and, the kernel being zero at rank two, complete).  Then

```text
G_6,15 = u_y(192 v_y^2-u_y^2)/65536
```

verified with grade-8/9 jets fully free and all load columns symbolic — and
in fact also with the `(A,B)`-part of `w` left *fully free*, so the identity
does not even depend on the particular.  Over a field this forces exactly
`u_y=0` (then `v_y!=0` from rank two) or `u_y^2=192v_y^2` (then `v_y!=0`),
the producer's dichotomy.  Two informative facts my reconstruction adds:
row 6 at grades 13 and 14 vanishes *identically* on this stratum (grade 15
is genuinely the first live row-6 equation), while row 4 at grade 14 is a
live five-term equation that remains imposed in `R4-02` — consistent with,
and covered by, the producer's "other grade-13–15 cokernel rows … remain
imposed".

## 8. Claim 6: the typed residual packets — `CONFIRMED`

The packet definition (`G_i,n=0` for `1<=i<=7`, `8<=n<=19`, plus the
displayed opens and boundary zeros, plus the stratum conditions) is complete
against the frozen compiler: every load and target that can arrive in the
window is in the equations (unknown census in the window: `d[4..15]`,
`k10[0..9]`, `k6[1..9]`, `k2[1..5]`, `mu2[1..5]`, `mu4[1..3]`, `mu6[1]`,
`Jdet[0]`; on the packets themselves the `d[15]` column — and in `R4-00`
also `d[14]` — multiplies only vanished functionals, a derived fact, not an
omission).  Grades 0–7 vanish identically on the stratum, so nothing below
the window is silently dropped.  Both packets are constructible (`rank
DQ(y)=2` is the open `Delta_y!=0` on the cone), disjoint (rank 0 vs rank 2),
and — given claims 2–5 — exhaust the grade-19 survivors of exact valuation
four; the Section-0 form of `R4-02` (`u_y(192v_y^2-u_y^2)=0` with rank 2) is
equivalent to the Section-5.2 branch form.  The `R4-00` entry point is
verified literally: for all seven rows,

```text
G_i,12 = Q_i(z) + kappa * polar_M2_i(x,z)
```

with `y=ell(s1,t1)`-independence, grade-7 jet independence, and load
independence all checked symbolically; row 6 is identically zero there, so
the system is six live affine quadrics in the six components of `z`.  No
target contaminates any equation used in claims 3–5 (targets first reach
rows 2/4/6/7 at grades 15/17/19/19; rows 1,3,5,7 are target-free through
grade 19, row 6 through grade 18).  The producer's refusal to normalize,
radicalize, or period-copy the packets is FALLACY-v2-conform (typed `OPEN`
residual, floor-vs-attainment respected, no periodicity inferred from
valuations two or five).

## 9. Claim 7: sensitivity and mutations — `CONFIRMED`

Producer-side: the custody gates and the in-memory `192->193` nonvacuity
control behave as documented (re-run observed).  Review-side, in my
independent pipeline, all of the following were performed and detected:

1. **Live tail mutation:** `+1` on the row-6 unloaded tail monomial
   `C4*C5^2*C6^4` changes the reconstructed cone cubic away from
   `u(192v^2-u^2)/65536` — detected.
2. **Live load-convention mutation:** `k6` shift `6->5` changes generic
   valuation-1 rows first at grades 7/8 (rows with/without `N1`) — detected;
   `k10` shift `2->3` changes them at grade 4 — detected (this is the
   promoted v=2 Repair-3 calendar point, `2+2v` not `2+3v`, re-observed).
3. **Live coordinate-map mutation:** `C4=(3+d4)/8 -> (1+d4)/8` breaks the
   constant-term cancellation in rows 2, 4, 6 — detected by the
   constant-census gate, demonstrating that the Section-3 cancellation is a
   real property of the frozen map, not a formality.
4. **`192->193`** on the derived (not asserted) row-6 cubic — detected.

## 10. Repairs required for promotion (none mathematical)

1. **Replay hardcodes the Section-4.2 matrix.**  The four quadratic-field
   rows in `leading_rank_two` are typed literals; the replay verifies only
   the RREF *of the literals*, not their derivation from the tails.  My
   derivation confirms they equal `(9/65536)` times the true projections
   `{c31, G4, c51, c71}` at `u=rv` divided by `v^2`.  Promotion should
   consume this membership (or a replay upgrade that derives the rows).
2. **Grade-10/12 `lambda`-forcing rows are prose-only.**  The replay never
   checks the rank-one forcing step at either level.  The producer's
   displayed grade-10 row `-(9i/2097152) v lambda^2` is the rescaling
   `(3v/8)*[G_7+(1/1024)G_1]@10` of a true cokernel row; promotion should
   record the clean forcing set
   `G_4@10 = -(3/4096) lambda^2` (leading) and its grade-12 old-plane
   analogue with identical constants, now independently verified.
3. **Replay's "raw homogeneous-degree calendar" check is min-degree-only.**
   The load-bearing constant-term cancellations `R_i(0)=M_i(0)=N_i(0)=
   P_i(0)=0` and the target arrival rows of the Section-1 table are
   unreplayed; both are now independently verified and should be recorded as
   consumed review facts.
4. **Wording:** Section 6's "the replay constructs the four rational
   quadratic-field rows" overstates item 1; and the Section-2 sentence
   "grades 10 and 11 become `Q(y)=0`, `DQ(y)[z]=0`" is correct only
   sequentially (with `y` already on the cone at grade 11) — my on-stratum
   check confirms the sequential reading and refutes the free-`y` reading.

## 11. Maximum exact statement safe to promote

Over any characteristic-zero field, on the exact normalized V20R2 source
with `C6=1`, `k10[0]=kappa!=0`, `k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0`,
`Jdet[0]!=0`, `d=Lambda^4 x+Lambda^5 y+...`, `x!=0`:

1. the reduced leading locus of the seven quadrics is exactly the plane
   `A=B=0`, with the exact rank fan of Section 4 above;
2. every leading rank-one and rank-two point dies at grade 12 (rank-one
   cells are nonempty only over fields containing `i` and die by the unit
   `+-(i/32)v^3`; the `u^2=192v^2` case dies by the `Q(sqrt192)` RREF
   `v=0, a=0, b=-(25/12)kappa^2`);
3. hence every grade-19 survivor has `x` on the old plane; there `y` lies on
   the reduced cone, next-rank-one dies at grade 15 by `+-(i/32)v_y^3`, and
   next-rank-two survivors through grade 15 satisfy `u_y=0` or
   `u_y^2=192v_y^2` with `v_y!=0`;
4. the exact residual through grade 19 is the disjoint constructible union
   `R4-00 ⊔ R4-02` as typed by the producer, with every literal equation
   `G_i,8..19` imposed, and with the verified `R4-00` grade-12 entry system
   `Q(z)+kappa*polar_M2(x,z)=0` (six live rows).

No attainment, no nonemptiness of either packet, no scheme-theoretic
(nilpotent) claim, no arc or map claim, no statement about valuations 3 or
5, and no periodicity transfer are licensed.  Formal jet data are not a map;
a floor is not attainment.

## 12. Cheapest decisive successor

Both successors are desk-scale with exactly this review's machinery; no AWS
discriminator is needed yet.

1. **`R4-02` branch closure (preferred).**  On each branch (`u_y=0` and
   `u_y^2=192v_y^2`, the latter over `Q[r]/(r^2-192)`), impose the
   target-free projections — rows `c31, c51, c71` and rows 4, 6 — at grades
   13–18: row 4 at grade 14 is already a live five-term equation (computed
   here), grade 16 brings the nonvanishing `C4_i(ell)` inhomogeneities
   (`C4_i(ell)!=0` for all rows except row 6, verified), and rows 1,3,5,7
   stay target-free through grade 19.  This either kills both
   one-parameter branches or produces an exactly typed surviving family.
2. **`R4-00` entry solve.**  Solve the verified six-quadric grade-12 system
   in `z` over the `(s,t,kappa)` base exactly (it is affine-quadratic with
   the known `(A,B)`-structure), then split `z` by the same reduced fan.

If either successor stalls at desk scale, the frozen AWS packet is: pinned
tails (`d72f774c...`), the branch ideal generators as typed here, `dp`
order over `Q` (adjoining `r`, `r^2-192` where needed), eliminate the jet
variables grade by grade through 19, decide emptiness; no other computation.

## 13. Review compute and firewall

Independent scripts: structure/cone census, leading branches, old-plane
branches, stratum/mutation battery, residual info — each finishing in
0.3–1.5 s, far under desk caps.  No Singular, no AWS job, no web request, no
external model, no `jc2-lean` access.  Scratch confined to `/tmp/k00r4rev/`.
This review created exactly one repository file (this report) and edited no
canonical or existing artifact.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `21336`.
- Body SHA-256:
  `220569e13dd5fbd14baffb53951992dbacbf5975e3c5a91795dced556ccf09d0`.
- Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`.
