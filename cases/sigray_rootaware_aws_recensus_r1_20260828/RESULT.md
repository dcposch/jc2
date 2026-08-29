# Result: root-aware AWS recensus R1

All four frozen lanes completed with return code zero, no timeout, zero swap,
and terminal classification `RUN_COMPLETE_SCOPE_AS_OUTPUT_SUMMARY`.  This is a
root/IV/OPEN/frontier census plus one exact before/after invariant check.  It
makes no endpoint claim and does not supply ambient-orbit cap completeness.

## Exact invariant result

The before/after lane returned `pass=true`.  The following frozen inventories
are exactly equal: AF2 nonroot graph, hiii nonroot graph, monodromy rows,
ordinary nonroot graph, pinned entry inventory, and TDU entry inventory.  The
root-pole negative control also passed.  Its scope expressly excludes root
terminals and OPEN/frontier ledgers.  This shows that the engine repair
preserved the certified nonroot transitions and singleton pole-entry data; it
does not prove any root or multipole closure.

## Census lanes and OPEN scope

`LEDGER_OPEN.txt` is a regex audit ledger, not a deduplicated count of
mathematical branches.  It records lines containing `OPEN`, `NO_VERDICT`, or
`RESIDUE`; the following counts therefore must not be read as survivor counts.

- Common lane: 1,886 lines.  By stage: bash 70, bash5 33, bash6 529,
  tduniform-80 1,144, selected TDU td4/6/8/9/10/12 respectively
  5/9/15/15/20/45, and smoke 1.  Selected td3/5/7/11 had no OPEN lines.
  Unresolved scopes include parametric IV tails, MU1 edge tails, and
  zero-charge IIa/III tails.  The separate tduniform-80 table is a bounded
  census through td=80, not a closure theorem.
- h3/hiii lane: 231 lines.  By stage: h3-SF1 32, hiii ordinary 101,
  pinned 18, AF2 79, smoke 1.  These are the ordinary, pinned, and AF2
  composition censuses with explicit root terminals and unresolved tails.
- Two-pole lane: 763 lines.  Default contributed 324 and raised-cap diagnostic
  438, plus smoke 1.  `RESIDUE` entries are deliberately included.  The exact
  root menu at l<=128 had 1,161 rows: 64 even-log-dead, 63 odd without a log
  obstruction, 1 exact l=1 entry, and 1,033 unchecked.  The ambient orbit-tree
  blocker leaves shared-budget cap completeness `NO_VERDICT`.
- Invariant lane: 2 regex lines (smoke and comparison prose), not open
  branches.  Its exact result is the restricted invariant statement above.

Separate ledgers contain, respectively, ROOT/IV/FRONTIER line counts:
common 1,199/1,305/39; h3/hiii 130/88/53; two-pole 69/28/0; invariant
18/0/1.  They remain separate by construction.

## Interpretation firewall

No diagnostic contradicts or promotes the repaired analytic theorem.  In
particular, the post-run analytic exclusion of the td6 all-M1 root meet by the
case-I relation `w=l/(r+l)<1` versus `W={2}` does not depend on these runs.
The AWS root outputs remain engine/completeness diagnostics and generic
SF1/mixed-root censuses only.  No universal `DEPTH w<1` root filter was applied;
case-I root merges remain represented, and only certified case-IV filtering is
eligible for that rule.

Strict overall verdict: `CENSUS_COMPLETE_WITH_EXPLICIT_OPEN_NO_VERDICT`, plus
the restricted exact before/after invariant PASS.  No endpoint, ambient-orbit,
or global completeness conclusion follows.
