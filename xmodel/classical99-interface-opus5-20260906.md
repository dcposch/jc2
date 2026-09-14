# Classical interface at (99,66): GGV22 §2 applies; the chart is predicted empty

**Verdict: `APPLIES_AS_EXTERNAL_THEOREM`**, with one typed
`OPEN[PRIMARY-TEXT-UNREAD]` on lane access, recorded below and not papered over.
No scope conflict and no specific gap was found in the objections the campaign
actually holds. The (99,66) configuration is **not** a legitimate counterexample
frontier: conditional on GGV22's §2 degree dichotomy, the complete physical-J
ideal at (99,66) is the unit ideal. D=108 is **not** touched — it is precisely
the one family the dichotomy leaves open.

**Custody.** Receipts: the eight charged inputs in `/tmp/jc2-lane.mStUJ3/inputs`
were `sha256sum`-checked against `charged-inputs.list`; all eight match
(`APPROACHES.md fb7f8571…`, `AUDIT.md aed95348…`, `FALLACY-v2.md e47fd16c…`,
`factored-jacobian-gate-fable5 c0199680…`, `factored-jacobian-pilot-astra
d870a8a6…`, `frontier_gate.py d709794d…`, `full-ideal-counterexample-gate-fable5
5fc61ae7…`, `linear-c-transverse-rank-astra 8cf51bd8…`). Desk-only: no AWS, no
CAS, no solve, no fleet, no `jc2-lean` (masked to an empty ro bind), no ledger
or instrument edit, no public communication, no other lane's live report or log
read. Repo files read outside the charged set: `ladder/REDUCTION.md`,
`ladder/CROSSCHECK.md`, `refs/` listing — static repo documents, consulted only
for the pinned external-source table. The single host write is this report.

## `OPEN[PRIMARY-TEXT-UNREAD]` — stated first, because it bounds everything below

The brief asks me to read `arxiv.org/pdf/2204.14178v1` (abstract, Theorem 2.1,
p. 2, §4 Case (9,24), §5). **I could not.** The lane is desk-only with no
network, and there is no local copy: `find / -iname "*2204.14178*"` returns
nothing, `refs/` holds `guccione_valqui2017_ja471_shape_counterexamples.pdf`
(GGV1, the *gcd* paper) but no GGV22, and the only local GGV page scans
(`box/census-coverage-*/ggv-p2,p33–p36`) are from arXiv:1401.1784v3 — their
header line reads `arXiv:1401.1784v3 [math.AC] 30 May 2016`, a different paper.

So I did **not** verify Theorem 2.1's hypotheses against its own printed text,
did not read §4 Case (9,24) or the §5 proof, and cannot confirm or deny the
brief's report that §5 explicitly discards actual (66,99). Every statement of
GGV22 §2 used below is quoted from the campaign's own pinned transcription, not
from the source:

- `ladder/REDUCTION.md:938` — “**GGV22** | Guccione–Guccione–Horruitiner–Valqui,
  arXiv:2204.14178v1, *Increasing the degree of a possible counterexample to the
  Jacobian Conjecture from 100 to 108*: §2 degree dichotomy and Proposition 4.3
  for `(A_0,m,n)=((8,28),3,2)`.”
- `ladder/REDUCTION.md:1247` — “The GGV22 ‘`≥125` or `(72,108)`’ result is a
  lower-bound dichotomy in polynomial degree…”
- `AUDIT.md:5413` — a char-0 unit ideal on the (72,108) family “would … raise
  that conditional degree bound **from 108 to 125**”, i.e. 108 is the *current*
  established floor and 125 is what killing (72,108) would buy.

Read together these pin the §2 statement as: **for any characteristic-zero
counterexample `(P,Q)`, either `max(deg P, deg Q) ≥ 125`, or
`{deg P, deg Q} = {72,108}`.** That is the object I audit. The correct next
action for the coordinator is a one-shot fetch of the PDF and a diff of
Theorem 2.1 against this transcription; nothing below should be promoted past
`CONDITIONAL` until that is done. Per FALLACY-v2 I return the typed `OPEN`
rather than filling the gap by analogy with GGV1, which I *can* read.

## Why (99,66) is in scope, not a Laurent/Newton label artifact

The brief's central distinction is the right one to check, and it resolves
cleanly in favour of applicability.

GGV's machinery genuinely does live on reduced objects: `L^{(1)} = K[x,x^{-1},y]`
with `[P,Q] = x^2`, Newton polygons with fractional corners, `1/l · Z × N_0`
supports (`REDUCTION.md:482,940–950`; GGV1 introduction, local scan
`core-ggv-layout.txt`). A degree pair read off a *polygon label* in that setting
is not an absolute total degree, and conflating the two would be exactly the
Flag/place/series error FALLACY-v2 warns about.

