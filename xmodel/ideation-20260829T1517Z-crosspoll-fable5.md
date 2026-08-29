# Adversarial cross-pollination — Fable 5 — round `20260829T1517Z`

Lane: `ideation-20260829T1517Z-crosspoll-fable5`. Identity: Fable 5.
Frozen basis `40c1ab3448209e3d87173feb947a733f6fe54f7f` (verified
`git rev-parse HEAD` at start and before sealing). This is adversarial
synthesis input, not promotion. No new exit price is asserted anywhere below,
so `charge_basis` is absent by design.

## 0. Custody and boundary compliance

Packet recomputed byte-exact: full
`fc6a6843545119a5e184755bf5a26b4edce0ae8fbe912935532704608a0c312e`,
body `8351` / `e6963ce96110f8f0f01d568da7ca5e0fca22242099e33957b245f4ed5c399fa5`.
All six named sealed inputs recomputed and matching (full / body):

```text
4d51f329... / fccf2517...  ideation-20260829T1517Z-sol56.md          (21571 B body)
8790a5e9... / cb03b901...  ideation-20260829T1517Z-fable5.md         (22449 B body)
b01c4882... / f809f402...  ideation-20260829T1517Z-grok46.md         (34124 B body)
7d545367... / ce6be254...  ideation-20260829T1517Z-opus5.md          (35263 B body)
1ec95a45... / 41da5999...  k00-grade4-rank0-plane-opus5-hostile-review-grok46-40c-20260829.md
068ed91b... / 2e5a062f...  td12-b25-resrow-sol56-hostile-review-opus5-40c-20260829.md
```

State packet `648acf8b...` (body `a2ed4405...`) and roundview `72284172...`
recomputed unchanged. Charged mathematical inputs:
atlas `ATLAS_EXACT_POLYNOMIALS.json` `d7ec6d18...` (62,072,089 B), compiler
`compile_fitting_atlas_v26.py` `24640d0d...` (digest convention only),
`AUDIT.md` `3f35e3a8...`. All reconstruction below is from atlas
`exact_terms` with a name-declared map; no Opus scratch was run or trusted.

No web, AWS, commit, push, canonical edit, or `jc2-lean` access. Desk caps
respected: Python audit `2.12 s` wall / `620 MB` RSS; Singular second method
`34.2 s` / `190 MB`, stdin closed, script ends `quit;`, wait-reaped. Exactly
one repository file is written: this one. Scratch: `/tmp/f5xp/` only —
`audit_final.py` `abf7b21b3d67032ee47d89744569b275e41062535b8847072121bfd2d9576752`,
stdout `0f366462b3575994c5c9429b307200997cd3bb616fbbbccbbd67d5efa785f90b`
(38/38 checks), `g5_second.sing` `a49797b6...`, its stdout `3025a563...`.

**Disclosure.** A repository grep for the frozen valuation-one semantics
surfaced four lines of `k00-grade5-rank0-plane-structural-provisional-sol56-
20260829.md` (mtime 08:57, after the packet at 08:51). The file was not
opened and is not charged; every typing statement below cites only
pre-packet sources, and my grade-five reconstruction was complete before the
exposure. The visible lines indicate Sol independently reached the same
typing conclusion; that convergence is noted, not consumed.

## 1. Required output 2 first — verdict on `G5-COLLAPSE`

```text
VERDICT: PASS_WITH_REPAIR   (independent full reconstruction, two exact methods)
```

Every load-bearing claim of Opus §3 reproduces exactly from the frozen atlas
bytes; two presentation-level repairs and one inherited typing rider are
required; three strengthenings were found. Checks (all exact, `Fraction` /
Gaussian-rational, no producer code executed):

1. **Custody.** 49/49 literal rows rebuilt from `exact_terms` reproduce the
   stored producer digests and term counts under the compiler's
   `p_payload`/`canonical_json` convention.
2. **Ring map.** Name-declared `phi`: `d*_1 -> (2s, t/8, s, t, s, 2t)`,
   `d*_2 -> u`, `d*_3 -> v`, `d*_4 -> x`, `k10_0 -> k`, `k10_1 -> k1`, over
   `Q`; never positional (Grok review Repair R1 honoured).
