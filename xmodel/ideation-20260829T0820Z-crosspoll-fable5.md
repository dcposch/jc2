# Cross-pollination synthesis — round `20260829T0820Z` — Fable 5

Producer: Fable 5 (exact `claude-fable-5`), written 2026-08-29, cross-poll
phase. Role: equal-standing synthesizer over the four blind reports of the
completed round.

## 0. Custody, read set, and compliance

All five charged inputs were read completely and verified byte-exact this
session:

```text
65afb334763023765f701ee9a2140087a47c6ae470877cee0a04b4f4651c0d8f  xmodel/ideation-20260829T0820Z-state-packet.md
cc58a521b92955b8c1e423aacdf60a5b619ba5384c9e05781bafec1ed7647b8c  xmodel/ideation-20260829T0820Z-fable5.md
142d1e3dcd1305dda7397b5cd8f812080c2bf6d6eeb7106203fce9912777e451  xmodel/ideation-20260829T0820Z-opus5.md
ec454b2e958690f396bbd14e901afcb1b5faf9204907911d27b8ab1c972cd98a  xmodel/ideation-20260829T0820Z-grok46.md
ad50d1ada197a3ad424f321707ea62105fafc74a650d8b55e34cc1130c2efa84  xmodel/ideation-20260829T0820Z-sol56.md
```

The four reports' internal body seals were also recomputed and match
(`7c97c36f…` at 29908 bytes, `17dacd75…` at 43633, `349dfed1…` at 22559,
`06933494…` at 28255). Two bounded canonical reads were made to adjudicate
specific lane disagreements: the `2026-08-29 07:10Z` trunk-consumer event and
the `08:15Z` B-charge event in `notes.md` (named file, scoped read). No
post-cutoff report, no other round file, and no prompt/log/run file was
opened. No canonical file was edited; no commit, push, web access, AWS
action, or heavy computation occurred; the only computations were `shasum`,
byte-prefix hashing, and the four hand-arithmetic checks reproduced verbatim
below. The separately owned `jc2-lean` tree was not entered, enumerated,
searched, read, built, statused, modified, or controlled. Scoped names
`G2-PSC`/`G2-BD` are used throughout; bare `G2` is not.

Standing type firewall, enforced in every verdict below: a flag/place is not
a conjugate Puiseux series; a formal cell is not a germ, a Keller map, a
landing statement, a degree ceiling, or a JC2 result; alive ≠ existent;
pole rays and finite-value cv rays are distinct types.

Tier legend used throughout: `T` = promoted theorem (hostile-reviewed);
`DV` = desk-verified in this synthesis (arithmetic shown); `CL` =
conditional lemma (hypotheses unpaid); `CJ` = conjecture; `EX` = experiment
proposal; `SW` = software proposal; `SYS` = systems proposal.

---

## 1. Deduplication by fingerprint

Fingerprint = (target, mathematical object, mechanism, cheapest exact test).
Names are ignored; four lanes used four vocabularies for substantially
overlapping objects.

| FP | Target / object / mechanism / cheapest test | Lane items collapsed | Canonical form |
|---|---|---|---|
| F1 | every charged extra-direction vertex / exit charge / q-dichotomy minimisation / calibration on the three reviewed charges | Opus §3 `Λ`; Fable M-NEW-1 `λ_min`; Grok §3.1 `FLAG-ARITY`; Sol §8 harness layer | **Opus `Λ = min(num(δ), 2·ceil(δ))`** — the only form that calibrates 3/3 (see §5.3) |
| F2 | `(3/4,4)@nu_F=17` sibling / B-direction exit weight / dichotomy re-price of frame data / ledger vs slack | Grok card 1 `SIBLING-ARITY`; Fable card 1 first half; Opus card 1 step-A pre-registration | merged `SIBLING-ARITY` (action 3) |
| F3 | td12 `nu_F=25` level-1 B-child / coefficient vector `C_1` / coupled Keller recurrence / gcd + membership test | Fable card 2 + §6 compiler; Grok card 2 + §5; Sol card 2 `B24-VERONESE`; Opus §6.2 forward framing | merged `B-RECURRENCE-L1` (action 5) |
| F4 | selected exit sets at extra-direction vertices / place-to-flag map / printed-statement audit or one countermodel vertex / statement search then one vertex | Opus card 2 `PLACE-CONSERVATION`; adjacent: Fable audit item 3, Sol §8 schema discipline, Grok's silent use (§5.4) | `PC-AUDIT` (action 1) |
| F5 | direct `nu=1` U2→U2 edge `99bbe233…` / finite edge equation + resonance kill / different-model hostile review with explicit resonant family / substitution at general `r` | Grok card 3 `NESTED-U2-EDGE`; Sol card 3 `U2-RESONANCE-CONTROL`; Fable §9 top-review-priority note; Opus §10 continue note | merged `U2-DIRECT-EDGE` review + mandatory fixture (action 2) |
| F6 | banked formal countermodels (Lemma 2.2 `kappa_i=42·2^r`; Lemma 3.1 `td=6b`) / total exit charge / `Λ` + budget pricing / one desk hour | Opus card 1 step B (`ARITY-CEIL` discriminator) | unique; inside action 4 |
| F7 | `q>=2` exit flags vs ramification of `hat g` / Riemann–Hurwitz count cap / typing question on three known configurations | Opus card 3 `EXIT-RH`; hazard independently declared by Grok's firewall table | HOLD (§3 item 8) |
| F8 | one complete boundary record / Neron–Severi lattices / saturation–discriminant identity + effective `R_phi` / integer linear algebra on one record | Sol card 1 `PIC-DISC` | unique; HOLD + schema adoption (§5.6) |
| F9 | one-affine-modification toric ansatz / `J(u,v)` closed form / exponent forcing / `|det|<=1` | Sol §6 `COVER-MOD` | unique; DV-verified negative control, banked (§3 item 22) |
| F10 | exit flags of the td12 route / `(g(P),g(Q))`-finiteness census / pole-purity typing × ACS rigidity / M7-F paragraph check | Fable card 3 `CV→A(F)`; direct dissent: Grok §3.3 SCOPE-CONFLICT verdict on purity×ACS | REVIEW — the objection *is* the review question (§3 item 19) |
| F11 | depth-24 bamboo / one-place branch datum / semigroup gcd typing / `gcd(6n,25)` arithmetic | Fable C-NEW-2; mild dissent: Grok avenue-6 row | folded into F3 side output |
| F12 | U2 ODE polynomial solutions / rigidity classification / avenue-3 mechanism supply | Fable C-NEW-3; Grok homonymy firewall; Opus avenue-3 reserve note | HOLD pending F5 verdict |
| F13 | 13-edge menu + MFE / td7 / LL-1 legacy floors / λ re-derivation sweep + verify-only passes | Fable card 1 second half | inside action 4 |
| F14 | withdrawn-inference propagation / producer+reviewer prompts / pattern ledger vs phrase denylist vs inference-ID taint / retro-count trial | Opus §8 `FALLACY.md`; Grok §6 denylist; Sol §9 `DECLARED-INFERENCE-ID-TAINT` | merged `FALLACY.md` — selected upgrade (§6) |
| F15 | stale hash pins in prompts/packets / pre-launch resolution linter / LL-1 R2 retro-test | Fable §7 completeness linter | distinct defect class; HOLD, queued (§6) |
| F16 | uniform-overpay global sketch ("every extra-direction of multiplicity `>=2i` costs `>=3` …") | Grok §3.3 | STOP — untyped, per its own proposer |
| F17 | A-tower double-branch → td12 pure-power child transfer dictionary | Grok §3.2 | optional side attempt inside F3; `NO HIT` ≠ kill |
| F18 | printed root-chart convention / narrow page-image adjudication / two-client rule | Fable bottleneck 4; Opus item 6 + card 2 branch; Grok live-family condition; Sol minimal-extraction | HOLD with a named trigger (§3 item 28) |