But the (99,66) datum is not a polygon label. `full-ideal-counterexample-gate`
Arrow 1 establishes, at **every** point of the semantic affine space and before
any row is imposed, that `h, D, C` are honest elements of `K[x,y]` (support
condition `r+z ≤ N`, no division by a variable), that
`F = h³+(3D+a)h/2+C` and `G = h²−bh/3+D` have **exact** total degrees 99 and 66
(corrections `≤98<99`, `≤65<66`), with parameter-free top forms
`F_top = y^{27}(y−x)^{72}`, `G_top = y^{18}(y−x)^{48}`. Arrow 2 then gives
`J(F,G) ∈ K^×` at every field point, and Arrow 3 pushes a proper ideal to a
`Qbar`-point. `factored-jacobian-gate-fable5:71` independently records
`deg h = 33, deg D = 34, deg C = 35`; `linear-c-transverse-rank-astra:52–54`
independently records `deg G = 66`, `G_top = H^6`, `H = (X+W)^3 W^8` with
`X=x, W=y−x` — the same `y^{18}(y−x)^{48}`. Three charged reports agree.

These are absolute total degrees of genuine polynomials over a field of
characteristic zero. Minimal-counterexample normalization does not rescue the
configuration either, and this is the step worth being explicit about: the
dichotomy's quantifier is over *all* counterexamples, not over a distinguished
minimal one. Even on the weakest reading — “the minimum over all counterexamples
of `max(deg)` is `≥125` unless the minimizer is `(72,108)`” — an actual
counterexample of degrees (99,66) would witness `max = 99 < 125` and force that
minimum to be `≤99`, contradicting the statement. The same structural point is
already recorded for the sibling invariant: `[[ggv-B-minimum-over-all-counterexamples]]`
notes GGV1 Cor 6.6 defines `B` on p. 2 as the min gcd over **all**
counterexamples, so `gcd ≥ 16` needs no “minimal degree sum minimizes gcd”
claim. A degree dichotomy proved for the reduced/normalized representative
transfers to the absolute pair because the reduction only ever decreases degree.
No normalization escape hatch exists here.

**No `SCOPE_CONFLICT`.** (99,66) is an ordinary in-scope point of GGV22 §2.

## Do our existing trust objections defeat this application? No.

I read every AUDIT/REDUCTION objection touching GGV22. All of them are about the
**(72,108) branch**, i.e. about Proposition 4.3 in §4/§5 and the reduction that
lands a counterexample in `(A_0,m,n)=((8,28),3,2)`. None of them is about the §2
dichotomy that excludes everything below 125.

| Recorded objection | Where | What it is about | Bites §2? |
|---|---|---|---|
| “parts of the supporting chain … are **arXiv-only/unrefereed**” | `AUDIT.md:10228` | trust class of the chain feeding **Prop 4.3** subcase analysis | No — a trust class, not a defect |
| “arXiv:2204.14178v1 … **Prop 4.3, THE dependency**” | `AUDIT.md:10313` | names Prop 4.3, not §2, as what the campaign leans on | No |
| “Subcase (1) … required before any ‘(72,108) family discarded / bound = 125’ statement” | `AUDIT.md:10300` | our own debt for raising 108→125 | No — it is a debt on *our* strengthening |
| “no unconditional degree-125 theorem … recorded here” | `AUDIT.md:10531` | our internal cCa2/cCa6 lift retirement | No — about our char-0 certificates |
| “Prop 4.3 as a universal reduction step: **FALSE AS STATED**” | `REDUCTION.md:504–506` | Prop 4.3 read as universal; “conditional on one bounded residual family” | No — §2 is the dichotomy, Prop 4.3 the (72,108) analysis inside it |
| “GGV22 line 1132 contains a `(1,0)`/`(0,1)` slip and later silently swaps P/Q” | `AUDIT.md:5403–5404` | a transcription-level orientation slip in the §4 recurrence | No — repaired by pinning orientation by polygon; it is a *typo* class defect |
| “no statement from GGV3/GGV5/GGV22 turns the bounded GGV family lane into an upper bound on polynomial degree” | `REDUCTION.md:962` | forbids using GGV as an **upper** bound | No — we are using it as a **lower** bound, its actual direction |

The brief's caution is exactly right and I want to state it as a finding rather
than a nicety: **absence of a campaign that reproves GGV22 is not a mathematical
gap in GGV22.** The campaign classifies GGV22 as “preprint” and “load-bearing
only for the repo's (72,108) polygon claim”. That is a correct statement of
*what we lean on*, and it has been silently read as *what is true*. It is not a
refutation of anything, least of all of a statement about degree 99, which no
lane has ever examined.