3. **(S1)** `phi(Lambda_{4,r}) = Q_r(u-mu)`, `mu=(s^2,st/8,16t^2,0,0,0)`:
   7/7. **(S2)** grade five on the plane: `d*_4` and `k10_1` disappear
   (7/7), each row affine-linear jointly in `(v,k10_0)` (7/7), and the
   `v`-coefficient equals `C_r(u-mu)` where `C` is the grade-three
   `d*_2`-coefficient matrix (42/42). Grok's cross-identity (`d*_3`-coeff of
   grade 4 = `d*_2`-coeff of grade 3) reconfirmed 42/42.
4. **Base residuals.** On reduced `W4` (`RA=RB=0`), with `X=8w1-w3`,
   `Y=w2-w4`: row 6 identically zero; row 4 unknown-free and exactly
   `(3/32768)(64sX^2+128tXY-sY^2)`; rows 3,5,7 linear parts exactly
   `-1/8,-1/128,-1/1024` times row 1's; `Phi3` exactly
   `(3/2048)(64tX^2-2sXY-tY^2)`; `Phi5=(-1/8)Phi3`, `Phi7=(-1/128)Phi3`;
   `t*Phi4' - s*Phi3' = 2(s^2+64t^2)XY`. All exact.
5. **Self-similar branch** (`X=Y=0`, i.e. `w` back on `Pi`): all
   `v`-coefficients and all constants vanish identically; the system
   collapses to `k10_0*(5/4096)*t(3s^2-64t^2)` and
   `k10_0*(5/65536)*s(s^2-192t^2)`, independent of the second-level plane
   parameters — exactly as Opus displayed. **Strengthening 1:** I replaced
   the case analysis by membership certificates
   `-512st^3 = 3t*g2 - s*g1`, then `t^5, s^3t^2, s^5 in (g1,g2)`, so
   `V(g1,g2)={0}` is certified, not cased.
6. **Conjugate branch** (`s=8it`, `Y=-8iX`, over `Q(i)`; conjugation settles
   `s=-8it`): all 15 minors of the rows-1,2 `v`-block vanish; the exact
   structure is sharper than reported: every `v`-coefficient is a Gaussian
   constant times `X` (so the block has rank at most 1 with degeneracy locus
   exactly `{X=0}`), `a2 = -(i/2) a1` as vectors, `b1=-(5/16)t^3`,
   `b2=-(5/32)i t^3`, `e1=-(3/8)tX^2`, `e2=(3/16)i tX^2`. **Strengthening
   2 (one-line kill):** `row2 + (i/2) row1 = -(5/16) i t^3 k10_0`
   identically on the branch — with `k10_0 != 0` this forces `t=0` with no
   elimination, no case split, and no degeneracy sublocus left open. Opus's
   displayed constant `-(15/16384) i t^3 X` is confirmed exactly as the
   `j=0` polynomial cross-combination `a1_0*row2 - a2_0*row1`.
7. **Witness.** `d*_1=0, d*_2=(4,1,1,0,0,-16), d*_3=0, k10_0=1` kills all 42
   rows of grades 0–5; so does `k10_0=7`, so the fibre over the origin is
   positive-dimensional, confirming the **projection** theorem: it is the
   image in the leading two-plane, not the full-coordinate locus, that is
   the origin.
8. **Second exact method (Groebner, Singular 4.4.1).** With the seven
   substituted grade-five rows, `RA`, `RB`, and `k10_0*z-1`: adjoining
   `s*y-1` gives the **unit ideal**; adjoining `t*y-1` gives the **unit
   ideal**; the origin fibre is **proper**, dimension 9 in the honest fibre
   variables `(u,v,k10_0,z)`. Exclusion and survival both confirmed at
   ideal level, independently of the branch decomposition.
9. **Controls.** `mu` mutation, plane mutation, one literal grade-five
   coefficient doubled, and a kill-constant mutation all fire; the checker
   detects nonvanishing where it must.

**Repairs (do not change the verdict).**

- **P-1 (argument completeness/presentation).** Opus's elimination step is
  silently degenerate on the whole hyperplane `{X=0}` of the conjugate
  branch (all twelve `v`-coefficients are multiples of `X`, not merely rank
  one). The written chain still closes it — `X=0` falls through to the
  self-similar bullet — but successors should state the degeneracy and may
  simply use the one-line kill above, which needs neither.
