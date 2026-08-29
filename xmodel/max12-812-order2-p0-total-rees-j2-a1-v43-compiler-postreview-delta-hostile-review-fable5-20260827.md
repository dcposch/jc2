# Hostile review (Fable 5): V43 compiler post-review delta c7ed7309 -> 0de6a2b2

Date: 2026-08-27  
Reviewer: Claude Fable 5 (hostile), local desk session with shell.  
Reviewed artifacts:

- `xmodel/max12-812-order2-p0-total-rees-j2-a1-v43-compiler-postreview-delta-sol-20260827.md`
  (the additive custody addendum);
- `cases/max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_20260827/compile_total_dvr_w30_v43.py`
  (current bytes).

Mandate: five checks, each returned `CONFIRMED`, `REFUTED`, or `GAP`.
Desk-scale only: no AWS launch, no web sweep, no canonical-ledger edit,
`jc2-lean` untouched.  This report reviews custody and code semantics only;
it does not review or endorse any AWS outcome that is not yet frozen.

## Verdicts

| # | Check | Verdict |
|---|-------|---------|
| 1 | Displayed diff is the complete byte delta c7ed7309 -> 0de6a2b2 | **CONFIRMED** |
| 2 | Zero assignment soundly solves a cyclic core with identically zero RHS before reverse leaf substitution | **CONFIRMED** |
| 3 | Mandatory full-product exact replay prevents a false dual certificate | **CONFIRMED** |
| 4 | On the reported census `forced_core_equations=1`, both versions fail closed; delta cannot change the weight-30 verdict | **CONFIRMED** (conditional as posed; provenance caveat below) |
| 5 | Consumers used by the launched total-dehom and LinBox lanes do not call `leaf_peel_dual` | **CONFIRMED** |

## Execution disclosure

This session had a working local shell.  All hashes below were computed
live (`shasum -a 256` / Python `hashlib`); the byte-level reversal was
executed, not hand-simulated.  The reconstruction was staged at
`/tmp/v43_reviewed_reconstruction.py` (not a campaign artifact).  The only
repository file written by this review is this report.

## Item 1 — diff completeness: CONFIRMED

- The on-disk compiler hashes to
  `0de6a2b279aeeab8c5a635c1d7658958f3f49f0f94f8473355d281cae9438b00`,
  matching the launched pin named by the addendum and by all five
  consumers.
- The displayed unified diff comprises exactly six line-level edits in the
  current file: inserted lines 266–267 (the `forced_core_equations`
  comprehension), inserted line 278 (the census key), line 280 replaced
  (`if core_equations:` -> `if forced_core_equations:`), inserted lines
  285–286 (the two comment lines).  Every context line in the diff
  byte-matches the current file, and the touched identifiers occur nowhere
  else (`forced_core_equations` appears only at lines 266/278/280), so hunk
  placement is unambiguous despite the bare `@@` markers.
- Reverse application was performed byte-exactly: each of the six touched
  lines was assert-checked for byte equality against the diff before
  removal/replacement; the file contains no CR bytes and splits cleanly on
  `\n`.  The reconstructed byte stream hashes to
  `c7ed730905592b571ef6746ad369297916810c671e4c6f2e6f1af0995caeade0` —
  the reviewed SHA, exactly.  By SHA-256 second-preimage resistance the
  reconstruction *is* the reviewed file; any byte difference not shown in
  the diff would have changed this hash.  The diff is therefore complete
  and exact, and the addendum's in-memory reversal claim is independently
  reproduced.

## Item 2 — homogeneous cyclic core solved by zero: CONFIRMED

Code facts (current bytes): equations exclude the target column
(line 240); `right_hand_sides[e] = -coeff_e(target)` (line 242); the peel
removes equations whose pivot variable has active incidence exactly 1;
`core` = equations still active afterwards; `forced` = core equations with
nonzero RHS (lines 266–267).  When `forced` is empty the launched code
back-substitutes with core variables left out of `values` (lines 287–295),
which reads them as `Fraction(0)`.

Soundness, verified against the code rather than taken from the addendum:

1. **The core is closed.**  A peeled pivot `v` cannot occur in any core
   equation: at `v`'s peel time its unique active incident equation was the
   one being peeled, and core equations are active at all times (activity
   only decreases).  So the core system involves only never-peeled
   variables, and assigning those zero touches no peeled pivot.
