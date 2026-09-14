# D125 same-source weighted exact certificate code gate

Status: **CONFIRMED for the exact frozen instrument delta.** Actual-engine behavior, the mathematical justification for selecting this order, and any production-source conclusion remain separate **GAPs**. Completed 2026-09-07 from the frozen lane only.

## Scope and custody

I read all nine files in `/tmp/jc2-lane.KBjyuG/inputs` in full (1,227 lines, 75,007 bytes): the producer report, both accepted predecessor gates, `FALLACY-v2.md`, complete changed `exact.py`, `driver.py`, `defect_order.py`, `test_order.py`, and the complete versioned patch. The charged producer report has the stated SHA-256 `bd664c9d6667cf22cd2963486265491d6eb322f40244a2eebfa68f020da6d789`; each of the five charged code/delta files is byte-identical to its frozen copy and has the reported pin.

The root-stated transaction verification, eight-pin check, and 28-method normal/`-O` replay are custody inputs, not results I relabel as mine. I used the accepted predecessor scope and reviewed only this delta. I did not re-review the unchanged full encoding, arithmetic/parser implementation, CAPRUN, limits, or cleanup machinery. I read no 269-variable stream and expanded no production ideal or lift row. No CAS, AWS, SSH, or live-peer access occurred, and no adapter, ledger, guardrail, or protected-project file was edited.

## Exact delta decisions

| delta claim | decision | basis |
|---|---|---|
| W1/W2/W3 then `dp` comparator | **CONFIRMED** | exact key and five independent tie-level controls |
| propagation through every leading-term, NF, and Buchberger use | **CONFIRMED** | static call-site audit plus live wrapped-call trace |
| production descriptor and tiny-fixture separation | **CONFIRMED** | fixed hashes and positive/negative descriptor controls |
| dp-source preservation, first-line-only adaptation, result-order binding | **CONFIRMED** | byte comparisons and changed prefix/header controls |
| full-original-row unit/proper criteria and strict stream invariants | **CONFIRMED** under the accepted predecessor scope | zero/duplicate, omission, cofactor, and false-proper controls |
| new caller job/cwd/authority separation | **CONFIRMED statically** as coordinator trust inputs | old schema/cwd/registration pins, wrong mode/order, and missing gates reject |

### Comparator and certificate call paths

For monomial exponent vector `alpha`, `exact.key` compares
`(W1.alpha,W2.alpha,W3.alpha,|alpha|,-alpha_last,...,-alpha_first)` lexicographically. Its nested final tuple is comparison-equivalent to that displayed flat key. The helper requires exactly three full integer rows and a strictly positive W1; no W4/W5 or implicit production fallback exists.

All four leading-key call sites pass `weights`: divisor leaders and the changing dividend leader in `normal_form`, and both S-pair leaders in `proper_certificate`. All three certificate NF sites pass the same value: each S-polynomial, `1`, and every original row. The production driver supplies `order['weight_rows']` explicitly. A live wrapper observed only the supplied descriptor weights over the graph certificate's four NF calls and all underlying key calls.

For `x-y^2,z-y^3` with variables `x,y,z` and W1 `(3,1,4)`, the leaders were `x,z` and the basis passed the weighted exact Buchberger/proper check. The identical basis failed with `dp` and with changed rows `((1,1,1),(0,0,0),(0,0,0))`. Separate pairs selected W1 (`x>y`), W2 (`x>z`), W3 (`x>t`), ordinary degree (`y^2>z`), and the final `dp` reverse-lex tie (`z>u`). This checks implementation of the declared order only; it supplies no theorem for choosing it.

### Descriptor, source, and protocol binding

The production path first requires the pinned 269-name dp identity, derives the three rows, then requires both descriptor SHA `64c212c...db66` and serialized ring-line SHA `d894d642...19bca`. Arbitrary descriptors are admitted only through the explicit ceiling of eight variables; synthetic 9- and 269-variable impostors and fake input to `fixed()` failed. There is no production order option in the CLI.

The patch does not alter `read_source`. A five-row frozen tiny source showed that it returns the original dp bytes through the ideal semicolon. `adapt_prefix` changed exactly the first ring line; the complete label/zero/coefficient suffix stayed byte-identical. A changed weight vector, changed polynomial, omitted zero row, altered ideal name, non-dp original, and appended text all failed the appropriate exact check.

The footer delta is its order digest only. Weighted output parsed only with the identical descriptor: dp, changed-vector, and changed-source headers failed. The verification path constructs the fixed order before parsing and emits separate original-source-ring and execution-order digests.

### Full-row and authority controls

The six-column unit fixture `0,x,0,x,1-x,0` retained all six cofactor positions and mapped engine columns to source positions `[0,1,0,1,4,0]`; a changed cofactor failed the expanded identity. Missing and changed nonzero engine rows failed. Properness rejected an omitted original `y`, and `(x*y-1,x^2)` failed Buchberger despite nonzero `NF(1)` and zero reductions of its listed rows. Literal whitespace stderr and a false `I_SIZE 0` both failed.

The new schema, cwd, plan/helper/order pins, nonblank job registration, and solver-only order gate/control fields are checked before launch. Tiny controls rejected the prior schema and cwd, old registration pins, control/solver mode crossover, wrong order, blank job, and missing order acceptance/control. These hash fields are cooperative coordinator trust inputs; this is not authentication against a hostile same-UID process.

## Independent replay and limits

Own evidence is confined to `box/d125-defect-order-code-gate-sol56-20260907/`. `gate_check.py` SHA `e7215b18...f228` ran 39 checks using the explicit relocated frozen-input path. Normal and `-O` records have SHA `ebe3d50e...f230` and `b6ae3451...94d1`; both passed, including live exception checks. They used 0.088/0.235 seconds wall, 0.087/0.235 seconds child CPU, and at most 22,380/24,836 KiB RSS. Each child was capped at 30 wall seconds, 25 CPU seconds, and 512 MiB address space. `run.json` SHA is `39c8ddd7...5a91`. AST scans found no Python `Assert` statement in the changed gating code or my replay code.

No installed-engine success, actual-engine ordering/index semantics, source-ideal properness, speedup, or JC2 result is claimed. The separately pending actual-engine controls and the unchanged runner controls remain outside this gate.
<!-- BODY-END -->