- **P-2 (normalization wording).** "The surviving `k10_0` coefficient is
  `-(15/16384) i t^3 X`" is slot-dependent (it is the `j=0`
  cross-combination). The invariant statement is
  `row2+(i/2)row1 = -(5/16) i t^3 k10_0`.
- **P-3 (inherited riders).** Grok's G4 review repairs R1 (jet-major ring
  order, name-based maps) and R3 (label `x,k1` as dummies) bind any
  grade-five packet; both honoured here.

### 1.1 Exact maximum theorem

Over an algebraically closed field of characteristic zero, with `d*_1` on
the promoted rank-zero plane `Pi`, the reduced grade-four input
`RA=RB=0`, and `k10_0 != 0`: the literal grade-zero-through-five compatible
locus **projects to the leading two-plane exactly onto `(s,t)=(0,0)`**,
i.e. `d*_1=0`; over that origin the fibre is nonempty, proper, and
positive-dimensional (dim 9 in `(u,v,k10_0,z)`), with exact witnesses
`u=(4,1,1,0,0,-16), v=0, k10_0 in {1,7}`. By the radical identity of §3.1
the same point-set statement holds verbatim for the scheme-input variant
`I4 + J5`. Nothing here is a later-grade, full-`P6`, arc, polynomial-map,
Keller-pair, or JC2 statement.

### 1.2 Source-scope consequence (mandatory typing decision)

The frozen source semantics define this seed on a **valuation-one prefix**:

```text
d_i = Lambda * x_i + O(Lambda^2),  k10 = kappa + O(Lambda),  kappa != 0
```

in the normalized unloaded K00 chart `C6=1`
(`xmodel/max12-812-order2-k00-v22r1-first-weighted-stratum-hostile-review-20260827.md:51`;
canonical confirmation `AUDIT.md:4121-4122`), and the reviewed record
explicitly types the origin of `x`-space as **the higher-valuation leak
`v(d)>1`, not a valuation-one point**
(`xmodel/ideation-20260827T1349Z-grok.md:264-266` and `:320`). The atlas
block `d*_1` is that leading vector `x`. Therefore `d*_1=0` is not an
admissible point of this seed, and:

> **Conditional on promotion of the grade-five theorem (three independent
> computations now exist: Opus §3, this reconstruction, and the owned
> two-input lane when it seals), the complete normalized valuation-one,
> `C6=1`, `k10_0 != 0` K00 seed is dead at grade five.** The surviving
> point is exactly the typed leak out of the stratum. Other coefficient
> valuations (the `v(d)>=2` locus as a separately normalized problem),
> finite jets as maps, arcs, polynomial maps, and JC2 are outside the
> claim. Opus's Card B question is hereby answered `EXCLUDED` from frozen
> semantics, not by cap or analogy.

## 2. Required output 1 — deduplicated mechanism table

Independent convergence is preserved in the "by" column; labels follow the
packet's vocabulary.

