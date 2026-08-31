# Cross-pollination report — round 20260831T1033Z

## Input integrity and method

Before reading, I verified all five frozen copies with `shasum -a 256`. They match the charged values exactly: packet `196e1700…b476`, fable5 `9f70069c…e3f2`, opus5 `240adb4b…0ea`, sol56 `7bf7502e…8b46`, and grok46 `32918248…07a3`. All citations below are frozen-copy line numbers, abbreviated `P`, `F`, `O`, `S`, and `G`. I used desk-scale source comparison and hand reasoning only: no CAS, no `jc2-lean`, and no inspection of charged originals or canonical ledgers.

Dedup rule: two cards are one fingerprint when their target, mechanism, mathematical object, and falsifier coincide. Repeated wording or the same source chain is not a vote. I mark a vote only when a genuinely different mechanism bears on the same launch decision.

## Fingerprint-level deduplication

After collapsing each author's section-3/card restatements, 13 within-author families remain; cross-author fingerprinting leaves **ten**. “Pass” below always means necessary-condition pass, never attainment.

| Fingerprint and provenance | Target obstruction | Mechanism | Typed object | Cheapest decisive test |
|---|---|---|---|---|
| **HF-ATTAIN** — Fable new avenue/Card A and Sol new avenue are one duplicate family, not two votes `[F:112–148,251–269; S:75–81,105–112]` | Algebraic attainment of a colourable rank-four survivor | Heegaard–Floer correction-term / semigroup-counting inequalities; separately licensed node formulas | Projective degree, genus, and **all** affine/infinity singularity records of the projective closure | First populate the complete `Delta_aff=6` dossier; one violated inequality kills that candidate, a pass is only a floor, and missing degree/tangency is `OPEN` |
| **BUDGET-N** — Fable B, Sol 2, and Grok III are one Orevkov-retyping family; Grok supplies the safer inertia fork `[F:271–296; S:134–140; G:262–277]` | Bound the number of branch components at every degree | Retype the `N-1` dicritical budget, distinct owner per component, and owner multiplicity | Canonical degree-`N` block; owner dicriticals split into nontrivial- and trivial-inertia classes | One primary-source matrix and the `N=5` case: decide whether a trivial-inertia owner costs 2, 1, or is untyped; stop at the first absent hypothesis |
| **THETA-SNC** — Sol 1 `[S:126–132]` | Close or reduce the one-cusp horn | Mark the charged coordinate on an allowed SNC completion and compute `Theta_h=d_h-r_h-2` | The explicit one-cusp ring, declared coordinate/map, allowed model, and unique horizontal vertex | Independently recompute the divisor table; negative/odd kills, nonnegative even selects exactly one row |
| **AS109-D12** — Sol 3 `[S:142–148]` | First fixed-support polynomial/Witt frontier | Linearized determinant-plus-collision rank calculation with frozen gauge and support | Exact seed, coefficient/Witt rings and maps, complete finite support cell | Provenance/dimension preflight, then an exact inconsistency certificate; inconsistency kills only the cell, out-of-support next lift stops it |
| **TWISTED-Z2** — Fable C `[F:298–314]` | A client-specific obstruction on the wild one-cusp flows | Pair flow-divisor classes with the generator of `Pic(R)=Z/2` | The explicit ring and the promoted flow divisors | One divisor-class calculation; zero closes this revival, while nonzero merely licenses defining a twisted pairing theorem |
| **EULER-INERTIA/M** — Opus new avenue/Card 1 `[O:156–231,257–278,515–541]` | Attainment quota, node exclusions, and a degree-uniform budget | Euler additivity `(E)` followed by replacement of actual affine fibres by fixed local-monodromy sheets to obtain `(M)` | `F`, `D=A_F`, finite normalization `q:Y→A2`, open source `U`, and local inertia groups | Proposed one-node replay plus fixed-point counts on banked colourings; the replacement step fails the adversarial test in §4 |
| **CANON-SIEVE/Y** — Opus 2 `[O:391–424,543–569]` | Structured counterexample search via intermediate surfaces | ZMT/finite normalization, localization for `Cl(Y)`, and ramification for `K_Y` | Normal `Y` containing `A2` with finite flat `q:Y→A2` | Verify the claimed `A2` complement and `K=0` for `xz=y^2-1`; this validates one exclusion, not finiteness of the survivor family |
| **THETA-CHEAP** — Opus 3 `[O:444–461,571–592]` | Avoid the full SNC model | Use hyperbolicity, puncture count `n`, and `gamma_h=Theta_h/2` before global resolution | The **global** general coordinate fibre and its places at infinity | Ask whether licensed existing data determine `n` and separate the four rows; otherwise stop the prefilter and build the model |
| **RESIDUAL-SHEET** — Grok new avenue/Card I `[G:106–121,227–243]` | Attainment after colouring | Treat fixed 1-cycles as degree-1/2 residual covers of `B^sm`, then test section extension or a `Z/2` character | A cover located in the affine source, not merely in its finite normalization | Lowest `(3,1)` and `(2,1,1)` records; currently `OPEN` because the sheet-location lemma is missing |
| **DELTA-REMAINDER** — Grok II `[G:125–143,245–260]` | Attainment from compactification shape | Put an Orevkov `mu=2/3` horizontal vertex on the delta-resolution graph and identify its remainder with `Theta` parity | Curve-at-infinity graph plus a Keller-map horizontal vertex and mapping degree | Lowest survivor graph; currently non-decisive because “same numerical species” is not an equality or a completeness theorem |

