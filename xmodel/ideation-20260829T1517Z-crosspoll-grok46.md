# Cross-pollination falsification — Grok 4.6 — round `20260829T1517Z`

Lane: Grok 4.6 (xAI), equal-standing adversarial synthesis after blind
collection. Lifecycle: post-blind, pre-synthesis. This memo is not an
ideation submission and does not reopen the blind round. Bare `G2` is
not used. Identity: Grok 4.6. Basis:
`40c1ab3448209e3d87173feb947a733f6fe54f7f`.

## 0. Custody

All charged full-file SHA-256 values were recomputed on disk before any
other analysis and match the packet exactly:

```text
fc6a6843545119a5e184755bf5a26b4edce0ae8fbe912935532704608a0c312e
  xmodel/ideation-20260829T1517Z-crosspoll-packet.md
  body 8351 / e6963ce96110f8f0f01d568da7ca5e0fca22242099e33957b245f4ed5c399fa5
4d51f32938de517f5edaa76a60a0ef2ce5036a872f631fce040585893e78045b
  xmodel/ideation-20260829T1517Z-sol56.md
  body 21571 / fccf25179ff06775e2fc5df825a454f6b0d93329cb606bd484e995ce696c0c68
8790a5e95627c8d2d113980be44df4c380a43d6413c4e6a3cc6b85b12afc4f37
  xmodel/ideation-20260829T1517Z-fable5.md
  body 22449 / cb03b90112e8670583cd86a611f3cc562f0a9e5c1473849c6a9add5465d118d1
b01c48821d22a3425861b172693a8c4f0e9e0ad45c6f5360da2ca485605d700d
  xmodel/ideation-20260829T1517Z-grok46.md
  body 34124 / f809f40262f55702f43d680faf019d9f371db5ad124672c756294b5475eb3545
7d5453672b51dcc6ee47859c8336a7f77c4840891ca021ef066a20a18a895e7a
  xmodel/ideation-20260829T1517Z-opus5.md
  body 35263 / ce6be25440230d89cac05ac5cb6717199120a9fd4ab6bf822e6297d152b56aed
1ec95a45d97658fbd3b2464831deb768ee19574feefc8bb9dcac656d5f79bb2e
  xmodel/k00-grade4-rank0-plane-opus5-hostile-review-grok46-40c-20260829.md
  body 25176 / 41da5999a230115a8a63bc0b7793534dd9ab39800aa5ed77ce493381cbb479c2
068ed91bae52d04aefb0fe5b941607f2918491d9808891fccf9846ce54fd9bad
  xmodel/td12-b25-resrow-sol56-hostile-review-opus5-40c-20260829.md
  body 37413 / 2e5a062fc0dc2e49c3fa5596d41c165aaead03ac91736d0ead040bd48a31d59c
```

The TD12 review has no `BODY-END` marker; its body is the bytes before
the literal `## Seal` heading, matching the declared 37413 /
`2e5a062f...`. State packet
`648acf8ba6d8cd2b498d7a0825fc0e239044a4270e0a928009811550806d3449`
and roundview
`72284172888e3c8ed38d9a619ac195c5060bd0b7dd5abf1b728634e0aa4cfdad`
were rehashed and match. Frozen HEAD (verified `git rev-parse HEAD`)
is `40c1ab3448209e3d87173feb947a733f6fe54f7f`. `FALLACY-v2.md` is
`e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5`.

Read set: the packet; all four blinds in full; both named post-blind
reviews in full; the state packet and ROUNDVIEW/v1 as charged context;
atlas
`d7ec6d18d58265421ff315fa00e38cd32992ac12f7d8166cf6c436e23bf06501`
`P6_literal_rows_through_grade6` plus `ring_variables` (exact_terms
only); `SOURCE_COLUMNS.json`
`2e8ceeb42dcc41752f82fe1df866c28b33e289097b065bf965db25574230919c`;
reviewed valuation-one typing in
`xmodel/max12-812-order2-k00-v22r1-first-weighted-stratum-hostile-review-20260827.md`
and the 1349Z higher-valuation sentence; sibling `(nu,kbar)=(17,13)`
from the charged inhomogeneous-row note; the 1224Z Grok cross-poll
for output shape only. No other `20260829T1517Z` cross-poll, peer
prompt, log, run record, or post-packet report was opened. A directory
grep displayed the filename of a later S-bridge review prompt; that
file was not read. The concurrently named Fable G5 two-input lane was
not opened.

No web, AWS, canonical edit, commit, push, or `jc2-lean` access of
any kind. Desk algebra: independent sparse `Fraction` reconstruction
of grades 0–6 from `exact_terms`, peak RSS 150 MB, CPU user 0.20 s
(G5) + 0.3 s (G6 linear test), under the 60 s / 1 GiB cap. No
Groebner basis, no Singular, no Opus `/tmp/op5id/` execution.

Disclosure. The blind lane `ideation-20260829T1517Z-grok46.md` and the
G4 review `...hostile-review-grok46-40c-20260829.md` are prior products
of this same model. Treat them as two opinions among four blinds plus
one already-sealed review, not as prior art belonging to this memo.
Self-agreement is not evidence. This session's G5 reconstruction is
`VERIFIED-HERE` and needs a different-model check before promotion.

