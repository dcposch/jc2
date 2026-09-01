# DOMRINA-1999 urgent audit: the published (N=4) claim versus the campaign

## 0. Audit controls and executive disposition

The three frozen inputs passed the required byte gate before inspection:

| frozen input | required and observed SHA-256 |
|---|---|
| `domrina1999_mathnotes65_four_sheeted_general_case.pdf` | `fd73196e85aefd93764fb3994c78bd8d763da03820e3beff623e698e90cfd43a` |
| `block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md` | `46e08515b12d21780b727c9035872fdb3a9bfb01c4c8ebc74d0efc950b6258fc` |
| `block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md` | `763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9` |

**Disposition.** The 1999 paper unmistakably announces the unconditional
four-sheet exclusion, but its four pages are an outline, not a stand-alone
proof: Propositions 1--2 are stated, Proposition 3 is called easy, Propositions
4--5 are transferred by analogy, and the root-location and terminal
canonical-class calculations are omitted. The announcement therefore has
status `CLAIMED/FULL-THEOREM; PROOF-ON-PAGE=INCOMPLETE-OUTLINE`.

The acquisition premise changed during this audit. A sound official English
copy of the 33-page sequel became available as
`refs/domrina2000_izv64_four_sheeted_general_case.pdf`; I independently
verified 408,814 bytes, 33 pages, a clean `qpdf --check`, and SHA-256
`0be24c5c6a9cc9423c3049c3402f2c98e44bac5f1c6018b3999989e0f32e5018`.
It substantially expands every announced stage. It also expressly imports
Domrina--Orevkov I's exclusion of the one-dicritical case, so it does not repair
the campaign-audited author inference in that input. Several finite
classification/calculation passages in II remain compressed by analogy or
omission; this audit spot-checked their role but did not replay all 33 pages.
Thus `DOMRINA-II-HOSTILE-SOUNDNESS=AUDIT-OPEN`, not `GAPPED`.

The literature posture is nevertheless strong. A refereed 2008 paper by
Żołądek both treats Domrina--Orevkov as proved and gives a different proof of
the stronger topological-degree-at-most-five theorem. Sigray's 2008 thesis also
gives a different degree-at-most-five proof, and later papers use six as the
known lower bound for a counterexample. Accordingly, `N=4-LITERATURE=CLOSED`
is the correct present research posture; that sociological/provenance status is
not a substitute for a line audit of Domrina II.

The charged campaign is not yet a complete independent proof of (N=4).
It has a rigorous repair of the known μ=1 inference, a sharper independent
derivation of the two-component residual, and ROW-KILL on the explicit
EXHAUST families. The frozen all-degree integration still records a missing
campaign pin, shape tails, and six AM-numerical candidates. Its correct status
is `INDEPENDENT-PARTIAL/OPEN`, not “first rigorous full treatment.”

## 1. Bibliographic identity and claim scope

The charged item is A. V. Domrina, *On Four-Sheeted Polynomial Mappings of
\(\mathbb C^2\). The General Case*, *Mathematical Notes* **65**:3 (1999),
386--389, translated from *Matematicheskie Zametki* **65**:3, 464--467,
received 7 May 1998; DOI
[10.1007/BF02675082](https://doi.org/10.1007/BF02675082). Its theorem is exact
and unconditional:

> A polynomial map \(f:\widetilde{\mathbb C}^{,2}\to\mathbb C^2\) of
> topological degree four cannot have non-zero constant Jacobian.

Here topological degree is generic fibre cardinality, not total polynomial
degree. The introduction says Domrina--Orevkov I handled maps having one
dicritical component and that this note handles “the remaining cases.” Hence
the advertised full theorem is the union of an imported one-dicritical result
and the note's residual analysis; a defect in the imported result is a defect in
that particular proof chain even if the two-dicritical part is sound.

The full publication is A. V. Domrina, *On four-sheeted polynomial mappings of
\(\mathbb C^2\). II. The general case*, *Izvestiya: Mathematics* **64**:1
(2000), 1--33, DOI
[10.1070/IM2000v064n01ABEH000273](https://doi.org/10.1070/IM2000v064n01ABEH000273).
Its [official record](https://www.mathnet.ru/eng/im273) says explicitly that the
paper proves nonexistence of a four-sheeted constant-Jacobian map.

## 2. Complete four-page announcement outline

## 3. Step-by-step comparison with the promoted campaign machinery

## 4. Soundness requirements for the full Izvestiya II proof

## 5. Literature reception and acceptance status

## 6. Campaign impact by soundness scenario

## 7. Process reconstruction: why three sweeps missed the theorem statement

## 8. Typed conclusions and open acquisition obligations
