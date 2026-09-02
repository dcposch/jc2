# Research lane: REDUCIBLE-BRANCH REPRICE — what do JAC-FIBRE / FRONTIER-EXACT / D1-PIN say when the asymptotic set A_F is reducible (H2 false)?

The day's exact machinery (integration #17, reviewed) was bound with
"H2 only where the campaign window [6,16] is quoted": JAC-FIBRE and
FRONTIER-EXACT hold for EVERY dominant map in Moh's monic gauge;
D1-PIN/D1-STAR use Moh Def 5.1(1), Lemma 5.2, Prop 6.1(1) (Moh's own
setting: a Keller pair with two points at infinity, degree-minimal in
his gauge), and the campaign's NU-TWO (from the subrectangular gauge /
orbit bridge, integration #14). Moh's D ≤ 100 theorem itself has no H2.
The campaign's REDUCIBLE branch (A_F reducible) has been untouched all
day: read what the record says about it (AUDIT.md, APPROACHES.md,
notes.md LIVE STATE blocks of 2026-09-01/02, integration #14 §C) —
which hypotheses of the (B2)/(B3) cell analysis, of NU-TWO, and of the
N ≥ 6 frontier actually use H2, and which are H2-free.
YOUR TASK (direct; research, not a census):
(1) SCOPE AUDIT. For each of JAC-FIBRE, FRONTIER-EXACT, DETECTOR-NULL,
    D1-PIN, D1-STAR, PIN-NOT-CEILING, the integrality filter, condition
    (15), HARMONIC-BOUND, N-CEILING: state whether it holds without H2
    (quote the hypothesis lines of the charged reports), and whether it
    holds without degree-minimality / NU-TWO (Moh's own gauge is for a
    counterexample of minimal degree in its orbit; his "two points at
    infinity" is Cor 6.1(3)). Produce a table: theorem × {Keller only,
    +degree-minimal, +NU-TWO, +H2}.
(2) THE REDUCIBLE BRANCH UNDER EXACT-N. If A_F = A₁ ∪ A₂ ∪ …, the
    non-proper places of the generic fibre of g map to the several
    components; FRONTIER-EXACT counts only proper places, so N = Σ_proper
    (1 − δ⁰)⁺ is unchanged. What DOES change: the count of non-proper
    places (PLACE-LEDGER's S·n), the minor-disc structure, and whatever
    the campaign's reducible-branch residual is stated in terms of. Say
    exactly what the reducible residual is in the record (cells? a
    single open?), and whether the pinned N = Σ_B V₂(B)q(B) + integrality
    reprices it: does any reducible-branch cell or case die, or is the
    branch untouched by design?
(3) THE N ≥ 6 FRONTIER. The N ≤ 5 closure (notes 01:10Z) — is it
    unconditional or under H2 (Domrina–Orevkov's N = 4 case assumes
    irreducible ramification curve; N = 5 by the campaign's dependency
    audit)? If the reducible branch has a different N_min, state it and
    rerun the (UNI) integrality kill counts at D ≤ 120 with that N_min
    (d1floor.py; one core, ~25 min).
(4) DIRECT VERDICT: after today, is the reducible branch (a) subsumed by
    the exact machinery (same skeleton census, same filter, no separate
    program), (b) a separate program needing its own instruments, or
    (c) partially subsumed — and name the single cheapest discriminating
    computation.
Discipline: PROVED-HERE/UNREVIEWED typing; quote hypotheses verbatim
with file:line; state the bounded quantity of any OPEN you raise;
desk-scale; do not edit canonical ledgers; do not inspect jc2-lean.
Report: xmodel/reducible-branch-reprice-opus5-20260902.md
Seal-at-completion (standard <!-- BODY-END --> marker); bounded writes;
target 20-30KB; 75 minutes.
charged_input=xmodel/integration17-coordinator-fable51-20260902.md
charged_input=xmodel/d1-subtree-opus5-20260902.md
charged_input=xmodel/d1-subtree-review-grok46-20260902.md
charged_input=xmodel/integration14-coordinator-fable51-20260902.md
charged_input=xmodel/integration16-coordinator-fable51-20260902.md
charged_input=box/moh_skeleton_N.py
charged_input=box/d1sub-drivers-20260902/d1floor.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  {{LANE_INPUTS}}/integration17-coordinator-fable51-20260902.md
26479b06b0f1ef526fe37bd34bccb61f50f207a509fcb0b0c1ae6fc5751858c0  {{LANE_INPUTS}}/d1-subtree-opus5-20260902.md
66c3e82ff6fb9a0e0ad339d3cd22a2b5236129b0b731f5cd68ff048df15c735c  {{LANE_INPUTS}}/d1-subtree-review-grok46-20260902.md
bf1d428c7ddc03ab002410174b995cdd01e8a3c76c52475b03faf959b33da2ca  {{LANE_INPUTS}}/integration14-coordinator-fable51-20260902.md
6b8a712344397e1248e4efe230f5fcbeb41ae8b64423de272a77e98ae6b1a241  {{LANE_INPUTS}}/integration16-coordinator-fable51-20260902.md
3022020435c86b62ecd28df8d28d1bdf9ab4e361828c028b913ba8aae3f11a39  {{LANE_INPUTS}}/moh_skeleton_N.py
cf0780cc0b3ef0f2de630e6901f836596c1dd58e3ff1dc0917e9c8d363baebe6  {{LANE_INPUTS}}/d1floor.py
```