Evidence tiers:

- **PROMOTED** — packet-charged, different-model reviewed.
- **REVIEWED** — the two named post-blind reviews.
- **PROVISIONAL** — exact producer, different-model review outstanding.
- **PACKET** — sealed-packet statement, not itself a theorem.
- **BLIND-OPINION** — one or more of the four lane reports.
- **VERIFIED-HERE** — desk identity from atlas `exact_terms` this session.
- **CONJECTURE / PROPOSAL** — unproved packaging.

Firewall, binding on every line. A cv flag is not a physical place and
is not a cover series. `REPRESENTATIVE` is not `FULL_ACTUAL_EXIT`. The
latter aliases `FULL_ACTUAL_FIRST_SEPARATION` and is a floor, never
attainment. A lower bound is not exact. `d*_1=0` is the higher-valuation
leak, not a valuation-one point. A projection to a plane is not the
full-coordinate locus. A linear-block identity is not a tower of rows.
If no safe replacement exists, the report returns typed `OPEN`. No new
exit price is asserted, so `charge_basis` is absent.

---

## 1. Deduplicated table

Fingerprint is (object, exact discriminator), not (label, proposing
lane). Independent convergence is a note, not an extra mechanism.

| ID | Object | Discriminator | Source | Label |
|---|---|---|---|---|
| RAD-ID | In any commutative ring, `sqrt(I+J)=sqrt(sqrt(I)+J)` | Expand `(x^n-j)^m`; converse from `I ⊂ sqrt(I)` | textbook; Sol Card 1 | `KNOWN` identity; **VERIFIED-HERE** as scheduling |
| RAD-UNIT | `I+J=(1)` iff `sqrt(I)+J=(1)` | 1 is radical-closed | RAD-ID | `KNOWN`; kills geometric unit-divergence |
| RAD-GEO | Same point set, same min primes, same Krull dim of `V(I+J)` vs `V(sqrt(I)+J)` | Nullstellensatz over an algebraic closure | RAD-ID | `KNOWN` |
| RAD-DIFF | Nilpotents, embedded primes, multiplicity, Fitting of modules, lifts through `sqrt(I)/I` | not determined by the radical | RAD-ID | `KNOWN` remainder; **not** a point-set split |
| FABLE-DIV | Stage-1 nonempty and stage-2 unit | contradicts RAD-UNIT | Fable Card B | **REFUTED** as geometry; keep nilpotent-lift *language* only if the point set is nonempty |
| GROK-DIV | “Unit on either input” as if the two G5 ideals can disagree | contradicts RAD-UNIT | Grok-blind Card 2 | **REFUTED** as geometry; Fitting-rank comparison on a *nonempty* gate is the valid remainder and is unarmed here |
| G4-CF | `phi(Lambda_{4,r})=Q_r(u-mu)`, `mu=(s^2,st/8,16t^2,0,0,0)` | generatorwise from `exact_terms` | REVIEWED G4 | `KNOWN` / reviewed |
| G4-RAD | `sqrt(I4)=(RA,RB,zk-1)` prime, dim 13, `A^{12}×G_m` | Singular + domain certificate | REVIEWED G4 | `KNOWN` / reviewed |
| SQ-LAW | `A=2st`, `B=s^2-64t^2`; `B±8i A=(s±8it)^2` | rewrite of `(RA,RB)` | Sol Card 1 | `KNOWN` coordinates of G4-RAD; unused by the G5 kill |
| G5-AFF | After `phi`, G5 is degree `≤1` in `(v,k10_0)` jointly; `d*_4` and `k10_1` absent 7/7 | support + degree | Opus §3.2; VERIFIED-HERE | `NEW` as G5 fact; term counts `42,49,57,53,64,33,61` match the reviewed G4 census |
| G5-SHIFT | G5 `v`-linear block `=` G3 `u`-linear block at `w=u-mu`, 7/7 and 42/42 | coeff extraction | Opus §3.2; VERIFIED-HERE | `KNOWN` producer claim, now desk-confirmed |
| G5-PHI | On W4: row 6 `=0`; row 4 `= (3/32768) formA`; row 3 `− (−1/8)` row 1 `= (3/2048) formB`; rows 5,7 extras `= (−1/8)` and `(−1/128)` of that Phi3 | exact `Fraction` | Opus §3.3; VERIFIED-HERE | `NEW` confirmed |
| G5-BR | `V(formA,formB)={X=Y=0}∪{s=t=0}∪{s=8it,Y=−8iX}∪{s=−8it,Y=8iX}` | `t formA − s formB = 2(s^2+64t^2)XY` plus square identities over `Q(i)` | Opus §3.4; VERIFIED-HERE | `NEW` confirmed; minus-branch `formA=−8i formB` is the conjugate of the plus identity |
| G5-PROJ | On `D(k10_0)`, every branch except `s=t=0` is empty | self-similar `k0·(t(3s^2−64t^2), s(s^2−192t^2))=0`; conjugate rank-1 elim leaves `k0·(unit)·t^3 X` | Opus §3.5; VERIFIED-HERE | `NEW` confirmed as a **projection** theorem |
| G5-FIBRE | Fibre over `s=t=0` is nonempty and is not a single point | witnesses `u=0` and `u=(4,1,1,0,0,−16)`, both with `v=0`, `k10_0=1`, grades 0–5 | Opus 3.5; VERIFIED-HERE two points | **repair**: the full-coordinate locus is not `{d*_1=0}` as a point |
| G5-VAL1 | Normalized val-1 prefix is `d_i=Lambda x_i+O(Lambda^2)`, `x≠0` | reviewed V22R1; 1349Z “origin of `x`-space is the higher-valuation leak” | reviewed K00 | `KNOWN` typing; `d*_1=0` is **not** val-1 |
| G5-COLLAPSE | Opus unreviewed point-set claim | this memo §2 | Opus §3 | `PASS_WITH_REPAIR` |
| RENORM | Full row identity `G_{g+2}=G_g(shifted)` as a tower | G6 after `phi` has `deg(v)=2` and `k10_1`; not G4 at a shift | Fable 3.1 | **REFUTED** as a tower; G4=G2(w) remains |
| SHIFT-LAD | `G_{g+2}=G_g(shift)+k10` as a tower | G6 `x`-linear `=` G4 `v`-linear at `w` (42/42), but G6 is quadratic in `v` | Opus 6.1; VERIFIED-HERE | **PARTIAL**; do not extrapolate |
| POLAR | Even grades after G4 are translated `V(Q2)` | G6 is not a quadratic in a shifted even jet; `d*_5` vanishes, `v^2` does not | Grok-blind Card 1; VERIFIED-HERE | **REFUTED** as a functor past G4 |
| THICK | Fitting ranks of G5 on `I4` vs `sqrt(I4)` as a geometric split | RAD-UNIT on the val-1 open, which is empty | Grok-blind Card 2 | `SCOPE-CONFLICT` on this gate; protocol kept for a later nonempty scheme |
| COTAN | Reduced affine cokernel/Fitting of G5 | existence already decided by G5-PROJ+G5-VAL1 | Sol Card 1 | `DUPLICATE` of the G5 gate for existence; Veronese/Fitting leftover only for the origin fibre / nilpotents, not a val-1 job |
| STAGED | Radical-input first, then scheme | RAD-ID licenses the order; Fable’s impossible branch does not | Fable Card B | staging `KNOWN`; impossible branch `REFUTED` |
| ADMIT | Is `d*_1=0` a val-1 point? | G5-VAL1 | Opus Card B | **resolved**; not a launch |
| S-RES | `kbar_S mod 17` places an S16 resonance | sibling `(nu,kbar)=(17,13)` from charged T1 note; MST-4 if the S row is typed | Fable Card A | **conditional corollary**, not a new residue calculus; S landing still unreviewed |
| WARD | Full `G_a` orbit of `x↦x+c` as transgression | top `c`-coefficient in known Jacobian syzygies? | Sol Card 2 | `NEW` composition of a `KNOWN` gauge; interface (`PairRef`) absent |
| ROWPROP | Pairwise proportional unknown-block rows in the td12 cascade | unknown block unbounded without a declared finite window | Opus Card C | `SCOPE-CONFLICT`; K00 G5 proportionality is a different finite block |
| HERM | Count `3i−2` Hermite slots vs 1-dim T1 | no declared ring map | Grok-blind Card 3 | `OPEN`; slot-count is not a transgression |
| J17 | `R_17=−S_17'` identically | product rule at `j=kbar` | REVIEWED RESROW | `KNOWN` / reviewed; stop descendants |
| J42 | First possibly nonvacuous **resonant** row | needs `P_1..P_42` and unpinned `C_17` | REVIEWED R-A, R-B | `KNOWN` blocked; `OPEN(WINDOW-INDEX-B25)` |
| LAND | `TD12-U1-ACTUAL-LANDING` | occurrence in costume | PACKET | `DUPLICATE` of P1; does not outrank it |
| CAPRUN | argv-only wait-authoritative capped runner | four independent selections | all four blinds | `NEW` systems object; independent convergence |