| Mechanism / claim | By | Label | Disposition |
|---|---|---|---|
| `K00-G5-RANK0-PLANE` two-input decision target | all four | KNOWN | Preregistered successor; Opus executed it; reconstructed here. |
| `G5-COLLAPSE` result | Opus | NEW | `PASS_WITH_REPAIR` (§1); strengthened (one-line kill, certificates, Groebner second method). |
| Radical-first scheduling theorem `sqrt(I+J)=sqrt(sqrt(I)+J)` | Sol (also implicit in Opus §3.3) | NEW-correct | Proved (§3.1). Kills two peers' geometric-divergence outcomes (below). |
| "Stage-1 nonempty, stage-2 unit" divergence branch | Fable (my blind Card B) | **REFUTED** | Impossible by §3.1 — my own binary algebra error. |
| "Unit on either input; report which input" discriminator | Grok (Card 2) | **REFUTED** | Unit-ness cannot differ between inputs; the discriminator is vacuous. Grok's Fitting-rank comparison survives as infinitesimal-only. |
| Conjugate-square / Veronese `B+8iA=(s+8it)^2` coordinates | Sol; convergent with Opus's `s=+-8it` branches | NEW | Confirmed load-bearing: the branch kill lives in the `Q(i)` eigenrelation `a2=-(i/2)a1`. |
| `K00-SHIFT-LADDER` (linear-in-newest-block covariance) | Opus | NEW, now **verified at grade six** | Card A's discriminator run here: `x_j`-linear coefficient of `phi(Lambda_{6,r})` equals `C_rj(u-mu)`, **42/42**. Grade-6 on-plane census: `d*_5` and `k10_2` disappear, `d*_4`/`k10_1` return — the grade-5 pattern shifted one block. |
| `K00-RENORM` full period-two law | Fable (mine) | **REFUTED** | At grade five `phi(L5_r) != L3_r(w,v)+k10-correction`: 0/7 ambient, and the non-`k0` residual is nonzero on `W4` for 7/7 rows. Only the linear-block ladder survives. |
| `K00-POLARIZATION-SHEAR` even-grade functor | Grok | NEW / untested at full scope | Naive `u`-only shear at grade 6 is refuted by the nonzero `x`-linear block; only a block-extended shear remains hypothetical. Full test unauthorized this round and moot for the valuation-one seed (§3.2). |
| `K00-G5-THICKENING-FITTING` | Grok | SCOPE-narrowed | Geometric half vacuous (§3.1); infinitesimal Fitting comparison remains valid custody for a re-seeded stratum only. |
| `K00-G5-COTANGENT-SQUARE` compiler + Fitting stratification | Sol | KNOWN-target, superseded | The desk collapse answered the gate; heavy modular/Fitting machinery unnecessary; the nilpotent-filtration study is moot for this seed after §1.2. |
| `d*_1=0` admissibility question | Opus (Card B) | ANSWERED | `EXCLUDED` from frozen semantics (§1.2). |
| Linear-in-newest-block prescreen router | Opus | NEW-method | Adopt as registration policy: measure newest-block degree before registering any heavy gate (1.5 s vs 21,000 s precedent). |
| `TD12-S-RESONANCE-PLACEMENT` | Fable (mine) | SUPERSEDED | The placement residue is `13 != 0 mod 17`, but MST-4 makes the in-window row automatically vacuous once typed (§3.4) — my card's live branch was structurally dead; folds into Launch L3. |
| `TD12-GA-TRANSLATION-WARD` | Sol | NEW, leverage-negative expected | Gauge-orbit tangent, not a transgression (§3.5); at most its own stop-condition check. |
| `TD12-ROW-PROPORTIONALITY` | Opus | **REFUTED-interface** | No common typed unknown block exists; distinct-row proportionality impossible (§3.5); the card's informative negative outcome is delivered at desk here. |
| `TD12-HERMITE-TRANSGRESSION-SHAPE` | Grok | NEW, defer | Expected immediate `OPEN` at dictionary declaration; ranked below `TD12-U1-ACTUAL-LANDING`. |
| `TD12-U1-ACTUAL-LANDING` conditional lemma | source audit / packet | NEW-ranked-first | Outranks all local-row work (§3.4/§3.5); Launch L2. |
| `CAPRUN/v1` wait-authoritative runner | all four | KNOWN-converged | Merged smallest spec in §4 (systems trial). |
| fd-separated telemetry (never stderr) | Opus | NEW | Adopted (as a required telemetry file). |
| Gaussian-integer cross-lane pattern | Opus §6.4 (declined) | NO-WEIGHT | Concur; note the `Q(i)` structure here is internal to K00 and proves nothing about td12 constants. |
| Avenue-4/36 raises | Sol | REFUTED-by-events | Both raises presupposed the seed's survival; after §1 they invert (Avenue 36 lowers hard on promotion). |
| Carrier×`[2,2,2]` SCOPE-CONFLICT; `FLOOR-COORD`×S17 DUPLICATE | Fable (mine) | stands | Negative results banked; unchallenged by any peer. |

## 3. Required output 3 — direct attacks on the mandatory items

### 3.1 Radical versus scheme (mandatory 1)

**Theorem (any commutative ring, any ideals `I,J`).**
`sqrt(I+J) = sqrt(sqrt(I)+J)`.
*Proof.* `I+J ⊆ sqrt(I)+J` gives `⊆` after radicals. Conversely
`sqrt(I) ⊆ sqrt(I+J)` and `J ⊆ sqrt(I+J)`, so
`sqrt(I)+J ⊆ sqrt(I+J)`, and radicals give
`sqrt(sqrt(I)+J) ⊆ sqrt(sqrt(I+J)) = sqrt(I+J)`. ∎

