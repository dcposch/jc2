# Research lane: DO1-MU2-REPLAY — audit the part-I unique-mu=2 analysis (last trust boundary)

Domrina II's soundness is now reduced (charged reports) to:
the two repaired root gaps (under review), structure packages,
and ONE unaudited inheritance: Domrina--Orevkov part I. The
campaign's Proposition 4.1 replaces part I's defective
unique-dicritical all-mu=1 inference AND NOTHING ELSE; the
"number of dicritical components greater than one" entry to
part II's Proposition 1.2 still rides part I's separate
unique-mu=2 analysis, which no lane has ever read.

Custody (hash-verify both before reading; stop on mismatch):
- AUTHORITATIVE: refs/domrina_orevkov1999_mzm_four_sheeted_I_russian.pdf
  SHA-256 6883978d6c24165de932c548acb1dfabde0492c0d8614ea4eb8734f14023bf1b
  (Mat. Zametki 64:6, Dec 1998, pp. 847-, coordinator
  first-page-verified). Russian; read it directly.
- AID ONLY: refs/domrina_orevkov1999_mzm_four_sheeted_I_orevkov_preprint.pdf
  SHA-256 6ca30d797810400ddfcddb5b92b046796b3fdda5c1fb8f0ba378511506bbfed3
  (Orevkov's English AMS-TeX preprint, 16pp; may differ from the
  published text — note any divergence you rely on).

Tasks, hostile standard, typed verdicts REPLAYED-SOUND /
REPAIRED / GAP per check:
(1) Locate the unique-dicritical mu=2 analysis in part I (the
    case: one dicritical component, generic local degree 2).
    Map its lemma structure and identify what exactly part II
    consumes (cross-check the charged replay-1 §5 binding
    ledger's DO-I-1/DO-I-2 statements).
(2) Replay it completely: every census, every determinant/root
    argument, every "it is easy to see". The known part-I defect
    (the all-mu=1 inference that campaign Prop 4.1 replaced) is
    adjacent — check whether the mu=2 track uses the defective
    step or its conclusion ANYWHERE. If it does, state whether
    Prop 4.1's slice covers that use.
(3) Also audit the part-I main-theorem assembly: does the mu=2
    track plus the (repaired) mu=1 slice plus part I's other
    cases actually exhaust part I's claimed statement (the
    one-dicritical impossibility)? Part II consumes the
    STATEMENT; an assembly hole is a hole in the inheritance.
(4) Final: the trust-boundary ledger line. Either
    DO-I-MU2 = REPLAYED-SOUND (+ any repairs), making the
    boundary a theorem modulo your named repairs, or typed
    GAP-CANDIDATE[...] with page and quote.

Report: `xmodel/do1-mu2-replay-sol56-20260901.md`.
Seal-at-completion contract; target 25-35KB; close at a clean
sub-boundary with OPEN[DO1-MU2-CONT] rather than overrun.
charged_input=xmodel/domrina-ii-replay1-sol56-20260901.md
charged_input=xmodel/domrina-gap-repair-opus5-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
b838a2860c88d64d2a2162fd1a157e345db027bf4c7e95d2abae899dba9dc5de  {{LANE_INPUTS}}/domrina-ii-replay1-sol56-20260901.md
99fc1e5870fb74d48e3d14a156115ef625fa9ecbc5843f0d8dd4a138a920e9bf  {{LANE_INPUTS}}/domrina-gap-repair-opus5-20260901.md
```