2. **Zero solves the core.**  With `forced` empty every core equation reads
   `sum c_i x_i = 0`; the all-zero assignment satisfies each identically.
   (Zero is a solution of any homogeneous linear system; a nonmembership
   witness needs only *some* exact solution, not a canonical one.)
3. **Reverse substitution is consistent.**  Processing peeled equations in
   reverse peel order, when equation `e` with pivot `v` is solved, every
   other variable `u` of `e` is either (a) the pivot of a *later*-peeled
   equation — already assigned in reverse processing, and never mutated,
   since a variable pivots at most once (its incidence set empties when its
   equation peels); (b) never a pivot — final value 0, exactly what
   `values.get(u, Fraction(0))` returns; or (c) the target, pinned to 1 and
   never a pivot (it occurs in no equation).  A variable peeled *earlier*
   than `e` cannot occur in `e` by the argument of point 1 with `e` still
   active.  Hence the final assignment satisfies every peeled equation
   exactly; pivot coefficients are stored only when nonzero (line 240), so
   the division is well defined in exact `Fraction` arithmetic.
4. **Independent in-function guard, present in both versions** (lines
   297–302, outside the diff): the assembled functional is replayed in
   exact rationals against *every* input polynomial, target column
   included; any nonzero sum raises `fail("leaf dual replay")`.  Even a gap
   in points 1–3 could not yield an unsound `nonmember` return.

The addendum's phrase "setting its variables to zero" is implemented
implicitly (core variables never enter `values` and are omitted from the
functional); this is mathematically identical to an explicit zero
assignment.

## Item 3 — full-product replay bars false dual certificates: CONFIRMED

The only path that emits a dual certificate is exact mode: the peel outcome
must be `nonmember` (lines 561–562, else `fail(...)` raises RuntimeError),
and then line 574 unconditionally runs
`v37.replay_certificate(certificate, special_products, special_indices, target)`
**before** any `result.json` or `PASS` banner is produced.  The v37 module
is import-gated on its pinned hash and its on-disk bytes hash to that pin
(`ba034c8cebaa27c5630872b9cf06d152e4577170486ac34ad7f695ead871845b`).  Its
nonmember branch (`solve_graded_ladder_v37.py` lines 323–329) decodes the
functional from the *serialized* certificate record (so the replay covers
the encode/decode round trip of exactly what would be frozen), requires
`lambda(target) == 1` exactly, and then evaluates the functional against
**every** product in the passed list — `for product in products`, exact
`Fraction` arithmetic — raising `fail("dual full-product replay")` on any
nonzero.  The passed list is `special_products`, the full rho-zero product
set built at lines 488–493, not merely the target component, so even a
defect in the component computation could not smuggle a functional past a
non-component product.

Both this replay and the in-function replay of Item 2 lie entirely outside
the diff and are byte-identical in the reviewed and launched versions.  The
delta enlarges the set of instances the leaf solver may *attempt*; it
cannot weaken the gate.  A functional that passes both checks is, by
definition, an exact separating functional for the constructed product
system, so a false dual certificate cannot be emitted.  Scope note: the
replay guards soundness *relative to the constructed products*; the
completeness of `reconstruct_rows`/`build_products` is unchanged bytes,
covered by the earlier design/erratum/correction reviews of the
`c7ed7309...` era, and is not re-adjudicated here.

## Item 4 — both versions fail closed on `forced_core_equations=1`: CONFIRMED (conditional as posed)

The implication is unconditional in the code.  By construction
`forced_core_equations` is a sublist of `core_equations` (lines 266–267),
so `forced = 1` forces `core_equations` nonempty.  Then:

- launched gate `if forced_core_equations:` (line 280) returns outcome
  `core`;
- reviewed gate `if core_equations:` returns outcome `core` on the same
  input — deterministically the *same* input, because every byte upstream
  of the gate (row reconstruction, product build, t=0 specialization,
  equation/RHS assembly, the peel itself) is identical between the two
  versions;
- exact solve mode then fails at lines 561–562
  (`"rho0 dual cyclic core requires sparse exact solver"`) before any
  certificate or verdict is written;
- the modp screen verdict (lines 576–581) is produced by
  `modular_membership` and never consults the peel outcome;