**Therefore equal for the two grade-five inputs:** point sets over any
field extension, unit/proper status (`K=(1)` iff `sqrt(K)=(1)`), minimal
primes, Krull dimension. **Still free to differ:** the ideals themselves —
nilpotents, embedded primes, primary structure, multiplicities, tangent and
cotangent spaces, Fitting ideals, Hilbert functions, infinitesimal lifting
through the `sqrt(I4)/I4` filtration.

**Errors identified (exact claims):** my own blind Card B outcome
"stage-1 nonempty, stage-2 unit -> nilpotent obstruction … while points
survive" describes an impossible state of affairs; Grok Card 2's first
outcome "Unit on either input … report which input" offers a discriminator
that can never discriminate, and §3.2's "if they agree, radical input
covers field-valued points of this gate" is misleading — coverage of
field-valued points is unconditional. **Preserved:** Grok's Fitting-rank
comparison on `T/I4` vs `T/sqrt(I4)` and Sol's nilpotent-filtration
Kuranishi reading are genuine infinitesimal questions the identity does not
touch. **Redesign radical-first:** done — both §1 methods ran the radical
input, and the scheme input is custody for ideal-level successors only.
Sol's Card 1 statement of all this was already correct.

### 3.2 Opus `G5-COLLAPSE` audit (mandatory 2)

Delivered in §1 (all six numbered sub-attacks of the packet executed:
literal-row reconstruction with declared map; affine-linearity and block
disappearance; shifted grade-three coefficient matrix; base residuals with
exhaustive four-branch decomposition and the conjugate branch; exclusion of
every nonzero `(s,t)` on `D(k10_0)` plus two exact witnesses over the
origin; projection-theorem precision; controls and a second exact method).
Source typing resolved in §1.2.

**Whether grade-six work remains useful if valuation one is killed:** the
grade-six gate on this plane stops being a falsification target for this
seed; what survives is (a) the verified ladder fact itself (42/42), which
becomes mechanism knowledge for any re-seeded stratum (e.g. the
higher-valuation locus under its own normalization, which is a different
normalization problem, not this seed), and (b) the router policy: measure
newest-block linearity before registering any heavy job. No grade-six or
grade-seven computation should be launched for the valuation-one seed.

### 3.3 Shift/renormalization reconciliation (mandatory 3)

The three proposals are **one verified mechanism plus two unverified
extrapolations**, now separated by computation:

- **Verified:** grade 4 = grade 2 at `w=u-mu` (full identity; reviewed);
  grade-5 `v`-block = `C(w)` (42/42); **grade-6 `x`-block = `C(w)` (42/42,
  new, the packet's authorized cheap test)** — with the same matrix `C` at
  the same shifted argument, and the census `d*_5, k10_2` disappearing at
  grade 6 exactly as `d*_4, k10_1` did at grade 5.
- **Refuted:** `K00-RENORM`'s full period-two law at grade 5 (0/7 ambient;
  7/7 nonzero residual even modulo `W4`). My own proposal; my own
  computation killed it.
- **Open but constrained:** `K00-POLARIZATION-SHEAR`'s full even-grade
  shear at 6. The nonzero `x`-linear block refutes any `mu_6` not
  absorbing `d*_4`; only a block-extended shear survives, untested, and
  now moot for this seed.

A partial match was not extrapolated: the tower theorem remains unproved;
what is proved is the linear-in-newest-block covariance at grades 4→5→6 on
this plane, which is exactly what makes each gate an elimination problem.

### 3.4 TD12 first resonance and the S route (mandatory 4)

**Route-generality: yes, and it is already reviewed.** MST-1..5 of the
RESROW review are universal in `(nu, kbar, i)` with `0 < kbar < nu`,
`gcd(kbar,nu)=1`, `D=nu*i`, given the row shape `(ROW_j)` and the landing
`ord_top(Dev) = kbar - D`. For the sibling `(nu,kbar,D)=(17,13,17i)`:
`gcd(13,17)=1`, the resonance lattice is `j ≡ 13 (mod 17)`, the window
S16 has depth `16 >= 13`, so the unique in-window resonance `j=13` **is
automatically the total-derivative row and both orbit residues vanish
identically** — the moment the S terminal reduced-deviation recurrence is
typed with those data. The first possibly nonvacuous **resonant** S row is
`j=30`, outside S16, carrying the same blockers as B's `j=42` plus the
`C_13` resonant-gauge analogue of MST-6.

