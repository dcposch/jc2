# Artifact for: A Vertex-Gap Obstruction for Low-Degree Strip Pairs in the Plane Jacobian Conjecture

Dan Clemens; Fable (AI system, Anthropic). August 2026.

> Note: some documents in `docs/` reference companion campaign files
> (AUDIT.md, notes.md, `systems/`, run logs, etc.) that are not included in
> this artifact; all paper-relevant content is self-contained here.

This bundle contains exactly the computational evidence the paper
(`paper/main.tex`, Section "Computational verification") rests on: four
exact-rational-arithmetic certificate scripts with executable assertions, the
Lean 4 development for the two central identities of the worked example, the
supporting library, unit/parity tests, and the derivation and adversarial
review documents. Nothing here depends on files outside this directory.

## Requirements

- Python >= 3.10 (developed and tested on 3.14). Standard library only —
  all certificate arithmetic is `fractions.Fraction`.
- Optional: `python-flint` (any recent version; tested with 0.9.0). Used
  only by `tests/test_parity.py` to cross-check the fast coefficient
  backend; without it that test still passes using the pure-Python backend.
- Optional (Lean check only): Lean 4 toolchain `leanprover/lean4:v4.32.2`
  via `elan`; `lake build` downloads mathlib (pinned `v4.32.2` in
  `lean/lakefile.toml` / `lean/lake-manifest.json`), roughly 10 minutes on
  first build. Not required for any Python certificate.

All commands below are run from the root of this artifact directory. Every
script locates its own imports relative to its file path; no PYTHONPATH or
installation is needed. Runtimes are for a 2023-class laptop core.

## Certificates: paper section -> command -> expected output

### 1. Section 4 (vertex-gap theorem at (2,2), Props A/B) and Section 5 counting

Block-local surplus engine; re-derives the counting propositions and the
reduction tables from corner data alone, classifies the leftover key
(PINS / TRIVIAL / OTHER), and runs an exact torus probe.
Companion derivation: `docs/SURPLUS.md`; adversarial review:
`docs/SURPLUS-REVIEW.md`.

    python3 cases/surplus_count.py          # ~40 s

Expected: for the paper's case the leftover is the pinning monomial of
Theorem 4 (artifact naming: `a(1,1)` = a2, `a(2,4)` = a6):

    == open_8_28_c2: d=(1, 2) k=2 wP=2 wQ=3 swapped=False (i) OK det=1
       n_keys=9 (cols {3: 4, 4: 5})  closed-form 2(wP+wQ)-1=9 MATCH
       n_unknowns=8 (Q-elim 7, P-zeroed 1: ['a(1, 2)'])
       surplus=1  leftovers: (4, 7):PINS -1/5*unit*a(1, 1)^2*a(2, 4)

and the closing summary table row:

    open_8_28_c2    2  (1, 2) 2  3  yes      9     8     1    1  1  2

Exit status 0.

### 2. Section 5 (Theorems 6-9: types (2,3), (2,4), certificates at (3,3),(4,3),(5,3), and k>=3 at d2=2)

Column-ODE layer: solves the block column relations exactly, cross-checks
against the lattice-determinant key enumeration (V1/W1), and carries the
Sylvester resultant certificates. Companion derivation:
`docs/SURPLUS-EXT.md`.

    python3 cases/surplus_ext.py            # ~3 s

Expected lines (among others; exit status 0 asserts all):

    V2 (inner extra = -a3^k c1 a1^{1-k}, k<=10): OK
    V3 (a3=0 => outer extra: 0 for k>=3; -(1/5)a2^2a6 at k=2): OK
    V4 (a3=0 => deg_y E <= k+3): OK
    W2 Res_a4(10L1,10L2) = -3200*a3^7: OK
    W4 (2,3) outer|a3=a4=0: L3 = (a2^3/21)(a2^2 b4 - 5 a2 b5 + 15 b6): OK | L4 == 0 identically: OK
    W6 (2,4) outer|binom vs R4 = a2^4b4-5a2^3b5+15a2^2b6-35a2b7+70b8: OK | O1=(-1/55*a2^4)*R4; O2=0; O3=0
    C3b d2=3 k=3: Res_a4=c*a3^15 (lead const True); slice Res_a2=c*a4^12 => rigidity OK
    C3b d2=3 k=4: Res_a4=c*a3^26 (lead const True); slice Res_a2=c*a4^34 => rigidity OK
    C3b d2=3 k=5: Res_a4=c*a3^40 (lead const True); slice Res_a2=c*a4^44 => rigidity OK

