# Read-only custody-cleanup confirmation

Act as the same-kind independent hostile reviewer, but perform **no file edits**
and return your answer only on stdout.  Do not use Bash, local CAS, a solver,
long Python, or the network.  Read:

- the immutable raw review
  `xmodel/max12-912-order3-nu-q8-w0-overlap-normal-rank-tangent-review-grok-20260825.md`;
- its run metadata file with suffix `.run`;
- the proposed nonmutating companion
  `xmodel/max12-912-order3-nu-q8-w0-overlap-normal-rank-tangent-review-grok-cleanup-20260825.md`; and
- the original review prompt with suffix `-prompt.md`.

Confirm or reject only these custody propositions:

1. The raw review is text-corrupted at lines 13--20, while its detailed
   mathematical body in sections 2--9 is coherent and ends in `CONFIRMED`.
2. The cleanup preserves the raw bytes, accurately restores only the missing
   execution/files-read context, and faithfully summarizes (without broadening)
   the intact body and its ordinary-only firewall.
3. The hashes, targets, source/case inventory, and verdict stated by the cleanup
   agree with the raw review, run metadata, and original prompt.

Explicitly recheck that `K3=(d2,d4)` means the `c`-free line, that the rank-drop
line and rank-one point are excluded only for ordinary `delta w=1`, and that
ramified/weighted arcs plus full selected saturation remain open.

Return a concise report with a verdict `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or
`REFUTED`, and end with that verdict word alone.  Do not write any repository
file; stdout will be captured to a path distinct from every reviewed artifact.