**Distinction kept:** that is a conditional corollary of reviewed
route-general algebra plus an untyped S hypothesis; it is *not* a review of
the S landing/deviation bridge, whose custody (failed producer seal) and
mathematics remain the open debt. Proving the corollary advances nothing
about the bridge itself.

**Self-attack:** my blind Card A (`TD12-S-RESONANCE-PLACEMENT`) computed
the right residue (`13 != 0`) but sold its live branch — "a live
window-internal constraint" — which MST-4 forecloses structurally. The
card's entire value collapses into the S-typing step of Launch L3.

**B `j=42`:** carried with both review repairs — the consumption list
includes the unpinned resonant gauge `C_17` (two affine conditions in one
unpinned constant; generic elimination leaves at most one), and the
`P_a`-index-vs-window-depth identification stays `OPEN(WINDOW-INDEX-B25)`;
no `j=42` launch, per the four independent blockers.

### 3.5 TD12 proof-side proposals (mandatory 5)

**`TD12-GA-TRANSLATION-WARD` (Sol): gauge orbit, not transgression.** The
S audit itself proves `tau_c` preserves the Jacobian, normalized type,
minimality, and the S17 cell — i.e. the orbit stays inside the admissible
family. Any identity proved for every admissible pair then transports, and
its `c`-expansion is the identity for the transported pair: the
differentiated relations lie in the Jacobian syzygy module (the tangent
identity of the orbit), which is Sol's own stop condition. The
top-`c`-coefficient escape fails concretely: the action is triangular
unipotent in depth, so the top coefficient of any transported depth-`a`
datum is built from depth-0 data `P_0 = lambda_f p^i` alone — already fully
constrained by the promoted T1/landing theorems. Middle coefficients
consume exactly the unpinned `P_k`: bottleneck P2 in Ward costume. The one
way the mechanism could bite — a consumed normalization *not* covariant
under `tau_c` — is absent from the frozen basis precisely because the
audit converted the only candidate (`FLOOR-COORD`) into a WLOG gauge.
**Missing premise: a named non-covariant normalization. Run at most Sol's
stop-condition discriminator; expect gauge-only; do not schedule ahead of
occurrence work.**

**`TD12-ROW-PROPORTIONALITY` (Opus): the claimed interface is absent.** The
packet's question — are rows at different grades maps with a common typed
unknown block? — answers **no** under every reading. (a) `T`-block: rows
are triangular, one fresh `T_j` per row, and coefficients involve the
unknown `P_a`; moreover the `a=0` slot of row `j` is the operator
`L_j = nu p d/deta + (nu i + j - kbar) p'`, and `L_j ∝ L_{j'}` forces
equality of the leading `nu p d/deta` parts (ratio 1) and hence
`j = j'` — no two distinct rows are proportional, ever. (b) `P`-block:
coefficients involve the unknown `T_b`. (c) Joint: bilinear, not linear.
The K00 mechanism worked because plane specialization made the
coefficients *known*; td12 has no such specialization without source
values. In a triangular system the only zero-new-unknown compatibility
conditions are the resonant cokernel conditions — the residues already
adjudicated (`j=17` vacuous by review; `j=42` quadruple-blocked). **The
card's own "no proportional pair / rows in general position" outcome is
hereby delivered at desk; the card is answered, not merely stopped.**

**`TD12-U1-ACTUAL-LANDING` should outrank all local-row work: yes.** After
this round the local lanes are uniformly closed or blocked: `j=17` reviewed
vacuous; `j=42` blocked (no `P_k`, unpinned `C_17`, cost, occurrence);
S `j=13` conditionally vacuous (§3.4); row-proportionality refuted (§3.5);
translation-Ward expected gauge-only (§3.5). Every remaining td12 attack
path passes through either source values (P2) or occurrence selection (P1),
and `TD12-U1-ACTUAL-LANDING` is the narrowest typed lemma on the P1 side:
it consumes only an actual equality record and reviewed contradictions,
and produces the named B25/S17 occurrence every terminal theorem is
conditioned on. All four blind reports rank occurrence first; this is its
minimal conditional form. Launch L2.

## 4. Required output 4 — launches