The dedupe's object lesson: F1 shows 4/4 *nominal* agreement concealing a
real mathematical divergence — only one of the three stated forms of "the
same" instrument reproduces the reviewed values (§5.3). Agreement was not
evidence; calibration was.

---

## 2. Consensus / dissent matrix

### Consensus (4/4 unless noted)

| # | Item | Tier | Exact scope and caveats |
|---|---|---|---|
| C1 | td8 affine equal-join family is dead (`2+2+3+1=8>7` uniformly in the affine parameter) | T (two independent reviews) | Exactly one formal family; not td8 globally, not a degree range, not JC2. All descendants stop (transport, `(0,y)`, layer-10, realization); Opus keeps only the root-chart adjudication alive via the F18 trigger. |
| C2 | td12 U1 `nu_F=25`: `lambda_B=8` exactly, `N=i`, `tau_0=25`, `q=1`; depth-24 unchanged-denominator pure-`i`-th-power child gate is necessary-only; `i=6n` on direct entries | T | One terminal of one trunk. Canonical 08:15Z event confirms the sibling `(3/4,4)@nu_F=17` "is not priced by this result." Exactness rests on the same inference shape as the td8 repair → D1. |
| C3 | Actual pole price is exactly 0; a pole ray has `g(P)=infinity`, cv flags lie on finite-value rays; literal and selected pole exit sets empty | T | Type statement about actual pole rays. Whether purity *composes* with ACS is contested → D6. |
| C4 | U2 reviewed scopes: fixed absorbed data, P0-only paths ending at P1; first integral `nu>=2` equality boundary `kbar=lW/(l-m)` | T | All four name the identical residual leaks: intervening P0 chains, recursively variable bases, rational-`kbar` `nu=1` boundary, and the provisional direct edge (F5). |
| C5 | The q-dichotomy should become a uniform pricing instrument plus a typed software harness | CJ + SW | 4/4 by fingerprint, but the forms are inequivalent; only `Λ` calibrates 3/3 (§5.3). Hypotheses (H1)–(H4) are unpaid debts, (H1) = D1. |
| C6 | The B-child level-1 recurrence test is the right next source discriminator, desk-scale, run forward as a coefficient generator as well as a kill test | EX | Necessary-condition tier only; passing levels never yields a germ, a Keller pair, or JC2. |
| C7 | The direct U2 producer `99bbe233…`/body `11e44767…` must receive different-model hostile review before any descendant work | EX (review) | Sol (its own producer) supplies an explicit resonant family the review must adjudicate — the round's best hostile hygiene. |
| C8 | No AWS this round; every named discriminator is desk-scale; Box01–03 stay idle | consensus policy | Matches the packet's standing rule. |
| C9 | Negative space: no numerical `kbar`/`nu` cap; `NUCAP=500` + legacy Q+E5 solver; case-I fractional-`kbar` negative control before any engine edit; no ambient/guided CE search; K00 stays the strongest actual bounded char-0 seed; family-kill ≠ ceiling; formal cell ≠ germ ≠ polynomial | consensus policy | Unanimous and identical in all four reports. |
| C10 | `G2-PSC`: zero active spending, owed only by a hybrid GGV-to-Sigray architecture; `G2-BD`: dormant until residue A; never merged | consensus policy | Sol phrases `G2-PSC` as REDESIGN-hybrid-only; substance identical. |
| C11 | The wave's evidenced systems failure is withdrawn-inference propagation (canonical 08:15Z: "The producer repeated the flag/series shortcut just exposed in the td8 review") | SYS | 3/4 proposed fixes for this class (Opus, Grok, Sol); Fable proposed a fix for a different class (stale pins). Selection in §6. |