Preserved independent convergence, not extra objects: stop homogeneous
window / `j=17` descendants; do not launch `j=42`; keep B and S
route-separated; bank finite-s; stop `TWIN-ORDER`; K00 rank 3–5 charts
stay stopped; no AWS math; no `jc2-lean`. All four blinds choose one
repo-owned wait-authoritative helper: that is one systems object.

---

## 2. `G5-COLLAPSE` — `PASS_WITH_REPAIR`

### 2.1 Reconstruction (not Opus scratch)

Declared ring map, coefficient field `Q`. Atlas `ring_variables` is
component-major 33-generator `PRIOR`; matching names are not a map.
Working images, jet-major:

```text
phi(d0_1,...,d5_1) = (2s, t/8, s, t, s, 2t)
phi(di_2)=ui,  phi(di_3)=vi,  phi(di_4)=xi,  phi(di_5)=yi
phi(k10_0)=k0, phi(k10_1)=k1, phi(k10_2)=k2
```

Unmapped names raise `KeyError`. Polynomials rebuilt from `exact_terms`
only; stored `sha256` and term counts matched 49/49. Positive controls:
G2 and G3 vanish identically on `Pi` with `u` free (7/7, 7/7); G4
closed form holds 7/7; mutating `16` to `15` in `mu` breaks 6/7 G4
rows; G4 vanishes on W4 (7/7). Plane mutation `t/8 → t/7` destroys G5
affine-without-`x` (1/7 remain).