**Vote hygiene.** Post-colouring attainment attracts four genuinely different proposed mechanisms—HF, Euler/fixed-point quota, residual-cover extension, and dual-graph remainder—so that priority has four mechanism-level votes. Validity is not additive: Euler and residual-cover share the same sheet-location gap, while the remainder bridge is unproved. Direct `THETA-SNC` and `THETA-CHEAP` are two different execution mechanisms, but their priority was supplied by the packet itself `[P:26–29]`. `BUDGET-N` is one mechanism repeated by three authors, hence one vote. The nearly identical semantic-replay upgrades in Fable, Sol, and Opus likewise count once, not three times.

Connection-only satellites are not extra votes: Sol's Shapiro/twisted-Alexander receiver needs an actual source cover `[S:85–91]`; Fable's survivor construction and conjectural Jelonek degree cap are possible second stages `[F:152–175]`; Opus's Swan and `Y`/LND connections are structural heuristics `[O:327–355]`. None repairs a missing typed input in the ten fingerprints above.

## Strongest composites and cheap discriminators

### 1. `THETA-STAGED/TYPED`

Combine Opus's cheap `n`/parity prefilter, Sol's direct divisor computation, and only the fail-closed interface of Grok's graph calculator. First declare the charged coordinate and ring map, the precise model class to which the partition theorem applies, the global horizontal vertex, and either a canonical/minimal-model clause or a transformation law proving that `Theta_h` is presentation-independent. Then ask whether an independently licensed global puncture count distinguishes the four rows. If it does, the prefilter wins; if it does not, build the single marked SNC model and compute `d_h,r_h`. Do **not** import Grok's Orevkov-remainder equality.

**Cheapest discriminator:** a one-page table of the four rows against `(n, Theta parity/range)`, preceded by the model/vertex scope check. Ambiguous global `n`, non-unique vertex, or model dependence returns `OPEN`; two surviving rows sends the lane immediately to SNC; negative/odd global `Theta` kills; nonnegative even narrows only to the selected row. This directly separates the prefilter from the full-model choice `[O:571–592; S:126–132; G:177–199]`.

### 2. `HF-DOSSIER/ONE-CANDIDATE`

Use Sol's typed, fail-closed singularity interface with Fable's HF counting test and its constructive fork. The essential repair is to separate **candidate kill** from **conductor-row kill**. Fable asserts a finite set of `(d,S_infty)` without supplying a degree cap `[F:138–143,213–229]`, while the same report acknowledges no cofinal degree ceiling `[F:77–79]`. Therefore no bounded scan is exhaustive until charged data or a theorem bounds projective degree. For a fixed complete dossier, however, the HF test remains independent of colouring and inexpensive.

**Cheapest discriminator:** try to fill exactly one `Delta_aff=6` record with projective degree, every affine branch, the infinity semigroup, and the theorem variant covering those singularities. A missing field gives typed `OPEN`. If complete, hand-evaluate the genus formula and the first nontrivial semigroup inequality. Failure kills that candidate (and the row only if exhaustiveness is separately proved); a pass is necessary-only and supplies an ansatz for the construction lane. This separates the only launch-ready attainment mechanism from the residual-sheet and remainder proposals `[F:251–269; S:105–112]`.

### 3. `SHEET-TYPED/WEIGHTED-BUDGET-N`

Merge the common source-typing card with Grok's trivial-inertia fork and Opus's finite-normalization viewpoint, while retaining Opus `(E)` only as a global checksum. For each component, distinguish: center in affine `U` versus boundary `Y-U`, and ramification index `e=1` versus `e>1`. Then type a distinct first-separation owner and count it once. Only a sourced theorem excluding the boundary/`e=1` box licenses cost 2 for every component and `2m<=N-1`. Otherwise the best possible result is a separately proved weighted inequality such as `2m_nt+m_triv<=N-1`, or `OPEN`; nontrivial `pi1` of a curve does not itself imply nontrivial inertia.