### Dissent

| # | Question | Positions | Adjudication (details in §5) |
|---|---|---|---|
| D1 | Is place conservation at extra-direction vertices printed, provable, or an unpaid hypothesis? | Opus: top audit item, one-unit td8 margin at stake. Grok: restates the `q=1` branch in a form that silently assumes it. Fable/Sol: treated the dichotomy as safe-by-construction at reviewed scope. | LAUNCH first (action 1), owner-constrained. Canonical addendum: the td8 margin *also* depends on the x-side charge being exactly one (`notes.md` td8-kill event) — both margin dependencies go into the audit's scope. |
| D2 | Which form of the exit-charge instrument is right? | Opus `Λ` (closed form); Fable `λ_min` (prose functional); Grok menu form. | DV: `λ_min` read literally fails two of three reviewed calibration points; `Λ` passes 3/3. Canonize `Λ`; `λ_min` DUPLICATE-superseded; Grok's menu form is the fallback if `Λ`'s derivation step fails (§5.3). |
| D3 | Sibling recorded state | Grok: "recorded floor=ceiling=8, slack 0, k=2". Fable: undetermined, an afternoon of frame arithmetic. | Canonical 07:10Z/08:15Z events confirm the two-terminal menu and that the sibling is unpriced, but do not state floor=ceiling=8; that reading presumably sits in the `86ccd2f1…` payload. Re-derive the floor under the dichotomy at launch — recorded floors predate the q-dichotomy. Grok's own rider binds: underpay ⇒ ledger mistyped ⇒ stop and audit. |
| D4 | Depth-24 ranking | Opus: demote to 4th (no theorem multiplier, 24 serial levels, one terminal). Grok/Fable: head of portfolio. Sol: M2 capped at ~20%. | Partially adopt Opus: actions 1–3 precede; level-1 stays in the top five because it is cheap and dual-use; the 24-serial-level grind is not scheduled this round. |
| D5 | Avenue 26 ceiling half (`ARITY-CEIL`) | Opus: raise to first-rank-conditional with a one-hour discriminator. Grok: stay down, family-kills are not a ceiling. Fable/Sol: unchanged. | Run the discriminator (inside action 4) — a one-hour decisive test does not need a prior agreement; defer any tier motion to its outcome. Binding guard (Opus's own + Grok's): if the bound is type-relative it is a DUPLICATE of KJN/RPMC and stops. |
| D6 | Does pole-purity compose with ACS? | Fable card 3 builds a census bridge on it. Grok §3.3: `SCOPE-CONFLICT` — poles are `g=infinity`, `A(F)` is affine; purity "does not compose with ACS". | REVIEW: the resolver is Fable's own step 0, the pending cheap different-model check of the banked M7-F paragraph; Grok's objection becomes the review question. If the reviewer upholds it, the card dies loudly (its stated stop condition). |
| D7 | U2 ODE as avenue-3 rigidity client | Fable C-NEW-3 proposes it for the rational-`kbar` `nu=1` boundary. Grok: homonymy `SCOPE-CONFLICT`. Opus: avenue 3 lowered as kill mechanism, narrow reserve kept. | HOLD pending action 2. Sol's DV resonant family (§5.5) strengthens the eventual case — the ODE provably admits polynomial families the degree lemma cannot kill — but the review decides whether a classification is needed and names the true load-bearing condition. |
| D8 | Allocation split | Sol: 35% landing+type/cofinal, 20% boundary/Picard, 20% falsification design, 20% M2, 5% systems. Fable/Grok/Opus: execution-first on the desk tests. | Adjudicated in §5.7: adopt Opus's two-independent-walls framing; reject percentage allocation; convert Sol's push into one named schema deliverable. |
| D9 | Avenue 4 tier label | Fable/Grok: lower (arming object died). Opus/Sol: unchanged (condition never fired; moving is noise). | Substance is identical in all four: no arming until a nonempty coefficient vector survives at least one level. Record: tier unchanged, arm condition re-pointed at F3's nonempty branch. No further debate warranted. |
| D10 | Systems upgrade choice | Four proposals, three in one defect class. | §6: merged `FALLACY.md` selected; linter queued; inference-ID taint deferred as escalation. |

---

## 3. Dispositions for every genuinely new proposal

Labels: `LAUNCH`, `REVIEW`, `HOLD`, `STOP`, `DUPLICATE`, `SCOPE-CONFLICT`.
Items already promoted (C1–C4) are calibration data, not proposals, and are
not re-dispositioned.