### 2.2 Confirmed algebra

1. Affine-linearity in `(v_0..v_5, k10_0)` and disappearance of
   `(d*_4, k10_1)`: 7/7. `k0` survives in rows 1,2,3,5,7; `v` in all
   but row 6; row 6 is identically zero on W4.
2. Shifted grade-three coefficient matrix: 42/42 slots.
3. Base residuals: `formA = 64 s X^2 + 128 t X Y − s Y^2`,
   `formB = 64 t X^2 − 2 s X Y − t Y^2`, `X=u3−u5/2`,
   `Y=u2−16t^2−u4`. Row 4 `= (3/32768) formA`. The extra of
   row 3 versus `(−1/8)` row 1 is `(3/2048) formB` (Opus Phi3);
   extras of rows 5 and 7 are `(−1/8)` and `(−1/128)` of Phi3.
   `b`-parts of rows 3,5,7 *are* proportional to row 1; `c`-parts
   are not, and that mismatch *is* Phi3. Identity
   `t formA − s formB = 2(s^2+64t^2)XY` holds. Over `Q(i)`,
   at `s=8it`, `formB = −t (Y+8i X)^2` and `formA = 8i formB`.
   Four-branch decomposition is exhaustive.
4. On `D(k10_0)`: self-similar `X=Y=0` collapses to
   `k0·(5/4096) t (3s^2−64t^2) = 0` and
   `k0·(5/65536) s (s^2−192t^2) = 0`, hence `s=t=0`. Conjugate
   plus branch: 15/15 of the `2×2` `v`-minors of rows 1,2 vanish;
   the `k0`-free residue after eliminating `v` is 0; the surviving
   `k0` coefficient is a nonzero `Q(i)`-multiple of `i t^3 X`
   (displayed sign depends on the elimination combination; Opus
   `−15/16384`, this session `+15/16384` for `b·row1 − a·row2`).
   With `t≠0` this forces `X=0`, hence the self-similar case,
   hence `s=t=0`, contradiction. Minus branch: 15/15 minors vanish;
   it is the `Q`-conjugate. Nonzero `(s,t)` on the self-similar
   branch with `k0=1` fires five of seven G5 rows. Reviewed G4
   witnesses W1, W2 fail G5 (6 nonzero rows). Exact witnesses
   above `(s,t)=(0,0)` with `k10_0=1`, grades 0–5 simultaneously
   zero: `u=0,v=0` and `u=(4,1,1,0,0,−16), v=0`.
5. Precise theorem: the **projection onto the leading two-plane**
   is the origin. The full-coordinate locus is not a point.
6. Ideal/radical/dimension: no Groebner this session. RAD-UNIT
   implies the val-1 *open* `(s,t)≠0` is empty for both scheme
   and radical inputs. The *whole* G5 ideal with localizer is
   **proper** (two witnesses). Fibre dimension over the origin
   is typed `OPEN`. Second method: direct substitution of
   witnesses and mutations, plus the `Q(i)` square identities,
   with no ideal machinery.

### 2.3 Maximum safe theorem

Work over an algebraic closure. Consume the promoted G3 incidence
`V(B,P3)=Pi × A^6_u` and the reviewed G4 identities
`phi(Lambda_{4,r})=Q_r(u-mu)` and `sqrt(I4)=(RA,RB,zk−1)`. After the
name-declared map `phi`, the seven literal grade-five rows are affine
in `(v,k10_0)`, independent of `(d*_4,k10_1)`, and the `v`-linear
block equals the grade-three `u`-linear block at `w=u-mu`. On the
reduced grade-four locus W4, the unknown-free conditions are equivalent
to `formA=formB=0`. On `D(k10_0)`, every W4-point with `(s,t)≠0` is
excluded. Hence the projection of the reduced G5 locus onto the
leading two-plane is the origin. The fibre over the origin is nonempty
and contains at least two distinct `u`-points. This is a point-set
statement on the reduced input; by RAD-UNIT the scheme input cannot
create val-1 points that the reduced input excludes, and cannot be
unit while the reduced input is proper.

### 2.4 Source-scope consequence

Frozen source semantics, not analogy. Reviewed V22R1 writes the
normalized valuation-one prefix as

```text
d_i = Lambda * x_i + O(Lambda^2),    k10 = kappa + O(Lambda),    kappa != 0
```

