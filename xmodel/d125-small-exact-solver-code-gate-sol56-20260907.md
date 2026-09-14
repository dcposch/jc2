# Independent exact-Q solver instrument gate

Status: **REFUTED for promotion as the stated strict-stream instrument; mathematical certificate logic CONFIRMED; actual platform behavior and any full-source result remain GAP.** Review completed 2026-09-07 from the frozen lane snapshot only.

## Scope and disposition

All eight files in `/tmp/jc2-lane.zYWOHb/inputs` were read in full: four reports/guardrails and all 748 lines of `exact.py`, `driver.py`, `test_exact.py`, and `run_tests.py` (994 lines total). Their SHA-256 values match the charged hashes; the producer report records the separately root-verified transaction and five owned pins. I did not read live peer or AWS-control artifacts, parse or reconstruct the 803-row production source, invoke Singular/CAS/SymPy, use SSH/AWS, or alter producer code.

| gate item | decision |
|---|---|
| exact-Q arithmetic, polynomial grammar, and `dp` leading order | **CONFIRMED** |
| unit and proper-superideal mathematical criteria | **CONFIRMED** |
| result-stream parser against the claimed strict contract | **REFUTED** by F1 and F2 below |
| frozen-source parser and literal suffix replacement | **CONFIRMED** on code and tiny controls |
| caller authority/caps/command construction | **CONFIRMED statically**, conditional on root and pinned CAPRUN |
| installed-Singular/CAPRUN behavior and any 803-row solve | **GAP**, intentionally unexecuted here |

The parser defects do not create a demonstrated false unit or false properness certificate: the independently replayed algebra remains decisive. They do mean the instrument does not yet satisfy the requested fail-closed stream contract, so the preparation stays provisional and needs a narrow fix plus re-gate before promotion.

## Concrete refutations

**F1 — nonempty stderr is accepted.** `exact.py:205-207` checks `not stderr.strip()`, not byte emptiness. My actual control supplied `b" \n\t"`; `parse_result` accepted it. This contradicts the preparation's claim that stderr must be empty. Ordinary Singular diagnostic text was rejected, but an all-whitespace nonempty error stream is not fail-closed. If literal emptiness is the contract, the check must compare against empty bytes.

**F2 — `I_SIZE` is not authenticated as a count.** `exact.py:210-228` parses the value but enforces only `0 <= engine_size <= len(engine)`. A complete stream containing engine polynomials `x,1-x` with `I_SIZE 0` was accepted. Thus a downward corruption of the reported generator count survives. The independently counted `I_BEGIN` lines, exact engine-to-source mapping, and final identity still protect the mathematical verdict, but the separate `I_SIZE` field cannot be described as an exact checked count. After the installed-Singular indexing control establishes its semantics, either enforce that invariant or explicitly demote this field to unauthenticated telemetry.

## Mathematical certificate review

Sparse addition and multiplication use normalized `Fraction` coefficients and canonical sorted variable-index tuples. Independent fixtures checked cancellation, products, constant division, and the precedence distinctions `-x^2`, `(-x)^2`, and `x/-2^2`. Unknown identifiers, implicit products, nonconstant/zero denominators, chained or negative powers, exponent overflow, command-like suffixes, and trailing syntax rejected in both interpreter modes.

The leading key is total degree followed by negative exponents scanned in reverse displayed-variable order, which is global degree-reverse-lexicographic order. A three-variable degree-two ordering and the decisive `y^2 > x*z` tie were independently checked, as was reduction by a nonmonic-capable exact reducer.

`proper_certificate` removes zero basis entries, checks every unordered S-pair by exact normal form, rejects a zero normal form of 1, and reduces every original row. Buchberger's criterion therefore makes `G` a Gröbner basis; `NF_G(1) != 0` makes `(G)` proper; and all 803 source normal forms being zero proves `I subset (G)`. That one-way containment is sufficient for `I` to be proper. Reverse containment is intentionally unnecessary. The false list `(x^2,x*y-1)` was rejected by its nonzero S-remainder, while zero-ideal and strict-superideal positives passed.

For a unit, every engine polynomial must equal an original polynomial and every distinct nonzero original polynomial must occur. Engine cofactors are aggregated at the first identical original row, omitted positions are padded, and the checker expands the identity against the entire original vector. Controls with leading/interior/trailing zero rows and duplicate `x` rows produced the expected map `[0,1,0,1,4]`; a changed cofactor failed. A printed basis `[1]` without cofactors was rejected as improper, and `CHECK 1` with false cofactors was rejected. Neither marker certifies anything alone.

## Source, serialization, and caller

Production source use is bound to both hard-coded full-file hashes, exact Q/global-`dp` header, ordered 269 variable names, 803 rows, unequal/rational tags, canonical footer/prefix hash, rational coefficient halves, unique row labels, and literal polynomial equality. The `.sing` file must have the exact ring prefix and unique import-only ending. `read_source` returns the original bytes through the ideal semicolon; only that ending is replaced. Tiny coefficient, label, ring-order, unknown-variable, duplicate-JSON-key, suffix-appending, and source-pin corruptions all failed.

The caller separates `engineering_control` from `solver` authority, requires root GREEN plus exact pins/host/instance/cwd/boot/deadline, and binds decision and verification through the same authority digest. Its fixed command uses pinned CAPRUN with isolated Python child argv, 300-second decision or 120-second verification limits and remaining time inside one 450-second authority window. The decision emits one `slimgb(I)` and only then conditionally executes `lift(I,ideal(1))` in that same child/cap. Static and mocked-launch controls confirmed 16 GiB AS/sampled-RSS arguments, inherited 64 MiB `RLIMIT_FSIZE` per regular stream, core size zero, the exact leader/PGID/parent/boot custody checks, exclusive phase paths, and absence of Singular file/system/library/read/second-solver commands.

These authority and parent checks are cooperative provenance checks, not a sandbox. CAPRUN supplies no byte cap; the byte defense depends on the child's inherited `RLIMIT_FSIZE`. The verifier also relies on root honoring a failed outer launch and completing the final instance/process audit; it is not a standalone security boundary.

## Controls and remaining GAPs

The frozen runner wrote a new evidence path and passed 17 producer tests normally and under `-O` in 0.508 wall seconds (peak child RSS 29,716 KiB). My relocation-capable `gate_check.py --inputs DIR` exercised positive cases and 41 caught negative cases. Its final bounded runner completed 12 processes: normal and `-O` positives plus cofactor, Buchberger, protocol-index, source-suffix, and authority-mode corruptions in both modes. All ten corruptions exited 1 at the intended explicit check; total wall time was 1.856 seconds, child CPU 1.777 seconds, peak RSS 25,228 KiB. No enforcement depends on a language `assert`.

Evidence is confined to `box/d125-small-exact-solver-code-gate-sol56-20260907/`: `producer-tests.json` SHA `31c21b54...974c8ed`, `gate_check.py` SHA `04e1ae4a...9fa5af5`, `run_controls.py` SHA `12c1a9d1...5fa30a`, and final `own-controls-final.json` SHA `3be1f15a...20e162b`. The earlier successful development batch remains separately retained and is not the cited final run.

Still **GAP** pending separately authorized root harvest: installed Singular zero/duplicate indexing, `size/ncols/I[k]` behavior, exact print formatting, lift-row mapping, actual stdout/stderr FSIZE overflow, and descendant cleanup. Root's final process/instance/ownership checks are also outstanding. No full-source acceptance, basis, cofactor vector, or solver verdict was produced or assessed by this gate.
<!-- BODY-END -->