Three mathematical launches (proof and falsification covered) plus exactly
one bounded systems trial. All desk; no AWS action is proposed this round.

**L1 — falsification: K00 grade-five adjudication and promotion packet.**
Reconcile the three independent computations (Opus §3; this report §1; the
owned `k00-grade5-rank0-plane-twoinput-primary-fable5` lane when it seals)
into one reviewed theorem carrying: the maximum theorem of §1.1, the
radical-first identity, repairs P-1..P-3, the `LADDER-6` 42/42 and
`RENORM` refutation as mechanism dispositions, and the §1.2 typing
consequence. Owner: Sol (coordinator integration); reviewer: Grok (owns
the G4 review context, produced no G5 result). Dependencies: the sealed
two-input lane; the already-reviewed G4 inputs. Desk only. Outcomes:
promotion ⇒ the valuation-one seed is closed, Avenue 36 lowers hard, and
falsification capacity re-seeds deliberately (higher-valuation stratum
under its own normalization, or Avenue 19's degree-twelve frontier) —
not by momentum; any disagreement among the three computations ⇒
adjudication before promotion (agreement is evidence about a computation,
never proof). Stop: disagreement, or a typing objection to §1.2 ⇒ typed
`OPEN`, no promotion, seed stays protected.

**L2 — proof: `TD12-U1-ACTUAL-LANDING`.** State and prove (or refute with
a named missing premise) the conditional lemma: assuming an actual td12 U1
equality record, every actual continuation meets a reviewed contradiction
or a named B25/S17 occurrence. Owner: Opus (fresh on coverage; produced
neither the S audit nor the B integration); reviewer: Fable. Dependencies:
promoted route-separation and terminal theorems only. Outcomes: proved ⇒
the hypothetical-minimal-counterexample funnel lands on named occurrences
and every conditional terminal theorem arms at once; refuted/`OPEN` ⇒ the
coverage gap acquires a precise type and Avenue-2 capacity shifts to
source-interface serialization (P2) with no illusions. Stop: if the lemma
requires continuation data an actual equality record does not supply ⇒
typed `OPEN`, per FALLACY-v2 (no fill by cap or analogy).

**L3 — proof: S-route typing completion.** The existing S-bridge review
debt (custody reseal + different-model mathematical reconstruction of
`1a6472f8...`), extended by one page: type the S terminal
reduced-deviation recurrence as `(ROW_j)` with landing `O = kbar - D`,
then invoke MST-4/5 verbatim for `j=13` (§3.4). Owner: Grok (untouched by
the S bridge); reviewer: Opus (owns the MST framework). Outcomes: typed
same ⇒ the S window is transparent at resonances and the P1/P2 funnel is
confirmed on both routes — my blind Card A closes with it; typed different
⇒ a real B/S asymmetry datum, which redirects the sibling analysis and is
worth having on its own. Stop: reseal fails again, or the recurrence
cannot be typed without source values ⇒ typed `OPEN`; no S objects reused
on B, no value transport without serialized maps.

**Systems trial (exactly one) — `CAPRUN/v1`, merged smallest spec.** One
file `ops/caprun.py`, argv-only, no call-site migration this wave. Union
of the four blind cards minus everything untestable: stdin `DEVNULL`
unless `--stdin-file` names an existing regular file; child in a new
session (`setsid`; PGID = child PID); `(pid, pgid, start-token)` captured
at spawn and re-validated before every signal; `Popen.wait(timeout)`
authoritative — no `kill -0` anywhere (source-grep fixture enforces);
timeout ⇒ TERM to the validated PGID, bounded grace, KILL to the validated
PGID, one reap; `RLIMIT_CPU` in the child (portable, exercised); RSS by
poll-and-kill with a typed `CAP_RSS` outcome — a hard `RLIMIT_AS` claim is
**rejected** because Darwin refuses it (recorded twice in the campaign
record) and the packet forbids overclaiming untestable features; telemetry
JSON to a **required `--telemetry-file`**, never stderr (Opus's measured
stderr-merge hazard), including caps, wall/CPU/RSS, argv hash, and typed
outcome `{EXIT_OK, EXIT_NONZERO, TIMEOUT_WALL, CAP_CPU, CAP_RSS,
SIGNALLED, RUNNER_FAIL}`; sha256 of captured stdout/stderr after the reap.
Fixture matrix (deterministic, run twice, byte-identical modulo declared
time/PID fields): (1) EOF-hang incident shape exits `<2 s` with full
stdout; (2) CAS-style script missing `quit;` is TERM/KILLed, one reap, no
orphan; (3) clean exit preserves streams and status; (4) nonzero exit with
empty stdout is not reported clean; (5) same-name decoy outside the PGID
survives untouched; (6) grandchild outliving the child is reaped with the
PGID; (7) TERM-ignorer dies at KILL after grace; (8) CPU spin and RSS
balloon produce their typed cap outcomes; (9) source grep forbids
`kill -0`/unscoped `pgrep`/`pkill`. Owner: coordinator-delegate; reviewer:
any different model. Rejected this wave (scope, not merit): `ops/lane.sh`
migration, nine-loop migration, fd-3 inheritance guarantees (file
telemetry is the tested equivalent), Linux-only `prlimit` claims.
Acceptance: 9/9 fixtures twice; failure retains fixtures and fails closed.

## 5. Required output 5 — stop/defer list and synthesis recommendation

**Stop:** `TD12-ROW-PROPORTIONALITY` (answered negative at desk, §3.5);
`K00-RENORM` (refuted, §3.3); K00 grade-six/seven gates and the full
polarization-shear test for the valuation-one seed (moot after L1);
Sol Card 1's heavy modular/Fitting compiler (superseded by the executed
desk collapse); the geometric half of `K00-G5-THICKENING-FITTING`
(vacuous by §3.1); all K00 rank charts (stay stopped); `j=42` and any
S `j=30` descendant (stay stopped); `TWIN-ORDER` (stays stopped).