with `C6=1`. Atlas `d*_1` are exactly those `x_i` (`SOURCE_COLUMNS`:
kind `d`, `series_index=1`, `first_Lambda_grade=1`, `FREE`). The
column table does not forbid `x=0` as a coefficient, but the
valuation-one *prefix* does: reviewed 1349Z, “the origin of `x`-space
is the higher-valuation leak `v(d)>1`, not a valuation-one point.”
Therefore a confirmed projection of the leading two-plane to the
origin **kills the complete normalized valuation-one, `C6=1`,
`k10_0≠0` K00 seed at grade five**. Other coefficient valuations,
the origin fibre as a `v(d)>1` jet, finite jets as maps, arcs,
polynomial maps, full-`P6`, and JC2 stay outside the claim.

Opus Card B is answered: `d*_1=0` is inadmissible *as val-1*, and
admissible *as a higher-valuation leak*. The protected val-1 seed
dies. Avenue 36 is not closed: a different valuation remains, untyped
as a replacement seed.

### 2.5 What fails in the producer prose

- “The locus is `{s=t=0}`, i.e. `d*_1=0`” identifies a projection
  with a full-coordinate point. Opus’s own nontrivial-`u` witness
  refutes the identification. Repair: projection theorem plus
  nonempty fibre.
- Conditional Avenue-36 lowering “to a single point” is the same
  conflation. The plane parameters die; the jet does not become
  0-dimensional by this argument.
- Leaving source typing `OPEN` was correct at ideation time; frozen
  reviewed semantics now fill it. Do not fill by cap.
- No scheme-primary decomposition was run. Do not promote a
  nilpotency statement at G5.

**Verdict: `PASS_WITH_REPAIR`.**

---

## 3. Direct attacks

### 3.1 Radical versus scheme

**Identity.** Let `I,J` be ideals in a commutative ring `R`. Then
`sqrt(I+J)=sqrt(sqrt(I)+J)`.

`I ⊂ sqrt(I)` gives `I+J ⊂ sqrt(I)+J`, hence one inclusion of
radicals. Conversely, if `x^n = a+j` with `a^m ∈ I` and `j∈J`, then
`(x^n−j)^m ∈ I`. Expanding, `x^{nm}` differs from that element by
terms in `J`, so `x^{nm} ∈ I+J`.

**Unit.** `I+J=(1)` iff `1∈I+J` iff `1∈sqrt(I)+J` iff
`sqrt(I)+J=(1)`, because `1` is a unit and radicals do not create
units. Same properness, same emptiness of `V(·)` over an algebraic
closure, same minimal primes, same Krull dimension of the support.

**Can still differ.** Nilpotent structure of `sqrt(I)/I`, embedded
associated primes, multiplicity, Fitting ranks of modules over
`R/(I+J)` versus `R/(sqrt(I)+J)`, and liftability through the
nilpotent filtration.

**Consequence for this round.** Fable’s “stage-1 nonempty, stage-2
unit” and Grok’s “unit on either input” as a possible geometric
split are **errors**. Redesign radical-first: the reduced input
decides geometric existence and unit/properness for both variants.
Retain infinitesimal/Fitting language only for a gate whose reduced
support is nonempty. On the val-1 open that support is empty, so
Fitting is moot there. On the origin fibre it is a possible later
job, not a val-1 job.

Sol’s scheduling theorem is the only correctly typed of the three
geometric readings.

### 3.2 Shift / renormalization

Already verified, and not a tower:

```text
Lambda4 = Lambda2 at w=u-mu
G5 v-linear = G3 u-linear at w
```

Cheap G6 linear-coefficient test (packet-licensed), after mapping
`d*_5` so the ring map is declared:

```text
G6 x-linear  =  G4 v-linear at w     7/7 rows, 42/42 slots
G6 after phi: deg(v)=2, deg(x)<=1, deg(y)=0, k10_1 present, k10_2 absent
```

**Reconciliation.** `K00-RENORM`, `K00-POLARIZATION-SHEAR`, and
`K00-SHIFT-LADDER` are **not** one mechanism.

- RENORM as full-row period-two identity is **false** at G6.
- POLARIZATION-SHEAR as an even-grade translated-`Q` functor
  **stops at G4**. G6 is mixed (`v^2`) and is not `Q(w−mu_6)`.
- SHIFT-LADDER as “each grade is an inhomogeneous linear problem”
  is **false** at G6 (`deg v=2`). The surviving fact is a
  **linear-block covariance** of the previous odd jet, plus the
  G4=G2 identity. A partial match must not be extrapolated.

If val-1 is already killed, G6 work on this plane is not a val-1
kill window. It remains a mechanism discriminator (already fired)
and a possible higher-valuation job on the origin fibre, which is
outside the val-1 claim. Do not register a G6 Groebner against
val-1. Do not skip G6 for a higher-valuation seed by quoting a
dead functor.

This lane’s own Card 1 is the functor just killed. Card 2’s
geometric split is the RAD-UNIT error above.

### 3.3 TD12 first resonance and S route

Reviewed MST-4: whenever the graded row is of the displayed
`(ROW_j)` shape with `O=kbar−D`, the two coefficients coincide iff
`j=kbar`, and then `R_kbar=−S_kbar'` identically. This uses none
of `nu=25`, the pattern of `p`, or T1. It does use C2’s landing.