Where a real unsupported computation would live, if one does: `REDUCTION.md:937`
records GGV5 (arXiv:1708.07936) Algorithm 8 as outputting all admissible
complete chains under an input bound, with “the reported run yields the bounded
tables used for the `max(deg P,deg Q) ≤ 150` farm,” load-bearing “for any
assertion that the farm exhausts GGV families under that stated degree cutoff.”
If GGV22 §2's sub-125 exclusion is carried by that machine enumeration, then §2
rests on an unreplicated computer search in an unrefereed preprint. **I could not
check whether it does** — that requires the §2 proof text. This is the single
highest-value item in the follow-up fetch, and I flag it as a place to look, not
as a defect found. It does not change the verdict: an unreplicated enumeration in
a preprint is a trust level, and the campaign has never held (99,66) to a
standard that survives it either.

## What this changes

**1. The (99,66) full ideal is predicted to be the unit ideal — conditionally,
and not by us.** Chain the two directions:

- *Internal, unconditional within the charged inputs:* every `Qbar`-point of the
  complete direct ideal `I` (indeed of `J_core ⊆ I`) yields `F,G ∈ Qbar[x,y]`
  with exact degrees (99,66) and `J(F,G) ∈ Qbar^×`
  (`full-ideal-counterexample-gate`, Arrows 1–3). Arrow 4 (Jung–van der Kulk)
  makes such a pair a counterexample, since `66 ∤ 99` and `99 ∤ 66`.
- *External:* GGV22 §2 says no counterexample has `max(deg) < 125` other than
  `(72,108)`. `max(99,66) = 99 < 125`, and `{99,66} ≠ {72,108}`.

Therefore `V(I)(Qbar) = ∅`, so by Arrow 3's Nullstellensatz step `I = (1)`.
The registered long solve `17(ooooooooooo)` (δ=2 literal subset `d2-z55`,
harvest ≈ 2026-09-07 04:26Z) has a **predicted** answer: `[1]`.

The epistemic label matters and the brief states it correctly. This unit result
**follows conditionally on an external theorem**; it is *not* an internally
computed certificate. If the solve returns `[1]`, that is a consistency check
against GGV22, not an independent proof — and it should be recorded as
corroboration, never promoted as a campaign kill. If it returns a **point**, the
correct reading is not celebration but a conflict to be adjudicated between our
chart and GGV22 §2, with the transcription and Theorem 2.1's hypotheses the
first suspects.

**2. The necessity GAP cannot rescue the (99,66) frontier.** This is the load-
bearing correction to how the charged gate's hard stop has been applied. That
gate types “Keller pair of degrees (99,66) ⇒ point of this chart” as a **GAP**
and concludes “a unit result or timeout on `I` … excludes nothing about the
`(99,66)` configuration.” That conclusion is sound **in its own direction** and
remains so. But it is a statement about `chart ⊉ configuration`; it says nothing
about `chart → Keller`, and it is precisely the latter direction — Arrows 1–4,
which the gate itself stresses “need no necessity” — that GGV22 attacks. A chart
point *is* an honest (99,66) Keller pair whether or not the chart captures every
such pair. So: the necessity debt makes the chart possibly *smaller* than the
configuration, and the external theorem empties the configuration; a subset of
the empty set is empty. Owing necessity has never been a reason to expect a
point, and can no longer be cited as one.

**3. D=108 is untouched.** `{72,108}` is exactly the surviving alternative of the
dichotomy, so the repaired-mean D108 chart (`(108,72)`, `J ∈ K^×`) is *not*
excluded and its lanes retain their status. It is worth saying plainly that
GGV22's title — “Increasing the degree … from 100 to 108” — means D108 sits **at
the current classical floor**, which is a reason to weight it, not to doubt it.

**4. Coverage gap in `ops/frontier_gate.py` (identified, not edited).** The gate
implements exactly one necessary condition — its own docstring says so — namely
`gcd(deg P, deg Q) ≥ 16` with `THEOREM = "GGV-Heitmann-gcd16"`,
`SOURCE = "https://arxiv.org/abs/1401.1784"` (GGV1). On (99,66) it computes
`gcd = 33 ≥ 16` and returns `NOT_CLOSED_BY_THIS_GATE`, exit 0. That verdict is
*correct for the theorem it implements* and the gate's own `warning` field
already says a pass “is not evidence that the scope … is viable”. The gap is
coverage: **there is no max-degree check anywhere in the file.** Every pair with
`gcd ≥ 16` and `max < 125` outside `{72,108}` — (99,66) gcd 33, (66,44) gcd 22,
(96,64) gcd 32, (120,80) gcd 40, and the rest of the sub-125 band — passes a
gate that a second pinned classical result closes outright. The `--total-cap` branch is affected
identically: it tests only `cap < 16`, so `--total-cap 100` is reported
inconclusive when the dichotomy closes it. The `--partial-y-degrees` branch is
correctly inconclusive either way, since partial-y bounds bound no total degree.
The fix, when the primary text is in hand, is a second registered theorem entry
(dichotomy, source `2204.14178`, trust class *preprint*) emitting its own
verdict field alongside the gcd one, so that a caller can see which theorem
closed the scope and at what trust level — not a silent merge into one boolean.
**No edit made in this lane** per the brief.

