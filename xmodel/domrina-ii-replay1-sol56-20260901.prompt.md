# Research lane: DOMRINA-II-REPLAY-1 — hostile replay of the §3 core of Domrina II

The official 33-page English Domrina II is in custody:
`refs/domrina2000_izv64_four_sheeted_general_case.pdf`, SHA-256
`0be24c5c6a9cc9423c3049c3402f2c98e44bac5f1c6018b3999989e0f32e5018`
(coordinator first-page-verified: Izv. Math. 64:1 1-33, DOI
10.1070/IM2000v064n01ABEH000273, theorem = no four-sheeted
polynomial self-maps of C^2 with nonzero constant Jacobian).
Verify the hash before reading; stop on mismatch.

The charged audit's §8 fixes the replay order for deciding
DOMRINA-II-SOUNDNESS. Your scope is the FIRST HALF:
(1) Lemma 3.12's local census: replay it completely — enumerate
    the local cases yourself from her stated hypotheses and check
    her census is exhaustive and each case's conclusion correct.
(2) Lemma 3.14's global census: same standard.
(3) Every implicit root-location branch in §§1-4: wherever the
    text asserts a root/branch location without displayed
    computation, reconstruct the computation or type it as a
    named GAP-CANDIDATE with the exact quote and page.
(4) The D--O I dependency: where Domrina II inherits from part I
    (the unique-dicritical mu=1 case), do NOT inherit the author
    inference — the audit typed the D--O I inference SOURCE-GAP;
    CAMPAIGN-REPAIRED. Bind each such use either to a repaired
    standalone argument you supply or explicitly to the
    campaign's Proposition 4.1 as stated in the charged audit
    (§3.1), and record which binding each use needs.
NOT in scope: §§5-7 (including Lemma 7.10 and the omitted §7
calculations) — a sibling lane will take those; do not spend
budget there beyond noting forward dependencies.

Standard: campaign hostile-review. Her arguments are presumed
neither sound nor gapped; the literature's acceptance
(N=4-LITERATURE=CLOSED at reception, per the audit §5) carries
zero weight here. Every check you replay gets a typed verdict:
REPLAYED-SOUND / REPAIRED (with your repair) / GAP (with the
irreducible missing step). Cite by page and displayed-formula
number in the official PDF.

Report: `xmodel/domrina-ii-replay1-sol56-20260901.md`.
Seal-at-completion contract: skeleton WITHOUT the marker, bounded
per-section writes, seal only at completion. Target 30-40KB body;
if the census replay outgrows this, close the report at a clean
sub-boundary with the remainder typed OPEN[REPLAY1-CONT] rather
than overrunning.
charged_input=xmodel/domrina-1999-audit-sol56-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
5739b317366d0a3c8905fcdc642f823c7bb71d44b79c7101b2cac256512f4d01  {{LANE_INPUTS}}/domrina-1999-audit-sol56-20260901.md
```