- preflight phase (lines 553–558) records census telemetry and emits no
  verdict.

The only behavioral differences on this input are the extra census key
`forced_core_equations` (which perturbs preflight/compile `result.json`
bytes — telemetry, not verdict) and nothing else.  Hence the delta cannot
change the current weight-30 verdict.  The addendum's statement that "the
post-review semantic branch is not exercised" on this instance is correct.

**Provenance caveat (mandated firewall):** the census values
`core_equations=23477`, `core_variables=47089`, `forced_core_equations=1`
appear in no locally frozen artifact — there is no `V43_PREFLIGHT` line, no
`rho0_dual_leaf_peel` key, and no `aws_*` results directory under the case;
the numbers exist only in the addendum and its review prompt, sourced from
an unfrozen AWS run.  They are dimensionally consistent with the earlier
desk-verified preflight dims (26200 rho0-component products and 66076
component monomials would give 2723 peeled equations), which is
corroboration, not verification.  This review verifies the *implication*
on the reported census, exactly as the check is posed, and endorses no
unfrozen AWS outcome.

## Item 5 — launched-lane consumers never call `leaf_peel_dual`: CONFIRMED

Launched lane wiring (from the case's run scripts):

- total-dehom lane: `run_total_dehom_aws.sh:43` invokes
  `compile_total_dehom_eliminant_v43.py`;
- LinBox lane: `run_rho0_dual_linbox_aws.sh:45,69` and
  `resume_rho0_dual_linbox_aws.sh:73` invoke
  `compile_rho0_dual_linbox_v43.py` and `validate_rho0_dual_linbox_v43.py`.

Verified for each of these consumers (and additionally for the pinned but
not-lane-wired `homogenize_total_dehom_lift_v43.py` and
`validate_rho0_dual_linbox_modp_v43.py`):

- each pins `TOTAL_COMPILER_SHA256 = 0de6a2b2...` and hard-fails on a
  digest mismatch *before* importing the compiler, so any successful
  consumer run anywhere must have imported exactly the launched bytes;
- the compiler is imported via `importlib` under a non-main module name,
  and `main()` (the only caller of `leaf_peel_dual`, line 497) sits behind
  `if __name__ == "__main__":` (lines 608–609), so import cannot invoke it;
- attribute census over each consumer's source: the total-dehom producers
  use only `source.reconstruct_rows`; the LinBox files use
  `source.reconstruct_rows`, `source.build_products`,
  `source.specialize_t0`.  No consumer references `source.main`, uses
  `subprocess`, or executes the compiler as a script;
- repo-wide search: the identifier `leaf_peel_dual` occurs only in the
  compiler itself (definition line 230, call line 497) and in two xmodel
  prose files;
- the imported helpers themselves (`reconstruct_rows` lines 395–441,
  `build_products` lines 130–147, `specialize_t0` lines 171–173) do not
  call `leaf_peel_dual`.

This matches the addendum's collective description of the imports.  The
addendum's further claim that the *remote* source trees carry immutable
`0de6a2b2...` bytes is not desk-verifiable; it is, however, enforced rather
than assumed, via the in-consumer digest gate above.

## Preservation and firewall

- Only `c7ed730905592b571ef6746ad369297916810c671e4c6f2e6f1af0995caeade0`
  was covered by the earlier Fable correction review.
  `0de6a2b279aeeab8c5a635c1d7658958f3f49f0f94f8473355d281cae9438b00` was
  **not** covered by that review; its review coverage is exactly the
  custody addendum plus this delta report layered on the `c7ed7309...`
  review, nothing more.  The addendum states this correctly and the
  statement is preserved here.
- No AWS outcome not yet frozen is reviewed or endorsed by this report.
- This report asserts nothing about `a1^6` membership or nonmembership, a
  total-rho certificate, chart closure, Gate T, or JC2.

## Addendum accuracy summary

Every desk-checkable factual claim in the custody addendum verified: the
diff is byte-complete and exact; the zero-core semantics are sound and
doubly replay-guarded; the replay gates are untouched by the delta; the
both-versions-fail-closed implication holds on the reported census; the
consumer import surface and pins are as described.  The only claims outside
desk reach are the AWS-side census values and remote-tree immutability,
both flagged above.