| # | Proposal (lane) | Tier | Disposition |
|--:|---|---|---|
| 1 | `Λ = min(num(δ), 2·ceil(δ))` closed-form exit charge (Opus) | CJ | **LAUNCH** — derivation-or-repair from printed St. 9.3 + `(C7.1*)`, then calibration; inside action 4. Debts (H1)–(H4) carried explicitly; (H1) = item 6. |
| 2 | `λ_min` dichotomy functional (Fable) | CJ | **DUPLICATE** of item 1, and defective as literally written (§5.3). Superseded; no separate work. |
| 3 | `FLAG-ARITY` uniform calculus (Grok) | CJ | **DUPLICATE** of item 1 (same mechanism, no closed form). Retained as the fallback per-vertex branch-menu form if item 1's derivation fails twice. |
| 4 | `SIBLING-ARITY` (Grok card 1 ≡ Fable card 1 first half) | EX | **LAUNCH** — action 3, with Opus's pre-registration rider and the D3 floor re-derivation. |
| 5 | 13-edge floor sweep + MFE/td7/LL-1 verify-only passes (Fable card 1 second half) | EX | **LAUNCH** — inside action 4, tool-driven. |
| 6 | `PLACE-CONSERVATION` audit (Opus card 2) | EX (audit) | **LAUNCH** — action 1, owner-constrained (§5.4): not Opus (self-declared author of the audited step); td8 instance → Fable (no td8 fingerprints); td12 instance → Grok (the audited step there is the Fable-authored review repair, which Grok did not touch); Sol hostile-reviews both outcomes. |
| 7 | `ARITY-CEIL` countermodel pricing (Opus card 1 step B) | EX | **LAUNCH** — inside action 4, after item 1 calibrates; guard binding (type-relativity ⇒ DUPLICATE of KJN ⇒ stop; `psi=r+l-1` used only at its licensed scope, some incoming `mu_e=1`). |
| 8 | `EXIT-RH` typing (Opus card 3) | CJ + declared hazard | **HOLD** — armed only if item 7's positive branch fires (both countermodels price dead); then the typing question only, one desk-day, fail-fast. The hazard is co-declared by Grok's firewall (local flag torsion is not target inertia); if typing fails it is the forbidden identification and stops loudly. |
| 9 | Uniform-overpay global sketch (Grok §3.3) | sketch | **STOP** as a lane, per its own proposer: it is a type-menu/landing obligation in costume. Retained as motivation text inside item 7's positive branch only. |
| 10 | `B-RECURRENCE-L1` merged (Fable card 2, Grok card 2, Sol card 2, Opus §6.2) | EX | **LAUNCH** — action 5, merged spec below. Necessity label downstream of item 6; CE-seed value independent of it. |
| 11 | `B24-VERONESE` catalecticant layer + normalization/delay branch (Sol card 2) | EX | **LAUNCH** — merged into item 10 as the per-level membership test; its `C_j=0`/wrong-degree branch is adopted as a **mandatory repair** to the naive gcd test (§5.2). |
| 12 | A-tower → td12 pure-power dictionary (Grok §3.2) | CL | **LAUNCH** — optional side attempt inside item 10; typed dictionary or `NO HIT`; failure is never a td12 kill. |
| 13 | Forward-generator reframing: record the determined coefficient vector at each passed level (Opus §6.2; echoed by Fable, Grok, Sol) | EX framing | **LAUNCH** — merged into item 10 at zero extra cost. |
| 14 | `TD12-BCHILD/v1` compiler (Fable §6) ≡ Grok §5 software | SW | **LAUNCH** — one build inside action 5; Grok's negative controls unioned in. |
| 15 | `LAMBDA-EVAL` (Opus §7) + `EXIT-PARTITION/v1` (Sol §8) | SW | **LAUNCH** — one merged tool inside action 4: Sol's typed schema (physical flags, place-to-flag map, conjugate series, orbit blocks, `q`, pole/cv type, area/integrality, per-exit weights; `UNTYPED/NO_VERDICT` fail-closed) is the input layer; Opus's `Λ` core + branch menu is the engine; acceptance suite = union of both lanes' fixtures plus the `kbar±1/2` mutation control. |
| 16 | `U2-RESONANCE-CONTROL` (Sol card 3) | DV fixture | **LAUNCH** — as the mandatory fixture of item 17; the family itself is desk-verified here (§5.5). |
| 17 | `U2-DIRECT-EDGE` different-model review (Grok card 3; Fable priority note; Opus continue note) | EX (review) | **LAUNCH** — action 2; recommended owner Opus (only lane with no U2 fingerprints; Sol is the producer and excluded from owning). |
| 18 | U2-ODE rigidity classification as avenue-3 client (Fable C-NEW-3) | CJ | **HOLD** — pending item 17's verdict; Grok's homonymy firewall respected; re-propose only by exhibiting the literal shared ODE, not the word. |
| 19 | `CV→A(F)` image-census bridge (Fable card 3) | CL | **REVIEW** — step 0 only: the pending cheap different-model check of the banked M7-F paragraph, with Grok's D6 `SCOPE-CONFLICT` objection put to the reviewer verbatim. No census day before that verdict; dies loudly on failure. |
| 20 | Semigroup/AM typing of the depth-24 bamboo (Fable C-NEW-2) | CJ | **LAUNCH-merged** — side output of action 5, no separate lane; carries the documented "fibers are multi-place" category-error warning as its typing step. |
| 21 | `PIC-DISC` (Sol card 1) | DV identity + CL setup | **HOLD** — arming condition: the first complete component-labelled boundary record. Core lattice identity verified here (§5.6). Its input spec is adopted **now** into the LL-2 family-record schema (§5.7); the only launchable fragment is the blowup-invariance lemma statement, folded into landing design. |
| 22 | `COVER-MOD` one-modification toric no-go (Sol §6) | DV | Accepted desk lemma, banked as an exact negative control (verified §5.6). Two-modification successor search: **STOP** (unauthorized, per its own proposer — "not permission for an unbounded successor search"). |
| 23 | Sol's percentage allocation (35/20/20/20/5) | policy | **Not adopted** — superseded by the §4 sequencing plus the §5.7 schema deliverable. |
| 24 | `FALLACY.md` anti-pattern ledger (Opus §8) | SYS | **LAUNCH** — selected upgrade, merged seed; measurable trial in §6. |
| 25 | Withdrawn-phrase denylist (Grok §6) | SYS | **DUPLICATE** → merged into item 24 as its grep-regression layer. |
| 26 | `DECLARED-INFERENCE-ID-TAINT` (Sol §9) | SYS | **HOLD** — the structured escalation path if item 24's trial retains and demands machine propagation; not built now. |
| 27 | Review-packet completeness linter (Fable §7) | SYS | **HOLD** — real but distinct defect class (stale pins); queued behind item 24 at the next 48-hour systems checkpoint (2026-08-31 07:24Z). |
| 28 | Root-chart page-image adjudication (all four, variously narrow) | EX | **HOLD** with the two-client trigger (Opus's formulation): fire iff `PC-AUDIT` step (a) is print-undecidable **or** a live family is shown to share the printed convention. One client alone does not justify it. |
| 29 | Avenue-26 tier raise (Opus) | portfolio | **HOLD** — deferred to item 7's outcome; no tier motion on a conjecture. |
| 30 | Avenue-25 raise-narrow as exit-arity consumer (Opus) | portfolio | **HOLD** behind item 8; zero allocation now; the monodromy census stays stopped in every branch. |
| 31 | Avenue-7 raise / avenue-31 reopen (Sol) | portfolio | No tier motion; the substance (construct labelled components) is adopted as the §5.7 schema deliverable instead. |

---

## 4. Best five next actions, in information-gain order

All five are desk-scale. **No AWS anywhere** — unanimous across lanes and
packet-compliant; Box01–03 stay idle. Owners are recommendations to the
coordinator; conflicts are stated.

**Action 1 — `PC-AUDIT` (place conservation).** Does the selected exit set
at an extra-direction vertex of multiplicity `m` necessarily carry all `m`
places? Step (a): locate the printed statement making the exit set
exhaustive on the multiplicity group (St. 9.3 / Def. 3.3 / St. 3.13 /
`U^full` construction); cite it and close, ~1 hour. Step (b): if absent,
attempt one explicit formal vertex with a lone flag carrying `m'<m` places
satisfying every promoted identity; one vertex decides. Scope addendum
(canonical): the td8 kill margin also depends on the x-side charge being
exactly one — carry both margin dependencies. Owners: td8 instance Fable,
td12 instance Grok, Sol hostile-reviews, Opus excluded (self-declared).
Dependencies: none. Stop: one desk-day; unresolved ⇒ escalate to the
page-image queue (which then fires item 28's trigger) and stop.
Outcomes: proved ⇒ both wave headlines harden and `Λ` gains (H1); refuted
⇒ td8 family revives, `lambda_B=8` degrades to a bound, depth-24 loses
necessity, `Λ` suspends pending repair — the largest reversal available;
undecidable ⇒ named source item, two-client adjudication fires. Highest
fanout per hour on the board.

**Action 2 — `U2-DIRECT-EDGE` review with the resonance fixture.**
Different-model hostile review of `99bbe233…`/body `11e44767…`, with
mandatory fixture: substitute `R=T^r-1, S=T^r, L=r, C=-rR` into the
producer's **full** edge system at general `r` (the bare ODE and the listed
side conditions already pass — DV, §5.5) and classify which named edge
condition, if any, excludes it. Verdict space: PASS-at-direct-edge-scope /
GAP / REFUTED / SCOPE-CONFLICT / finitely-many-`r`. Owner: Opus (no U2
fingerprints); Sol excluded as producer. Dependencies: none. Stop: review
verdict; no nested/descendant U2 enumeration before it. Near-free, and the
downside branch reverses a provisional advance before anything consumes it.

**Action 3 — `SIBLING-ARITY` with pre-registered `Λ` prediction.**
(i) Opus writes down `Λ`'s predicted charge for `(3/4,4)@nu_F=17` from its
frame data **before** anyone computes; (ii) re-derive the sibling's recorded
floor under the q-dichotomy (recorded floors predate it; Grok's
floor=ceiling=8 reading is treated as unconfirmed until re-derived — D3);
(iii) compute the exact B-direction weight ledger and compare to slack.
Recommended computer: Sol; Fable spot-checks the re-derived floor.
Dependencies: `Λ` statement (five minutes of action 4's step A); any kill
publication is conditional on action 1's step (a) outcome. Stop: one exact
ledger, or an untyped extra-direction / missing frame datum ⇒ file the
typing debt and stop. Outcomes: overpay ⇒ sibling dead, td12 U1 rides on
one terminal and depth-24 becomes family-decisive; exact fit ⇒ knife-edge
survivor with its own (shorter) source gate — do not import `tau_0=25`;
underpay ⇒ stop and audit the recorded ledger. Out-of-sample hit or miss
for `Λ` either way.

**Action 4 — merged pricing tool + sweeps.** Build the one tool of item 15
(Sol's typed schema + fail-closed `UNTYPED/NO_VERDICT`, Opus's `Λ` core and
branch menu, union acceptance suite including the `kbar±1/2` mutation and
the flag-count⇒series mutation). Step A: derive-or-repair `Λ` from printed
St. 9.3 + `(C7.1*)`; two failed repairs ⇒ closed form dead, fall back to the
branch-menu form (item 3). Then: (i) re-price the 13-edge menu floors
(N1/R1 filters enforced; the false `C_iv` annotation not cited); (ii) price
the two banked formal countermodels — Lemma 2.2 (`kappa_i=42·2^r`, `td=6`)
and Lemma 3.1 (`kappa_P=6`, `td=6b`) — under `Λ` plus
`sum lambda <= td-1-psi` at licensed `psi` scope: the `ARITY-CEIL`
discriminator, decisive in both directions; (iii) MFE/td7/LL-1 verify-only
passes. Dependencies: `Λ` statement; action 3's hand ledger becomes a hard
out-of-sample fixture; all outputs carry action 1's (H1) label until it
closes. Stop: countermodel survival closes the ceiling half loudly
(negative-results channel + `FALLACY.md` seed candidate); type-relativity ⇒
DUPLICATE of KJN ⇒ stop. Desk, stdlib `Fraction`, no CAS.

**Action 5 — `B-RECURRENCE-L1` merged.** Build `TD12-BCHILD/v1`:
reconstruct the `(2/3,3)@nu_F=25` frame from the hash-pinned trunk and
B-charge reports; derive the level-1 coupled Keller recurrence; emit `C_1`.
Test order per the merged spec: Sol's normalization guard first (`C_1`
nonzero and `deg C_1 = 6n` exactly — else the delay/normalization branch,
**not** a pass); then `deg gcd(C_1,C_1')=6n-1`; then the binomially
normalized `2x2` catalecticant minors as the decisive membership test.
Controls: perturbed recurrence coefficient must fail (Fable); a split `C_1`
must violate `J=1`, the gcd gate, or the `N=i` lock (Grok); the
interpolation-only A/B top must be rejected as a non-realization (Grok).
Record the determined coefficient vector at each passed level (item 13).
Side attempts: A-tower dictionary (item 12), bamboo semigroup typing
(item 20). Dependencies: promoted reports only; necessity label downstream
of action 1. Stop: first failing level, level 3, or two desk-days; any
AWS-sized blowup means the object was mis-scoped — stop and repackage for
sealed review. Every branch kills, cuts, or upgrades the only live infinite
budget-fitting family.

Queued behind the five (not scheduled this round): the M7-F paragraph
review (item 19, one paragraph, unlocks or kills F10); `EXIT-RH` typing
(item 8, armed by action 4); the page-image adjudication (item 28, armed by
its trigger).

---

## 5. Named adjudications

### 5.1 Sibling arity

Merged card as in action 3. Three lanes proposed it (Grok, Fable, Opus's
pre-registration); Sol abstained but guarded it correctly ("do not touch
the sibling through" the recurrence card). The genuine content beyond the
blind reports: (i) the canonical record confirms the sibling is unpriced —
so this is the only remaining P1-fitting terminal with no post-dichotomy
ledger; (ii) D3 shows the lanes disagree about its *recorded* state, which
is itself evidence that the recorded floor must be re-derived, not trusted
(recorded floors predate the q-dichotomy — Fable's audit point, Grok's
underpay rider). The pre-registration discipline matters: `Λ`'s first
out-of-sample prediction is worth more than the kill itself.

### 5.2 td12 B-child recurrence

One merged action (action 5), four lanes' enhancements unioned. The
substantive adjudication: **Sol's normalization/delay branch is a mandatory
repair to the packet's naive test.** `deg gcd(C_1,C_1')=6n-1` presupposes
`C_1` nonzero of exact degree `6n`; a zero or degree-deficient `C_1` is a
normalization/delay case that must be routed to the source rules, not
counted as a pass. Grok's two negative controls and Fable's perturbation
control are complementary and all three run. Opus's demotion argument is
partially adopted (D4): the serial 24-level grind has no theorem
multiplier and is not scheduled; level 1 (through level 3 at most) is
scheduled because it is hours, dual-use, and the packet's named smallest
missing datum. Scope guard, unanimous: 24 passed levels would be one
necessary formal source condition — never a germ, never a Keller pair,
never JC2.

### 5.3 Opus's conjectural closed-form exit charge `Λ`

Adjudicated as the canonical form of F1, at CJ tier with debts (H1)–(H4)
explicit. The adversarial finding of this synthesis (DV): **the three
"equivalent" lane forms are not equivalent.** Write `δ = tau_0^min - kbar`.

- Opus: `Λ = min(num(δ), 2·ceil(δ))` → `δ=3/2 ↦ 3` (td8 trunk, reviewed
  twice), `δ=8 ↦ 8` (td12 B, reviewed), `δ=2 ↦ 2` (td8 A-copy, reviewed).
  **3/3.**
- Fable's `λ_min`, read literally — `min(q·δ over q>=2 single-flag, 2·δ
  forced-arity at q=1)` — evaluates to `2δ` in both branches: `δ=8 ↦ 16`
  against the reviewed exact `lambda_B=8`, and `δ=2 ↦ 4` against the
  reviewed exact A-charge `2`. **1/3.** The literal form omits the legal
  single-flag `q=1` branch at integral `δ`, which is precisely the
  attainment in both reviewed exact charges (canonical 08:15Z: "no parting
  occurs, `N=i`, `tau_0=25`, `q=1`, and `lambda_B=8` exactly").
- Grok's `FLAG-ARITY` states the dichotomy without a closed form; correct
  as far as it goes, and it is the fallback menu form.

So the round's 4/4 "agreement" on the instrument concealed a form that
mis-prices integral-defect vertices by a factor of two. `Λ` is canonized;
`λ_min` is DUPLICATE-superseded with this repair note; the derivation
attempt (action 4 step A) is where `Λ` either becomes a lemma or exposes a
hidden hypothesis in one of the three reviewed values — both outcomes
valuable. Note the (H2)–(H1) interaction: (H2) (per-flag descent keeps
`tau_0^min` after a genuine split) and (H1) (place conservation) are both
statements about what a split does to per-flag data; a single countermodel
vertex could break both, which is why action 1 step (b) and action 4 step A
should share their vertex constructions.

### 5.4 Place conservation

The single most load-bearing unaudited inference of the wave, and `Λ`'s
(H1). Margin arithmetic: the td8 kill's whole margin is one unit and lives
in the trunk-charge-3-vs-2 difference, which rests on "a lone flag would
carry all `2i` places"; the td12 exactness (`=8`, excluding 9) rests on the
same shape via `N=i`/`tau_0=25`. Canonical addendum from the promotion
event: the margin *also* depends on the x-side charge being exactly one —
the audit carries both. Adversarial observation (this synthesis): **Grok's
own blind restatement of the `q=1` branch — "a unique flag carrying a
nonintegral area weight is impossible" — silently assumes the lone flag
carries the full group's area, i.e. assumes (PC)**, in the very lane that
firewalled the flag/series shortcut. That is direct evidence both that the
audit is needed and that the inference pattern propagates through
firewalled prompts (feeding §6's motivation). Ownership is
separation-critical: Opus authored the td8 instance of the audited step
(self-declared); the td12 instance lives in the Fable-authored review
repair (canonical 08:15Z "Repair by cases…"). Hence: Fable audits td8
(zero td8 fingerprints), Grok audits td12 (no fingerprints on that step;
its td12 work was the trunk menu, not the B-charge repair), Sol
hostile-reviews both, Opus excluded. Until it closes, every `Λ`-derived
verdict published by actions 3–4 carries `(H1) OPEN` as a labelled
hypothesis.

### 5.5 Sol's U2 resonant family

Verified by hand in this synthesis (DV). With `R=T^r-1`, `S=T^r`, `L=r`,
`C=-rR`:

```text
r·R·S' = r(T^r-1)·rT^(r-1) = r^2·T^(2r-1) - r^2·T^(r-1)
L·R'·S = r·rT^(r-1)·T^r    = r^2·T^(2r-1)
r·R·S' - L·R'·S = -r^2·T^(r-1) = d/dT[-r(T^r-1)] = C'.
```

`R` is squarefree in characteristic zero (distinct `r`-th roots of unity),
`gcd(T^r-1, T^r)=1`, both monic of degree `r`. Sol's conclusion therefore
stands at theorem tier for the bare system: **a degree argument cannot
remove the sole resonance from the ODE plus the listed side conditions
alone.** Consequence: the provisional direct-edge finiteness claim
(`99bbe233…`) is review-critical — either a named, source-backed edge
condition excludes this family for all large `r`, or the direct-edge
advance reverses. This is the round's best piece of hostile hygiene (a
producer attacking its own provisional result), and it upgrades the
already-queued review (C7) from routine to fixture-driven. It does not, by
itself, refute the producer: the producer's full edge system may contain
exactly the excluding condition; finding and naming it *is* the review.
Disposition: action 2, owner Opus, fixture mandatory.

### 5.6 `PIC-DISC` (and `COVER-MOD`)

The lattice core of `PIC-DISC` is verified standard (DV): for a
generically finite `phi: X -> Y` of degree `d` between smooth projective
rational surfaces, `(phi^*a · phi^*b) = d(a·b)` gives `Gram(M) = d·Q_Y` on
`M = A(NS(Y))`, so `|disc M| = d^rho(Y)` by unimodularity of `NS(Y)`;
saturation index `h` gives `|disc Mbar| = d^rho(Y)/h^2`; and for a
primitive sublattice of the unimodular `NS(X)`, `|disc K| = |disc Mbar|`
for `K = Mbar^perp`. Hence `|disc K|·h^2 = d^rho(Y)` — the identity is
theorem-grade *conditional on the resolved-morphism setup* (modifications
isomorphisms over the source affine plane; target compactification
retaining its affine plane; `R_phi = K_X - phi^*K_Y` effective and
supported at infinity). The campaign-side debt is the setup, not the
lattice algebra: it requires exactly the complete component-labelled
boundary record that avenues 7/31 have never paid. Adjudication: genuinely
`NEW`, the first *typed* non-M2 post-landing consumer this campaign has
produced — a direct answer to packet item 7's composition request — and
**HOLD** behind its arming condition (first complete record). What is
adopted now: its input field list goes into the LL-2 schema (§5.7), and
its blowup-invariance lemma is folded into landing design work. Guard
(Sol's own): a lattice necessary condition is not universal JC2 coverage.

`COVER-MOD`'s one-modification no-go is also verified (DV): for
`u=s^a t^b, v=s^c t^d` with `s=x`, `t=(y-h)/x^k`,
`J(u,v) = (ad-bc)·x^(a+c-1-k(b+d))·(y-h)^(b+d-1)`; a nonzero constant
Jacobian forces `b+d=1`, `a+c=k+1`, and polynomiality plus nonconstancy
then force `|ad-bc|=1` in both cases. Banked as an exact negative control;
the successor search stays unauthorized.

### 5.7 Landing / cofinality allocation split

The positions are less contradictory than their percentages: all four
lanes agree the two terminal walls are unpaid, and Opus states the
structural fact cleanest — **landing totality and the cofinal ceiling are
independent walls; a complete ceiling with no landing theorem proves
nothing, and complete landing with no ceiling proves nothing.** That
framing is adopted as canon language. Sol's 35/20/20/20/5 allocation is
not adopted: this round's five actions are hours-to-days each with
guaranteed information, while landing work is design-heavy and gained no
new mechanism this round — Sol's own `PIC-DISC` is blocked on landing
output, so front-loading percentages onto it buys nothing this week. But
Sol's underlying criticism — that the M2 decomposition could quietly
consume the portfolio — is answered concretely rather than dismissed:

- **Named deliverable (design, background lane): the LL-2 labelled
  family-record schema absorbs, now,** (i) Sol's `EXIT-PARTITION` typed
  fields (physical flags, place-to-flag map, conjugate series, orbit
  blocks, `q`, pole/cv type, per-exit weights), (ii) `PIC-DISC`'s input
  spec (boundary components, divisor-level pullback multiplicities,
  canonical data, blowup-invariance), and (iii) an explicit
  (PC)-ready place-to-flag field so action 1's outcome slots in either
  way. This makes every future landed record simultaneously consumable by
  the priced-graph, `A(F)`, and lattice lanes — which is what "raise
  avenue 7" actually needs, without a tier motion.
- Grok's line is binding and unanimous: family-kills must never be
  advertised as ceiling progress. Opus's `ARITY-CEIL` gets its one-hour
  discriminator (action 4), not a ranking promotion; the tier moves only
  if both banked countermodels price dead.
- The review queue (M7-F paragraph; direct-U2 edge) keeps two non-M2
  composition tests moving at paragraph cost.

---

## 6. Selected systems upgrade and its measurable trial

Deduplication (F14/F15): Grok's phrase denylist, Opus's `FALLACY.md`
pattern ledger, and Sol's inference-ID taint are three grades of machinery
for **one evidenced defect class** — refuted inference patterns propagate
into fresh reports even when every file hash is fresh. The canonical
record proves the class: the td12 producer repeated the flag/series
shortcut inside the same wave that exposed it, and §5.4 shows the shape
surviving in a blind report of this very round. Fable's completeness
linter addresses a different class (stale pins) and is queued, not merged.

**Selected: `FALLACY.md` — Opus's form, Grok's regression layer, Sol's
replacement-registration discipline.** One append-only file, hard-capped
at ~40 lines / 1.5 KiB, one line per refuted **inference pattern**
(`pattern | why wrong | correct replacement | exposed-by hash | date`),
injected verbatim into every producer and reviewer prompt, with one added
reviewer-contract line ("state which listed anti-patterns you checked
for"). Seed with the seven patterns already in the record (flag-count ⇒
place/series content; per-ray charge ⇒ exit-set charge; pole typed as
interior child; floors read as exact costs; `sat()` list-wrapping; raw
remainder degree as filtered invariant; matching variable names as a ring
map), registering the two safe replacements of the flag/series pattern
separately (the `q>=2` weight branch and the `q=1` integral-arity branch —
the latter to be annotated with action 1's (H1) status either way). No DAG
machinery now: Sol's taint-ID system is the recorded escalation path if
the cheap version proves value and demands structure.

**Measurable trial (pre-registered, ~1 hour, inside the standing 48-hour
window; next checkpoint 2026-08-31 07:24Z):**

1. Retro-apply the seeded list to the last ten promoted-or-reviewed
   reports; count recorded repairs that are instances of a listed pattern.
   Prediction: `>=3` of 10. Retain only if `>= 2` **and** the injected
   payload stays under 2 KiB.
2. Grep-regression (Grok's layer): the two banked producer bodies that
   used the flag/series shortcut must both hit (old-fail); the repaired
   td8 kill, the td12 exact-charge review, and one unrelated U2 claim must
   not hit (new-pass, no false taint).

Fail either ⇒ record a reasoned `NO_UPGRADE`, delete the file, and do not
rebuild it in a heavier form without new evidence.

---

## 7. Negative space carried forward (unanimous, binding)

No numerical `kbar`/`nu` cap campaign under any branch. `NUCAP=500` and
the legacy Q+E5 solver stay; the case-I `nu_G=1` fractional-`kbar`
negative control precedes any engine edit. No ambient or guided
counterexample search; K00 remains the protected strongest actual bounded
characteristic-zero seed; no new heavy launch this round. No AWS use for
any action in §4. No revival of the killed td8 affine family; no
identification of any family-kill with a `td` ceiling; no inference of a
Keller map, germ, landing theorem, degree ceiling, or JC2 result from any
formal cell, charge, or ledger named in this report. `G2-PSC` and `G2-BD`
remain scoped exactly as in C10. Nothing in this synthesis proves or
disproves JC2.

Compliance restated: this file is the only file written; no canonical
edit, commit, push, web access, AWS action, or heavy computation; no
post-cutoff report read; `jc2-lean` untouched in every mode.

*Report body ends. The seal below covers everything above this line.*

## Seal

```text
report_body_sha256 = 5c3ae2c807d0722bcf43cceb4c11a17526abd8c208b7032c21cbcae9d8874322
report_body_bytes  = 40736
```

The body seal is the SHA-256 of the first 40736 bytes of this file, i.e. up
to and including the line
`*Report body ends. The seal below covers everything above this line.*`
and its trailing newline. Verify with:

```
python3 -c "import hashlib,pathlib; b=pathlib.Path('xmodel/ideation-20260829T0820Z-crosspoll-fable5.md').read_bytes(); print(hashlib.sha256(b[:40736]).hexdigest())"
```

The full-report SHA-256 covers the complete file bytes including this
appendix. Compute with:

```
python3 -c "import hashlib,pathlib; print(hashlib.sha256(pathlib.Path('xmodel/ideation-20260829T0820Z-crosspoll-fable5.md').read_bytes()).hexdigest())"
```

Sealed inputs verified this session:

```text
65afb334763023765f701ee9a2140087a47c6ae470877cee0a04b4f4651c0d8f  state packet
cc58a521b92955b8c1e423aacdf60a5b619ba5384c9e05781bafec1ed7647b8c  fable5 blind report
142d1e3dcd1305dda7397b5cd8f812080c2bf6d6eeb7106203fce9912777e451  opus5 blind report
ec454b2e958690f396bbd14e901afcb1b5faf9204907911d27b8ab1c972cd98a  grok46 blind report
ad50d1ada197a3ad424f321707ea62105fafc74a650d8b55e34cc1130c2efa84  sol56 blind report
```
