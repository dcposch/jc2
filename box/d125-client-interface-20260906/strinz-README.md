# Carrier degeneration at the degree-(75,125) frontier of the plane Jacobian problem

Exact root-jet obstructions, an uncomposed reduction lemma, and reproducible
finite-algebra data.

> **Status — open problem.** No degree-`(75,125)` exclusion or counterexample
> is claimed. The genuinely new mathematical center is conditional on an
> unproved attachment of an actual standardized pair to the normalized carrier
> model; the unconditional fixed-degree reduction is chiefly a careful
> specialization and proof extraction from published machinery. The two
> results are deliberately **not composed**. An independent Gate-B dataset
> closes exactly `26/32` support cells, but the six open cells are the largest
> ones and the count is not presented as “81% of a proof.”

## Three ways to read this repository

- **For the mathematical narrative:** start with the
  [technical manuscript](paper/MANUSCRIPT.md), then consult
  [THEOREMS.md](THEOREMS.md) for the exact trust boundaries and the theorem
  directories under [`proofs/`](proofs/).
- **For verification:** read [REPRODUCE.md](REPRODUCE.md), then run
  `python scripts/verify_quick.py`. Repeated theorem-local dependency snapshots
  are explained and hash-checked in
  [`proofs/VENDORED_DEPENDENCIES.md`](proofs/VENDORED_DEPENDENCIES.md).
- **To continue the research:** start with
  [OPEN_FRONTIER.md](OPEN_FRONTIER.md), the draft
  [novelty matrix](literature/NOVELTY_MATRIX.md), and the
  [Gate-B custody matrix](gate_b/CUSTODY_MATRIX.md). A separately scoped
  [30 August post-freeze research note](POST_FREEZE_FRONTIER_2026_08_30.md)
  exposes the newer literal source-band/K7 frontier and possible interfaces to
  other active projects without changing the preview's claims. The earlier
  [25 August note](POST_FREEZE_FRONTIER_2026_08_25.md) remains as a dated
  historical checkpoint.
- **To audit the trust boundaries:** use the compact
  [trust map](TRUST_MAP.md) and the derived-only
  [Grand Portage receipt](artifacts/GRAND_PORTAGE_AUDIT.md).

## Mathematical center

1. **Carrier root jets.** In the normalized F2 carrier model, the K3/K4
   equations have an exact necessary-and-sufficient root-jet classification.
2. **First post-root-jet obstruction.** K5 eliminates every generic K4 root
   and leaves an explicit positive-dimensional deeper-contact survivor locus.
3. **Limit of the mechanism.** Corrected K6/K7 add partial conditions, while
   the honest K8 top row makes the proposed Chang–Wang selector cancel:
   `f_-115 = 0` under its stated pins.
4. **Front-end reduction lemma.** Over every characteristic-zero field `K`, a
   hypothetical Keller pair of degrees `(75,125)` becomes, after an
   automorphism over `Kbar`, a standard `(3,5)` pair in GGV Family `F2`,
   `j=1`, with initial corner `A0=(5,20)` and transformed gcd `25`.
5. **Reproducible data appendix.** Exact characteristic-zero certificates
   close 26 of the 32 Gate-B support cells. The five size-four cells and the
   size-five cell remain open.

The most important unresolved comparison is with Roy van Rijn's independent
F2 programme: both calculations produce `27T^2-9T+1`, but his tested return
packet retains both roots while this carrier model kills its generic roots at
K5. No variable or filtration crosswalk is known, so this is a research
question—not a contradiction or an identity of theorems.

The exact hypotheses and non-claims are in [THEOREMS.md](THEOREMS.md).

## Evidence levels

This repository distinguishes:

- **written proof:** a mathematical argument with cited published inputs;
- **exact checked:** exact arithmetic replay with retained receipts and hostile
  controls;
- **kernel checked:** Lean compilation of a theorem or consumer;
- **modular reconnaissance:** finite-field evidence that is never promoted to
  a characteristic-zero theorem.

The reduction lemma is a written proof extraction plus an exact custody
checker; it is not a proof-kernel formalization of the Newton-polygon or weak
Nullstellensatz inputs. The carrier calculations are exact symbolic
classifications within their stated model. Gate-B custody is intentionally
reported cell by cell rather than flattened into one evidence grade.

## Repository state

This is a curated outward-facing export from the research/provenance repository
`wstrinz/math-stuff`, source commit `96da278f`. Campaign chronology, agent
coordination, failed solver logs, and unrelated experiments are deliberately
excluded.

The preview release is complete enough for public inspection. Its remaining
publication gates are deliberately external or archival:

1. ~~completing the 32-row Gate-B custody audit~~ — complete in this tree;
2. ~~completing the bounded claim-by-claim novelty comparison~~ — complete in
   this tree, with conservative classifications;
3. one final clean-clone Linux reproduction of the pinned release commit;
4. external review of the finite-witness transfer and carrier hypotheses.

See [OPEN_FRONTIER.md](OPEN_FRONTIER.md) for the mathematical frontier and
[REPRODUCE.md](REPRODUCE.md) for the verification tiers.
The exact preview contents and limitations are summarized in
[RELEASE_NOTES.md](RELEASE_NOTES.md).

Post-freeze developments are intentionally not folded into those release
claims. Researchers interested in the live interfaces can read
[POST_FREEZE_FRONTIER_2026_08_30.md](POST_FREEZE_FRONTIER_2026_08_30.md).

## Formal registry and archival plans

The repository is being prepared for a versioned Zenodo archive.  It now also
contains a registry-ready [Palomar formalization](formalization/README.md) of
one short local K5 divisibility lemma. Comparator confirms that `Solution.lean` proves
the declarations exposed by `Challenge.lean`; both NanoDa and Lean's default
kernel accept the exported proof. Its registry value is exact statement/proof
alignment and independent replay, not depth or coverage of the campaign. It
verifies only that displayed local polynomial criterion, not the carrier
derivation, the complete informal argument, or a `(75,125)` exclusion. See the
[Palomar submission plan](literature/PALOMAR_SUBMISSION.md)
and [statement alignment](formalization/STATEMENT_ALIGNMENT.md) for the exact
scope and nonclaims.

## Authorship and provenance

Research and compilation: Will Strinz, with extensive AI-assisted symbolic,
formal, and software work. Published mathematical inputs are credited in
[literature/REFERENCES.md](literature/REFERENCES.md). No priority claim is made
for a statement until the bounded novelty audit classifies it.
