# Stable-basis hostile rereview: M2 legacy full-exit safe-floor repricing R1

You are Opus 5, acting as an independent adversarial mathematical referee.
Work in `/Users/dc/code/math/jc2` at the exact committed basis
`c3598b92598c1596e6c6331f4c877619b432a115`.

## Required output and write boundary

Write exactly one mathematical report:

`xmodel/m2-exit-safe-floor-legacy-reprice-r1-stable-hostile-rereview-opus5-20260829a.md`

Do not edit any existing file. Do not create any other file. In particular,
do not edit `APPROACHES.md`, `AUDIT.md`, `COORDINATION.md`, `PROGRESS.md`,
`notes.md`, any `ladder/` file, any `cases/` file, `FALLACY.md`, or any
`ops/` file. Read-only shell commands and small exact-rational desk checks
are allowed. Do not commit, push, use the web, use AWS, install anything, or
run heavy computation.

Never enter, enumerate, search, read, build, modify, status, or control
`jc2-lean`. Avoid repository-global commands whose scope could include it.

## Review target

Hostile-review the provisional producer report

`xmodel/m2-exit-safe-floor-legacy-reprice-r1-sol56-20260829.md`.

Its numerical claim is that the new lower floor for a FULL_ACTUAL_EXIT set
changes no td=12 U1 menu row, but raises exactly four LL-1 P0 cells

`(17,5)@2`, `(51,15)@7`, `(85,25)@12`, `(119,35)@17`

from nonzero-direction price `1` to `2`, because every one has
`delta=2/3`. Its conditional graph replay changes the frozen LL-1 alive or
fragile inventory from 13 to 7.

The decisive question is not merely arithmetic. Determine, separately for
each upgraded LL-1 cell, whether the original P0 consumer is source-licensed
as FULL_ACTUAL_EXIT. The frozen LL-1 record calls its values AF2 lower bounds
and has no machine-checked carrier tag. That absence is not by itself a
refutation: if the source definition of the geometric `lambda_F` and the P0
construction already make it the total weight of all actual cv flags first
separating at that vertex/direction, the stronger floor may follow without a
new JSON field. Conversely, a formula derived only by selecting one cv
witness per direction, or by MFE representative pricing, cannot be silently
upgraded.

## Mandatory attacks

1. Verify every hash below at the beginning and again immediately before
   writing the final verdict. If any declared source changes, write only an
   `INPUT_MUTATED / NO_PROMOTION` custody diagnostic.
2. Verify the target's full and body seals. Re-run the target checker in
   ordinary and `python3 -O` modes, compare exact stdout, and independently
   reconstruct enough arithmetic to catch shared-code errors. Check all 16
   unique LL-1 full-cell keys, the four changed cells, zero summands, graph
   pooling/deduplication, terminal budgets, and the 13-to-7 inventory claim.
3. Reconstruct the full-exit safe floor from the cited theorem and hostile
   review. Keep physical places, cover-level Puiseux series, actual cv flags,
   direction-orbits, MFE-selected witnesses, and first-separation sets
   distinct. Keep strict-below versus exact-cv-level separation explicit.
   Treat the floor as a lower bound, never attainment.
4. Audit the carrier license for every upgraded LL-1 cell. Trace the exact
   chain from the printed/source definition of `lambda_F`, through the
   Section-9 first-exit partition and P0/AF2 construction, to what the LL-1
   transition record consumes. Answer all of:
   - Is the nonzero root of multiplicity 3 an up direction in each cell?
   - Does the charged object contain every distinct actual cv flag below that
     direction, or only one representative/witness?
   - Are different nonzero directions disjoint at the charged vertex?
   - Are full exit sets charged at successive trunk vertices disjoint by a
     typed first-separation assignment, rather than by analogy?
   - Does Corollary 7.1's single global budget permit all these flags to be
     inserted simultaneously without double counting?
   - Is any zero/epsilon direction accidentally repriced?
   Do not infer FULL_ACTUAL_EXIT merely from the words `lambda`, `price`,
   `ray`, `orbit`, or from the producer's declaration that this is its
   interpretation. Find the load-bearing source statement and cite it.
