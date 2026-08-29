# Hostile review — M2 ARITY-LAW place-conservation source audit (Sol 5.6)

Date: 2026-08-29  
Lane: Fable 5, different-model hostile review, adversarial and independent.  
Target: `xmodel/m2-arity-law-place-conservation-source-audit-sol56-20260829.md`  
Target seals verified this session: full SHA-256
`05f68f4b7278a8ac1216ba82b40e7081bfff66f351380ccd671d12a955784d84`; body =
first `20836` bytes, SHA-256
`1608a44660e094e0fa8cf05b4f1db3b97173243a9e8319a7f55d4c44f0f1cb85`. Both
match the tasking values and the target's own seal block.

Perimeter honoured: work confined to `/Users/dc/code/math/jc2`; no canonical
or target file edited; no commit, push, web, or AWS; `jc2-lean` not entered,
enumerated, searched, read, built, statused, modified, or controlled. Desk
work only: `shasum`, `pdftotext` on the pinned `refs/sigray_full.pdf`, file
reads of pinned reports, and one throwaway exact-`Fraction` python check
(32 assertions, §8). Only this report was written.

## 0. Verdict

**`PASS_WITH_REPAIR`.**

Every load-bearing verdict component of the audit is **CONFIRMED** by
independent reconstruction from the printed source and the pinned reviewed
reports:

1. Literal Opus Card-2 H1 ("selected exit-set flags exhaust exactly all `m`
   places") — **REFUTED AS STATED**, for exactly the two independent typing
   reasons the audit gives. Confirmed.
2. `FULL-EXIT-COVERAGE` for the full actual exit set — **theorem-grade**, from
   Statement 7.3 + Statement 3.13 + Definition 3.3 + Corollary 7.1, all
   re-read on-page. Confirmed, with one well-definedness fine-print note (R2).
3. The td8 trunk floor `lambda >= 3` and the td8 route kill `2+2+3+1=8>7` —
   **survive** on the corrected carrier dictionary. Confirmed.
4. The td12 B-charge **exactly 8**, excluding 9 — **survives**. Confirmed.
5. The proposed equality `Lambda = min(num(delta), 2*ceil(delta))` does
   **not** follow from H1–H4 plus the reviewed exact-separation identities;
   the §6.1 `delta = 4/3` counterprofile is a valid **axiomatic** countermodel
   to the derivation and refutes nothing more. Confirmed, checked exactly.
6. The safe lower floor — `delta` for positive integral defect,
   `ceil(2*delta)` for nonintegral defect, full actual exit set only — is
   **proved** from promoted inputs. Reconstructed independently; floor only,
   no attainment. Confirmed.
7. The §7 wording repairs and the MFE no-repair disposition. Confirmed
   (the MFE quarantine line "a claim that every actual cv flag is one of the
   selected witnesses" is verbatim in the pinned MFE report).

Two repairs, both at qualification/wording tier; **neither changes any
numbered conclusion**:

- **R1 (endpoint rider).** Every "no divergence / no shedding" statement in
  the audit's singleton branches is a **strictly-below-the-cv-level**
  statement, and the audit's replacement wording for the state packet
  ("all `2i` series remain in the common prefix") must carry that rider.
  Separation **exactly at** the cv level remains admissible in general (it is
  the reviewed td8 knife-edge `q=2`, `tau_0=17/2` attainment configuration);
  under Notation 3.5's inclusive convention (`alpha_j <= u`) a `q=1` flag
  additionally excludes at-level conjugate shedding, but not at-level
  physical-place divergence. The audit's `N(tau)=m` "throughout" is literally
  correct only because Proposition 3.1(*) makes `N` count series agreeing
  **strictly below** the level; that convention is load-bearing and unstated.
- **R2 (kappa well-definedness fine print).** Printed Notation 3.5 defines
  `kappa_F` through a choice of place `P` with `F = I_P(u)`. At a vertex whose
  height is simultaneously the exact contact of two places and a
  characteristic exponent of one of them, the printed definition is
  choice-dependent. I verified (§3.3) that every audited conclusion — the
  coverage theorem, both charges, and the floor lemma — is robust under any
  fixed reading, because per-place integrality prices each configuration into
  one of the audit's branches and at-level jumps only move a configuration
  into a **more** expensive branch. This must be recorded where Corollary 7.1
  charges "each distinct flag once".

One supplementary finding, pro-target in direction (§7.3): the audit's §8
risk 5 can be answered constructively. There **is** a candidate source-grid
law (drop levels of `N` carry the denominators of their own `kappa`-jumps)
that excludes the §6.1 profile and, in worked examples, restores exactly the
numerator branch as a floor. It is stated below at CONJECTURE tier; it is not
in the reviewed inputs, which is precisely the audit's point.

## 1. Custody

Target seals: recomputed, both match (header above). The declared body
convention (first `20836` bytes, through the newline after
`*End of sealed report body.*`) was verified by direct byte-range hashing.

All twenty pinned read-set hashes recomputed byte-exact this session:
`refs/sigray_full.pdf` `9bf9f032…`; the five blind-round files
`65afb334…`, `cc58a521…`, `ec454b2e…`, `142d1e3d…`, `ad50d1ad…`; the seven
separation/route packets `991e1b35…`, `ec355795…`, `3c2c9a7e…`, `d9db2440…`,
`a5c342e4…`, `2a151eef…`, `3f214db8…`; the eight exit-set/budget repairs
`c253bd12…`, `727f5850…`, `2763d970…`, `0729a576…`, `86b491ad…`, `ac49c025…`,
`9f4526f2…`, `f55a00f5…`. No substitution, no stale pin.

The audit's quoted body seals were cross-checked against the pinned files'
own declared seal lines and all match: blind lanes Fable `7c97c36…`, Grok
`349dfed1…`, Opus `17dacd75…`, Sol `06933494…`; exact separation
`f1ae6c2b…`/`463a8f48…`; td8 trunk `688dbf41…`/`51f3ed7c…`/`fdb2a6e…`; td12
`b25217e9…`/`8ef16e10…`.

Source pages re-read directly with `pdftotext` (stacked-fraction hazard
respected; every load-bearing formula taken from a display or numbered
statement): Statement 3.1, Definitions 3.1–3.4, Statement 3.2, Notations
3.1–3.14 (pp. 10–16), Proposition 3.1 with its `R^*` proof (p. 14),
Statements 3.9–3.13 (pp. 15–16), Notation 7.1, Statements 7.1–7.3 (pp.
34–35), Corollary 7.1 with the Proposition 7.5 context (p. 38).

One paraphrase note, no repair needed: the audit's §0 block quote of Opus
Card 2 is a fair restatement, not verbatim. The card poses `(PC)` as a
question ("do the selected exit-set flags carry exactly `m` places — i.e. is
no place of the group uncharged?") and H1 as the debt. The audit answers both
halves: "`m` places" is a type error; "no place uncharged" is certified for
the **full** actual set and correctly denied for the MFE **selected** set.

## 2. Attack 1 — the carrier dictionary, and what `mult` counts

**Decision: `mult(p_F,c)` counts Puiseux SERIES on the suitable cover, not
physical places. The audit's §2 is correct on-page.**

- **Physical places/ends.** Statement 3.1 (p. 10) begins "Set
  `P ∈ Rbar_a \ R_a`" — a point of the compactification — and attaches its
  Puiseux expansion with `kappa` = the multiplicity of `x` (or `y`) at `P`.
  Definition 3.2 defines the contact of two **points** as the **max** over
  corresponding series pairs; Statement 3.2's selector `Omega` picks one
  coherent series per point preserving contacts.
- **Rays and flags.** Definition 3.3 builds
  `T_a^* = ((Rbar_a \ R_a) x [0,inf])/~` with `(P,u) ~ (P*,u)` iff
  `u <= O(P,P*)`. One ray per **place**; a flag is a class `I_P(u)`, which
  merges several places whenever their contact is at least `u`. Conjugate
  series of one place never create a second ray.
- **Series on the cover.** Proposition 3.1's proof (p. 14) is explicit:
  `deg(p_d) = #{P ∈ R^* : x(P)=inf, eta_n(P) ∈ C}` and
  `mult(p_d,c_n) = #{P ∈ R^* : x(P)=inf, eta_n(P)=c_n}`, where `R^*` is the
  smooth closure of `h(t^kappa,y)=0`. Cover points are in bijection with
  **series**, and one physical place of `Rbar_a` contributes `kappa_P/kappa`
  … i.e. possibly several of them. Statement 3.9(i) transports this to
  `mult(p_F,c*) = deg(p_(F*c*))`, so `m` is a series count. The reviewed
  A-step conjugate regime (`E_+=2`: one place, one ray, one cv flag, `N`
  dropping `2 -> 1`) realizes the distinction inside the pinned dependency
  set, exactly as the audit says.
- **Direction-orbits.** One `mu_nu` root orbit is one child direction
  (Definitions 3.2–3.3 plus `Omega`; separately verified as a probe in the
  pinned Opus trunk review). Distinct tree vertices are distinct flags;
  conjugate series are not distinct rays.
- **Full actual exit set vs MFE selected set.** `E_all(F,c*)` (audit §3) is
  the set of all Statement-7.3 witnesses of places through the up child. The
  MFE object is one chosen witness `H(F,d)` per **priced direction-orbit**
  `d ∈ D_F` (pinned MFE §4), with the quarantine list stating verbatim that
  "a claim that every actual cv flag is one of the selected witnesses"
  remains quarantined (§6). The pinned selected-orbit attachment repair
  proves attachment and injectivity of the chosen witnesses (its Lemma 3.1),
  not exhaustiveness. The audit's §3.1 three-way disposition — full slice
  covered / MFE subset not exhaustive and never claimed / "`m` places"
  refuted by type — is exactly right, and its formal picture (rays `P,Q`
  splitting inside one direction while `d_f>0`, only `H_P` selected) is
  consistent with the td12 review's two-flag parting mode.

The six objects are pairwise distinct and the audit never conflates them.
**Attack fails to land; §2 confirmed.**

## 3. Attack 2 — FULL-EXIT-COVERAGE

**Verdict: CERTIFIED-CONFIRMED, with hypotheses named and one fine print.**

The chain, each link re-read on-page:

1. **Statement 7.3 (p. 35), verbatim and universal in `P`:** "Set
   `P ∈ Rbar_a \ R_a`. Assume that there exists `u ∈ Q+` such that
   `I_P(u) ∈ T_a^up`. Then there exists `v ∈ Q+` such that
   `I_P(v) ∈ T_{a,cv}`." The witness is on the **same ray**. For
   `P ∈ P(G)` with `G ∈ T_a^up`, take `u = pi(G)`.
2. **Uniqueness.** Notation 7.1 puts `T_{a,cv}` inside `T_a^0 = {d_F = 0}`,
   and Statement 3.13 gives exactly one `u` per place with `d_{I_P(u)} = 0`.
   So any cv flag on the ray sits at `u_0(P)`, and `H(P) = I_P(u_0(P))` is
   **the** unique same-ray cv flag. Existence needs the up hypothesis;
   uniqueness does not.
3. **No remerging.** Definition 3.3 makes the coincidence set of two rays a
   down-set: flags are shared exactly at heights `u <= O(P,P*)`. Places that
   split at contact `s` have distinct flags at every height `> s`; places
   with contact **equal** to a common `u_0` still share the cv flag (this is
   where many-to-one lives, and where R1's endpoint rider bites).
4. **Charging.** Corollary 7.1 (p. 38) is verbatim for any finite subset
   `{F_1,…,F_n} ⊂ T_{a,cv}`: `td(f,g) >= 1 + sum kappa_{F_i}(pi(F_i)-1)`;
   the reviewed actual-weight form accepts any pairwise-distinct set. Each
   distinct flag is charged once — not each place, not each conjugate series.

Consequently every physical place through an up child has a unique same-ray
cv flag; `E_all` leaves no place uncarried; the place-to-flag map may be
many-to-one; and no count of `m` places or `m` flags is implied. The audit
also correctly does not claim injectivity. Two hypotheses to keep visible:
the child must be typed **up** (at reviewed tier this is exactly `delta > 0`
via Notation 6.1 / Statement 6.2, as discharged in the pinned td8 review),
and the standing `c* != 0` assumption of the audit's §2 (the `c*=0` branch
of corrected Statement 9.3 carries a different gap and is not covered).
`P(G)` is nonempty since `deg p_G = m >= 1`.

### 3.3 R2 — the `kappa_H` fine print

Notation 3.5 (p. 12), verbatim: "Assume `F = I_P(u)` for some
`P ∈ Rbar_a \ R_a` … Set `kappa_F := kappa/e_j`, where
`alpha_j <= u < alpha_{j+1}`." Equivalently `kappa_F` = lcm of the
denominators of the characteristic exponents `<= u` of `P`. Strictly below
`u` this is prefix data shared by every place through `F`; **at** `u` it can
differ: if `u` is the exact contact of `P,P*` and a characteristic exponent
of `P` only, then `kappa_{F}` computed via `P` strictly contains the value
via `P*`. The printed Corollary 7.1 implicitly assumes a per-vertex value.
Robustness check, run against every audited use: per-place integrality
(`kappa_{H,P}(pi(H)-1) ∈ N*`, the reviewed (INT) proved at an actual place)
holds for each choice; a reading that includes an at-level jump moves the
configuration from a `q=1` branch to a `q>=2` branch, whose floor is higher
and whose td8/td12 outcome is a contradiction anyway; a minimal reading
reproduces the audit's branches verbatim. So no conclusion moves. Record the
fine print next to `FULL-EXIT-COVERAGE` so no consumer silently assumes
`kappa_H` is place-independent at exact-contact characteristic heights.

## 4. Attack 3 — td8 and td12 on the corrected dictionary

**Both numerical conclusions survive. The missing endpoint qualification is
R1, and it is the only defect found.**

### 4.1 td8 trunk (`m=2i`, `D=17i`, `kbar=7`, `delta=3/2`)

Reconstructed with `E_all` only: every `H ∈ E_all` has
`tau_H >= 17/2`, `q_H ∈ N*`, `w_H = q_H(tau_H-7) ∈ N*` (Theorem A of the
pinned exact-separation primary, Fable-confirmed; (INT) at printed-proof
scope). So `w_H >= 2`.

- Some `q_H >= 2`: that flag alone has `w_H >= 2(17/2-7) = 3`.
- All `q_H = 1`: a singleton `E_all` is impossible — coverage excludes place
  divergence strictly below the common cv level (two places diverging at
  `s < u_0` would carry distinct flags), and `q=1` excludes conjugate
  shedding at or below it (Notation 3.5's inclusive `alpha_j <= u`), so
  `N = 2i` on `(0,tau_0]` under Proposition 3.1(*)'s strictly-below counting,
  the area identity `17i = 2i·tau_0` gives `tau_0 = 17/2`, and
  `w = 3/2 ∉ N*` contradicts (INT). Hence at least two flags, each `>= 2`,
  total `>= 4`.

Floor `min(3,4) = 3`; budget `2+2+3+1 = 8 > 7`. This is exactly Lemma R1 of
the pinned Opus review (their partition "some `q>=2` / some `q=1`", the
audit's "some `q>=2` / all `q=1`"; both exhaustive, same conclusions). The
kill's margin remains exactly one unit and consumes the x-side `psi=1` flag,
as recorded in the pinned review — the audit does not restate this and does
not need to. **No step uses `2i` physical places or MFE exhaustiveness.**

### 4.2 td12 B-direction (`m=i`, `D=25i`, `kbar=17`, `delta=8`)

Every `H ∈ E_all` has `w_H = q_H(tau_H-17) ∈ N*`, `tau_H >= 25`, so
`w_H >= 8`. A shedding flag (`q>=2`) costs `>= 16` and `12 >= 1+16` fails; a
place divergence gives two flags and `12 >= 1+8+8` fails. Both are
single-application subsets of printed Corollary 7.1 — legitimate. The only
surviving configuration is a singleton with `q=1`; then `N = i` throughout,
`tau_0 = 25`, and `w = 8` **exactly**, excluding 9. This matches the pinned
Fable R1 case split line by line (conjugate parting = one flag with
`r >= 2`, weight `>= 16`; distinct parting = two flags). Negative control:
at `td = 18` the shedding branch `18 >= 1+16` survives, so exactness is a
consequence of the `td=12` budget cap, not of the local law alone — the
audit's "Corollary 7.1 gives … impossible" phrasing is correctly cap-relative.

### 4.3 R1 — the missing endpoint qualification, stated exactly

All audit statements of the form "neither loss mechanism occurs before the
cv level" are correct with "before" = strictly below. What must be added
before the wording is promoted:

> Separation **exactly at** the cv level is admissible and charged
> correctly. Place divergence at exact contact `u_0` leaves the flag shared
> (Definition 3.3 allows `u = O`); conjugate shedding at exactly `u_0`
> forces `q >= 2` (Notation 3.5 is inclusive at `u`), moving the
> configuration into the `q >= 2` branch. `N(tau_0)` counts series agreeing
> **strictly below** `u_0` (Proposition 3.1(*)), which is why `N = m` "on
> `(0,tau_0]`" and the area identity are exact in the singleton `q=1`
> branch. The td8 floor-3 attainment candidate is precisely the at-level
> configuration (`q=2`, `tau_0=17/2`, conjugates separating **at** the cv
> level), so the rider is not decorative: dropping it would make the
> repaired wording deny the very knife-edge the reviewed extremal analysis
> permits.

With R1 attached, the audit's §0 state-packet replacement and §4/§5
reconstructions are canonical-grade.

## 5. Attack 4 — the proposed universal equality

**Confirmed: the closed form does not follow from H1–H4 plus the reviewed
identities, and the audit says exactly what its counterprofile does and does
not refute.**

Checked exactly (§8, checks 1–6): `delta = 14/6-1 = 4/3`; area
`6·(13/6)+3·(5/2-13/6) = 14 = D`; `w = 2(5/2-1) = 3 ∈ N*`;
`tau_0 = 5/2 > D/m = 7/3`; every reviewed scalar clause holds — H2
(`tau_0 >= D/m`), H3 (`w ∈ N*`), H4 (`q ∈ N*`), Theorem A(4)
(`q = 2 = E_+/E_0`, `E_+ = 2 <= m = 6`), monotone integer `N`, the area
identity, and declared singleton coverage — yet
`min(num(4/3), 2·ceil(4/3)) = 4 > 3`.

- **What it refutes.** (i) Opus's single-flag inference "integrality forces
  `den(delta) | q`, so `w >= num(delta)`": here `q·delta = 8/3 ∉ Z` while
  `w = 3 ∈ Z`, because integrality applies to `q(tau_0-kbar)`, not
  `q·delta`, and shedding lets `tau_0` sit above `D/m`. (ii) Any claim that
  `Lambda = min(num(delta), 2·ceil(delta))` is a consequence of H1–H4 plus
  the reviewed exact-separation identities.
- **What it does not refute.** The formula as a possible *source-level*
  theorem under an additional hypothesis (the profile is declared axiomatic;
  it is not produced by any Puiseux characteristic sequence, and §7.3 below
  gives desk evidence that honest characteristic grids exclude this exact
  profile), and it produces no Sigray-tree or Keller counterexample. The
  audit's own framing ("axiomatic countermodel … leaves the stronger law
  itself unproved") is precisely calibrated.

Supplementary observation, same direction: the derivation gap does not need
`delta > 1`. On a grid sweep (§8) the safe floor is already strictly below
the proposed value at e.g. `delta = 2/11` (floor `ceil(4/11) = 1`, proposed
`min(2,2) = 2`). The audit's calibration table is verified: at the three
reviewed values `3/2, 8, 2` floor and formula coincide (3, 8, 2), so the
three in-sample matches cannot distinguish them.

## 6. Attack 5 — the safe lower floor

**PROVED at the audit's stated scope; reconstructed independently.**

Scope: full actual exit set `E_all` of an up child in a `c* != 0` extra
direction with `delta = D/m - kbar > 0`; inputs all promoted (per-ray
Theorem A(2) descent `tau_H >= D/m`, (INT), `q ∈ N*`, coverage §3,
Definition 3.3).

- `|E_all| >= 2`: each flag has `w_H >= delta` and `w_H ∈ N*`, so
  `w_H >= ceil(delta)`; total `>= 2·ceil(delta) >= ceil(2·delta)`.
- Singleton, `q >= 2`: `w = q(tau_0-kbar) >= 2·delta`, integral, so
  `>= ceil(2·delta)`.
- Singleton, `q = 1`: coverage kills strictly-below place divergence, `q=1`
  kills at-or-below shedding, so `N = m` and `tau_0 = D/m` exactly, forcing
  `w = delta` — consistent only for integral `delta` (for nonintegral
  `delta` this branch is vacuous by (INT)).

Minimum over live branches: `ceil(2·delta)` for nonintegral `delta`,
`delta` for positive integral `delta` (branch table verified over eight
deltas, §8). Three sharpness remarks, none an error:

1. The floor is **tight at axiomatic scope**: the §6.1 profile family
   attains `ceil(2·delta)` for nonintegral `delta` (e.g. `w = 3` at `4/3`),
   and the singleton `q=1` branch **forces** exactly `delta` when integral.
   So no better floor is derivable from H1–H4 alone; strengthening requires
   new source input (§7.3).
2. `floor <= min(num(delta), 2·ceil(delta))` everywhere (checked on a
   `num < 40`, `den < 13` grid), as consistency requires.
3. The lemma prices the **full** set only. For an MFE one-witness subset the
   singleton `q=1` step is not licensed (audit §8 risk 4) — confirmed: the
   contradiction needs "no place diverges", which only coverage of the full
   set supplies. No attainment is claimed anywhere, and none is granted
   here: grid-admissibility of a minimizing profile is not existence of a
   curve, still less of a Keller pair.

## 7. Attack 6 — wording repairs and the strengthening hypothesis

### 7.1 Canonical wording repairs (audit §7) — all five confirmed

1. State packet lines 45–52: replace "a lone flag would carry all `2i`
   places" by the two-mechanism series statement — **with the R1 rider**
   ("agree strictly below the common cv level; separation exactly at the
   level remains admissible, and at-level shedding forces `q >= 2`").
2. Opus Card 1: no equality promotion; carry the safe floor for the full
   actual exit set only; attainment and any numerator/divisibility law stay
   open. Confirmed.
3. Opus Card 2 / H1: literal H1 `REFUTED`; replace by `FULL-EXIT-COVERAGE`
   — **with the R2 fine print** on `kappa_H` at exact-contact characteristic
   heights. Never write "`m` places" without a separate unramifiedness
   theorem. Confirmed. Note explicitly: Card 2's pre-registered downside
   branch ("(PC) refuted ⟹ withdraw the td8 kill, degrade td12") does
   **not** fire, because neither reviewed proof consumes literal H1 — both
   consume per-ray coverage plus the `q`-dichotomy. Verified against the
   pinned review bodies `51f3ed7c…` and `8ef16e10…`.
4. MFE: no repair; its quarantine already forbids exhaustiveness (verbatim
   line re-read). A consumer needing arity must upgrade explicitly to the
   full local actual flag set and prove disjointness. Confirmed.
5. td8 and td12: retain both conclusions on the repaired proofs. Confirmed.

### 7.2 What "selected" must mean downstream

Anywhere the campaign writes "the selected exit set", it must say which of
the three objects it means: the MFE representative subset (lower bound only,
never exhaustive), the Section-9 first-separation slice `E_i` (exhaustive at
flag level; its cumulative budget (4.3) is proved for singleton poles only),
or `E_all(F,c*)` (exhaustive for one direction; usable directly in
Corollary 7.1 with no pole-count hypothesis). The td8 kill deliberately uses
the third; that must not be "simplified" away.

### 7.3 The remaining source-grid hypothesis (CONJECTURE tier)

The audit's §8 risk 5 asks for a reviewed constraint coupling `q`, the full
step function `N`, and `delta` strong enough to exclude the §6.1 profile.
Candidate, assembled from Definition 3.1, Notation 3.5, and the conjugate
count already used inside Theorem A(4)'s proof — **not** among the reviewed
numbered clauses, hence consistent with the audit's verdict:

> **GRID (unproved).** In the singleton-coverage branch, all places through
> the child share their characteristic levels strictly below the cv level,
> so `N` descends through exact divisions `N = m/q_j` along a divisor chain
> `1 = q_0 | q_1 | … | q_r = q`, and the `j`-th drop sits at a normalized
> level `tau_j ∈ (1/q_j)Z \ (1/q_{j-1})Z`.

Desk evidence (§8): GRID excludes the §6.1 profile outright
(`13/6 ∉ (1/2)Z`); at `(m,D,kbar) = (6,14,1)` an honest `q=2` singleton is
impossible (`3 ∤ 22` obstruction), and the cheapest honest singleton is the
`q=3` shed-at-level knife edge with `w = 3(7/3-1) = 4 = num(4/3)` — i.e.
GRID restores exactly Opus's numerator branch there, and in further spot
checks (`delta = 5/4, 7/4, 2/11`) the honest minimum reproduces
`min(num, 2·ceil)`. Alternatively the audit's own two riders
(`tau_0 = D/m`, or directly `q·delta ∈ Z`) are weaker special cases.
Status: a proposal for a separate producer/review cycle. Even with GRID
proved, `Lambda` equality still needs an attainment theorem; a
grid-admissible minimizer is not a curve.

## 8. Mutation and negative controls

One throwaway exact-`Fraction` python run; 32 assertions; nothing installed;
no file written except this report. 31 behaved as predicted; the one
scripted "failure" was my own wrong minimality expectation (I predicted
`4/3` is the smallest floor/formula divergence; the sweep found `2/11` and
friends below 1 — a finding about the formula, §5, not an audit defect;
recorded, not repaired away).

- **Control A (slack removal).** Force `tau_0 = D/m = 7/3` in the §6.1
  profile: `w = 2(7/3-1) = 8/3 ∉ N*`, violating (INT). The profile *needs*
  the shedding slack `tau_0 > D/m`; and `q·delta = 8/3 ∉ Z` confirms it
  violates the audit's proposed divisibility rider — the rider would exclude
  it, exactly as §6.2 states.
- **Control B (td8 kbar mutation).** `kbar: 7 -> 13/2` makes `delta = 2`
  integral; the singleton `q=1` branch returns with `w = 2 ∈ N*` (no
  contradiction), the trunk floor drops to 2, and the budget reads
  `2+2+2+1 = 7 <= 7`: the kill evaporates. The audited machinery is
  sensitive to the half-unit that carries the theorem — the verdicts are not
  produced vacuously. (This is also Opus Card 1's pre-registered control.)
- **Control C (td12 cap dependence).** At `td = 18`, `18 >= 1+16` holds, the
  shedding branch survives, and exactness fails: the audit's exact-8 pin is
  correctly a consequence of the `td=12` cap plus the local law, not of the
  local law alone.
- **Control D (GRID discriminator).** `2·(13/6) ∉ Z`: the §6.1 profile dies
  under GRID while passing every reviewed clause — separating cleanly what
  is axiomatic from what is source-bound, which is the audit's central
  distinction.

## 9. Clause ledger

| Audit clause | Verdict |
|---|---|
| Target full/body seals; 20 pinned hashes; quoted body seals | **VERIFIED byte-exact** |
| §0 literal H1 refuted for two independent typing reasons | **CONFIRMED** |
| §2.1–2.3 places/series/flags dictionary; `mult` counts series | **CONFIRMED on-page** (Prop 3.1 proof, St 3.9(i), Defs 3.2–3.3, St 3.2) |
| §3 FULL-EXIT-COVERAGE chain (St 7.3 + St 3.13 + Def 3.3 + Cor 7.1) | **CONFIRMED**; up-typing and `c* != 0` hypotheses named; R2 fine print added |
| §3.1 `E_i` slice exhaustive; MFE subset not exhaustive, never claimed | **CONFIRMED** (Section-9 §4.6 and MFE §§4,6 verbatim) |
| §4 td8 floor 3 and route kill on corrected carriers | **CONFIRMED**; R1 endpoint rider; margin-1/`psi` dependency stands as pinned |
| §5 td12 exact charge 8, excludes 9 | **CONFIRMED**; cap-relative (Control C) |
| §6/§6.1 closed form does not follow; counterprofile scope | **CONFIRMED**, arithmetic exact; refutes derivation, not the law-as-theorem |
| §6.2 safe-floor lemma | **PROVED**; tight at axiomatic scope; full-set-only; floor `<=` proposal everywhere |
| §7 wording repairs 1–5 | **CONFIRMED**, with R1 attached to item 1 and R2 to item 3 |
| §8 risk list | **CONFIRMED**; risk 5 answered constructively by GRID (conjecture tier) |
| "`N(tau)=m` throughout" / "remain in the common prefix" wording | **REPAIR R1** — strictly-below rider and Prop 3.1(*) counting convention must be stated |
| `kappa_H` per-vertex well-definedness at exact-contact characteristic heights | **REPAIR R2** — printed Notation 3.5 fine print; all conclusions robust |

## 10. Scope and exclusions

This review certifies the audit's carrier corrections, the coverage theorem,
the survival of the two reviewed numerical conclusions, the refutation of
the closed-form derivation, and the safe floor — nothing more. Explicitly
not established, here or in the target: attainment of any floor; the GRID
law (a proposal only); any degree ceiling or `td` exclusion beyond the two
reviewed formal routes; realizability of any profile by a curve; source
landing; a Keller pair or counterexample; anything about JC2. The td8 kill
retains its recorded margin-1 dependence on the x-side `psi = 1` flag. No
canonical file was edited; no commit, push, web, or AWS action occurred;
`jc2-lean` was untouched.

*End of sealed report body.*

## Seal (outside the sealed body)

- Body length: `27888` bytes (the complete file before this seal heading,
  through the newline following `*End of sealed report body.*`).
- Body SHA-256:
  `00284d5fefa49f998439f772025f845b5d0050bd38dcb6967db637a1a045aa35`.