Sibling data, charged, not analogized from B values:
`(nu,kbar,D)=(17,13,17i)`. Then `0<13<17` and `gcd(13,17)=1`, so
**if** the same terminal reduced-deviation recurrence is typed for
S, `j=13` is automatically the first resonance and the unique
exact-derivative row. That is a **conditional corollary** of MST-4,
not a new calculation.

It is **not** the S landing/deviation bridge. That bridge is still
unreviewed (producer seal failed). Until the S row is declared with
the same `O=kbar−D`, the corollary is `OPEN`. Fable’s Card A then
likely lands in outcome (iii) (in-window and vacuous) *if* the row
types, and in (iv) if it does not. Do not analogize `L_j` from B
to S by matching the words `kbar` and `nu`.

For B `j=42`: include unpinned `C_17` (reviewed R-A). Do not
identify the `P_a` index with window depth (reviewed
`OPEN(WINDOW-INDEX-B25)`). No packet licenses a `j=42` lane.

### 3.4 TD12-GA-TRANSLATION-WARD

Source translation `x↦x+c` is, on the S side, a provisional WLOG
gauge arranging floor coordinates. An identity that holds for every
`c` is an identity on a gauge orbit. Differentiating it in `c` at
`c=0` is the tangent space of that orbit: a Jacobian syzygy, not a
new transgression invariant, unless a coefficient of the polynomial
in `c` lies *outside* the known syzygy module.

Cheapest discriminator, desk, no new emitter: declare the triangular
action on a finite symbolic packet; reduce the highest `c`-degree
coefficient of the transported endpoint class by reviewed Keller
recurrences. If every coefficient reduces, the idea is gauge-only
and **stops**. If the chart map is not serialized, return `OPEN`.

The claimed interface — named occurrence, `PairRef`, completion,
chart transport — is **absent**. Do not launch a Ward lane against
a missing packet. Sol’s “high at low cost” is cost-true only after
the packet exists.

### 3.5 TD12-ROW-PROPORTIONALITY

At G5 the unknown block `(v,k10_0)` is finite and typed, so
proportionality of coefficient vectors is a literal `2×2` vanishing.
The td12 cascade’s unknown is the positive-order source jet
`P_a (a≥1)` together with the `T_b`, which no promoted result
bounds. Rows at different grades are not maps on a common typed
finite unknown without a declared window.

Cheapest discriminator: declare a finite unknown block (for example
only the newest `T_j` in a named row, with `P_a` treated as
indeterminate coefficients, not values). If that declaration cannot
be made from promoted structure, return `OPEN` and **stop**. Do not
test “nearly proportional.” Approximate minors are not a theorem.

The idea as stated — “no source values needed” — silently assumes
the unknown block is the same object that was finite at K00 G5.
That interface is absent. Stop.

### 3.6 `TD12-U1-ACTUAL-LANDING`

A hypothetical exact counterexample supplies completions; no theorem
selects td12/U1 or B25/S17 (T9(c)/T10 remain `OPEN`). The named
lemma is the occurrence theorem under a U1 hypothesis. It is the
correct *shape* of the proof bottleneck and does **not** outrank
occurrence/coverage work, because it *is* that work. It does
outrank further local-row arithmetic whose interface is absent
(Ward, row-proportionality, `j=42`). Local-row work stops; the
landing lemma is not a cheaper substitute for P1.

### 3.7 This lane’s other cards, attacked as hard as the others

`TD12-HERMITE-TRANSGRESSION-SHAPE`. Counting `3i−2` original
Hermite slots against a 1-dimensional T1 solution is not a
transgression. FALLACY-v2 variable/ring map: original cross-sum and
reduced `T` live in different charts; matching letters `A,B` prove
nothing. An unbounded original tail can absorb any finite slot
count, so “overdetermined” is not a cap. Discriminator cannot even
be declared. Typed `OPEN`. Do not launch.

`K00-G5-THICKENING-FITTING`. Method-transfer of associated-scheme
Fitting is a real protocol on a nonempty nonreduced gate. This
gate’s val-1 open is empty, so ranks of the zero module over two
unit ideals are not a campaign decision. The card’s “unit on either
input” line is the RAD-UNIT error. Stop as a G5 launch.

### 3.8 Systems — `CAPRUN/v1`

All four blinds independently select one repo-owned
wait-authoritative capped runner. Independent convergence is
evidence about the incident, not about portable correctness.

Smallest nonduplicative contract:

- argv-only `Popen`; closed stdin (`DEVNULL`) unless
  `--stdin-file` names a regular file;
- child in a new process group; record PID, PGID, start identity
  (start time + argv hash), cwd, UTC;
- one authoritative `wait`/`communicate` and one reap;
- timeout path: recheck PID/PGID/start identity, TERM to that
  PGID only, bounded grace, KILL to that PGID, same reap;
- wall/CPU/RSS telemetry on a **separate fd**, not stderr
  (Opus’s `/usr/bin/time` burial is a real supervisor-class bug
  and is testable);