**Defer/bank:** `TD12-GA-TRANSLATION-WARD` at its own stop-condition check
only; `TD12-HERMITE-TRANSGRESSION-SHAPE` below L2; nilpotent-filtration
lifting study (only if a re-seeded stratum revives it); finite-pole
carrier (banked, consumer search recorded); LL-1 equality profiles
(banked); `ops/lane.sh` and nine-loop migration (next wave, after the
trial); AWS (idle; no reviewed heavy packet exists).

**Synthesis recommendation (under 250 words).** Adopt the grade-five
collapse as the round's promotion candidate: three independent exact
computations, two methods each, one repaired presentation, and a frozen
typing chain (`AUDIT.md:4121`, v22r1:51, 1349Z:264) that converts it into
the death of the complete valuation-one `C6=1, k10_0!=0` K00 seed. Gate
promotion only on reconciling the owned two-input lane and Grok review of
this report's repairs; then lower Avenue 36 hard and re-seed falsification
deliberately rather than by momentum. Register the verified
linear-in-newest-block ladder (grades 4→5→6, matrix `C` at `u-mu`) and the
elimination-first router as reviewed method, not conjecture; retire RENORM
and the naive even-grade shear. On the proof side, accept that every td12
local-row lane is now closed or source-blocked — `j=17` vacuous and
route-general, `j=42` gauge-entangled, S `j=13` conditionally vacuous,
proportionality interface nonexistent, translation-Ward gauge-only — and
concentrate Avenue-2 capacity on the two lemmas that need no source
values: `TD12-U1-ACTUAL-LANDING` (L2) and S-typing completion (L3). Ship
`CAPRUN/v1` exactly once, without migration, with the untestable features
rejected in writing. The campaign's honest position after this round: the
falsification frontier moves off K00's valuation-one stratum entirely, and
the proof frontier is one occurrence lemma away from arming everything
already built.

## 6. Non-claims

Nothing here proves or disproves JC2, exhibits or excludes a Keller pair,
polynomial map, arc, or occurrence, bounds any degree, asserts attainment
of any floor, or declares an exit price (`charge_basis` absent). The
grade-five theorem is a point-set statement about a formal jet stratum on
the reduced grade-four input with `k10_0 != 0`, conditional for promotion
on the reconciliations named in L1. `REPRESENTATIVE` is not
`FULL_ACTUAL_EXIT`; a vacuous row is silence, not survival; agreement
among models is evidence about a computation, never proof.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `30933`.
- Body SHA-256: `4449c061881962e7a62edeb163c21f6386824745ea82f9b25e0c55f418f53f68`.
- Frozen basis: `40c1ab3448209e3d87173feb947a733f6fe54f7f`.
