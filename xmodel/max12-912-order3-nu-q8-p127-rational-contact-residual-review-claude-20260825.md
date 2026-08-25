# Hostile review: Q8 bidegree residual bound plus rational high-contact kill

Date: 2026-08-25
Reviewer: independent hostile referee (Claude), read-only session
Verdict: **CONFIRMED_WITH_REPAIRS** (composed existential theorem survives; the
exact intersection constant `35,582` is not established by the frozen evidence
and must be repaired to `37,010`, which preserves the contradiction with
margin `3,950`)

## 0. Scope, evidence, and execution disclosure

Reviewed in full: the bidegree report
(`max12-912-order3-nu-q8-sparse-bidegree-residual-bound-20260825.md`), the
rational-contact report
(`max12-912-order3-nu-q8-p127-rational-contact-residual-20260825.md`), the
review-cleared component successor
(`max12-912-order3-nu-q8-p127-component-reviewed-successor-20260825.md`), the
full-contact Jacobian certificate
(`max12-912-order3-nu-q8-p127-full-contact-jacobian-aws-20260825.md`), the
bidegree case (`README.md`, `verify.py`, both `result.json`), the order-16384
contact case (`README.md`, `replay.py`), and the three accepted lanes'
`result.out`/`run.meta` under `aws_box02_v5/` and
`dependency_linear26_order8192/`.  Additionally consulted read-only for
hostile cross-checks: the sparse contact-to-component lemma, `bidegree.py`,
`generate_order16384.py`, the base generator `generate.py`, the pinned
`aws_box02_v1/result.json` of the Jacobian case, the pinned
`interpolation_candidate.json`, the four negative-control `run.meta` files,
`FREEZE.md`, and the frozen 658 case's subset records.

Execution gaps (disclosed, per the no-shell constraint of this session): I
could not rehash any file against custody values, could not execute
`verify.py`/`replay.py`, and could not re-run Normaliz.  All SHA-256 equalities
are checked only as cross-document consistency of the *recorded* strings; the
per-subset Normaliz volumes and the two 127-term polarization sums are
consumed as frozen attestations.  Everything else below is hand algebra.

## 1. Class convention and the two fibre bounds (audit point 1)

The convention is coherent and consistently applied.  With
`V=[w=alpha]` of class `(1,0)` and `Hz=[v=beta]` of class `(0,1)`, a curve of
class `(A,B)` (equal to `A*V+B*Hz`, i.e. `(deg_w, deg_v)` of its defining
polynomial) satisfies `C.V=B`, `C.Hz=A`, and
`(21,190).(a,b)=190a+21b`.  The `result.json` `class_convention` strings, the
report, and the case README all agree.