- typed outcome: exit / timeout / RSS / CPU / signal / runner
  failure; hash stdout/stderr after reap;
- generated Singular scripts end with `quit;` when the helper
  is the one writing the script.

Light fixtures, ordinary and `-O`, byte-identical logs modulo
declared time/PID fields:

1. EOF: a child that waits on stdin exits promptly (closed stdin).
2. Decoy: a same-name process outside the PGID survives TERM/KILL.
3. Orphan: child plus sleeping grandchild times out; no
   registered-group descendant remains.
4. Early-exit: child exits before the first poll; recorded status
   is the true exit (no `kill -0` continuation).
5. TERM-ignore: grace then KILL, one reap, typed signal/timeout.
6. Clean `1+1; quit;` vs `1+1;` without `quit;` under `wall=2`.

Reject, rather than overclaim: Linux `prlimit` as a macOS desk
requirement; session-leader vs process-group if the fixture cannot
distinguish them on Darwin; migration of `ops/lane.sh` or the nine
`kill -0` loops; D43 `poll_stage` mutation. Portable CPU/RSS via
`resource.setrlimit` where it works, documented Linux path as
optional, not as an untested universal.

No `ops/lane.sh` migration in this wave.

---

## 4. Launches

Two mathematical, one systems. No third math launch: G6 val-1,
Ward, row-proportionality, Hermite-shape, thickening-Fitting, and
`j=42` all fail an interface or a discriminator already fired.

### M1 — `K00-G5-COLLAPSE` different-model review (falsification)

- **Object.** Promote or roll back §2’s maximum theorem and the
  val-1 kill, from atlas `exact_terms`, not from this memo and not
  from Opus scratch. Include RAD-UNIT, the projection/fibre split,
  and G5-VAL1 source typing.
- **Dependencies.** Promoted G3 incidence `d453b956...`; reviewed
  G4 `PASS_WITH_REPAIR`; atlas `d7ec6d18...`; V22R1 val-1 prefix;
  `SOURCE_COLUMNS.json`. The owned Fable two-input G5 lane, once
  sealed, is a comparison input, never a premise. Agreement is
  evidence about a computation, never proof.
- **Owner / reviewer.** Not Opus (producer), not Grok (this
  reconstruction and the G4 review). Suggested owner of the
  official review: Sol. If the owned Fable G5 primary seals first,
  Sol reviews both against the atlas.
- **Desk / AWS.** Desk. Stdlib `Fraction` sparse polynomials, same
  mutation battery (plane coefficients, `mu`’s `16`, one literal
  G5 coefficient, localizer `−1`). Wall 60 s, RSS 1 GiB. No
  Groebner. No AWS.
- **Both outcomes.** `PASS` / `PASS_WITH_REPAIR` ⇒ the normalized
  val-1 K00 seed is dead at grade five; Avenue 36 val-1 slot
  closes; origin fibre is a *different* valuation and is not
  auto-armed. `FAIL` ⇒ quarantine §2 and Opus §3; do not lower
  Avenue 36; rerun the owned G5 gate as the authority.
- **Stop.** Missing literal labels; unnamed remainder ring;
  treating the origin fibre as val-1; collapsing scheme/radical
  existence by slogan rather than RAD-ID; any G6 Groebner; any
  JC2 sentence.

### M2 — `TD12-S-TERMINAL-ROW-FORM` (proof; conditional `j=13`)

- **Object.** From frozen sibling T1 data and the in-flight S
  reconstruction, declare or refute the terminal reduced-deviation
  row of MST-1 shape with `O=kbar−D` at `(nu,kbar,D)=(17,13,17i)`.
  If declared, `j=13` is an exact derivative by MST-4. If not,
  typed `OPEN`. No B values transported.
- **Dependencies.** Reviewed B MST (this packet’s TD12 review);
  charged sibling `(17,13)` in
  `xmodel/td12-inhomogeneous-row-first-invariant-sol56-20260829.md`;
  S-bridge different-model reconstruction (already in flight).
  Explicitly not: `PairRef`, source values, Fable Card A as a
  free-standing residue lane.
- **Owner / reviewer.** Rider on the in-flight S reconstruction.
  Reviewer: not the S producer. Suggested: Sol or Opus after
  reseal.
- **Desk / AWS.** Desk reading plus the identities already in
  MST. `$0`. No CAS.
- **Both outcomes.** Typed row ⇒ Fable Card A outcome (iii)
  (structural vacuity) is the theorem; stop S-window residue
  hunting; occurrence remains P1. Untyped ⇒ `OPEN`; Card A
  stops; do not fill by B analogy.
- **Stop.** One declaration. No `j=13+17` expansion. No
  identification of Hermite class with reduced `T`.

### S1 — `CAPRUN/v1` (exactly one systems trial)

- **Object.** One file `ops/run_capped_wait.py` implementing §3.8,
  plus the six fixtures. No caller migration.
- **Owner / reviewer.** Implementation: any; not a math lane.
  Reviewer: a different model than the implementer. Suggested
  implementer: Sol (smallest original contract); reviewer: Fable
  or Opus.