The resultant exponents (15,12), (26,34), (40,44) are the ones quoted in
Theorem 8 of the paper.

### 3. Section 6 (the (8,28) worked example: ten-event chain, census, -1 collapse)

Full-pipeline replay with per-equation provenance; derivation and review:
`docs/LEMMA.md`, `docs/LEMMA-REVIEW.md`.

    python3 cases/eq3_chain.py              # ~5 s (default case open_8_28_c2)

Expected lines:

    [open_8_28_c2] cascade: reduced (2s); zeroed 3, elim 41, eqs left 50
        coeff = (-1/5)*a2^2*a6*ia1^2
        cascade events touching src (10): ['zero:b1(1, 1)', 'zero:b2(1, 2)', 'elim:b10(3, 6)', 'elim:b9(3, 5)', 'elim:b8(3, 4)', 'elim:b7(3, 3)', 'elim:b6(2, 4)', 'elim:b5(2, 3)', 'elim:b4(2, 2)', 'zero:a3(1, 2)']
    census after chart (0s): 51 identically zero, 40 polynomial, constants: [(3, (2, 0), Fraction(-1, 1))]
    final rhs-key eq: (-1)*1

i.e. 92 keys, ten events reduce the key-(3,6) coefficient to
(-1/5) a2^2 a6 ia1^2, the census is 51 zero / 40 polynomial / one constant
(equation #3 = -1), matching the paper's Section 6 exactly. A no-collapse
control: `python3 cases/eq3_chain.py reg_9_24_c3` (census has no constant).

### 4. Section 7 (log-residue functional: unit factors, all computed cells)

Residue-functional checks over the 11-cell grid, including the verified
unit factors a2^3/21, -a2^6/99, 2a2^9/1001, -a2^4/55, -a2^8/364 and the
empty sum at (5,3) quoted in Section 7. Companion: `docs/RESIDUE.md`.

    python3 cases/residue_check.py          # <1 s

Expected final line: `ALL OK` (48 checks; exit status 0).

### 5. Section 6 (Lean 4 machine check of the two central identities)

`lean/Jc/Culprit.lean` proves (A) `eq3_at_b3_zero` (equation #3 evaluates to
-1 at b3 = 0) and (B) `culprit_key36_reduction` (the ten-event reduction of
the key-(3,6) coefficient to (-1/5) a2^2 a6 ia1^2 b3). See `lean/README.md`.
The file is generated from the recorded cascade event log by:

    python3 cases/export_lean.py            # ~5 s

Expected: `wrote .../lean/Jc/Culprit.lean (51 lines)`, and the regenerated
file is byte-identical to the shipped one (check with `diff` against a
pristine copy). To machine-check the proofs:

    cd lean && lake build                   # first run downloads mathlib (~10 min)

Not run as part of the Python self-test; the shipped `Culprit.lean` was
verified with `#print axioms`: (A) uses `propext` only, (B) `propext`,
`Classical.choice`, `Quot.sound` — no `sorry`.

## Tests

    python3 tests/test_jc.py                # <1 s, expect: ALL TESTS PASS
    python3 tests/test_parity.py            # ~4-25 s, expect: ALL PARITY TESTS PASS

`test_jc.py` exercises the bracket/lattice core (`lib/jc.py`);
`test_parity.py` replays the full pipeline for `reg_9_24_c3` and
`open_8_28_c2` and checks the emitted systems are byte-identical between
the pure-Python and (if installed) python-flint backends.

## Contents

    paper/      main.tex, main.pdf — the paper
    cases/      certificate scripts (emit.py holds the case corner data)
    lib/        exact-arithmetic pipeline: jc.py (bracket systems),
                reduce.py/reduce2.py/reduce3.py (unit-pivot cascades),
                chartelim.py (generic-chart decomposition),
                fastcoef.py (optional flint-backed coefficient backend)
    tests/      unit and backend-parity tests
    lean/       Lean 4 project (mathlib pinned); source only, no build cache
    docs/       LEMMA.md, SURPLUS.md, SURPLUS-EXT.md, RESIDUE.md —
                derivations; LEMMA-REVIEW.md, SURPLUS-REVIEW.md —
                adversarial review documents cited in the paper

## Scope

This artifact covers the unconditional theorems of the paper (Sections 4-7)
and the worked example (Section 6). The msolve Groebner-basis discard of the
remaining strata of the (72,108) campaign (the "companion claim" of the
paper's Section 8) is a separate computation and is not part of this bundle.