Horizontal run (`A<=176`): the fibre `v=beta` pulls back through
`v=(x3-2x5)/x5` (equivalently the pinned row `v*x5-x3+2*x5`) to
`x3-(beta+2)*x5`, support `{x3,x5}`, matching `line_support`
`[[...,1],[...,1,0]]`.  Vertical run (`B<=550`): support `{1,w}` for
`w-alpha`.  `bidegree.py` rebuilds the six source supports live from the
hash-pinned `quotient_compiler.py` (`approx`, imposed rows `(1,3,5,7,2,4)`,
variables `w,c,d2,d4,x1,x3,x5`), origin-augments every support, and calls the
hash-pinned parent `mixed_volume.py` (`a6a516d6...`, identical to the
review-cleared 658 pipeline's custody hash).

Hostile checks passed:

- Multiplicity safety.  Rojas's affine bound counts isolated roots with
  multiplicity; for a generic fibre the pulled-back local lengths dominate
  `sum_i m_i * (C_i . fibre)` by the projection formula
  (`phi_* phi^* = deg(phi)`), including inseparable-projection cases, several
  components through one source point, and pushforward multiplicities
  `m_i >= 2`.  The bound direction is safe.
- No fixed basepoints.  `{v=beta}` meets the boundary of `P1xP1` only at
  `(infinity,beta)` and `{w=alpha}` only at `(alpha,infinity)`; a generic
  fibre avoids the finitely many boundary points of each image closure, so
  the affine count captures all of `A` (resp. `B`).  (Contrast §2.)
- Localization and junk strata are upper-safe: the affine system omits the
  localizer, and the cleared horizontal line acquires the spurious stratum
  `{x3=x5=0}`; both only add isolated roots, never subtract.
- Coordinate boundaries: origin-augmentation licenses counting over all of
  `K^7`, not only the torus.
- Support monotonicity in arbitrary characteristic: mod-127 coefficient
  vanishing shrinks supports; mixed volume is monotone; augmented origins are
  kept.  Correct as stated.
- Arithmetic: `887,040 = 176*5040` and `2,772,000 = 550*5040` (hand-checked).
- Cross-run identity: the source-only subset records (indices 1..63) are
  byte-identical (volumes and `normaliz_out_sha256`) across the horizontal
  run, the vertical run, and **both** boxes of the review-cleared 658
  computation; the line-only subset (index 64) differs exactly as the two
  line supports dictate (rank 3 for `{0,x3,x5}`, rank 2 for `{0,w}`).  This
  ties the new runs' source polytopes to the already-reviewed computation
  byte-for-byte.

Conclusion: `A<=176` and `B<=550` are established, conditional only on the
frozen Normaliz attestations (single-run each; see finding R3).

## 2. The `A+B<=658` step is NOT established (audit points 1 and 3) — FINDING R1

The frozen 658 computation (component-lemma custody; line support
`{x5, x3, w*x5}`, the clearing of the affine line `a*w+b*v+c`) bounds the
number of affine intersections with a generic plane line.  In `P2` a generic
line avoids all points at infinity of the image closures, so that count
equals the plane degree: `deg_P2(pi_*Z) <= 658`.  That is exactly how the
lemma states and uses it, and how the reviewed successor consumed it.

The bidegree report instead asserts `A+B<=658` in `P1_w x P1_v`.  This is a
strictly stronger statement and it does not follow: the bihomogenization
`a*W1*V0 + b*W0*V1 + c*W0*V0` of **every** affine line vanishes at
`(infinity,infinity)`, a fixed basepoint of the affine-line family in
`P1xP1`.  If any image component `C_i` passes through `(infinity,infinity)`
— equivalently its monomial `w^{A_i} v^{B_i}` is absent, equivalently
`A_i+B_i > d_i` (plane degree) — the affine count misses
`I_{(inf,inf)}(C_i, line) >= 1` per line, and `A_i+B_i` exceeds what 658
bounds.  The phenomenon is present in this very configuration: `H` itself has
`A_H+B_H = 211 > 190 = d_H`, so `H`'s closure passes through
`(infinity,infinity)`.  No frozen evidence constrains the residual components
at that point.  In general `A+B >= d` with equality iff the top-bidegree
monomial survives, so `deg_P2 <= 658` can never imply `A+B <= 658`.

Consequently the constraint `a+b <= 658-211 = 447` is unproven, and with it
the exact constant in the report's equation (1), `I(H,R) <= 35,582`, and the
derived eight-contact threshold `M=4,448`.  (The subtraction `658-211` is
additionally incoherent on its own terms: under the only licensed `P2`
reading, an `H`-summand consumes `190`, not `211`, of the 658 budget, and the
leftover plane-degree budget transfers no useful `a+b` constraint at all.)

This is a **false mathematical implication** in the producer bidegree report
(one sentence: "The generic `(1,1)` target-line calculation frozen previously
also gives `A+B<=658`"), not merely a custody or exposition omission.  The
case README and `verify.py` are not themselves at fault (the README expressly
delegates the cycle arguments to the report; `verify.py` computes a correct
LP value *given* the constraint set), but the printed line
`residual_H_intersection<=35582` and `replay.py`'s echoed
`residual_bound=35582` inherit the defect.

**Smallest exact repair (no new computation).**  Drop the `a+b` constraint
and restate (1) as

```text
I(H,R) <= 190*155 + 21*360 = 37,010,
```

using only `A<=176`, `B<=550`, one `H`-summand of class `(21,190)`, and
effectiveness.  Then the composed inequality (3) becomes
`40,960 > 37,010`, strict with margin `3,950`, and the rational-contact
theorem's conclusion is unchanged.  Downstream constants: "a single residual
source point with verified order at least `35,583` is impossible" becomes
`37,011`; the eight-contact threshold `M=4,448` becomes `M=4,627`
(`8*4627=37,016>37,010`, `8*4626=37,008<=37,010`); the sentence "improves the
separate-coordinate-only value 37,010" is withdrawn.  Optional sharper
repair, requiring one new run: an origin-augmented affine-BKK computation
with the basepoint-free `(1,1)` support `{x5, x3, w*x5, w*x3}` (clearing of
`a*w+b*v+c+d*w*v`), whose mixed volume legitimately bounds `A+B`; by
monotonicity it will return a value `>= 658`.

## 3. Removing one H-summand (audit point 2)

Verified, given R1's repair.  If at least one component of the localized
cycle has image `H`, the `H`-part of `pi_*Z` is `mu*H` with integer
`mu>=1`, so the effective residual has class
`(a,b) = (A_tot-21*mu, B_tot-190*mu)` with `a<=155`, `b<=360`; `mu>=2` only
tightens.  Attacks fail: negative coefficients are impossible for effective
classes on `P1xP1` (both fibre intersections of an effective curve are
nonnegative); no assumption on source degree or on the size of the
source-to-image multiplicities is used beyond `m_i>=1`; several `H`-supported
summands are absorbed into `mu`.  The load-bearing bidegree of `H` itself,
`(21,190)`, I verified directly against the pinned
`interpolation_candidate.json` (hash-pinned by every lane's `run.meta`):
`degree_v=190`; the `"190"` row is `[[0,1]]` (monic, `v`-leading coefficient
constant `1`); a full pattern scan finds **no** `w`-exponent `>= 22` anywhere
in `nonzero_support`, and `w`-degree `21` is attained with nonzero
coefficient (`[21,29]` in the `v^0` row).  So `deg_w H = 21` exactly.  (Note
`maximum_support_count: 21` is a support-count field, not the degree; the
degree fact needed here is the scan just described.)

## 4. The linear optimization (audit point 3)

`verify.py`'s brute force is correct arithmetic for its constraint set, and I
reproduce it by hand: maximizing `190a+21b` under `a<=155`, `b<=360`,
`a+b<=447` pushes `a` first (`190>21`), giving the vertex `(155,292)` and
value `190*155+21*292 = 29,450+6,132 = 35,582`; the competing vertices give
`24,090` (`(87,360)`), `29,450`, `7,560`.  No projective or common-component
term is missed *on the upper-bound side*: `190a+21b` is the full `P1xP1`
Bezout total including boundary contributions, and `H` (irreducible) shares
no component with the non-`H` residual by construction.  However, per R1 the
constraint `a+b<=447` is unlicensed; the honest optimum over the licensed
constraints is `(155,360) -> 37,010`.  Both `35,582` (conditional) and
`37,010` (licensed) beat `40,960` — see §9.

## 5. Three distinct rational contacts (audit point 4)

Hand-verified from frozen data, independently of any solver.  Multiplying
`(v+101)(v+69)(v+60)` gives `v^3+103v^2+24v+56` over `F_127`; multiplying by
the pinned quintic `v^5+53v^4+38v^3+26v^2+118v+79` gives

```text
[106, 122, 106, 126, 72, 61, 60, 29, 1]   (low-to-high),
```

which equals `q8_monic_low_to_high` in the pinned Jacobian-case
`result.json` byte for byte.  The three linear factors have the three
distinct `F_127` roots `26, 58, 67` (`-101,-69,-60` mod 127), matching
`replay.py`'s `FACTORS` and its root/factor consistency check
`(factor[0]+factor[1]*root) % 127 == 0`.  These are three genuinely distinct
rational plane points `(0,26),(0,58),(0,67)` — distinct `v` at `w=0` — not a
residue-field orbit (each lane works in `F_127[a]/(linear) ~ F_127`), not a
repeated root (`q8_squarefree` attested; distinctness of the three linear
roots suffices for the additivity used), and the three lanes consumed three
distinct pinned `input.sing` files.

## 6. Branch certificates and the Newton lanes (audit point 5)

I audited the base generator `generate.py` (hash `77ab6350...`, identical in
all three lanes' `run.meta`) line by line, plus the `generate_order16384.py`
adapter, which I confirm only widens the accepted order list
(`... 8192` -> `... 8192, 16384`) against the pinned base hash with a
unique-anchor check.

- Same source everywhere: the eight equations are rebuilt per lane from the
  hash-pinned `quotient_compiler.py` (`approx`; rows `e1,e3,e5,e7,e2,e4`
  asserted equal to `(1,3,5,7,2,4)`) plus `ev=v*x5-x3+2*x5` and
  `eloc=inv*x5*(x3-2*x5)-1` — exactly the Jacobian certificate's chart
  (`source_chart` field agrees).  The base section is imported from the same
  pinned `result.json` (`804f9fbb...` in every lane and in the adapter's
  dependency list).
- Unit Jacobian at the three points, hand-verified: evaluating the frozen
  determinant representative `101+42v+36v^2+116v^3+8v^4+110v^5+107v^6+14v^7`
  at `v=26,58,67` gives `104, 27, 61` mod 127, all nonzero.  (The frozen
  `gcd(det,Q8bar)=1` and norm `88` attestations cover all eight geometric
  contacts; the three rational ones are now independently hand-checked.)
  Together with `base_fail=0` (which re-proves the eight base equations, the
  membership `H(0,v0)=0`, `gcd(detJ0,q)=1` via `gcd_detJ_factor_degree=0`,
  and the Bezout inverse and `J0*K0=I` checks), each contact carries exactly
  one reduced formal source branch with `w` as parameter, the completed local
  ring is `F_127[[w]]`, and the localizer stays a unit along the branch
  (`eloc` holds identically on the jet, so `x5` and `x3-2x5` are units in
  `F_127[s]/(s^N)`).
- The lift is genuine and on-fibre: the certificate is **not** Newton theory
  but the final gate — `evalFinal` re-substitutes the lifted jet into all
  eight equations in `F_127[s,a]/(s^N, q)` and `final_fail=0` attests
  `F(s,y(s)) = 0 mod s^N`.  The jet's constant term is structurally pinned to
  the base section (`DELTA(0)=K(0)*F(0,y(0))=0` inductively), so by Hensel
  uniqueness (unit Jacobian) the jet **is** the truncation of the unique
  formal branch.  `H` is then evaluated at the branch's own coordinates
  `(w,v)=(s, v(s))` — not a projection, not an off-fibre congruence, not a
  quotient-by-`H` ring.  Iteration counts match the doubling schedule
  (`14 = log2(16384)`, `13 = log2(8192)`), and `moving_vdim = N * deg(q) = N`
  for the linear factors, as printed.

## 7. Semantics of `h_contact_order=-1` and the failed lanes (audit point 6)

From the generator source: `h_contact_order=-1` with `h_lead_coefficient=0`
is printed exactly when `reduce(evalFinal(H), ZA) == 0`, i.e.
`H(s,v(s)) = 0` in `F_127[s]/(s^N)` — a statement modulo `s^N` only.  The
code then prints `h_contact_at_least=N`, and every consuming document claims
only `ord >= 16384/16384/8192`.  No infinite-order identity is claimed
anywhere.  Correct.

Negative controls: the two Box03 order-16384 lanes have `rc=14`,
`endpoint=FAIL` (explicit memory failures on the same pinned inputs — I
confirmed `input_sha256` equality with the corresponding V5 PASS lanes); the
two 384-GiB V6 mirrors have `rc=143` (SIGTERM), `endpoint=FAIL`, and their
`run.meta` start times (`07:34:08Z`) postdate both V5 completions
(`07:33:54Z`, `07:34:00Z`), consistent with the "terminated as redundant
after both V5 passes" claim.  `replay.py` consumes them only as FAIL-classed
controls.  They contribute nothing, and nothing rests on them.

## 8. The contradiction and additivity (audit point 7) — FINDING R2

The contradiction argument is sound with one definitional repair.

- Under the hypothesis that none of the three branches is `H`-supported:
  each contact lies on exactly one component of the localized source (local
  ring `F_127[[w]]` is a domain), whose image is a curve (the branch image
  `{(s,v(s))}` is nonconstant in `w`, so the image cannot be a point and
  cannot be a vertical fibre `w=const`); it cannot be a horizontal fibre
  `v=v0` either, since `H(w,v0) = 0 mod w^N` with `N > 21 = deg_w H` would
  force `(v-v0) | H`, contradicting irreducibility of the degree-190 `H`.
- No normalization loss: the branch is parametrized by `w=s`, which is also a
  plane coordinate, so the map onto its image branch is birational and
  `ord_(image branch)(H) = ord_s H(s,v(s)) >= N` exactly; pushforward
  multiplicities `m_j >= 1` and any additional branches over the same plane
  point only increase the local term.  Local intersection numbers at the
  three **distinct** plane points add, and every other local term of
  `I(H,R)` (including at `P1xP1` boundary points and on any vertical
  residual components through `(0,v0)`) is nonnegative since `H` shares no
  component with `R`.  Hence `I(H,R) >= 16384+16384+8192 = 40,960` — the
  displayed sum needs no renormalization.
- **R2 (exposition/definition, not a false implication):** the bounded cycle
  must be defined to contain the three contact components.  The
  contact-to-component lemma's `Z` ("components meeting the charged
  fixed-fibre points") does not obviously contain them, and the bidegree
  report's "relevant pushed-forward source cycle" is undefined.  The frozen
  BKK evidence bounds the pushforward of the **full** localized one-cycle
  (every curve component of the six-row scheme not contained in
  `{x5*(x3-2x5)=0}`) at no extra cost, and both the reviewed `H`-witness
  component and the three contact components lie in that cycle (the latter
  because the localizer denominators are units at all Q8 contacts —
  `gcd`-1 attestations, hand-confirmed at the three rational points).  The
  repair is one definition sentence in the bidegree and rational-contact
  reports; without it, the step "each then lies on the non-`H` residual
  source cycle" has an unstated premise.

## 9. Strict arithmetic and the firewall (audit point 8)

`16384+16384+8192 = 40,960`; `40,960 - 35,582 = 5,378` (as displayed) and,
under the R1 repair, `40,960 - 37,010 = 3,950` — strict either way.
Robustness of the repaired composition against the single-run Normaliz
attestations: with `A<=176` fixed, the argument survives any `B <= 738`
(34% headroom over 550); with `B<=550` fixed, any `A <= 196` (11% headroom
over 176).  Thresholds `8*4448=35,584>35,582` and `8*4447=35,576<=35,582`
are correct as integers but tied to the unlicensed constant (repaired:
`M=4,627`).

Firewall: enforced correctly and consistently across the bidegree report,
the rational-contact report (§6), the case README, and `FREEZE.md`.  The
conclusion is the existential disjunction over exactly the three rational
contacts `26,58,67`: not which one, not the quintic orbit or all eight
contacts, not source degree one, not characteristic-zero no-merger, not
Taylor/terminal conclusions, not maximum-12, not JC2.  The composed claim is
everywhere marked provisional pending precisely this bidegree review.
`FREEZE.md` scopes the unconditional payload to the three exact contact
lower bounds — correct.

## 10. Findings and classification

- **R1 (false mathematical implication; repairable exactly, no new
  computation).**  "`A+B<=658`" does not follow from the frozen affine-line
  count, which bounds the `P2` degree only; fixed basepoint
  `(infinity,infinity)` in `P1xP1`; `H` itself exhibits the gap
  (`211 > 190`).  Constant `35,582`, threshold `M=4,448`, and the `a+b<=447`
  constraint are unestablished.  Repair: restate (1) as `I(H,R) <= 37,010`
  from `A<=176`, `B<=550`, `mu>=1`; composed conclusion unchanged
  (`40,960 > 37,010`).  Optional: new basepoint-free `(1,1)` mixed-volume run
  with support `{x5,x3,w*x5,w*x3}` for a legitimate sharper constant.
- **R2 (exposition/definition).**  Define the bounded cycle as the full
  localized one-cycle so that the three contact components are inside it;
  one sentence in each report.
- **R3 (custody/hygiene, non-blocking).**  The vertical `B<=550` run has no
  pipeline controls (`controls={}`) and neither bidegree run has a
  second-box execution replication, unlike the twice-run 658 value; `B` is
  load-bearing even after repair.  Mitigation already in evidence: identical
  pinned pipeline, and byte-identical source-only subset records across all
  four Normaliz runs.  Recommend one replication of the vertical run with
  controls.
- **R4 (disclosure).**  This review could not rehash files or execute the
  verifiers; hash equalities were checked as recorded-string consistency
  across `verify.py`, `replay.py`, `run.meta`, custody blocks, and
  `FREEZE.md` (all consistent), and Normaliz volumes were consumed as frozen
  attestations.

Under the review instruction to mark any unestablished intersection
hypothesis: the composed theorem **as numerically stated** (with `35,582`) is
unconfirmed; the composed conditional existential theorem — at least one of
the three rational corrected-Q8 contacts `(0,26),(0,58),(0,67)` lies on an
`H`-supported mod-127 source component, conditional on the review-cleared
`H`-component existence — **is established by the listed immutable evidence
after the named exact repairs**, with strict margin `3,950`.

CONFIRMED_WITH_REPAIRS