## Secondary: positive-C rank 191, and the exact classical dependence

`linear-c-transverse-rank-astra` proves `ker(V_C → k[X,W], P ↦ J(P,G)) = k·1`
and hence **full**-C rank 191 at every char-0 base point, unconditionally
(`:88–96`). For the **positive-only** rows the kernel condition weakens to
`J(P,G) = κ ∈ k`, and the report closes `κ = 0` only by assuming the base admits
an actual Keller pair `(F,G)` of degrees (99,66): it sets `Q = P − (κ/j)F`,
uses the centralizer `k[G]`, and derives `deg Q = 99 ∉ 66·Z_{>0}` (`:113–137`).
That is why the statement is currently conditional on a Keller point.

GGV22 §2 removes the Keller hypothesis from that step. Let `P ∈ V_C` be
nonconstant with `J(P,G) = κ ∈ k^×`. Then `(P,G)` is a Keller pair with
`deg P ≤ 35` (`linear-c…:54`, `factored-jacobian-gate…:71`) and `deg G = 66`, so
`max = 66 < 125` and `{deg P, 66} ≠ {72,108}`. By §2 it is not a counterexample,
hence `K[P,G] = K[x,y]` and `G` is a **coordinate**. Now the classical input,
stated exactly:

- Jung (1942) / van der Kulk (1953) alone give only `deg P | 66` or `66 | deg P`;
  with `deg P ≤ 35` this permits `deg P ∈ {1,2,3,6,11,22,33}` and **does not
  close the case**. Divisibility is insufficient and must not be cited as if it
  were.
- The operative statement is the top-form corollary: a coordinate of `K[x,y]`
  has one place at infinity, so its leading form is `c·ℓ^{deg}` for a single
  linear form `ℓ`. This is the Abhyankar–Moh embedding theorem
  (*Embeddings of the line in the plane*, Crelle 276 (1975), Moh's `[A-M.2]`,
  Moh p. 212) together with Jung–van der Kulk tameness — the same two references
  Arrow 4 of the charged full-ideal gate already carries, so no new external
  perimeter is opened.

`G_top = y^{18}(y−x)^{48}` has **two distinct** linear factors, so `G` is not a
coordinate. Contradiction; hence `κ = 0`, hence `P ∈ k·1` by the unconditional
full-C theorem. **Conclusion: positive-C rank 191 at every characteristic-zero
base point of the frozen source**, conditional on GGV22 §2 and on the two
classical results named — and on nothing else, in particular not on the existence
of a Keller point. Note the pleasant asymmetry: the hypothesis “two distinct
leading linear factors” is what does the work, and it is a property our `G` has
*by construction* at every base point, parameter-free.

Three limits, held deliberately:

- This is **not an independent proof**. It is an interface: the derivation above
  is three lines, and all of its force is borrowed from GGV22 §2, which this lane
  did not read. It inherits `OPEN[PRIMARY-TEXT-UNREAD]` verbatim.
- **No posterior global `(C,a)` injectivity claim.** The enlarged `(C,a)` block
  is not rescued: at the actual source specialization `D=0, b=0` one has `G=h²`,
  and `P=h` (`Δa=2, ΔC=0`) satisfies `J(h,h²)=0` — a nonconstant element of the
  **`κ=0`** kernel (`linear-c…:139–145`). GGV22 removes only the `κ≠0` branch and
  is silent on `κ=0`; the `h`-centralizer direction survives untouched. A uniform
  full-rank `(C,a)` claim over the whole base remains **refuted**, exactly as the
  charged report states.
- The report's separate 190-constant-positive-row-pivot lemma is untouched here,
  and no constant 191-minor is exhibited by this argument either (`:167–172`).

## FALLACY-v2

No floor is promoted to attainment: the degree facts used are exact attained
degrees from parameter-free top forms, not bounds, and where the charged gate
supplies a bound (`deg W ≤ 145`) it is not used. No `sat()`, no raw remainder,
no vanished-leader division, no pole identity. The ring, field, and coordinate
map `X=x, W=y−x` are declared and matched across three charged reports by their
recomputed top forms, not by name agreement. The absolute-degree vs
Laurent/Newton-label distinction is carried explicitly and is the substance of
the scope finding. Quantifier direction on the external theorem is stated and
checked in both readings. Where the brief asked for something I could not do —
read the primary text — I return a typed `OPEN` rather than substituting the
readable sibling paper, and I mark the enumeration question as unexamined rather
than closing it by analogy. No new exit price is asserted, so no `charge_basis=`
line applies.

<!-- BODY-END -->