5. Test both hypotheses fairly:
   - H-full: `lambda_F` is the actual total first-separation charge, and AF2
     was only a weak lower bound obtained from one witness per direction;
     then a stronger theorem about the full actual set may automatically
     improve the same lower bound.
   - H-representative: the ledger consumer itself transports only the chosen
     representatives or their formula prices; then the upgrades are UNTYPED
     until a full-set insertion/disjointness bridge is proved.
   Decide from sources, not metadata. If the sources do not settle the bridge,
   fail open as `UNTYPED / NO_PROMOTION` rather than choosing the useful side.
6. Check whether pooling transition templates by reduced `(w,M)` remains
   legitimate after repricing, including the collision at displayed
   `(20,16,5)` with distinct `(X,kbar)` data and the two paths to
   `(2/7,7,4)`.
7. State the maximum licensed disposition. Use one of:
   - `PASS` (all arithmetic and every full-exit carrier/disjointness bridge
     source-certified),
   - `PASS_WITH_REPAIR` (only non-load-bearing wording/metadata repairs),
   - `UNTYPED_NO_PROMOTION` (conditional arithmetic correct but one or more
     upgraded cells lack a proved full-exit consumer bridge),
   - `REFUTED` (load-bearing mathematics/arithmetic false),
   - `INPUT_MUTATED_NO_PROMOTION` (custody failure).
   A conditional correct calculation is not a pass if its actual LL-1
   consumer is untyped.
8. Include a compact cell-by-cell license table, exact commands/results,
   before/after hash custody table, limitations, and a sealed-body SHA-256
   convention. End the sealed body with a unique end marker, then put the
   body byte count/hash outside it.

If you affirm an exit-charge claim, include valid one-line machine-readable
`charge_basis=` declarations with exact rational deltas, permitted branch
labels, positive flag counts, and precise file/section citations. If the
claim remains untyped, say so rather than manufacturing a declaration.

## Frozen source perimeter (SHA-256)

```text
aaa7496bd6182bd124935b8534307ad3167fffe9393efad3e56cf349942ddeb7  xmodel/m2-exit-safe-floor-legacy-reprice-r1-sol56-20260829.md
6ca098b8145f091884d7f11ab1d6aac49dadaab91a6ba7ed18f7c022efce99b5  cases/m2_exit_safe_floor_legacy_reprice_r1_20260829/check.py
205e7f5825604e0e334d1a822b13a595dfe6b9ce06d0f011b199a0ddcb725a1e  cases/landing_ledger_ll1_r3_20260829/out/ll1_book.json
05f68f4b7278a8ac1216ba82b40e7081bfff66f351380ccd671d12a955784d84  xmodel/m2-arity-law-place-conservation-source-audit-sol56-20260829.md
56e95db58e53aa030ef1100cc1640d115105a77607d40e3f160e77b46174a34d  xmodel/m2-arity-law-place-conservation-source-audit-hostile-review-fable5-20260829.md
2763d9708e25ff5f6f51754e678f0b5fd7f785a236d64e89eee4aa6189459933  xmodel/sigray-section9-source-audit-sol-ultra-20260828.md
0729a5765729a9e3a6f99720a638cc94a3d3a7837e3946412e13c4233e6b5bad  xmodel/sigray-section9-source-audit-hostile-review-gpt55-20260828.md
86b491adc6ba6b21fcec5a8722126d80f3666d8e3d9f2cdcf4568d408bbc83a8  xmodel/sigray-multipole-global-first-exit-partition-sol-ultra-20260828.md
ac49c025e3e010d3ecaf3839adf51c40cb88b0088198ae1c5ab1198e07cc8004  xmodel/sigray-multipole-global-first-exit-partition-hostile-review-gpt56-20260828.md
f501bf91815aa7862fe36f665ea7ec7d379bc4c5f26502c4a0273bf97eff9aa6  xmodel/landing-ledger-ll1-r3-provenance-repair-fable5-20260829.md
8f56d1e4f2b159bbddf170010d9ac85337639e00e3b4ea537e0cc218a7b9bcf0  xmodel/landing-ledger-ll1-r2-hostile-review-grok46-20260829.md
40104334b5e21d6495f9857a6c13a2877ad0e31a67529c5f23243e7170cfaaaa  ladder/BOOK-OFFAXIS.md
6bea12ccd5c710d9ddd1c694ad7b65632ccedf75af0d93013486388fdb4f2c39  ladder/REDUCTION.md
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
```

The lane appends its own pinned compact reasoning guardrail. Treat it as
mandatory review discipline.
