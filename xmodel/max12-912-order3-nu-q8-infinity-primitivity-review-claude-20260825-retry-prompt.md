# Bounded retry — selected-Q8 infinity passport plus Galois primitivity

The prior hostile-review process for this task exhausted its 64,000-token
response ceiling before producing a report.  Perform the same audit specified
in
`xmodel/max12-912-order3-nu-q8-infinity-primitivity-review-claude-20260825-prompt.md`,
which you must read in full, subject to these additional fail-closed output
constraints:

- Do not transcribe source files, manifests, polynomial coefficient lists, or
  long calculations.  Refer to exact file paths, hashes, and short formulas.
- Keep the written report below 8,000 words and preferably below 5,000 words.
- For each of the seven charged audit items, give only: checks performed,
  decisive evidence, and any flaw or scope restriction.
- Give separate exact promotable sentences for the infinity/passport theorem,
  the primitivity theorem, and their conditional combination.
- If the evidence is too large to inspect within the response budget, return
  `GAP` and name the smallest unaudited dependency; do not expand the report.

Treat all producer and canonical bytes as immutable.  Do not use Bash, web
tools, or local computation.  Write exactly
`xmodel/max12-912-order3-nu-q8-infinity-primitivity-review-claude-20260825.md`
and edit no other file.  End with exactly one verdict: `CONFIRMED`, `GAP`, or
`REFUTED`.