**Cheapest discriminator:** the four-box generic-sheet table plus one primary-source `N=5` replay. Stop at the first degree-four-only identity, missing distinctness lemma, or untyped trivial-inertia coefficient. This cleanly separates the strong Fable/Sol version from Grok's weighted version and from Opus's purported topological rederivation `[F:271–296; S:134–140; G:262–277; O:271–278]`.

## Adversarial attack on the strongest proposal

On advertised reach, Opus's `EULER-INERTIA/M` is the strongest proposal: it claims an exact, degree-uniform quota, a shorter one-node theorem, an attainment filter, and an Orevkov-independent budget. The global Euler identity

`1 = d(1-e(D)) + e(F^{-1}(D))`

is sound. The conversion to `(M)` is not.

Opus first constructs a finite normalization `q:Y→A2` in which the original source is only an open subset `U≅A2` `[O:177–187]`. It then asserts that a sheet fixed by the local group fills in as a point of the **original** fibre, hence `#F^{-1}(p)=#Fix(H_p)` `[O:204–219]`. A fixed orbit only says that the sheet fills in under the finite map `q`; its center may lie on the omitted boundary `Y-U`. A degree-one boundary/dicritical sheet is precisely an unramified escape: fixed monodromy, no affine point. The local countermodel is `q:Delta→Delta` equal to the identity with `U=Delta*`; monodromy fixes one sheet while the `U`-fibre over `0` is empty. Taking a product with a disk gives the generic-divisor version. Thus the claimed implication needs a new global theorem specific to Keller sources; topology does not provide it.

This breaks three load-bearing statements at once:

1. `D=A_F` need not be a branch divisor of `q`, so `g!=1` and `sigma<=d-2` do not follow. Conversely, outside the rank-four promoted cycle types a nonidentity permutation can be fixed-point-free, so the advertised all-degree `1<=sigma` also does not follow `[O:204–228]`.
2. Even if `sigma=#Fix(g)`, the generic number `a` of fixed sheets whose centers lie in `U` can be smaller. In the simplified two-stratum situation, with `n_p=#F^{-1}(p)`, Euler additivity yields
   `a(nu+s-1)-sum_p n_p=d nu-1`,
   not `(M)`. Writing `b=sigma-a` and `b_p=s_p-n_p`, Opus has omitted
   `-b(nu+s-1)+sum_p b_p`.
3. Singular points are not necessarily the complete fibre-drop set. An affine component over `D` can acquire a boundary center over a smooth point. A correct ledger must stratify the full typed first-separation/exit set and count each jump once; local singularity groups alone do not determine `e(F^{-1}(D))`.

Consequently the proposed one-node “control” is not validating: its corrected equation is `a-a_p=d-1`, which is compatible with `a=d-1,a_p=0` unless the missing theorem already gives a two-sheet ramified loss. That is exactly the dicritical/inertia input the proposal claims to replace. The quota checker, the local-group attainment law, and the Orevkov-budget rederivation therefore return typed `OPEN`, while `(E)` survives as a useful checksum. Even downstream group inference is overstated: a subgroup `S3` acting on three letters has the same single fixed point as a 3-cycle, so `#Fix(H_p)=1` does not force `H_p` cyclic `[O:257–269]`.

There is also a scope failure. Opus correctly notes that `m=1` concerns actual rank-four **proper blocks** `[O:13–23]`, but `(M)` assumes irreducibility and `A1` normalization from that promotion `[O:168–176]` and later admits those hypotheses are essential `[O:294–302]`. Step `(E)` may be block-free; the sharp consequences do not reach the primitive/no-proper-block front.

**Hard verdict:** retain `(E)` and the finite-normalization setup; reject promotion of `(M)` and every quota consequence until a constructible actual-fibre stratification and a theorem locating fixed sheets in `U` are supplied. The four-box `U/boundary × e=1/e>1` audit is cheaper and more discriminating than the proposed one-node replay.

## Shared hidden assumptions and correlated errors

1. **Proper-block scope silently expands to all rank four.** The promotion is for every actual rank-four proper block `[P:3–7]`. Fable's “any rank-four counterexample” construction target `[F:152–160]`, Grok's unqualified singleton `Irr(A_F)` wording `[G:22–23]`, and Opus's primitive reach all need an independent route-to-proper-block statement. Shared `m=1` language is not a landing theorem.

2. **A delta-sequence is repeatedly inflated into a full curve/map dossier.** An infinity semigroup or resolution graph does not by itself specify projective degree, every affine singularity, puncture positions, a Keller extension, or a marked dicritical. Fable's finite-and-small `(d,S_infty)` claim lacks the degree bound its own bottleneck list says is absent `[F:77–79,138–143]`; Grok says the delta-sequence determines affine punctures `[G:112–119]`; Sol's version is safer because it returns `OPEN` on missing degree or an unlicensed singularity `[S:105–112]`. Likewise, `A1` normalization plus one place at infinity does not make the singular image a smooth embedded line, so Abhyankar–Moh coordinate recognition cannot be invoked without an embedding/extension proof. Semigroup-at-infinity tools may still be licensed, but that is a narrower theorem.