- **Desk / AWS.** Desk. No CAS. Seconds.
- **Both outcomes.** 6/6 plus ordinary/`-O` log identity ⇒ bank
  the helper; still no `ops/lane.sh` migration this wave. Any
  fixture fail ⇒ fail closed, keep the fixture, do not silently
  drop the untestable clause.
- **Stop.** One helper, one fixture matrix. Reject untestable
  portable claims rather than overclaiming them.

---

## 5. Stop / defer list

| Item | Action | Missing premise / reason |
|---|---|---|
| Scheme vs radical as a G5 geometric split | **stop** | RAD-UNIT |
| `K00-RENORM` as a tower | **stop** | G6 `deg v=2` |
| `K00-POLARIZATION-SHEAR` past G4 | **stop** | G6 is not translated `Q` |
| `K00-SHIFT-LADDER` as “every grade is linear” | **stop** | same G6 fact; keep only the linear-block covariance as a recorded identity |
| G5 Fitting / cotangent-square existence job | **stop** | val-1 open already empty |
| G6 Groebner on val-1 | **stop** | val-1 already killed if M1 passes |
| Origin fibre as a val-1 continuation | **stop** | G5-VAL1 |
| Origin fibre as a new higher-valuation seed | **defer** | needs coordinator GO; fibre dim `OPEN` |
| Veronese/conjugate-square coordinates as a G5 job | **defer** | unused; optional on a nonempty fibre |
| Avenue 4 arming from a K00 jet | **stop** | a nonempty finite jet is not a germ client |
| `TD12-GA-TRANSLATION-WARD` lane | **stop** | no `PairRef`; likely gauge |
| `TD12-ROW-PROPORTIONALITY` as stated | **stop** | unbounded unknown block |
| `TD12-HERMITE-TRANSGRESSION-SHAPE` | **stop** | no declared map |
| `j=17` descendants | **stop** | reviewed vacuous |
| `j=42` | **stop** | no `P_k`; `C_17` unpinned; `OPEN(WINDOW-INDEX-B25)` |
| Fable Card A as a free residue lane | **stop** | absorbed by M2 |
| `TD12-U1-ACTUAL-LANDING` as a cheaper P1 | **stop** | it is P1 |
| Finite-s consumer search | **stop** | completed negative; bank the theorem |
| `TWIN-ORDER` | **stop** | `OPEN`; Gaussian resemblances prove nothing |
| Rank 3–5 K00 charts | **stop** | promoted plane |
| Homogeneous-window cascade | **stop** | unchanged |
| `ops/lane.sh` / nine `kill -0` migrations | **defer** | after S1 review |
| Linux `prlimit` as a desk requirement | **stop** | untestable here |
| AWS / heavy CAS / `jc2-lean` | **stop** | nothing in this round licenses them |
| New exit price | **stop** | none asserted |

---

## 6. Synthesis recommendation

The radical identity is ordinary commutative algebra and kills every
proposed geometric scheme/radical split at G5. Independently, from
atlas `exact_terms` and a name-declared map, Opus’s grade-five
projection theorem holds: on `D(k10_0)` the leading two-plane
collapses to the origin, while the fibre over the origin is nonempty
and is not a point. Frozen reviewed source typing says that origin
is the higher-valuation leak, so the complete normalized val-1,
`C6=1`, `k10_0≠0` K00 seed dies at grade five. That is not a scheme
statement, not a later-grade statement, and not JC2. The three shift
names are not one tower: G4=G2(w) and the G5/G6 linear-block
identities are real, G6 is quadratic in `v`, and even-grade
translated-`Q` stops at G4. Do not Groebner G6 against val-1. On
td12, `j=17` is reviewed vacuous; `j=13` on S is a corollary only
after the S row is typed; Ward and row-proportionality lack their
interfaces; the occurrence lemma is still P1. Launch one G5 review,
one S-row-form rider, and `CAPRUN/v1`. Nothing else.

(163 words)

---

## 7. Non-claims

No proof or counterexample to JC2. No Keller pair, polynomial map,
arc, germ, occurrence, landing theorem, cofinal `td` ceiling, or
exit price. The val-1 K00 seed kill is a point-set statement on one
normalized prefix at grade five, `VERIFIED-HERE`, pending M1. The
origin fibre is not that seed. Self-agreement with the Grok-blind
report is not evidence; where this memo retains linear-block
covariance or a Fitting protocol, it does so only after the attacks
in §3, and it launches neither as a val-1 job.

No canonical file was edited. No commit, push, AWS action, web
access, or heavy computation. No other round cross-poll or
post-packet report was read. The separately owned `jc2-lean` tree
was not entered, enumerated, searched, read, built, statused,
modified, or controlled. This file is the only file written.
Scratch lived under `/tmp/k00g5_xpoll_grok46/` and is not in-tree.

No new typed exit price is asserted, so no `charge_basis` line
appears.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `34411`.
- Body SHA-256:
  `a430e8ee5888d140c7a28aa79ea045fc1316a6440ba1560f740ea887c7aac76d`.
- Frozen basis: `40c1ab3448209e3d87173feb947a733f6fe54f7f`.