3. **Nonproperness is conflated with ramification/nontrivial inertia.** This is the common premise behind Opus `(M)`, Grok's residual sheet, and the strong `2m` budget. A boundary component can be generically unramified (`e=1`) yet still be omitted from `U`; an `A_F` component is not “nontrivial inertia by definition” `[F:280–285]`. The promoted existence of a component with nontrivial `pi1` also does not say its cover representation has nontrivial inertia `[G:262–272]`. These are correlated errors, not support from different techniques.

4. **Local boundary data are treated as a global marked SNC model.** The affine ring alone does not select the charged coordinate, horizontal vertex, or allowed resolution. `r_h` can change under boundary blowups unless the source fixes a minimal model or proves invariance. Opus's global puncture count from local flow data is not derived `[O:444–461]`; Grok's claim that Orevkov correction terms and `Theta_h` are the “same numerical species” is analogy, not a declared map/equality `[G:125–143]`. Keep critical-value flags, physical places, cover series, and boundary vertices separate; check vertex class before any pole identity.

5. **The disproof seed has a provenance/ring collision.** Sol names an `F_109`/`AS109` fixed-support seed `[S:99–101,142–148]`, whereas Grok distinguishes the all-Witt `F_3` Artin–Schreier tower from the 109-sheet `Z_109` Hensel lane `[G:90–98]`. Before any matrix, declare the exact seed, characteristic, coefficient and Witt rings, reduction maps, full `x` **and** `y` support, generator order, gauge, and transported collision. Matching “AS”, “109”, and “degree 12” labels proves no ring map.

6. **Floors are occasionally marketed as objects.** HF pass is not a curve; a residual double cover is not an affine source cover until its carrier is located; an admissible graph vertex is not a Keller extension; nonnegative-even `Theta` selects a row but does not attain it; a survivor curve is only a counterexample seed; and a surface passing `K_Y` still lacks the finite map `q`. The submissions often state these cautions individually, but composites must preserve all of them rather than inherit only the positive branch.

7. **Agreement is heavily packet-correlated.** The packet itself names `Theta_h`, all-degree budget typing, and attainment as the flagship choices `[P:26–40]`. The three replay-linter proposals also use the same quarantined defect and nearly identical fixtures. This is priority convergence, not independent mathematical evidence.

## Ranked launch recommendations

1. **Launch `SHEET-LOCATION/BUDGET-GATE` first.** Make the `U/boundary × e=1/e>1` table at the generic point of one `A_F` component, then demand a sourced lemma for each empty box and a constructible actual-fibre stratification. **Stop condition:** after one generic-valuation/source pass, if fixed sheets can center on the boundary or smooth-point fibre drops remain untyped, retain Euler `(E)`, mark `(M)` `OPEN`, and allow at most a separately proved weighted budget; do not run the quota checker. If all boxes type, send the repaired identity through different-model review before consumption. **Expected information gain:** **very high at minutes-to-hours cost**—it either rescues the broadest new theorem or prevents three correlated false launches and decides strong versus weighted all-degree budgeting.

2. **Launch `THETA-STAGED/TYPED`.** First fix the charged coordinate, map, admissible/minimal SNC model and unique horizontal vertex; try the licensed `n`/row signature once, then perform the direct divisor table if it does not separate. **Stop condition:** ambiguity or presentation dependence gives typed `OPEN`; negative/odd `Theta_h` stops the horn; nonnegative even stops the generic valuation lane and hands only the selected row to its specific successor. **Expected information gain:** **very high per desk-day**—conditional on the model typing, the outcome is either a whole-horn kill or a four-to-one reduction. This priority is packet-primed, but it is still the most executable mathematical test.

3. **Launch `HF-DOSSIER/DELTA6`.** Attempt one complete projective dossier, then one integer inequality; use Sol's fail-closed singularity typing and prohibit Fable's row-level exhaustiveness claim without a degree cap. **Stop condition:** missing projective degree, missing singularity data, or an unlicensed tangency returns `OPEN` immediately; a violation kills the fixed candidate; a pass remains necessary-only. Stop the mechanism after the first two smallest fully typed survivors if it neither kills nor produces a materially smaller construction target. **Expected information gain:** **medium-high**—it is the only presently credible post-colouring attainment test genuinely independent of the ladder, and its input failure would precisely identify the next data-production task.

No disproof-side proposal presently displaces these three. `AS109-D12` is the best reserve only after the `F_3/F_109` seed and full-support provenance are reconciled; `CANON-SIEVE/Y` is a useful structural filter but its first negative control does not make the candidate class finite; the K00 graded-ring suggestion does not yet exhibit the graded presentation or the claimed algebraization implications.

<!-- BODY-END -->
